# for scenes in the cave

label caveDialog:
    scene cave inside with fastFade
    # if first visit (need a variable for this)
    player "(This cave... I've heard legends of this place. Of its apparent capacity to grant wishes.)"
    player "(I don't know much about it, and it sounds like a farfetched fantasy, but it's part of the reason we settled in this village.)"
    player "(Such a miracle might be our only hope.)"

    menu:
        "> You have [actionsLeft] actions left."

        "Investigate the cave. (This will take 1 action.)":
            player "(I attempted to explore the cave, but...)"
            player "(It was filled with monsters.)"
            player "(Of course. Of course a 'mystical wish-granting cave' would come with a catch.)"
            player "(The wooden sword I brought with me was effective enough in scaring off some of the weaker beasts, but I can't venture very far with just that. It's little more than a toy, after all.)"
            player "(The cave also contains" #TODO UNFINISHED CRYSTAL TALK
            player "(I picked up a handful of loose ones before leaving. Perhaps they could be useful for something.)"
            "> You obtained Gleaming Crystals x2."

        "Leave for now":
            player "(Maybe another time. I don't know how much my wooden sword could be of use if I ran into danger.)"
            scene black with fastFade
            call screen map_screen with fastFade

    if swordLevel == 0:
        player "Something here about how the wooden sword is only good for fending off monsters, not fighting them"
    elif swordLevel == 1:
        player "Something about how I can fight monsters now with this sword from the Blacksmith"
    else:
        # swordLevel == 2
        player "I can attempt the Wishgranter's Trial."
    menu:
        "> You have [actionsLeft] actions left."

        "Collect crystals. (This will take 1 action.)":
            player "(The floor and walls of this cave are filled with beautiful, shining crystals.)"
            player "(While taking care to avoid monsters, I spent time collecting some that were loose enough to pick up. Perhaps they'll be valuable.)"
            "> You obtained Gleaming Crystals x2."
            $ numCrystals += 2
            $ actionsLeft -= 1
            if actionsLeft <= 0:
                jump endOfDay
        
        "Hunt for monsters. (This will take 1 action.)" if swordLevel > 0:
            player "(The Blacksmith's sword is sharp, and far better at fighting off monsters than my old wooden one.)"
            player "(I'm not the most experienced fighter, but I still managed to take down a couple of those beasts and picked up their remains.)"
            player "(I feel... Stronger now, too.)"
            "> You obtained Monster Shards x1."
            $ numShards += 1
            $ actionsLeft -= 1
            if actionsLeft <= 0:
                jump endOfDay

        "Attempt the trial. (This will take 1 action.)" if swordLevel >= 2:
            $ actionsLeft -= 1
            jump trialEnding

        "Leave the cave.":
            scene black with fastFade
            call screen map_screen with fastFade

label trialEnding:
    # TODO
    player "."
    menu:
        # At this point the player has 0 actions
        # It's a menu but only one option is actually available
        "> You have [actionsLeft] actions left."

        "Press onward. (This will take 1 action.)":
            "woahh cool dragon woahhhh"
    jump gameOver