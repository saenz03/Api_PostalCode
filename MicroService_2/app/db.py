from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from microservice_1 import Location  # Importamos el modelo del microservicio 1

DATABASE_URL = "postgresql://user:password@db:5432/postcodes_db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def get_unprocessed_locations():
    """Obtiene las coordenadas que aún no tienen código postal asignado"""
    return session.query(Location).filter(Location.postcode == None).all()

def update_location_with_postcode(location, postcode):
    """Actualiza el registro de la ubicación con el código postal obtenido"""
    location.postcode = postcode
    session.commit()
