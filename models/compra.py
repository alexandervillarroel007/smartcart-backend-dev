# models/compra.py
from config import conectar_db
from datetime import datetime

# Registrar una compra sin id_cliente (usa solo carrito y total)
# 📁 models/compra.py
# 📁 models/compra.py

# 📁 models/compra.py
def registrar_compra(id_carrito, total, nombre_cliente=None, nit_cliente=None, metodo_pago="Simulado"):
    print("🚨 ENTRANDO A FUNCION registrar_compra CORRECTA 🚨")
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            
            print("🧾 VALORES A INSERTAR:")
            print("carrito:", id_carrito)
            print("total:", total)
            print("nombre_cliente:", nombre_cliente)
            print("nit_cliente:", nit_cliente)
            print("metodo_pago:", metodo_pago)

            cursor.execute("""
                INSERT INTO compras (id_carrito, total, nombre_cliente, nit_cliente, metodo_pago, fecha)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (
                id_carrito,
                total,
                nombre_cliente,
                nit_cliente,
                metodo_pago,
                datetime.now()
            ))

            id_nueva_compra = cursor.fetchone()[0]
            conexion.commit()
            conexion.close()
            return id_nueva_compra
        except Exception as e:
            print("❌ Error al registrar compra:", e)
            return None
