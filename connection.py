#connection function file
from ping3 import ping
"""
This module creates a connection object to store information about data sources

Classes:
- Connection: A connection class to store information on added data sources' connections

"""

class Connection:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self._online = False
        self._respons_time = None

   #test the connections url and update attributes
    def check_connection(self) -> [bool, float]:
        self._response_time = ping(self.url)

        if self._response_time is not None:
            self._online = True

        return self._online, self._response_time
