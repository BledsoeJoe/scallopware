#function file for scallop
from datetime import datetime
from connection import Connection

class Scallop:
    def __init__(self, name="default"):
        self.name = name
        self._last_update = datetime.now()
        self.connections = {}

    def update_name(self, name):
        self.name = name
        self._last_update = datetime.now()

    def add_connection(self, connection):
        if not isinstance(connection, Connection):
             raise TypeError('Connections added to Scallop must be of type "Connection"')
        else:
            self.connections[connection.name] = connection
            self._last_update = datetime.now()

    def list_connections(self):
        for name, conn in self.connections.items():
            status, ping = conn.check_connection()
            print(f"Connection Name: {name}, Online: {status}, Latency: {ping}")

    def print_to(self):
        print(f"name: {self.name}\nlast update: {self._last_update}")

def test() -> None:
    print("Test Succeeded!")
