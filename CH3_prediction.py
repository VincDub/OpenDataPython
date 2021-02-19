import geopandas as gpd
"""
def calcul_V_fac(bati):
    S_facade = bati["SURFACE_PAROI_TOT"] - bati["SURFACE_VITRAGE"]
    ep = bati["Shape_Area"] - (bati["SURFACE_HABITABLE"]/bati["NB_NIV"])
    bati["V_facade"] = S_facade*ep
    return bati



# Enregistrement du jeu apuré dans un nouveau fichier
bdtopo.to_file("F:\\BASES_APUREES\\BDTOPO_APURÉ")


batis = gpd.read_file("F:\\BASES_APUREES\\JEU_AGG\\JEU_AGG.shp")
batis = batis.apply(lambda bati : calcul_V_fac(bati))

bdtopo = gpd.read_file("F:\\BASES_APUREES\\JEU_AGG\\JEU_AGG.shp")

def decodage_mur(mat_mur):
  # Pierre
  if mat_mur in ["1","01","10","11","19","91"]:
      mat_mur = "Pierre"
  # Meulière
  elif mat_mur in ["2","02","12","20","21","22","29","92"]:
      mat_mur = "Meulière"
  # Béton
  elif mat_mur in ["3","03","13","23","30","31","32","33","34","36","39","43","63","93"]:
      mat_mur = "Béton"
  # Briques
  elif mat_mur in ["4","04","14","24","40","41","42","44","49","94"]:
      mat_mur = "Briques"
  # Aggloméré
  elif mat_mur in ["5","05","15","25","35","45","50","51","52","53","54","55","56","59","65","95"]:
      mat_mur = "Aggloméré"
  # Bois
  elif mat_mur in ["6","06","16","26","46","60","61","62","64","66","96"]:
      mat_mur = "Bois"  
  return mat_mur

def decodage_toit(mat_toit):
  # Tuiles
  if mat_toit in ["1","01","10","11","13","19","31","91"]:
      mat_toit = "Tuiles"
  # Ardoises
  elif mat_toit in ["2","02","12","20","21","22","23","24","29","32","42","92"]:
      mat_toit = "Ardoises"
  # Zinc/Aluminium
  elif mat_toit in ["3","03","30","33","39","93"]:
      mat_toit = "Zinc/Aluminium"
  # Béton
  elif mat_toit in ["4","04","14","34","40","41","43","44","49","94"]:
      mat_toit = "Béton"  
  return mat_toit

# Application des fonctions de decodage
bdtopo["MAT_TOITS"] = bdtopo["MAT_TOITS"].map(decodage_toit)
bdtopo["MAT_MURS"] = bdtopo["MAT_MURS"].map(decodage_mur)
"""
batis = gpd.read_file("F:\\BASES_APUREES\\JEU_AGG\\JEU_AGG.shp")
print(batis["C_PERCONST"].value_counts().to_dict())
table_periodes = {
  1: "Avant 1800",
  2: "1801-1850",
  3: "1851-1914",
  4: "1915-1939",
  5: "1940-1967",
  6: "1968-1975",
  7: "1976-1981",
  8: "1982-1989",
  9: "1990-1999",
  10: "2000-2007",
  11: "Après 2008"
}
# Décodage de la période de construction
batis["C_PERCONST"] = batis["C_PERCONST"].map(table_periodes)
print(batis["C_PERCONST"].value_counts().to_dict())
# Enregistrement du jeu apuré dans un nouveau fichier
batis.to_file("F:\\BASES_APUREES\\JEU_AGG")

"""
table_mattoit = {
    # Tuiles
    ["1","01","10","11","13","19","31","91"] : 0,
    # Ardoises
    ["2","02","12","20","21","22","23","24","29","32","42","92"] : 1,
    # Zinc/Aluminium
    ["3","03","30","33","39","93"] : 2,
    # Béton
    ["4","04","14","34","40","41","43","44","49","94"] : 3,
}
# Transformation en notation explicite pour chaque valeur
# "1" : 0, "01" : 0, "10" ; 0, etc...
table_mattoit = { _ : k for _ in v for k,v in table_mattoit.items()}

table_matmur = {
    # Pierre
    ["1","01","10","11","19","91"] : 0,
    # Meulière
    ["2","02","12","20","21","22","29","92"] : 1,
    # Béton
    ["3","03","13","23","30","31","32","33","34","36","39","43","63","93"] : 2,
    # Briques
    ["4","04","14","24","40","41","42","44","49","94"] : 3,
    # Aggloméré
    ["5","05","15","25","35","45","50","51","52","53","54","55","56","59","65","95"] : 4,
    # Bois
    ["6","06","16","26","46","60","61","62","64","66","96"] : 5,
}
# Transformation en notation explicite pour chaque valeur
# "1" : 0, "01" : 0, "10" ; 0, etc...
table_matmur = { _ : k for _ in v for k,v in table_matmur.items()}

table_nature = {
    "logement individuel" : 0,
    "logement collectif" : 1,
    "bâtiment mixte" : 2,
    "batiment tertiaire ou industriel" : 3,
    "non déterminée" : 4 
    }
# Pas besoin de transformation

batis["MAT_TOIT"] = batis["MAT_TOIT"].map(table_mattoit)
batis["MAT_MURS"] = batis["MAT_MURS"].map(table_matmur)
batis["Typologie_apur"] = batis["Typologie_apur"].map(table_nature)
"""








