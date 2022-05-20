from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_base import Paises

engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()

#Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".

paises = session.query(Paises).filter(or_(Paises.cldr_display_name.like("%uador%"), Paises.capital.like("%ito"))).all()
print (paises)