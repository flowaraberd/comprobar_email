import imaplib
from controller.readSMS import read_sms
from controller.config import (
    HOST,
    USERNAME,
    PASSWORD
)
import ssl
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def connect_with_sms():
    # Conexión al servidor IMAP
    with imaplib.IMAP4_SSL(HOST, ssl_context=ssl_context) as client:
        # Inicio de sesión
        client.login(USERNAME, PASSWORD)

        # Seleccionar la carpeta de entrada (INBOX)
        client.select('INBOX')

        # Buscar todos los correos no leídos
        typ, data = client.search(None, 'UNSEEN')
        messages = data[0].split()
        decoded_messages = [msg.decode('utf-8') for msg in messages]

        read_sms(client=client, messages=decoded_messages)

