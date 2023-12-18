import json
import csv
import os
import pandas as pd

class Organismo:
    def __init__(self, id, parent_id, tipo_organo):
        self.id = id
        self.parent_id = parent_id
        self.tipo_organo = tipo_organo

# Obtener la ruta del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta al archivo JSON dentro de la subcarpeta 'data'
json_path = os.path.join(script_dir, 'data', 'puestos2023.json')

# Ruta al archivo CSV de jerarquía dentro de la subcarpeta 'data'
csv_path = os.path.join(script_dir, 'data', 'departamentos2023.csv')

# Ruta al archivo CSV de puestos con jerarquía de departamentos dentro de la subcarpeta 'data'
csv_puestos_path = os.path.join(script_dir, 'data', 'puestos_departamentos.csv')

print(f"La ruta completa al archivo JSON es: {os.path.abspath(json_path)}")

# Lee el JSON desde el archivo
with open(json_path, "r", encoding="utf-8") as json_file:
    datos_json = json.load(json_file)

# Contador para registros anómalos
registros_anomalos = 0

# Crear nodo raíz (Ayuntamiento)
organismo_raiz = Organismo(999999, None, "Ayuntamiento")
organismos = [organismo_raiz]

# Diccionario para almacenar la relación ID de puestos y ID de departamentos
id_departamentos = {}

# Procesar los datos JSON y construir la jerarquía
for i, registro in enumerate(datos_json, start=1):
    parent = organismo_raiz  # Comenzamos desde el Ayuntamiento
    for tipo_organo in [registro["areaGobierno"], registro["delegacion"], registro["servicio"], registro["departamento"]]:
        if not tipo_organo or not isinstance(tipo_organo, str):
            # Registro anómalo, el nombre está en blanco o no es un valor de texto
            print(f"Advertencia: Registro anómalo encontrado en el registro JSON {i}.")
            registros_anomalos += 1
            continue

        node_id = len(organismos) + 1
        node = Organismo(node_id, parent.id if parent else None, tipo_organo)
        organismos.append(node)

        # Almacenar la relación ID de puestos y ID de departamentos
        if "puesto" in registro and "departamento" in registro:
            id_departamentos[registro["puesto"]] = node.id

        parent = node  # Actualizamos el padre para el próximo nivel

# Escribir la jerarquía en el archivo CSV
with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=";")

    # Encabezados del CSV
    csv_writer.writerow(["ID", "Parent_ID", "Tipo_Organo"])

    # Datos de la jerarquía
    for organismo in organismos:
        csv_writer.writerow([organismo.id, organismo.parent_id, organismo.tipo_organo])

print(f"La jerarquía se ha guardado en {csv_path}")

# Mostrar el número de registros anómalos encontrados
print(f"Registros anómalos encontrados: {registros_anomalos}")

# Crear DataFrame de puestos con jerarquía de departamentos
puestos_data = []
for registro in datos_json:
    if "puesto" in registro and "nombrePuesto" in registro and registro["puesto"] in id_departamentos:
        id_departamento = id_departamentos[registro["puesto"]]
        puesto_data = {
            "id_departamento": id_departamento,
            "Puesto": registro["puesto"],
            "Nombre": registro["nombrePuesto"],
            "TipoPuesto": registro.get("TipoPuesto", ""),
            "tipoPersonal": registro.get("tipoPersonal", ""),
            "formaProvision": registro.get("formaProvision", ""),
            "adcripcionGrupos": registro.get("adcripcionGrupos", ""),
            "adcripcionEscalas": registro.get("adcripcionEscalas", ""),
            "nivelComplementoDestino": registro.get("nivelComplementoDestino", ""),
            "complementoEspecificoPuntos": registro.get("complementoEspecificoPuntos", ""),
            "complementoEspecificoEuros": registro.get("complementoEspecificoEuros", ""),
            "observacionesRequisitos": registro.get("observacionesRequisitos", ""),
            "situacion": registro.get("situacion", ""),
            # Agregar más campos según sea necesario
        }
        puestos_data.append(puesto_data)

# Crear DataFrame
puestos_df = pd.DataFrame(puestos_data)

# Reordenar columnas y renombrar
puestos_df = puestos_df[["id_departamento", "Puesto", "Nombre", "TipoPuesto", "tipoPersonal", "formaProvision",
                         "adcripcionGrupos", "adcripcionEscalas", "nivelComplementoDestino",
                         "complementoEspecificoPuntos", "complementoEspecificoEuros", "observacionesRequisitos",
                         "situacion"]]

# Guardar DataFrame en CSV
puestos_df.to_csv(csv_puestos_path, index=False, sep=";")

print(f"El DataFrame de puestos con jerarquía de departamentos se ha guardado en {csv_puestos_path}")











