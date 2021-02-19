from shapely.geometry import Polygon,Point
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

"""
p = Polygon([(0,0),(1,0),(1,1),(0,1)])
p2 = p.buffer(0.1,cap_style=3,join_style=2)
plt.plot(*p.exterior.coords.xy)
plt.plot(*p2.exterior.coords.xy)
plt.show()
"""
"""
p = Polygon([(0,0),(1,0),(1,1),(0,1)])
p2 = Polygon([(30,30),(38,36),(31.5,33)])
p3 = Polygon([(-10,-20),(-20,-40),(-20,-10)])

gp1 = gpd.GeoDataFrame({ "geometry" : [p,p2,p3],"v1" :[0,1,2], "v2" :[1512,25,35]})


pt1 = Point((32.2,32.9)).buffer(0.1)
pt2 = Point((-15.6,-25.4)).buffer(0.1)
pt3 = Point((0.4,0.4)).buffer(0.1)
pt4 = Point((25.3,-18.6)).buffer(0.1)

gp2 = gpd.GeoDataFrame({ "geometry" : [pt1,pt2,pt3,pt4],"v4" :[12,5,36,789], "v3" :[1512,25,35,12]})

intersect = gpd.sjoin(gp1,gp2,how="inner")#.drop(columns=["index_right"])
print(intersect.shape)
print(intersect)

for l in intersect["geometry"]:
    plt.plot(*l.exterior.coords.xy)
plt.show()

"""
df = pd.DataFrame({ "col1" : ["lol","putain","mdr","vache"],"col2" : [0,0,0,0]})
print(df)

df["col1"] = df["col1"].map({
    "lol": 30,
    "putain" : 45
})
print(df)