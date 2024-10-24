from app.file_handler import validate_csv
from app.db import add_location

def process_csv_file(file):
    """Valida y procesa el archivo CSV, almacenando los datos en la base de datos"""
    try:
        # Validar el archivo CSV
        df = validate_csv(file)
        
        # Almacenar cada ubicación en la base de datos
        for index, row in df.iterrows():
            add_location(row['latitude'], row['longitude'])
        
        return {"message": "Archivo procesado y data guardada"}, 200
    except ValueError as e:
        return {"error": str(e)}, 400
