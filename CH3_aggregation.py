import geopandas as gpd
from shapely import speedups
speedups.enabled

apur = gpd.read_file("F:\\DATABASE\\APUR\\BESOIN_THEORIQUE_CHAUFFAGE_ET_TYPOLOGIE_AU_BATI.geojson")
apur.crs = 4326
apur.to_crs(2154)

attributs_apur = [
    "geometry"
    "SURFACE_VITRAGE",
    "SURFACE_HABITABLE",
    "C_PERCONST_APUR",
    "Shape_Area",
    "SURFACE_PAROI_TOT",
    "NB_NIV",
    "H_MEDIANE",
    "Typologie_apur"
    ]

for attribut in attributs_apur:
    apur = apur[~apur[attribut].isna()]

apur = apur[(apur["NB_NIV"] > 1) & (apur["C_PERCONST_APUR"].isin([99,"99"]))]

bdtopo = gpd.read_file("F:\\BD_TOPO_IDF\\BATI\\BATIMENT.shp")

bdtopo = bdtopo[["geometry","MAT_MURS","MAT_TOITS"]]
bdtopo = bdtopo[
    (~bdtopo["MAT_MURS"].isna()) & 
    (~bdtopo["MAT_TOITS"].isna()) & 
    (~bdtopo["MAT_MURS"].isin(["9","09","90","99"])) & 
    (~bdtopo["MAT_TOITS"].isin(["9","09","90","99"])) & 
    (bdtopo["LEGER"] == "Non")
    ]

bdtopo["geometry"] = bdtopo["geometry"].apply(lambda poly : poly.centroid)

mats_murs = []
mats_toits = []

for bati in apur["geometry"]:
    isinside = bdtopo.within(bati)
    pt = bdtopo.loc[isinside]
    if len(pt) == 1:
        mats_murs.append(pt.iloc[0]["MAT_MURS"])
        mats_toits.append(pt.iloc[0]["MAT_TOITS"])
    else:
        mats_murs.append(None)
        mats_toits.append(None)

apur["MAT_MURS"] = mats_murs
apur["MAT_TOITS"] = mats_toits
apur = apur[(apur["MAT_MURS"] != None) & (apur["MAT_TOITS"] != None)]

apur.to_file("F:\\BASES_APUREES\\JEU_APURÉ.geojson")


