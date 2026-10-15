
hunt_1 = "Where you ride but never drive, your next clue waits where a the cutest girl would sit."
hunt_2 = "Where dirty things become clean and stink meets its match, your next clue is hiding among the supplies."
hunt_3 = "I am soft, I am comfy, and you play zelda on top of me! Search where you sit and cuddle."
hunt_4 = "I lie beneath your feet but rarely get a second glance. Lift me up and see what's underneath."
hunt_5 = "Enter the world of witches, wizards, and one very dangerous prisoner. Your next letter is hiding inside a magical story."
hunt_6 = "I make something delicious with a little cheese and a lot of love. Find the machine that turns tortillas into tacos."
hunt_7 = "I have many keys but open no doors. Find the seat where music comes to life." 

reading_1 = "You've unlocked chapter 12 reading from Harry Potter and the Sorcerer's Stone!\n " \
"To listen, open file explorer, then copy this link into the top search bar:\n" \
"C:/Users/User/Videos/Captures"
reading_2 = "You've unlocked chapter 13 reading from Harry Potter and the Sorcerer's Stone! \n" \
"To listen, open file explorer, then copy this link into the top search bar:\n" \
"C:/Users/User/Documents/My Web Sites"
reading_3 = "You've unlocked chapter 14 reading from Harry Potter and the Sorcerer's Stone! \n" \
"To listen, open file explorer, then copy this link into the top search bar:\n" \
"C:/Users/User/Desktop/Complex Variables"
reading_4 = "You've unlocked chapter 15 reading from Harry Potter and the Sorcerer's Stone! \n" \
"To listen, open file explorer, then copy this link into the top search bar:\n" \
"C:\Users\User\Desktop\Linear and Multivariable Control"
reading_5 = "You've unlocked chapter 16 reading from Harry Potter and the Sorcerer's Stone! \n" \
"To listen, open file explorer, then copy this link into the top search bar:\n" \
"C:\Users\User\Desktop\Small Unmanned\project_setup"
reading_6 = "You've unlocked chapter 16 reading from Harry Potter and the Sorcerer's Stone! \n" \
"To listen, open file explorer, then copy this link into the top search bar:\n" \
"C:\Users\User\Desktop\Engagement Photos\post"

hunts = {
    18: hunt_1,
    19: reading_1,
    21: hunt_2,
    22: reading_2, 
    24: hunt_3, 
    25: reading_3,
    27: hunt_4,
    28: reading_4,
    30: hunt_5,
    31: reading_5,
    1: reading_6
}

def load_hunts(day):

    if day in hunts:
        print()
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║                       New Hunt Found!                        ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print()        
        print(hunts[day])
    else:
        print()
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║                No hunt available for this day.               ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print()  

