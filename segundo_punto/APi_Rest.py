from flask import Flask, request, jsonify
import pandas as pd
import os

#para correr el API_REST pon en la terminar python app.py

app = Flask(__name__)

# Ruta del archivo Excel
EXCEL_PATH = r"D:\prueba_tecnica_deloite\Escaneo_Prueba.xlsx"

# Endpoint GET /vulnerabilidades
@app.route('/vulnerabilidades', methods=['GET'])
def get_vulnerabilidades():
    if not os.path.exists(EXCEL_PATH):
        return jsonify({'error': 'Archivo no encontrado'}), 404
    
    df = pd.read_excel(EXCEL_PATH)
    data = df.to_dict(orient='records')
    return jsonify(data)

# Endpoint POST /vulnerabilidades
@app.route('/vulnerabilidades', methods=['POST'])
def post_vulnerabilidad():
    nueva_vuln = request.get_json()

    if not nueva_vuln:
        return jsonify({'error': 'JSON vacío o inválido'}), 400

    # Validar campos obligatorios
    campos_obligatorios = ['IP', 'First Detected', 'Last Detected', 'CVE ID', 'Gid', 'Categoria', 'Riesgo', 'Criticidad']
    faltantes = [campo for campo in campos_obligatorios if campo not in nueva_vuln]
    if faltantes:
        return jsonify({'error': f'Faltan campo o campos: {", ".join(faltantes)}'}), 400

    # Cargar archivo existente
    if os.path.exists(EXCEL_PATH):
        df = pd.read_excel(EXCEL_PATH)
    else:
        return jsonify({'error': 'Archivo no encontrado'}), 404

    # Convertir entrada en DataFrame (1 fila)
    nueva_fila = pd.DataFrame([nueva_vuln])

    # Agregar y guardar con manejo de permisos
    try:
        df = pd.concat([df, nueva_fila], ignore_index=True)
        df.to_excel(EXCEL_PATH, index=False)
    except PermissionError:
        return jsonify({'error': 'No se pudo guardar el archivo. Asegúrate de que no esté abierto.'}), 500

    return jsonify({'mensaje': 'Información agregada correctamente'}), 201


if __name__ == '__main__':
    app.run(debug=True, port=5000)




