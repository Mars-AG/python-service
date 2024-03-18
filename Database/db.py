import mysql.connector
from Config.EnvService import Env

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=Env.get('MYSQL_HOST'),
            port=int(Env.get('MYSQL_PORT')),
            user=Env.get('MYSQL_USER'),
            password=Env.get('MYSQL_PASSWORD'),
            database=Env.get('MYSQL_DATABASE')
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, data=None):
        if data:
            self.cursor.executemany(query, data)
        else:
            self.cursor.execute(query)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()