import os
import pandas as pd
from datetime import datetime
import json
import shutil
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))

def cargar_rpt(nombre_archivo, year):
    json_path = os.path.join(script_dir, 'data', nombre_archivo)
    if not os.path.isfile(json_path):
        raise FileNotFoundError(f"El archivo JSON no existe en la siguiente ruta: {json_path}")

    with open(json_path, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)
    
    return json_data


# FASE 1: fabricar la jerarquia de departamentos a partir del json de la rpt

def montar_departamentos(nombre_json, nombre_csv, year)
        def __init__(self, id, parent_id, tipo_organo):
            self.id = id
            self.parent_id = parent_id
            self.tipo_organo = tipo_organo

    json_data = cargar_rpt(nombre_json)
        
    registros_anomalos = 0
    organismo_raiz = Organismo(999999, None, "Ayuntamiento")
    organismos = [organismo_raiz]

    for i, registro in enumerate(json_data, start=1):
        parent = organismo_raiz
        for tipo_organo in [registro["areaGobierno"], registro["delegacion"], registro["servicio"], registro["departamento"]]:
            if not tipo_organo or not isinstance(tipo_organo, str):
                print(f"Advertencia: Registro anómalo encontrado en el registro JSON {i}.")
                registros_anomalos += 1
                continue

            node_id = len(organismos) + 1
            node = Organismo(node_id, parent.id if parent else None, tipo_organo)
            organismos.append(node)
            parent = node
            
    csv_path = os.path.join(script_dir, 'data', year, nombre_csv)
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"El archivo CSV no existe en la siguiente ruta: {csv_path}")

    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";")
        csv_writer.writerow(["ID", "Parent_ID", "Tipo_Organo"])
        for organismo in organismos:
            csv_writer.writerow([organismo.id, organismo.parent_id, organismo.tipo_organo])

    print(f"La jerarquía se ha guardado en {csv_path}")
    print(f"Registros anómalos encontrados: {registros_anomalos}")
    
    return organismos

def montar_puestos(nombre_archivo="puestos.json", nombre_salida="puestos2022.csv", year=None):
    json_data = cargar_rpt(nombre_archivo)
    
    df_puestos = pd.DataFrame(json_data)
    df_puestos["nombreUnidadOrganizativa"] = df_puestos[["areaGobierno", "delegacion", "departamento", "servicio"]].apply(
        lambda row: ' - '.join(row[row.notna()].unique()), axis=1
    )

    df_informacion = df_puestos.copy()
    df_informacion["dotacion"] = 0
    df_informacion["numeroVacantes"] = 0

    for _, group in df_puestos.groupby(["nombreUnidadOrganizativa", "TipoPuesto", "puesto"]):
        idx = group.index
        dotacion = len(idx)
        vacantes = group["situacion"].eq("VACANTE").sum()

        df_informacion.loc[idx, "dotacion"] += dotacion
        df_informacion.loc[idx, "numeroVacantes"] += vacantes

    df_informacion = df_informacion.drop_duplicates(subset=["nombreUnidadOrganizativa", "TipoPuesto", "puesto"])
    columnas_seleccionadas = ["puesto", "nombrePuesto", "nombreUnidadOrganizativa", "dotacion", "numeroVacantes"]
    df_informacion = df_informacion[columnas_seleccionadas]
    df_informacion.sort_values(by=["nombreUnidadOrganizativa", "dotacion", "numeroVacantes"], inplace=True)

    if year is None:
        year = datetime.now().year
    else:
        year = int(year)

    output_subdir = os.path.join(script_dir, 'data', str(year))
    if not os.path.exists(output_subdir):
        os.makedirs(output_subdir)

    csv_path = os.path.join(output_subdir, nombre_salida)

    df_informacion.to_csv(csv_path, index=False)
    
    return df_informacion

if __name__ == "__main__":
    montar_departamentos("nombre_json.json", "nombre_csv.csv", year=2023)
    montar_puestos(nombre_archivo="puestos2022.json", nombre_salida="puestos2022.csv", year=2023)

