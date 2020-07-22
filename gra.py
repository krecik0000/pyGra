import random
import os 
import time

choiceMenu = 0

while choiceMenu != 3:
    print("|1|Play")
    print("|2|Upgrades")
    print("|3|Exit")
    choiceMenu = int(input(":"))
    if choiceMenu == 1:
        #play()
        print("1")
    elif choiceMenu == 2:
        #upgrades()
        print("2")
    elif choiceMenu != 3 and choiceMenu != 1 and choiceMenu != 2:
        print("invalid keys pressed")
