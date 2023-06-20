import schedule
import time
import os
from controller.connectSMS import connect_with_sms

import ssl

# Desactivar la verificación SSL
ssl._create_default_https_context = ssl._create_unverified_context


if __name__ == "__main__":
    print("Script inicializado.")
    connect_with_sms()


def cronjop():
    print("Ejecutando Cronjop cada 5 minutos")
    connect_with_sms()


# Define la tarea programada
schedule.every(1).minutes.do(cronjop)

# Ejecuta el programa en un bucle infinito
while True:
    schedule.run_pending()
    time.sleep(1)

