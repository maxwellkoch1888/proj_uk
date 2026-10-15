
hunt_18 = "Where you ride but never drive, your next clue waits where a the cutest girl would sit."
hunt_19 = "Where dirty things become clean and stink meets its match, your next clue is hiding among the supplies."
hunt_20 = "Behind doors where toothpaste, towels, and bathroom treasures hide, your next clue awaits where deodorant lies."
hunt_22 = "I am soft, I am comfy, and you play zelda on top of me! Search where you sit and cuddle."
hunt_23 = "I help you run, but today I'm staying put. Look inside my running shoes."
hunt_25 = "I lie beneath your feet but rarely get a second glance. Lift me up and see what's underneath."
hunt_26 = "I'm outside, but I have a roof and walls. Look where we store things we don't need inside."
hunt_28 = "I make something delicious with a little cheese and a lot of love. Find the machine that turns tortillas into tacos."
hunt_29 = "I have many keys but open no doors. Find the seat where music comes to life." 
hunt_31 = "Enter the world of witches, wizards, and one very dangerous prisoner. Your next letter is hiding inside a magical story."
hunt_1 = "A little packet of something sweet and refreshing, waiting to keep you hydrated."

hunts = {
    18: hunt_18,
    19: hunt_19,
    20: hunt_20,
    22: hunt_22, 
    23: hunt_23, 
    25: hunt_25,
    26: hunt_26,
    28: hunt_28,
    29: hunt_29,
    31: hunt_31,
    1: hunt_1,
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

