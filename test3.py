import geopandas as gpd
from shapely import speedups
speedups.enabled

gpd1 = gpd.read_file('DONNEES/volumesbatisparis.geojson')
gpd1["geometry"] = gpd1["geometry"].apply(lambda poly : poly.centroid)


gpd2 = gpd.read_file('DONNEES/volumesbatisparis.geojson')

print(gpd1)
print(gpd2)

masks = []
for geom in gpd2["geometry"]:
    mask = gpd1.within(geom)
    masks.append(mask)
    pt = gpd1.loc[mask]
    print(pt.iloc[0]["l_b_u"])
