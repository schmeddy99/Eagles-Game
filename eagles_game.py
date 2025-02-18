print(r'''
*******************************************************************************
///,        ////
\ `/,      /` .&gt;.
 \  /,   _/` /.
  \_ `/_/`  /.
    \__/_  .&lt;
    /&lt;&lt;&lt;&lt;\_\_
   /,)^&gt;&gt;_._\\
   (/   \\ /\\\
        // ````
     ,-((--,/|
     &gt;_&gt;-~~``'
*******************************************************************************
''')

# Introduction
print("You have arrived on Eagle Island, a legendary land said to hold the lost Lombardi Trophy,")
print("an artifact of immense power. To claim it, you must pass through three great trials,")
print("each guarded by formidable foes: the Packer, the Commander, and the Chief.")
print("Choose wisely, or risk being lost to the island forever.\n")

#Game start
play = input("Would you like to play? (Y/N): ").upper()

if play != 'Y':
    print("Lame. Hope you play again another time.")

else:
    print("\nYou brace yourself and step onto the island, ready to face the trials ahead.\n")

    #Trial 1 - The Packer
    print("As you venture into the dense Greenwood Forest, a mystical warrior known as")
    print("Jordan 'The Packer' Love blocks your path. Cloaked in green and gold, he wields")
    print("an enchanted cheese shield and demands a challenge.")
    print("'To pass,' he says, 'you must prove your worth!'")

    choice = input("\nYour choice: (A) Steal the cheese, (B) Fight head-on: ").upper()
    if choice == "A":
        print("\nYou attempt to steal the cheese! The Packer slips while chasing you,")
        print("and you escape deeper into the island. You feel a surge of confidence.\n")
    elif choice == "B":
        print("\nYou charge at The Packer, but his enchanted shield deflects your attacks!")
        print("He banishes you from the forest, and you lose your way.\n")
        print("Game Over.")
        exit()
    else:
        print("\nYou hesitate, and The Packer grows impatient. He banishes you from the forest.\n")
        print("Game Over.")
        exit()

     # Trial 2 - The Commander
    print("Deep within the ruins of an ancient stronghold, The Commander Jayden Daniels awaits.")
    print("Dressed in burgundy and gold, he commands an army of spectral warriors.")
    print("'To pass,' he declares, 'you must prove your strategy or strength!'")

    choice = input("\nYour choice: (A) Sneak past, (B) Challenge him in battle: ").upper()
    if choice == "A":
        print("\nYou use your wits to slip through the shadows and evade his forces.")
        print("The Commander's army never even notices you. You continue your journey.\n")
    elif choice == "B":
        print("\nYou charge into battle, but The Commander's spectral warriors overwhelm you!")
        print("Defeated, you are forced to retreat.\n")
        print("Game Over.")
        exit()
    else:
        print("\nYou hesitate, and The Commander's army surrounds you. You are captured.\n")
        print("Game Over.")
        exit()

    # Trial 3 - The Chief
    print("At the peak of Mount Arrowhead, within the fiery depths of an ancient temple,")
    print("The Chief Patrick stands guard over the lost Lombardi Trophy. Wielding a")
    print("flaming spear, he watches as you approach.")
    print("'To claim the trophy,' he growls, 'you must prove your cunning or strength!'")

    choice = input("\nYour choice: (A) Trick him, (B) Face him in a test of strength: ").upper()
    if choice == "A":
        print("\nYou convince The Chief that the trophy is cursed! He flees in fear,")
        print("leaving the Lombardi Trophy unguarded. You grasp it with triumph!\n")
        print("You Win! The Lombardi Trophy is yours!")
    elif choice == "B":
        print("\nYou challenge The Chief to a test of strength, but his power is too great.")
        print("He casts you into the volcano, and you are never seen again.\n")
        print("Game Over.")
        exit()
    else:
        print("\nYou hesitate, and The Chief grows angry. He casts you into the volcano.\n")
        print("Game Over.")
        exit()



