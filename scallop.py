#main function file
from datetime import datetime

class scallop:
   def __init__(self, name="default"):
      self.name = name
      self.last_update = datetime.now()

   def update(self, name):
      self.name = name
      self.last_update = datetime.now()
   def print_to(self):
      print(f"name: {self.name}\nlast update: {self.last_update}")

def test() -> None:
   print("Test Succeeded!")
