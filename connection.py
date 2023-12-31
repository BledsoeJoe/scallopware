"""
This module creates a connection object to store information about data sources

Classes:
- Connection: A connection class to store information on added data sources' connections

"""
from dataclasses import dataclass
from ping3 import ping

@dataclass
class Connection:
    """
    Class that defines connection to a single data source

    Attributes:
        name (str): Name of the connection
        url (str): The url of the data source
    """
    _name: str
    _url: str
    _online: bool
    _response_time: float

    def __init__(self, name, url):
        self._name = name
        self._url = url
        self._online = False
        self._response_time = None

    def get_name(self) -> str:
        """ 
        Getter for connection's name.
            Returns:
                str: name of the connection
        """
        return self._name

    def get_url(self) -> str:
        """
        Getter for connection's url.
            Returns:
                str: url of the connection
        """
        return self._url

    def check_connection(self) -> [bool, float]:
        """
        Checks the status of the connection.
            Returns:
                bool: whether the destination is reachable
                float: the conneciton latency
        """
        self._response_time = ping(self._url)

        if self._response_time is not None:
            self._online = True

        return self._online, self._response_time

    def update(self, name=None, url=None) -> None:
        """
        Updates the name and/or url of the connection
            Args:
                name (str): Updated name
                url (str): Updated url
        """
        if name is not None:
            self._name = name
        if url is not None:
            self._url = url
