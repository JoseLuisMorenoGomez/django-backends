import os
import pandas as pd
from datetime import datetime
import shutil

def extract_and_save_csv(input_csv, output_dir, year=None):
    # Obtener el año actual si no se proporciona uno
    if year is None:
        year = datetime.now().year
    else:
        year = int(year)

    # Crear la subcarpeta con el nombre del año
    year_folder = str(year)
    output_subdir = os.path.join(output_dir, year_folder)

    if not os.path.exists(output_subdir):
        os.makedirs(output_subdir)

    # Obtener la ruta completa del archivo CSV de entrada
    input_csv_path = os.path.join(output_subdir, os.path.basename(input_csv))

    # Cargar el DataFrame desde el archivo CSV
    df = pd.read_csv(input_csv_path, encoding="utf-8", delimiter=";")

    # Extraer y guardar archivos CSV para cada campo
    fields = ["TipoPuesto", "tipoPersonal", "formaProvision", "adcripcionGrupos", "adcripcionEscalas"]
    for field in fields:
        # Obtener valores únicos de la columna
        unique_values = df[field].unique()

        # Crear un DataFrame con valores únicos
        unique_df = pd.DataFrame({field: unique_values})

        # Construir el nombre del archivo CSV de salida
        output_csv = os.path.join(output_subdir, f"{field.lower()}.csv")

        # Guardar el DataFrame como CSV
        unique_df.to_csv(output_csv, index=False)

        print(f"Archivo CSV {field.lower()}.csv creado en {os.path.abspath(output_csv)}")

def main():
    # Obtener la ruta completa del archivo CSV de entrada
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(script_directory, "data", "puestos_departamentos.csv")

    # Obtener la ruta completa del directorio de salida
    output_directory = os.path.join(script_directory, "data")

    # Obtener el año deseado como parámetro
    target_year = input("Ingrese el año deseado para los archivos (deje en blanco para el año actual): ")

    # Manejo de casos para el escenario de cadena vacía
    if not target_year:
        target_year = None

    # Extraer y guardar archivos CSV para cada campo
    extract_and_save_csv(input_csv, output_directory, target_year)

if __name__ == "__main__":
    main()





