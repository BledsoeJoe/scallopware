"""Main file to test functions"""
import time
from scallop import Scallop
from connection import Connection

def main() -> None:
"""Main method"""
    test = Scallop("test")
    test.print_to()
    time.sleep(3)
    test.update_name("new name")
    test.print_to()


    conn = Connection("google", "google.com")
    test.add_connection(conn)
    test.list_connections()

if __name__ == "__main__" :
    main()
