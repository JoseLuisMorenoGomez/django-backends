import os
import pandas as pd
import json

def cargar_estructura(nombre_archivo="puestos2022.json", nombre_salida="informacion_puestos_unidades.csv"):
    # Obtener la ruta del directorio del script actual
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta completa al archivo JSON en la subcarpeta "data"
    path_json = os.path.join(script_dir, "data", nombre_archivo)

    # Verificar si el archivo JSON existe
    if not os.path.isfile(path_json):
        raise FileNotFoundError(f"El archivo JSON no existe en la siguiente ruta: {path_json}")

    # Leer el JSON desde un archivo externo
    with open(path_json) as f:
        json_data = json.load(f)

    # Crear DataFrame de puestos
    df_puestos = pd.DataFrame(json_data)

    # Agregar un campo auxiliar para nombreUnidadOrganizativa sin redundancias
    df_puestos["nombreUnidadOrganizativa"] = df_puestos[["areaGobierno", "delegacion", "departamento", "servicio"]].apply(
        lambda row: ' - '.join(row[row.notna()].unique()), axis=1
    )

    # Crear DataFrame con la información solicitada
    df_informacion = df_puestos.copy()

    # Inicializar contadores
    df_informacion["dotacion"] = 0
    df_informacion["numeroVacantes"] = 0

    # Contar dotación y vacantes para cada unidad organizativa y tipo de puesto
    for _, group in df_puestos.groupby(["nombreUnidadOrganizativa", "TipoPuesto", "puesto"]):
        idx = group.index
        dotacion = len(idx)
        vacantes = group["situacion"].eq("VACANTE").sum()  # Contar los puestos con situacion "VACANTE"
        
        # Actualizar dotación y vacantes en el DataFrame principal
        df_informacion.loc[idx, "dotacion"] = dotacion
        df_informacion.loc[idx, "numeroVacantes"] = vacantes

    # Eliminar duplicados
    df_informacion = df_informacion.drop_duplicates(subset=["nombreUnidadOrganizativa", "TipoPuesto", "puesto"])

    # Seleccionar columnas necesarias y reordenar
    columnas_seleccionadas = [
        "nombreUnidadOrganizativa", 
        "dotacion", 
        "numeroVacantes", 
        "puesto", 
        "nombrePuesto", 
    ]
    df_informacion = df_informacion[columnas_seleccionadas]

    # Ordenar DataFrame
    df_informacion.sort_values(by=["nombreUnidadOrganizativa", "dotacion", "numeroVacantes"], inplace=True)

    # Construir la ruta completa para guardar el archivo CSV en la misma carpeta que el script
    path_csv = os.path.join(script_dir, nombre_salida)

    # Persistir DataFrame en un archivo CSV
    df_informacion.to_csv(path_csv, index=False)

# Uso de la función con el archivo por defecto y nombre de salida por defecto
cargar_estructura()











