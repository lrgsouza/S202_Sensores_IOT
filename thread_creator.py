import threading
import time
import random
from monitor import Monitor

def thread_sensor(db,nome_sensor,intervalo):
    alarm = False
    while True:
        if alarm:
            print(f'“Atenção! Temperatura  muito  alta! Verificar {nome_sensor}!”')
            break
        else:
            #instanciando novo monitor
            monitor = Monitor(db)
            #gerando temperatura S1
            temperatura = random.randint(30, 40)
            #update do bd
            alarm = monitor.updateTemp(nome_sensor,temperatura)
            #esperando intervalo
            time.sleep(intervalo)
