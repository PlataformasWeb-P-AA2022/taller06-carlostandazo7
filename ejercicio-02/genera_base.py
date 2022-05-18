from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Paises(Base):
    __tablename__ = 'lospaises'
    
    id = Column(Integer, primary_key=True)
    cldr_display_name = Column(String)
    capital = Column(String)
    continent = Column(String)
    dial = Column(String)
    geoname_id = Column(String)
    itu = Column(String)
    languages = Column(String)
    is_independent = Column(String)


Base.metadata.create_all(engine)

