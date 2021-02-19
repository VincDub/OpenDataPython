import geopandas as gpd
import rasterio
from rasterio.mask import mask
import os

dossier_bdortho = "F:\\ORTHO_94"
dossier_photos = "C:\\Users\\vinc\\Desktop\\PHOTOS"
fichiers = os.listdir(dossier_bdortho)

for j,f in enumerate(fichiers):
    if f.endswith(".jp2"):
        carreau = rasterio.open(os.path.join(dossier_bdortho,f))
        limites = carreau.bounds
        batis = gpd.read_file("F:\\BASES_APUREES\\JEU_AGG\\JEU_AGG.shp",bbox=limites)
        for i,bati in batis.iterrows():
            poly = bati["geometry"].buffer(0.1,cap_style=3,join_style=2)
            img,trs = mask(carreau,[poly],crop=True,pad=True)
            path = os.path.join(dossier_photos,"%i.png"%bati["id"])
            with rasterio.open(path,"w+",transform=trs,dtype=rasterio.uint8,driver="PNG",height=60,width=60,count=3) as p:
                p.write(img)
            print("bati %i/%i : carreau %i/%i"%(i,len(batis),j,len(fichiers)/2),end="\r")

print("------\nfini !")        

