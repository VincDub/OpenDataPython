from CH1_extraction_batis_avec_hauteurs import import_b_h
import plotly.graph_objects as go

# exécution de la fonction du script du chapitre 1
volumes_avec_hauteur = import_b_h("DONNEES/volumesbatisparis.json",h_etage=3)

# tri par ordre croissant des hauteurs
hauteurs = sorted(list(set([volume['h'] for volume in volumes_avec_hauteur])))
grp_par_hauteur = {}
for hauteur in hauteurs:
    # Récupération du nombre de volumes correspondant à chaque hauteur
    volumes = [vol for vol in volumes_avec_hauteur if vol["h"] == hauteur]
    grp_par_hauteur[hauteur] = volumes


data = []
# itération à travers les groupes de polygones
for hauteur,volumes in grp_par_hauteur.items():
    x = []
    y = []
    # itération à travers les polygones
    for vol in volumes:
        #itération à travers les points de chaque polygone
        for coords in vol["coords"][0]:
            x.append(coords[0])#longitude (x)
            y.append(coords[1])#latitude (y)
            # ajout de valeurs nulles pour séparer les polygones
        x.append(None)
        y.append(None)

    # Teinte de gris (plus le volume est haut, plus il sera clair)
    couleur = "rgb(" + ",".join([str(hauteur/hauteurs[-1]*255)]*3) +")"
    # Traçage des volumes sur une carte
    data.append(go.Scattermapbox(
    name="R+" + str(int(hauteur/3)),
    mode="lines",
    line = {"width" : 0.5, "color" : couleur},
    lon=x,
    lat=y,
    opacity=1.0,
    hoverinfo="name",
    fill="toself"))

fig = go.Figure(data)
# Définition du style du fond
fig.update_layout(title="Hauteurs des volumes bâtis",legend_title="Hauteur",
    autosize=True,
    mapbox = {'style':"carto-positron",'center': {'lon': 2.3848515, 'lat': 48.8272092}, "zoom" : 16.6})
# Export sous forme d'une page web interactive
fig.write_html("OUTPUT/carte_des_hauteurs.html")