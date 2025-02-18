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
print("You have arrived on Eagle Island, a legendary land said to hold the lost Lombardi Trophy, an artifact of immense power. To claim it, you must pass through three great trials, each guarded by formidable foes: the Packer, the Commander, and the Chief. Choose wisely, or risk being lost to the island forever.")
play = input("Would you like to play? Y/N\n")
if play == 'Y' or 'y':
    print("As you venture into the dense Greenwood Forest, a mystical warrior known as Jordan 'The Packer' Love blocks your path. Cloaked in green and gold, he wields an enchanted cheese shield and demands a challenge.")
    fight_packers = input("Your choice, should we steal the cheese (a) or fight head-on (b)?\n")
    if fight_packers == 'a':
        print("The Packer slips while chasing you! You escape deeper into the island.")
    else:
        print("His enchanted shield deflects your attacks! You are Banished.")
        print("Game Over.")

    print("Deep within the ruins of an ancient stronghold, The Commander Jayden Daniels awaits. Dressed in burgundy and gold, he commands an army of spectral warriors. He offers you a choice—strategy or brute force.")
    fight_commanders = input("Should we sneak past (a) or challenge him in battle (b)?\n")
    if fight_commanders == 'a':
        print("You slip through the shadows and evade his forces.")
    else:
        print("His army overwhelms you! Defeated.")
        print("Game Over.")

    print("At the peak of Mount Arrowhead, within the fiery depths of an ancient temple, The Chief Patrick stands guard over the lost Lombardi Trophy. Wielding a flaming spear, he watches as you approach.")
    fight_chiefs = input("Should we trick him (a) or face him in a test of strength (b)?\n")
    if fight_chiefs == 'a':
        print("You convince The Chief that the trophy is cursed! He flees, leaving it unguarded.")
        print("You Win! The Lombardi Trophy is yours!")
    else:
        print("The Chief's power is too great. You are cast into the volcano.")
        print("Game Over.")
else:
    print("Lame. Hope you play again another time.")


