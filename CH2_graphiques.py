from CH1_extraction_batis_avec_hauteurs import import_b_h
import plotly.graph_objects as go

# exécution de la fonction du script du chapitre 1
volumes_avec_hauteur = import_b_h("DONNEES/volumesbatisparis.json",h_etage=3)

# tri par ordre croissant des hauteurs
hauteurs = sorted(list(set([volume['h'] for volume in volumes_avec_hauteur])))
n_hauteurs = []
for hauteur in hauteurs:
    # Récupération du nombre de volumes correspondant à chaque hauteur
    n = len([vol for vol in volumes_avec_hauteur if vol["h"] == hauteur])
    n_hauteurs.append(n)

# traçage d'un graphique en barres grâçe à plotly
fig = go.Figure([go.Bar(x=hauteurs, y=n_hauteurs)])
fig.update_xaxes(type='category')
fig.update_layout(title="Répartition des hauteurs",xaxis_title="hauteur (m)",yaxis_title="nombre de volumes",width=600,height=600)
# Export sous forme d'image statique
fig.write_image("OUTPUT/graphique_hauteurs.png")
# Export sous forme d'une page web interactive
fig.write_html("OUTPUT/graphique_hauteurs.html")

# traçage d'un graphique en "donut"
fig2 = go.Figure(data=[go.Pie(labels=hauteurs, values=n_hauteurs,hole=.6)])
fig2.update_layout(title="Répartition des hauteurs",legend_title="Hauteur (m)",width=600,height=600)
fig2.write_image("OUTPUT/graphique_hauteurs_donut.png")
fig2.write_html("OUTPUT/graphique_hauteurs_donut.html")
