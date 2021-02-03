import json

# Fonction pour charger les fichiers à aggréger
def charger_json(path):
    with open(path, "r",encoding='utf-8') as fichier:
        output = json.load(fichier)
        fichier.close()
    return output

# Fichier principal
bati_paris = charger_json("F:\\DONNEES_APUR\\EMPRISE_BATIE_PARIS.json")

# Données à intégrer
sport = charger_json("F:\\DONNEES_APUR\\EQUIPEMENT_EMPRISE_SPORT.json")
eco = charger_json("F:\\DONNEES_APUR\\EQUIPEMENT_EMPRISE_ACTIVITE_ECONOMIQUE.json")
loisirs = charger_json("F:\\DONNEES_APUR\\EQUIPEMENT_EMPRISE_CULTURE_LOISIRS.json")
edu = charger_json("F:\\DONNEES_APUR\\EQUIPEMENT_EMPRISE_ENSEIGNEMENT_EDUCATION.json")

def inclusion_batiment(bati,jeu_ext):

new_features = []
# Itération à travers chaque 
for bati in bati_paris["features"]:

    bati = inclusion_batiment(bati,sport)
    eco = inclusion_batiment(bati,sport)
    loisirs = inclusion_batiment(bati,sport)
    bati = inclusion_batiment(bati,sport)

    new_features.append()

