from datetime import date 
from art import startup 
from hunt import load_hunts
from quests import load_quests
today = date.today() 

startup()
run = True

while run == True:
    load = input("Would you like to load today's hunts? (yes/no) ").lower()

    if load == "no":
        print()
        print("──────────────────────────────────────────────────────────────")
        print("Okie smokie, cutie!")
        print("Come back when you're ready to start a new day!")
        print("I LOVE YOU SO MUCH")
        print("──────────────────────────────────────────────────────────────")
        run = False
        break

    elif load == "yes":
        print()
        print("──────────────────────────────────────────────────────────────")
        print("AWESOME! Let's get started! ")
        print()
        print("Loading today's hunt...")
        load_hunts(today.day)
        break

    elif load == "i<3u":
        print()
        print("──────────────────────────────────────────────────────────────")
        print("Awww... I love you too!! ")
        print("In fact I love you so much that here's a bonus quest!")
        print()
        print("Loading SECRET quest...")
        print("──────────────────────────────────────────────────────────────")
        load_quests(today.day)
        break

    else:
        print()
        print("──────────────────────────────────────────────────────────────")
        print("Hmm... I don't recognize that answer. ")
        print("Please enter 'yes' or 'no'.")
        print("──────────────────────────────────────────────────────────────")
        print()


while run == True:
    load = input("Would you like to load today's quests? (yes/no) ").lower()

    if load == "no":
        print()
        print("──────────────────────────────────────────────────────────────")
        print("Okie smokie, cutie!")
        print("Come back when you're ready to start a new day!")
        print("I LOVE YOU SO MUCH")
        print("──────────────────────────────────────────────────────────────")
        run = False
        break

    elif load == "yes":
        print()
        print("──────────────────────────────────────────────────────────────")
        print("AWESOME! Let's get started! ")
        print()
        print("Checking for quests...")
        print("──────────────────────────────────────────────────────────────")
        load_quests(today.day)        
        break

    elif load == "i<3u":
        print()
        print("──────────────────────────────────────────────────────────────")
        print("Awww... I love you too!! ")
        print("In fact I love you so much that here's a bonus quest!")
        print()
        print("Loading SECRET quest...")
        print("──────────────────────────────────────────────────────────────")
        load_quests(today.day)
        break

    else:
        print()
        print("──────────────────────────────────────────────────────────────")
        print("Hmm... I don't recognize that answer. ")
        print("Please enter 'yes' or 'no'.")
        print("──────────────────────────────────────────────────────────────")
        print()
