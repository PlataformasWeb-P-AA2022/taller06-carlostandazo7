from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_base import Paises

engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()

#Presentar los países de Asía, ordenados por el atributo Dial.

paises = session.query(Paises).filter(Paises.continent=="AS").order_by(Paises.dial).all()
print (paises)