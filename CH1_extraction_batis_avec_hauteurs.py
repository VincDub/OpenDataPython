import json

def import_b_h(chemin_json,h_etage):
    #ouverture du fichier json
    with open(chemin_json,"r",encoding="utf-8") as file:
        volumes = json.load(file)

    def extraire_intervalles(hauteur_paf):
        intervalles = [] 
        intervs = hauteur_paf.split("_et_")
        #itération à travers les intervalles de hauteur (s'il y en plusieurs)
        for interv in intervs:
            #filtrage des différentes notations de "l_b_u"
            if "encorbt_au_" in interv:
                intervalles.append([
                    (int(interv.strip("encorbt_au_"))-1)*h_etage,
                    int(interv.strip("encorbt_au_"))*h_etage
                    ])
            elif "a" in interv:
                if "R" in interv:
                    intervalles.append([0,int(interv.strip("Ra"))*h_etage])
                else:
                    intervalles.append([int(a)*h_etage for a in interv.split("a")])
            elif interv == "R":
                intervalles.append([0,h_etage])
        #listes des intervalles en sortie
        return intervalles

    volumes_avec_hauteur = [] #liste vide

    for volume in volumes:
        coordonnees = volume["fields"]["geom"]["coordinates"]
        hauteur_max = volume["fields"]["h_et_max"]*h_etage
        
        try:
            hauteur_paf = volume["fields"]["l_b_u"]
            #ajout des intervalles de hauteur si le volume n'a pas de rdc
            volumes_avec_hauteur.append({
            "coords" : coordonnees,
            "h" : hauteur_max,
            "interv" : extraire_intervalles(hauteur_paf)
            })

        except KeyError: 
            #si le volume est au rdc
            volumes_avec_hauteur.append({
            "coords" : coordonnees,
            "h" : hauteur_max})
    
    return volumes_avec_hauteur