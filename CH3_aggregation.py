import geopandas as gpd
from shapely import speedups
import shapely
speedups.enabled
"""
apur = gpd.read_file("F:\\DATABASE\\APUR\\BESOIN_THEORIQUE_CHAUFFAGE_ET_TYPOLOGIE_AU_BATI.geojson")
apur.crs = 4326
apur = apur.to_crs(2154)

attributs_apur = [
    "geometry",
    "SURFACE_VITRAGE",
    "SURFACE_HABITABLE",
    "C_PERCONST_APUR",
    "Shape_Area",
    "SURFACE_PAROI_TOT",
    "NB_NIV",
    "H_MEDIANE",
    "Typologie_apur"
    ]

apur = apur[attributs_apur].dropna()

apur = apur[(apur["NB_NIV"] > 1) & (~apur["C_PERCONST_APUR"].isin([99,"99"]))]

apur.to_file("F:\\BASES_APUREES\\APUR_APURÉ")

bdtopo = bdtopo[
    (~bdtopo["MAT_MURS"].isna()) & 
    (~bdtopo["MAT_TOITS"].isna()) & 
    (~bdtopo["MAT_MURS"].isin(["9","09","90","99","00","0"])) & 
    (~bdtopo["MAT_TOITS"].isin(["9","09","90","99","00","0"])) & 
    (bdtopo["LEGER"] == "Non")
    ]

bdtopo = bdtopo[["geometry","MAT_MURS","MAT_TOITS"]]

bdtopo = gpd.read_file("F:\\BASES_APUREES\\BDTOPO_APURÉ")
def decodage_mur(mat_mur):
  # Pierre
  if mat_mur in ["1","01","10","11","19","91"]:
      mat_mur = "Pierre"
  # Meulière
  elif mat_mur in ["2","02","12","20","21","22","29","92"]:
      mat_mur = "Meulière"
  # Béton
  elif mat_mur in ["3","03","13","23","30","31","32","33","34","36","39","43","63","93"]:
      mat_mur = "Béton"
  # Briques
  elif mat_mur in ["4","04","14","24","40","41","42","44","49","94"]:
      mat_mur = "Briques"
  # Aggloméré
  elif mat_mur in ["5","05","15","25","35","45","50","51","52","53","54","55","56","59","65","95"]:
      mat_mur = "Aggloméré"
  # Bois
  elif mat_mur in ["6","06","16","26","46","60","61","62","64","66","96"]:
      mat_mur = "Bois"  
  return mat_mur

def decodage_toit(mat_toit):
  # Tuiles
  if mat_toit in ["1","01","10","11","13","19","31","91"]:
      mat_toit = "Tuiles"
  # Ardoises
  elif mat_toit in ["2","02","12","20","21","22","23","24","29","32","42","92"]:
      mat_toit = "Ardoises"
  # Zinc/Aluminium
  elif mat_toit in ["3","03","30","33","39","93"]:
      mat_toit = "Zinc/Aluminium"
  # Béton
  elif mat_toit in ["4","04","14","34","40","41","43","44","49","94"]:
      mat_toit = "Béton_toit"  
  return mat_toit

# Application des fonctions de decodage
bdtopo["MAT_TOITS"] = bdtopo["MAT_TOITS"].map(decodage_toit)
bdtopo["MAT_MURS"] = bdtopo["MAT_MURS"].map(decodage_mur)

bdtopo.to_file("F:\\BASES_APUREES\\BDTOPO_APURÉ")

"""
apur = gpd.read_file("F:\\BASES_APUREES\\APUR_APURÉ\\APUR_APURÉ.shp")
bdtopo = gpd.read_file("F:\\BASES_APUREES\\BDTOPO_APURÉ\\BDTOPO_APURÉ.shp")

bdtopo["geometry"] = bdtopo["geometry"].apply(lambda poly : poly.centroid.buffer(0.1))

intersection = gpd.sjoin(apur,bdtopo, how='inner')
intersection = intersection.drop(columns=["index_right"])
intersection['id'] = intersection.index

intersection.to_file("F:\\BASES_APUREES\\JEU_AGG")



