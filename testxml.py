import geopandas as gpd

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'


data = gpd.read_file("DONNEES/volumesbatisparis.geojson")

data = data[["geometry","m2_pl_tot","h_et_max","l_b_u"]]
data = data.rename(columns={
    "m2_pl_tot" : "surface",
    "h_et_max" : "hauteur",
    "l_b_u" : "hauteur_paf"
    })

h_etage = 3
def texte_to_num(volume):
     # Si le volume n'est pas en porte à faux
    if volume["hauteur_paf"] == None:
        # Affecter une valeur nulle
        volume["hauteur_paf"] = None
    else:
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
            elif "a" in interv:
                if "R" in interv:
                    output.append([0,(int(interv.strip("Ra"))+1)*h_etage])
                else:
                    output.append([(int(h)+1)*h_etage for h in interv.split("a")])
            elif interv == "R":
                output.append([0,h_etage])
            # Remplacement par la notation numérique
            volume["hauteur_paf"] = output

    volume["hauteur"] = (volume["hauteur"] + 1)*h_etage
    return volume

# Application à chaque ligne avec .apply()
data = data.apply(lambda volume : texte_to_num(volume),axis=1)
# Affichage des 3 premiers volumes
print(data.head(3))
"""

print(data["hauteur"].value_counts().to_dict())

import plotly.express as px
def is_paf(volume):
    if volume["hauteur_paf"] == None:
        return 0
    else:
        return 1

df = data.drop(columns=["geometry"])
df["is_paf"] = df.apply(lambda row : is_paf(row), axis=1)
#df = pandas.DataFrame(volumes).drop(columns=["coords","hauteur_paf"])
fig2 = px.parallel_coordinates(df, color="hauteur",color_continuous_scale=px.colors.sequential.amp)
fig2.update_layout(font={"size":20},width=1800,height=800)
fig2.write_image("OUTPUT/graphique_repart.png")
fig2.write_html("OUTPUT/graphique_repart.html")

volumes_par_hauteur = data.groupby("hauteur")


import plotly.graph_objects as go
# Liste accueillant les couches de la carte
traces = []
for h,volumes in volumes_par_hauteur:
  couleur = "rgb(" + ",".join([str(h/max(data["hauteur"])*255)]*3) +")"
  X = []
  Y = []
  for geom in volumes["geometry"]:
    coords = geom.exterior.coords.xy
    X += list(coords[0][:-1])+[None] # longitude
    Y += list(coords[1][:-1])+[None] # latitude
    # Traçage des volumes
  print(X)
  traces.append(go.Scattermapbox(
    name=str(h) +"m",
    mode="lines",
    line = {"width" : 0.5, "color" : couleur},
    lon=X,
    lat=Y,
    opacity=1.0,
    hoverinfo="name",
    fill="toself"))

fig = go.Figure(traces)
fig.update_layout(title="Hauteurs des volumes bâtis",legend_title="Hauteur", autosize=True,
    mapbox = {'style':"carto-positron",'center': {'lon': 2.3848515, 'lat': 48.8272092}, "zoom" : 16.6})
# Export sous forme d'une page web interactive
fig.write_html("OUTPUT/carte_des_hauteurs.html")
"""
data.crs = 4326
print(data)
data = data.to_crs(2154)
print(data)
"""
import utm

print(utm.from_latlon(48.82753,2.38462))
print(utm.latlon_to_zone_number(48.82753,2.38462))
print(utm.latitude_to_zone_letter(48.82753))
"""

print(data.drop("geometry",axis=1))