from time import sleep
from threading import *


def display1():
    for i in range(20):
        print("Hi I am the Player - 1 playing the Game")
        sleep(2)


def display2():
    for i in range(20):
        print("Hi I am the Player - 2 playing the Game")
        sleep(2)


thread1 = Thread(target=display1)
thread2 = Thread(target=display2)

thread1.start()
sleep(1)
thread2.start()

thread1.join()
thread2.join()

print("Bye, The Game is Ended for both the Players!!!!!")
