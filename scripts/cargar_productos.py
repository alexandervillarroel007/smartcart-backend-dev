# 📁 scripts/cargar_productos.py

import csv
import psycopg2

# Conexión a PostgreSQL
conn = psycopg2.connect(
    database="smart_cart",  # Asegúrate de que el nombre es correcto
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Leer CSV (asegúrate de estar en la carpeta del proyecto)
with open('C:/Users/Alexader/OneDrive/Desktop/18042025(1)/smart_cart_backend/scripts/productos_utf8.csv', newline='', encoding='utf-8') as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila in lector:
        cursor.execute("""
            INSERT INTO productos (nombre, descripcion, precio, stock, umbral_minimo, umbral_maximo, modelo, id_categoria, imagen, visible)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            fila['nombre'],
            fila['descripcion'],
            float(fila['precio']),
            int(fila['stock']),
            int(fila['umbral_minimo']),
            int(fila['umbral_maximo']),
            fila['modelo'],
            int(fila['id_categoria']),
            fila['imagen'],
            fila['visible'].strip().lower() == 'true'  # Convierte a booleano
        ))

conn.commit()
conn.close()
print("✅ Datos cargados correctamente.")
