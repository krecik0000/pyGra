import random
import os 
import time

class Easy:
    distance = random.randrange(9,20) #Distance difference "11"
    maxDist = distance
    minDist = 8
    shotChance = 10

class Normal:
    distance = random.randrange(9,17) #Distance difference "8"
    maxDist = distance
    minDist = 8
    shotChance = 15

class Hard:
    distance = random.randrange(9,15) #Distance difference "6"
    maxDist = distance
    minDist = 8
    shotChance = 20


choiceMenu = 0
def valueException():
    print("Ops! try use other keys")
    time.sleep(1)
    os.system("cls")

def newGame(choiceMenu):
    while choiceMenu != 4:  #Menu loop which will be executed until you click "4" button
        print("Select Difficulty Level:")
        print("|1|Easy")
        print("|2|Normal")
        print("|3|Hard")
        print("|4|Back")
        try: #Try input number
            choiceMenu = int(input(":"))
            os.system("cls")
            if choiceMenu == 1:
                print("1")               
            elif choiceMenu == 2:
                print("2")
            elif choiceMenu == 3:
                print("3")
            elif choiceMenu != isinstance(choiceMenu,str) and choiceMenu != 3 and choiceMenu != 1 and choiceMenu != 2 and choiceMenu != 4:
                valueException()
        except ValueError: #When input value is not a number print this exception
            os.system("cls")
            valueException()

def play(choiceMenu):
    while choiceMenu != 3:  #Menu loop which will be executed until you click "3" button
        print("Select Option:")
        print("|1|New Game")
        print("|2|Load Game")
        print("|3|Back")
        try: #Try input number
            choiceMenu = int(input(":"))
            os.system("cls")
            if choiceMenu == 1:
                newGame(choiceMenu)
            elif choiceMenu == 2:
                print("2")
            elif choiceMenu != isinstance(choiceMenu,str) and choiceMenu != 3 and choiceMenu != 1 and choiceMenu != 2:
                valueException()
        except ValueError: #When input value is not a number print this exception
            os.system("cls")
            valueException()
            
def menu(choiceMenu):
    while choiceMenu != 3:  #Menu loop which will be executed until you click "3" button
        print("GAME NAME")
        print("|1|Play")
        print("|2|Settings")
        print("|3|Exit")
        try: #Try input number
            choiceMenu = int(input(":")) 
            os.system("cls")
            if choiceMenu == 1:          
                play(choiceMenu)
            elif choiceMenu == 2:
                #settings()
                print("2")
            elif choiceMenu != isinstance(choiceMenu,str) and choiceMenu != 3 and choiceMenu != 1 and choiceMenu != 2:
                valueException()
        except ValueError:     #When input value is not a number print this exception
            os.system("cls")
            valueException()

os.system("cls")
menu(choiceMenu)