"""
import geopandas as gpd
import pandas
import plotly.express as px

# Chargement du jeu agrégé
batis = gpd.read_file("F:\\BASES_APUREES\\JEU_AGG\\JEU_AGG.shp")
# Encodage des valeurs de "Typologie_apur"
typo = pandas.get_dummies(batis["Typologie_"])
# Encodage des valeurs de "MAT_MURS"
matm = pandas.get_dummies(batis["MAT_MURS"])
# Encodage des valeurs de "MAT_TOITS"
matt = pandas.get_dummies(batis["MAT_TOITS"])
# Encodage des valeurs de "C_PERCONST_APUR"
perconst = pandas.get_dummies(batis["C_PERCONST"])
# Intégration des nouvelles colonnes
batis = batis.join([typo,matm,matt,perconst])
# Abandon de l'identifiant
batis = batis.drop(columns=["id"])
# Calcul des coefficients de corrélation
correlation = batis.corr()
# Construction du corrélogramme
fig = px.imshow(
    correlation,
    color_continuous_scale='RdBu_r')
# Export du corrélogramme
fig.write_html("OUTPUT/matrice_corrélation.html")
# Séléction spécifique dans la matrice
correl_nature = correlation[[
    "bâtiment mixte",
    "logement collectif",
    "logement individuel"
    ]]
# Construction du second corrélogramme
fig2 = px.imshow(
    correl_nature,
    color_continuous_scale='RdBu_r')
# Export du second corrélogramme
fig2.write_html("OUTPUT/matrice_corrélation_nat.html")



import geopandas as gpd

# Chargement du jeu agrégé
batis = gpd.read_file("F:\\BASES_APUREES\\JEU_AGG\\JEU_AGG.shp")

table_periodes = {
  "Tuiles": 1,
  "Ardoises": 2,
  "Zinc/Aluminium": 3,
  "Béton_toit": 4,
}
# Encodage de la période de construction
batis["MAT_TOITS"] = batis["MAT_TOITS"].map(table_periodes)

batis = batis.sample(1000)

from PIL import Image
import numpy as np
# Dossier des photos aériennes
dossier_photos = "C:\\Users\\vinc\\Desktop\\PHOTOS"

def charger_photo(bati):
    print(bati.name,end="\r")
    # Chemin de l'image associée au bâtiment
    path = dossier_photos+"\\"+str(bati["id"])+".png"
    try:
        # Essaye de charger l'image
        # et de l'inclure dans une colonne "photo"
        # sous forme de matrice
        img = Image.open(path)
        bati["photo"] = np.asarray(img)
    except:
        # Si l'image nexiste pas
        bati["photo"] = None
    return bati

# Chargement des images
batis = batis.apply(charger_photo,axis=1)
# Filtrage des bâtiments sans images
batis = batis.dropna()

import tensorflow as tf
import autokeras as ak

# Extraction des données pour l'entraînement
labels = batis["MAT_TOITS"].to_numpy()
images = np.stack(batis["photo"].to_list())
print(images[0])
print(images[0].shape)
print(labels.shape)
print(images.shape)

# Initialisation du modèle vierge
mdl = ak.ImageClassifier(metrics=['accuracy'])
# Entraînement et sauvegarde
mdl.fit(Z
    images,
    labels,
    validation_split=0.15,
    epochs=10)
mdl.save("DONNEES/mdl_datation", save_format="tf")
"""
from tensorflow.keras.models import load_model

img1 = np.asarray(Image.open("DONNEES/img1.png"))
img2 = np.asarray(Image.open("DONNEES/img2.png"))
img3 = np.asarray(Image.open("DONNEES/img3.png"))
img4 = np.asarray(Image.open("DONNEES/img4.png"))
imgs_test = np.vstack([img1,img2,img3])

mdl = load_model("DONNEES/mdl_classification", custom_objects=ak.CUSTOM_OBJECTS)
mdl.predict(imgs_test)
