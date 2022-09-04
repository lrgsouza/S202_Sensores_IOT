from helper.WriteAJson import writeAJson

class Monitor():

    def __init__(self,db):
        self.db = db

    def updateTemp(self,nome_sensor,value):
        #mostrando no terminal
        unidade_medida = self.db.readOne(nome_sensor)[0]['unidadeMedida']
        print(f'Temperatura atual do {nome_sensor} - {value}{unidade_medida}')
        self.db.update(nome_sensor,'valorSensor',value)
        alarm = True if value > 38 else False
        #atualizando doc se alrmar
        if alarm:
            self.db.update(nome_sensor,'sensorAlarmado',True)
        return alarm