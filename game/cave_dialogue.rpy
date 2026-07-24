# for scenes in the cave

label caveDialog:
    scene cave inside with fastFade
    "Some introductory dialogue here or whatever aaaa"
    if swordLevel == 0:
        player "Something here about how the wooden sword is only good for fending off monsters, not fighting them"
    elif swordLevel == 1:
        player "Something about how I can fight monsters now with this sword from the Blacksmith"
    else:
        # swordLevel == 2
        player "I can attempt the Wishgranter's Trial."
    menu:
        "> Explore the cave? This will take 1 action."

        "Collect crystals.":
            player "(The floor and walls of this cave are filled with beautiful, shining crystals.)"
            player "(While taking care to avoid monsters, I spent time collecting some that were loose enough to pick up. Perhaps they'll be valuable.)"
            "> You obtained Gleaming Crystals x2."
            $ numCrystals += 2
            $ actionsLeft -= 1
            if actionsLeft <= 0:
                jump endOfDay
        
        "Hunt for monsters." if swordLevel > 0:
            player "(The Blacksmith's sword is sharp, and far better at fighting off monsters than my old wooden one.)"
            player "(I'm not the most experienced fighter, but I still managed to take down a couple of those beasts and picked up their remains.)"
            player "(I feel... Stronger now, too.)"
            "> You obtained Monster Shards x1."
            $ numShards += 1
            $ actionsLeft -= 1
            if actionsLeft <= 0:
                jump endOfDay

        "Attempt the trial." if swordLevel >= 2:
            jump trialEnding

        "Leave the cave.":
            scene black with fastFade
            call screen map_screen with fastFade

    # Sword Level 0 and 0 crystals means player has never been to the cave (in this run)

label trialEnding:
    # TODO
    jump gameOver