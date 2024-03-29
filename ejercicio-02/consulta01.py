from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_base import Paises

engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()

#Presentar todos los países del continente americano

paises = session.query(Paises).filter(Paises.continent.in_(['NA', 'SA'])).order_by(Paises.cldr_display_name).all()
print (paises)