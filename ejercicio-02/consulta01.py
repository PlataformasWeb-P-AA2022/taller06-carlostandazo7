from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_base import Paises

from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Paises).all()

print("Presentación de todos los Paises")
for s in paises:
    print("%s" % (s))
    print("---------")

# Presentar todos los países del continente americano

paises = session.query(Paises).filter(Paises.continent=="SA").order_by(Paises.cldr_display_name).all()

print (paises)