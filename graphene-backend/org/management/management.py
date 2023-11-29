import os
import pandas as pd
import json

# Obtener la ruta del directorio del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

def cargar_rpt(nombre_archivo):
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
    
    return df_puestos


def montar_puestos(nombre_archivo="puestos2022.json", nombre_salida="puestos2022.csv"):
    # Cargar un df desde el json
    df_puestos = cargar_rpt(nombre_archivo)

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
        vacantes = group["situacion"].eq("VACANTE").sum()  # Contar los puestos con situación "VACANTE"

        # Actualizar dotación y vacantes en el DataFrame principal
        df_informacion.loc[idx, "dotacion"] += dotacion
        df_informacion.loc[idx, "numeroVacantes"] += vacantes

    # Eliminar duplicados después del bucle
    df_informacion = df_informacion.drop_duplicates(subset=["nombreUnidadOrganizativa", "TipoPuesto", "puesto"])

    # Seleccionar columnas necesarias y reordenar después del bucle
    columnas_seleccionadas = ["puesto", "nombrePuesto", "nombreUnidadOrganizativa", "dotacion", "numeroVacantes"]
    df_informacion = df_informacion[columnas_seleccionadas]

    # Ordenar DataFrame después del bucle
    df_informacion.sort_values(by=["nombreUnidadOrganizativa", "dotacion", "numeroVacantes"], inplace=True)

    # Construir la ruta completa para guardar el archivo CSV
    path_csv = os.path.join(script_dir, "data", nombre_salida)

    # Persistir DataFrame en un archivo CSV después del bucle
    df_informacion.to_csv(path_csv, index=False)
    
    # Visualización del DataFrame
    print("DataFrame de Información:")
    print(df_informacion)

    return df_informacion


def montar_jerarquia(df_informacion, nombre_salida="departamentos2022.csv"):
    # Supongamos que df_informacion es el DataFrame con la columna 'nombreUnidadOrganizativa'
    # y que ya has ejecutado el código para obtener df_informacion

    # Crear una lista para construir el DataFrame de jerarquía
    jerarquia_list = []

    # Conjunto para rastrear nodos ya agregados
    nodos_agregados = set()

    # Obtener Niveles Únicos
    niveles_unicos = set()
    for nombre in df_informacion['nombreUnidadOrganizativa']:
        niveles_unicos.update(nombre.split(' - '))

    # Asignar IDs Únicos
    id_mapping = {nombre: idx + 1 for idx, nombre in enumerate(niveles_unicos)}

    # Dividir Niveles y Asignar Parent_ID
    for nombre in df_informacion['nombreUnidadOrganizativa']:
        niveles = nombre.split(' - ')
        for i, nivel in enumerate(niveles):
            # Verificar si el nodo ya ha sido agregado
            if nivel not in nodos_agregados:
                jerarquia_list.append({'id': id_mapping[nivel], 'parent_id': id_mapping[niveles[i-1]] if i > 0 else None, 'name': nivel})
                nodos_agregados.add(nivel)  # Agregar nodo al conjunto

    # Crear DataFrame de jerarquía
    df_jerarquia = pd.DataFrame(jerarquia_list)

    # Convertir ID y Parent_ID a enteros
    df_jerarquia['id'] = df_jerarquia['id'].astype(int)
    df_jerarquia['parent_id'] = df_jerarquia['parent_id'].astype(pd.Int64Dtype()) 
    
    # Construir la ruta completa para guardar el archivo CSV de la Jerarquía
    path_csv_jerarquia = os.path.join(script_dir, "data", nombre_salida)

    # Persistir DataFrame Jerárquico en un archivo CSV
    df_jerarquia.to_csv(path_csv_jerarquia, index=False)

    # Mostrar el DataFrame jerárquico
    print("DataFrame Jerárquico:")
    print(df_jerarquia)
    
    return df_jerarquia
