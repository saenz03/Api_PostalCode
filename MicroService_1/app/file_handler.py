import pandas as pd

def validate_csv(file):
    """Valida si el archivo CSV tiene el formato correcto (columnas y tipo de datos)"""
    try:
        df = pd.read_csv(file)
        # Verificar que las columnas sean 'latitude' y 'longitude'
        if not {'latitude', 'longitude'}.issubset(df.columns):
            raise ValueError("CSV file does not have the required columns")
        # Verificar que los valores de latitud y longitud sean números
        if not pd.api.types.is_numeric_dtype(df['latitude']) or not pd.api.types.is_numeric_dtype(df['longitude']):
            raise ValueError("Latitude and longitude columns must contain numeric values")
        return df
    except Exception as e:
        raise ValueError(f"Error reading or validating CSV file: {str(e)}")
