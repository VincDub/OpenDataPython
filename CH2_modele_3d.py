from CH1_extraction_batis_avec_hauteurs import import_b_h
import utm

# chargement d'une instance de Rhino sans fenêtre
import rhinoinside
from pathlib import Path
rhino_path = Path("C:/Program Files/Rhino 7/System")
rhinocore_path = Path("C:/Program Files/Rhino 7/System/RhinoCore.dll")
rhinoinside.load(str(rhino_path))
import System
import Rhino

# exécution de la fonction du script du chapitre 1
volumes_avec_hauteur = import_b_h("DONNEES/volumesbatisparis.json",h_etage=3)

# Création du document
DOC = Rhino.RhinoDoc.Create("")
DOC.ModelUnitSystem = Rhino.UnitSystem.Meters

# Création d'un calque principal
calque_bati =  Rhino.DocObjects.Layer()
calque_bati.Color = System.Drawing.Color.FromArgb(255,0,0,0)
calque_bati.Name = 'batiments'
DOC.Layers.Add(calque_bati)

c_actuel = DOC.Layers.FindByFullPath("calque_bati",-1)
DOC.Layers.SetCurrentLayerIndex(c_actuel,False)

# Ajout de chaque volume
for volume in volumes_avec_hauteur:
    pts = System.Collections.Generic.List[Rhino.Geometry.Point3d]()
    # Conversion des coordonnées géodésiques (lat/lon) en cartésiennes (x/y)
    for coords in volume["coords"][0]:
        c = utm.from_latlon(coords[1],coords[0])
        pts.Add(Rhino.Geometry.Point3d(c[0],c[1],0.0))
    poly = Rhino.Geometry.Polyline(pts)
    
    try:
        # Si le volume est en porte à faux
        for intervalle in volume['interv']:
            poly.SetAllZ(float(intervalle[0]))
            polyz = poly.ToPolylineCurve()
            h_cible = float(intervalle[1])-float(intervalle[0])
            extr = Rhino.Geometry.Extrusion.Create(polyz,-1*h_cible,True)
            DOC.Objects.AddExtrusion(extr)

    except KeyError:
        # Si le volume repose au rdc
        polyz = poly.ToPolylineCurve()
        extr = Rhino.Geometry.Extrusion.Create(polyz,-1*float(volume["h"]),True)
        DOC.Objects.AddExtrusion(extr)

success = DOC.SaveAs('OUTPUT/modele.3dm')