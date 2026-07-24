# for scenes in the cave

label caveDialog:
    scene cave inside with fastFade
    "Some introductory dialogue here or whatever aaaa"
    menu:
        "> Explore the cave? This will take 1 action."

        "Collect crystals.":
            player "."
            "> You obtained Gleaming Crystals x2."
            $ numCrystals += 2
            $ actionsLeft -= 1
            if actionsLeft <= 0:
                jump endOfDay
        
        "Hunt for monsters." if swordLevel > 0:
            player "."
            "> You obtained Monster Shards x1."
            $ numShards += 1
            $ actionsLeft -= 1
            if actionsLeft <= 0:
                jump endOfDay

        "Leave the cave.":
    scene black with fastFade
    call screen map_screen with fastFade

    # Sword Level 0 and 0 crystals means player has never been to the cave (in this run)