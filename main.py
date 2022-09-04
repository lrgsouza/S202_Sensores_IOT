import threading

from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.sensores import dataset
from thread_creator import thread_sensor

##### == Exercício Avaliativo 1 –Simula Sensores== ####

#criando e resetando db
db = Database("bancoiot","sensores",dataset)
db.resetDatabase()

#iniciando threads
S1 = threading.Thread(target=thread_sensor(db,'Sensor_1',0.5))
S2 = threading.Thread(target=thread_sensor(db,'Sensor_2',0.5))
S3 = threading.Thread(target=thread_sensor(db,'Sensor_3',0.5))

#start threads
S1.start()
S2.start()
S3.start()

