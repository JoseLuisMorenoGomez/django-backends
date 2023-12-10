import json
import csv
import os

class Organismo:
    def __init__(self, id, parent_id, tipo_organo):
        self.id = id
        self.parent_id = parent_id
        self.tipo_organo = tipo_organo
        self.hijos = []

# Obtener la ruta del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta al archivo JSON dentro de la subcarpeta 'data'
json_path = os.path.join(script_dir, 'data', 'puestos2023.json')

# Ruta al archivo CSV dentro de la subcarpeta 'data'
csv_path = os.path.join(script_dir, 'data', 'departamentos2023.csv')

print(f"La ruta completa al archivo JSON es: {os.path.abspath(json_path)}")

# Lee el JSON desde el archivo
with open(json_path, "r", encoding="utf-8") as json_file:
    datos_json = json.load(json_file)

# Crear nodo raíz (Ayuntamiento)
organismo_raiz = Organismo(999999, None, "Ayuntamiento")
organismos = [organismo_raiz]

# Diccionario para realizar un seguimiento de nodos existentes por tipo_organo
nodos_por_tipo = {"Ayuntamiento": organismo_raiz}

# Procesar los datos JSON y construir la jerarquía
for registro in datos_json:
    parent = organismo_raiz  # Comenzamos desde el Ayuntamiento
    for tipo_organo in [registro["areaGobierno"], registro["delegacion"], registro["servicio"], registro["departamento"]]:
        # Obtener o crear un nodo con el mismo tipo_organo
        if tipo_organo in nodos_por_tipo:
            nodo_existente = nodos_por_tipo[tipo_organo]
        else:
            # Si no existe, crear un nuevo nodo y agregarlo como hijo
            node_id = len(organismos) + 1
            nodo_existente = Organismo(node_id, parent.id if parent else None, tipo_organo)
            organismos.append(nodo_existente)
            nodos_por_tipo[tipo_organo] = nodo_existente
            parent.hijos.append(nodo_existente)

        parent = nodo_existente  # Actualizar el padre para el próximo nivel

# Escribir la jerarquía en el archivo CSV
with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=";")

    # Encabezados del CSV
    csv_writer.writerow(["ID", "Parent_ID", "Tipo_Organo"])

    # Función recursiva para escribir los datos
    def escribir_organismo(organismo):
        csv_writer.writerow([organismo.id, organismo.parent_id, organismo.tipo_organo])
        for hijo in organismo.hijos:
            escribir_organismo(hijo)

    # Datos de la jerarquía
    escribir_organismo(organismo_raiz)

print(f"La jerarquía se ha guardado en {csv_path}")






