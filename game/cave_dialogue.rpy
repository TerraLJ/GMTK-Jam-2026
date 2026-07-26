# for scenes in the cave
image dragon = "dragon.png"

define dragon = Character("The Wishgranter", color= "#ffbf00")

label caveDialog:
    scene cave inside with fastFade
    if not visited_cave:
        $ visited_cave = True
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
                player "(The cave was also filled with countless shining crystals sprouting from the cavern walls and floor.)"
                player "(I picked up a handful of loose ones before leaving. Perhaps they could be useful for something.)"
                "> You obtained Gleaming Crystals x2."
                $ numCrystals += 2
                $ actionsLeft -= 1
                if actionsLeft <= 0:
                    jump endOfDay

            "Leave for now":
                player "(Maybe another time. I don't know how much my wooden sword could be of use if I ran into danger.)"
                scene black with fastFade
                call screen map_screen with fastFade

    if swordLevel == 0:
        player "(My wooden sword can protect me enough to gather crystals from this cave, but that's about the extent I can do here currently.)"
    elif swordLevel == 1:
        player "(This iron sword from the Blacksmith should be enough to allow me to hunt the monsters in this cave.)"
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
            scene dragon
            "woahh cool dragon woahhhh"
    jump gameOver