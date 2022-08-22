import pymysql

class bd:
    def __init__(self):
        self.connection = pymysql.connect(
            host="db4free.net", #ip
            user="rootcondominios",
            password="cocoblanconegro",
            db="dbcondominios"
        )

        self.cursor = self.connection.cursor()

        self.cursor.execute('select * from APARTAMENTOS_DISPONIBLES')
        myresult = self.cursor.fetchall()

        for x in myresult:
            print("")
            print(f"apartamento {x[0]} del condominio {x[1]}")
            print(f" id de apartamento: {x[0]}")
            print(f" id de condominio: {x[1]}")
            print(f" numero de habitaciones: {x[2]}")
            print(f" numero de baños: {x[3]}")
            print(f" monto de alquiler: {x[4]}")
            print("______________________________________________________________________")

database = bd()
