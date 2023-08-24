import psycopg2
import pandas as pd

# Configura la conexión a la base de datos
conn = psycopg2.connect(
    dbname="bd_curso1",
    user="postgres",
    password="098023190",
    host="localhost",
    port="5432"
)

# Función para obtener la información de las tablas en el esquema especificado
def obtener_informacion_tablas(esquema):
    cursor = conn.cursor()
    query = f"""
        SELECT column_name, data_type, character_maximum_length, is_nullable
        FROM information_schema.columns
        WHERE table_schema = '{esquema}'
    """
    cursor.execute(query)
    columnas = cursor.fetchall()
    cursor.close()
    return columnas

# Función para generar el diccionario a partir de la información de las tablas
def generar_diccionario():
    cursor = conn.cursor()
    query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public' -- Cambia 'public' por el esquema deseado
    """
    cursor.execute(query)
    tablas = cursor.fetchall()

    diccionario = {}
    for tabla in tablas:
        tabla_nombre = tabla[0]
        diccionario[tabla_nombre] = obtener_informacion_tablas('public' if tabla_nombre == 'public' else tabla_nombre)

    cursor.close()
    print(diccionario)
    return diccionario

# Ejecuta la función para generar el diccionario
diccionario_db = generar_diccionario()

# Convierte el diccionario en un DataFrame de pandas
df = pd.DataFrame.from_dict(diccionario_db)

# Guarda el DataFrame en un archivo Excel (.xlsx)
nombre_archivo_excel = 'diccionario_db.xlsx'
df.to_excel(nombre_archivo_excel, index=False)

# Cierra la conexión a la base de datos
conn.close()
