from datetime import date 
from art import startup 

today = date.today() 

startup()
run = True

while run == True:
    load = input("Would you like to load today's adventures? (yes/no) ").lower()

    if load == "no":
        while run == True: 
            load2 = input("Would you load old hunts and quests? (yes/no)")
            if load2 == "yes":
                print("Holy peak lets do this")
                print("loading old hunts...")
                # old_hunts()
                print("loading old quests...")
                # old_quests()
            elif load2 == "no": 
                print()
                print("Okie smokie, cutie!")
                print("Come back when you're ready to start a new day!")
                print(" I LOVE YOU SO MUCH")
                run = False
                break
            else: 
                print()
                print("Hmm... I don't recognize that answer. ")
                print("Please enter 'yes' or 'no'.")
                print()

    elif load == "i<3u":
        print()
        print("Awww... I love you too!! ")
        print("In fact I love you so much that here's a bonus quest!")
        print()
        print("Loading SECRET quest...")
        # load_quests()
        break

    elif load == "yes":
        print()
        print("AWESOME! Let's get started! ")
        print()
        print("Checking for quests...")
        # load_quests()
        print("Loading today's hunt...")
        # load_hunts()
        break

    else:
        print()
        print("Hmm... I don't recognize that answer. ")
        print("Please enter 'yes' or 'no'.")
        print()


