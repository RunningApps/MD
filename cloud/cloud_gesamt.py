import sqlite3
import time


class Cloud:
    def __init__(self):   
        self.conn = sqlite3.connect('cloud.db')
        self.c = self.conn.cursor()

    def create_cloud(self, table):
        self.c.execute(f"CREATE TABLE IF NOT EXISTS {table}\n(id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT)")
        print(f"Cloud {table} erstellt")

    def del_data(self, table):
        self.c.execute(f"DELETE FROM {table}")  # Die Tabelle "messages" leeren
        self.conn.commit()
        print(f"Clouddaten von {table} geleert")
    
    def stop_cloud(self):
        self.conn.close()

    def send_to_topic(topic, message):
        conn = sqlite3.connect('cloud.db')
        c = conn.cursor()
        c.execute(f"INSERT INTO {topic} (message) VALUES (?)", (message,))
        conn.commit()
        conn.close()


#Beispielbefehle:
cloud = Cloud()
cloud.create_cloud("arduino")
cloud.create_cloud("nothalt")
cloud.create_cloud("gui")

cloud.send_to_topic("arduino", "ARDUINO: distance_up,distance_down;distance_right;distance_left;temperature;humidity;air_dust_density;brush1_speed;brush2_speed;flow_velocity;vibration")
cloud.send_to_topic("gui","test")

cloud.del_data("arduino")

cloud.stop_cloud()
