from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_base import Paises

import json
import requests


engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()


# leer el archivo de datos

# archivo = open("data/data-personas-001.json", "r")
archivo = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")

# datos_json =  json.load(archivo) # paso los datos del archivo a json
res = archivo.json()

#documentos = datos_json["docs"]

for d in res:
    print(d)
    print(len(d.keys()))
    p = Paises(cldr_display_name=d['CLDR display name'], capital=d['Capital'], continent=d['Continent'], \
            dial=d['Dial'], geoname_id=d['Geoname ID'], itu=d['ITU'], languages=d['Languages'], is_independent=d['is_independent'])
    session.add(p)

# confirmar transacciones

session.commit()
