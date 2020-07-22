import random
import os 
import time

def play():
    print("1")

def menu():
    choiceMenu = 0
    while choiceMenu != 3:  #Menu loop which will be executed until you click "3" button
        print("GAME NAME")
        print("|1|Play")
        print("|2|Upgrades")
        print("|3|Exit")
        try: #Try input number
            choiceMenu = int(input(":")) 
            os.system("cls")
            if choiceMenu == 1:          
                play()
            elif choiceMenu == 2:
                #upgrades()
                print("2")
            elif choiceMenu != isinstance(choiceMenu,str) and choiceMenu != 3 and choiceMenu != 1 and choiceMenu != 2:
                print("Ops! try use correct numbers")
                time.sleep(1)
                os.system("cls")
        except ValueError:     #When input value is not a number print this exception
            os.system("cls")
            print("Ops! try use number keys")
            time.sleep(1)
            os.system("cls")

os.system("cls")
menu()