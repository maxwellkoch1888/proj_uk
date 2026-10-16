
hunt_1 = "Where you ride but never drive, your next letter waits where a the cutest girl would sit."
hunt_2 = "I have many keys but open no doors. Find the seat where music comes to life."
hunt_3 = "I am soft, I am comfy, and you play zelda on top of me! Search where you sit and cuddle."
hunt_4 = "I lie beneath your feet but rarely get a second glance. Lift me up and see what's underneath."
hunt_5 = "Enter the world of witches, wizards, and one very dangerous prisoner. Your next letter is hiding inside a magical story."

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
reading_6 = "You've unlocked chapter 17 reading from Harry Potter and the Sorcerer's Stone! \n" \
"To listen, open file explorer, then copy this link into the top search bar:\n" \
"C:\Users\User\Desktop\Engagement Photos\post"
reading_7 = "You've unlocked chapter 1 reading from Harry Potter and the Chamber of Secrets! \n" \
"To listen, open file explorer, then copy this link into the top search bar:\n" \
"C:\Users\User\Desktop\Small Unmanned"
reading_8 = "You've unlocked chapter 2 reading from Harry Potter and the Chamber of Secrets! \n" \
"To listen, open file explorer, then copy this link into the top search bar:\n" \
"C:\Users\User\Documents\OneNote Notebooks"
reading_9 = "You've unlocked chapter 3 reading from Harry Potter and the Chamber of Secrets! \n" \
"To listen, open file explorer, then copy this link into the top search bar:\n" \
"C:\Users\User\Documents\MATLAB"

hunts = {
    17: reading_1,
    19: reading_2,
    20: hunt_1,
    21: reading_3,
    23: reading_4,
    24: hunt_2, 
    25: reading_5,
    26: reading_6,
    27: hunt_3,
    28: reading_7,
    29: hunt_4,
    30: reading_8,
    31: hunt_5,
    1: reading_9
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

