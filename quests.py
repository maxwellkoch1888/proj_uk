quest_3 = """
╔══════════════════════════════════════╗
║              QUEST UNLOCKED!         ║
╠══════════════════════════════════════╣
║                                      ║
║  QUEST 03: THE STONE OF ADVENTURE    ║
║                                      ║
║     Difficulty: Easy                 ║
║                                      ║
║  Legend has it that a special stone  ║
║  resides on lookout mountain nature  ║
║  preserve. Only the most beautiful   ║
║  maiden of the land will be able to  ║
║  locate it, so you can only imagine  ║
║  how relieved we were to find you!   ║
║                                      ║
║  Some people say the real stone of   ║
║  adventure is the stone that speaks  ║
║  to you!                             ║
║                                      ║
║  Hike to the nature preserve and     ║
║  retrieve the sacred stone of        ║
║  adventure.                          ║
║                                      ║
║     Required Proof:                  ║
║     One adventure stone              ║
║                                      ║
╚══════════════════════════════════════╝
"""
quest_4 = """
╔══════════════════════════════════════╗
║              QUEST UNLOCKED!         ║
╠══════════════════════════════════════╣
║                                      ║
║  QUEST 04: THE STICK OF COURAGE      ║
║                                      ║
║     Difficulty: Easy                 ║
║                                      ║
║  Well done collecting the stone of   ║
║  adventure! The legend says that     ║
║  the finder of the adventure stone   ║
║  will also be able to find the stick ║
║  of courage!                         ║
║                                      ║
║  Travel to a nearby park and obtain  ║
║  the stick of courage from the wild. ║
║  Make sure to keep an eye out for    ║
║  good picnic spots when I get back!  ║
║                                      ║
║     Required Proof:                  ║
║     The stick of courage             ║
║                                      ║
╚══════════════════════════════════════╝
"""
quest_5 = """
╔══════════════════════════════════════╗
║              QUEST UNLOCKED!         ║
╠══════════════════════════════════════╣
║                                      ║
║  QUEST 05: THE CRAFT OF LEGEND       ║
║                                      ║
║     Difficulty: Easy                 ║
║                                      ║
║  Use the stone of courage and the    ║
║  sticks of courage to make a craft.  ║
║                                      ║
║     Required Proof:                  ║
║     One craft of legend              ║
║                                      ║
╚══════════════════════════════════════╝
"""
quest_2 = """
╔══════════════════════════════════════╗
║              QUEST UNLOCKED!         ║
╠══════════════════════════════════════╣
║                                      ║
║  QUEST 02: THE WILDLIFE SIGHTING     ║
║                                      ║
║     Difficulty: Hard                 ║
║                                      ║
║  Many people say that phoenix is     ║
║  rather ugly. That may be true, but  ║
║  there are still some cool creatures ║
║  all around!                         ║
║                                      ║
║  Use you desert spirit to find local ║
║  wildlife.                           ║
║                                      ║
║  Rabbits, quails, and lizards can be ║
║  found near the park or at the       ║
║  nature preserve.                    ║
║                                      ║
║     Required Proof:                  ║
║     One picture of local wildlife    ║
║                                      ║
╚══════════════════════════════════════╝
"""
quest_1 = """
╔══════════════════════════════════════╗
║              QUEST UNLOCKED!         ║
╠══════════════════════════════════════╣
║                                      ║
║  QUEST 01: THE GREAT PEANUT RESCUE   ║
║                                      ║
║     Difficulty: URGENT               ║
║                                      ║
║  HELP!! The peanut and his reindeer  ║
║  have been captured and hidden in a  ║
║  remote location. Rumor has it that  ║
║  an SOS call was sent near Max's     ║
║  spare tire...                       ║
║                                      ║
║  Your mission is to infiltrate the   ║
║  enemy base, rescue the captives,    ║
║  and return them to safety.          ║
║                                      ║
║     Required Proof:                  ║
║     Photo evidence of the saved      ║
║     peanut! (He may need a spa       ║
║     night to feel better)            ║
║                                      ║
╚══════════════════════════════════════╝
"""
quest_6 = """
╔══════════════════════════════════════╗
║              QUEST UNLOCKED!         ║
╠══════════════════════════════════════╣
║                                      ║
║  QUEST 06: TRUE LOVE'S KISS!         ║
║                                      ║
║     Difficulty: URGENT               ║
║                                      ║
║  The love of your life has finally   ║
║  completed their adventure! You must ║
║  traverse across the city and        ║
║  make your way to the evil phoenix   ║
║  sky harbour airport to save them!   ║
║                                      ║
║  Your mission is to infiltrate the   ║
║  enemy base, rescue your true love,  ║
║  and reunite with true love's kiss.  ║
║                                      ║
║     Required Proof:                  ║
║     In person meeting!               ║
║                                      ║
╚══════════════════════════════════════╝
"""
hunts = {
2: quest_6,
17: quest_1,
21: quest_2, 
24: quest_3, 
27: quest_4,
30: quest_5
}
def load_quests(day):

    while run == True: 
        load = input("Would you load old hunts and quests? (yes/no)")
        if load == "yes":
            print("──────────────────────────────────────────────────────────────")
            print("Holy peak lets do this")
            print("loading old hunts...")
            # old_hunts()
            print("loading old quests...")
            # old_quests()
            print("──────────────────────────────────────────────────────────────")
        elif load == "no": 
            print()
            print("──────────────────────────────────────────────────────────────")
            print("Okie smokie, cutie!")
            print("Come back when you're ready to start a new day!")
            print(" I LOVE YOU SO MUCH")
            print("──────────────────────────────────────────────────────────────")
            run = False
            break
        else: 
            print()
            print("──────────────────────────────────────────────────────────────")
            print("Hmm... I don't recognize that answer. ")
            print("Please enter 'yes' or 'no'.")
            print("──────────────────────────────────────────────────────────────")
            print()