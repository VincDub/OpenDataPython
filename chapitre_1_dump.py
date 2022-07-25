# Export pour réutilisation dans le code du chapitre 2
import geopandas as gpd

def texte_to_num(volume, h_etage=3):
            
    if volume["hauteur_paf"]:
        # Liste vide pour contenir les notations numériques
        output = []
        # Séparation des sous-notations au niveau du "_et_"
        # Si absent, la notation sera conservée telle quelle
        intervalles = volume["hauteur_paf"].split("_et_")
        # Itération à travers les sous-notations
        for interv in intervalles:
            # filtrage par syntaxe
            if "encorbt_au_" in interv:
                n = int(interv.strip("encorbt_au_"))
                if n == volume["hauteur"]:
                    output.append([n*h_etage,(n+1)*h_etage])
                else:
                    output.append([(n+1)*h_etage,(volume["hauteur"]+1)*h_etage])
            elif "auvent_n" in interv:
                n = int(interv.strip("auvent_n"))
                output.append([n*h_etage,(n+1)*h_etage])
            elif "a" in interv and "_avec_equiv_" not in interv:
                if "R" in interv:
                    output.append([0,(int(interv.strip("Ra"))+1)*h_etage])
                else:
                    output.append([(int(h)+1)*h_etage for h in interv.split("a")])
            elif interv == "R":
                output.append([0,h_etage])
            elif "_avec_equiv_" in interv:
                n = int(interv[-2])
                if interv[-2] == 0:
                    n = int(interv[-3:-2])
                output.append([0,h_etage*n])
        # Remplacement par la notation numérique
        volume["hauteur_paf"] = output

    volume["hauteur"] = (volume["hauteur"] + 1)*h_etage
    return volume

def import_data_batiments(path, h_etage):

    data = gpd.read_file(path)
    data = data[["geometry","m2_pl_tot","h_et_max","l_b_u"]]
    data = data.rename(columns={
        "m2_pl_tot" : "surface",
        "h_et_max" : "hauteur",
        "l_b_u" : "hauteur_paf"
        })

    data = data.apply(texte_to_num,axis=1)

    return data
