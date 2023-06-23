from scallop import scallop
import time

def main() -> None:
   test = scallop("test")
   test.print_to()
   time.sleep(10)
   test.update("new name")
   test.print_to()

if __name__ == "__main__" :
    main()


#test()
