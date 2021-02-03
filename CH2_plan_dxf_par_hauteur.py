from CH1_extraction_batis_avec_hauteurs import import_b_h
import ezdxf
import utm
# exécution de la fonction du script du chapitre 1
volumes_avec_hauteur = import_b_h("DONNEES/volumesbatisparis.json",h_etage=3)

# initialisation d'un nouveau dessin
doc = ezdxf.new(dxfversion='R2010')
msp = doc.modelspace()

# tri par ordre croissant des hauteurs
hauteurs = sorted(list(set([volume['h'] for volume in volumes_avec_hauteur])))
# Création des calques dans une première boucle
# afn de créer une graduation des couleurs
for i,h in enumerate(hauteurs):
    calque = doc.layers.new(str(h+3) + "m")
    calque.rgb = tuple([255*(h/hauteurs[-1])]*3)

for volume in volumes_avec_hauteur:

    coords_cart = []
    # Conversion des coordonnées géodésiques (lat/lon) en cartésiennes (x/y)
    for coords in volume["coords"][0]:
        c = utm.from_latlon(coords[1],coords[0])
        coords_cart.append((c[0],c[1]))
    
    calque = str(volume["h"]) + "m"
    msp.add_polyline2d(coords_cart, dxfattribs={'layer': calque})

doc.saveas("OUTPUT/plan_bati.dxf")