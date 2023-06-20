# import ssl

# Ruta al certificado firmado en formato PEM
# cert_path = './certificado.pem'
# cert_path_key = './claveprivada.key'
#
# # Crear el contexto SSL con el certificado
# ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# ssl_context.load_cert_chain(certfile=cert_path, keyfile=cert_path_key, password='123456')

# Configuracion del servidor y las credenciales

HOST = 'mail.recarxpress.com'
USERNAME = 'referenciasbanco@recarxpress.com'
PASSWORD = '&DDeNo_mcNBd'

# Configuracion de la Base de datos
DATABASE_CONFIG = {
    'username': 'recarxpr_referencias',
    'password': 'K%#-o[j$fBJT',
    'host': '69.46.6.238',
    'port': 3306,
    'database': 'recarxpr_referencias',
    'raise_on_warnings': True,
    # 'ssl_disabled': False,
    # 'ssl_ca': cert_path,
    # 'ssl_cert': cert_path,
    # 'ssl_key': cert_path,
    # 'ssl_verify_cert': True,
    # 'ssl_context': ssl_context
}