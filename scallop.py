"""
This module provides the main utility of this library, which filters 
information out of streams of data

Classes:
- Scallop: The highest level object that provides the ability to 
add/modify/remove connections and retrieve information
"""
from datetime import datetime
from connection import Connection

class Scallop:
    """
    The highest level object that provides the ability to
    add/modify/remove connections and retreive information
    """
    def __init__(self, name="default"):
        self._name = name
        self._connections = {}
        self._last_update = datetime.now()

    def update_name(self, name) -> None:
        """
        Updates name of scallop
            Args:
                name (str): new name for scallop
        """
        self._name = name
        self._last_update = datetime.now()

    def add_connection(self, connection) -> None:
        """
        Adds new connection
            Args:
                connection (Connection): connection to be added to scallop
        """
        if not isinstance(connection, Connection):
            raise TypeError('Connections added to Scallop must be of type "Connection"')

        self._connections[connection.get_name()] = connection
        self._last_update = datetime.now()

    def list_connections(self) -> None:
        """ Prints all the connections and their statuses """
        for name, conn in self._connections.items():
            status, ping = conn.check_connection()
            print(f"Connection Name: {name}, Online: {status}, Latency: {ping}")

    def print_to(self) -> None:
        """ Prints info about the scallop instance """
        print(f"name: {self._name}\nlast update: {self._last_update}")
