import pandas
from management import montar_puestos, montar_jerarquia
from datetime import datetime

year = datetime.now().year
nombre_archivo = "puestos" + str(year) + ".json"
nombre_salida_puestos = "puestos" + str(year) + ".csv"
nombre_salida_jerarquia = "departamentos" + str(year) + ".csv"

df_puestos = montar_puestos(nombre_archivo, nombre_salida_puestos)
df_jerarquia = montar_jerarquia(df_puestos, nombre_salida_jerarquia)
