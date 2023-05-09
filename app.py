import xmltodict
import json
import glob
from flask import Flask

app = Flask(__name__)

todos=[]
xml_files = glob.glob('/home/asobrados03/archivos_xml/*.xml')

for file in xml_files:
    # Abrir el archivo XML y leer su contenido
    with open(file, 'r') as file_xml:
        # Convertir el XML a un diccionario de Python
        diccionario = xmltodict.parse(file_xml.read())
        todos.append(diccionario)

# Convertir el diccionario a una cadena de JSON y pasarselo a Flask
@app.route('/JSON_Vendedores')
def cadena_json():
    return json.dumps(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)