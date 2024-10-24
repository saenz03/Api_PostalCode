from flask import Flask, request, jsonify
from app.services import process_csv_file

app = Flask(__name__)

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    """Endpoint para subir y procesar el archivo CSV"""
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    
    # Llamar al servicio para procesar el archivo
    response, status = process_csv_file(file)
    
    return jsonify(response), status

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)