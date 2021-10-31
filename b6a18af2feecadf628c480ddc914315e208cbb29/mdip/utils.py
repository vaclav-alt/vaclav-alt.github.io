from IPython.display import Image, display
from time import sleep

def display_duck():
    for i in range(5, 0, -1):
        print("\r{}".format(i), end="")
        sleep(1)
        
    print("\rGet READY!")
    sleep(2)
        
    display(Image(filename = "duck.jpeg"))