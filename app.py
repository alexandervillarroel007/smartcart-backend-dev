
 
from flask import Flask
from flask_cors import CORS
from config import conectar_db
from config import SECRET_KEY
# Importar blueprints
from routes.token import token_bp
from routes.productos import productos_bp
from routes.usuarios import usuarios_bp
from routes.auth import auth_bp
from routes.bitacoras import bitacora_bp
from routes.carrito import carrito_bp
from routes.detalle_carrito import detalle_carrito_bp
from routes.ventas import ventas_bp
from routes.clientes import clientes_bp
from routes.inventario import inventario_bp
from routes.reportes import reportes_bp
from routes.roles import roles_bp
from routes.categorias import categorias_bp
from routes.catalogo import catalogo_bp
from flask_sqlalchemy import SQLAlchemy
#from routes.stripe_checkout import stripe_checkout_bp
from routes.simular_pago import simular_pago_bp
from routes.reportes_compras import reportes_compras_bp
import os
from routes.calificacion import calificacion_bp
from routes.voz.procesar_comando import procesar_comando_bp
from routes.voz.voz_inteligente import voz_inteligente_bp
from routes.voz.comandos_voz import comandos_voz_bp
from routes.compras import compras_bp
#from routes.voz.comandos_voz import utilidades_voz_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY  # Usa la que tienes en config.py

#app.config['SECRET_KEY'] = 'clave_secreta_smart_cart'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tu_contraseña@localhost:5432/smart_cart'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tu_contraseña@localhost:5432/smart_cart'

# Conexión a base de datos en Render
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
#CORS(app)

# Conexión inicial (opcional)
#conexion = conectar_db()

# Registrar rutas
app.register_blueprint(token_bp)
app.register_blueprint(productos_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(bitacora_bp)
app.register_blueprint(carrito_bp)
app.register_blueprint(detalle_carrito_bp)
app.register_blueprint(ventas_bp)
app.register_blueprint(clientes_bp)
app.register_blueprint(inventario_bp)
app.register_blueprint(reportes_bp)
app.register_blueprint(roles_bp)
app.register_blueprint(categorias_bp)
app.register_blueprint(catalogo_bp)
#app.register_blueprint(stripe_checkout_bp)
app.register_blueprint(simular_pago_bp)
app.register_blueprint(reportes_compras_bp)
app.register_blueprint(calificacion_bp)

app.register_blueprint(compras_bp)
app.register_blueprint(procesar_comando_bp)
app.register_blueprint(voz_inteligente_bp)
app.register_blueprint(comandos_voz_bp)
 
#app.register_blueprint(utilidades_voz_bp)

@app.route('/')
def home():
    return '🚀 ¡Smart Cart backend funcionando!'

if __name__ == '__main__':
    print("🔍 Rutas registradas:")
    print(app.url_map)


    app.run(debug=True, host='0.0.0.0', port=5000)
