# for scenes in the cave
image dragon = "dragon.png"
define dragon = Character("Wishgranter", color = "#ffffff")

label caveDialog:
    scene cave with fastFade
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
            g "(The trial...)"
            g "(This is not hard in terms of combat, in truth, but...)"
            g "(It is as the blacksmith said. It is a test of endurance and will. Everything looks the same down here, and the cave's beasts infest every corner.)"
            g "(The blade makes survival not a worry, at least, but...)"
            g "(I have no idea if I'm any closer to the Wishgranter. I don't even know how long I've been down here anymore.)"
            g "(And I... I'm so...)"
            g "(I'm so tired...)"
            g "(...)"

            scene black with fastFade

    g "(...)"
    g "(When had I fallen? How long had I been unaware?)"
    g "(How much time is left before moonhigh?)"
    g "(I...)"
    g "(I don't know. I don't know. She could already be...)"
    g "(...)"
    g "(No… I can't dwell. I don't know if it's true.)"
    g "(But I know I can't stop. I'm too close to stop now.)"

    menu:
        "> You have [actionsLeft] actions left."

        "Press onward. (This will take 1 action.)":

            g "(She needs this.)"
            g "(She needs me to win the Wishgranter's favor.)"
            g "(There is just no other choice.)"
            g "(...)"
            g "(This looks... Different,  though.)"
            dragon "That is because it is, trialgoer. Your prize from the belly of the labyrinth rests before you."
        
    scene dragon with fastFade

    dragon "Kneel and bare your soul to me. Let me hear you speak, to see if your heart and mind align."
    dragon "And tell me this: what drives you to push through such torment?"

    menu:
        "And tell me this: what drives you to push through such torment?"

        "My sister.":
            dragon "Ah, a bleeding heart, one with next to no care for itself."

        "My sister.":
            dragon "Ah, a bleeding heart, one with next to no care for itself."

        "My sister.":
            dragon "Ah, a bleeding heart, one with next to no care for itself."

    dragon "A pitiful beast indeed. Such selflessness is selfish. You only cause grief like this."
    dragon "But that is not my place to stop, nor to punish. Pitiful as you are, you have done all I require of those who wish for an audience."
    dragon "Yet I fear I cannot aid you in what you originally sought."
    g "(...What?)"
    dragon "Another trialgoer, one from many years past... I smell that brave soul on you. Had it not shared the limitations?"
    dragon "For such ephemeral things as souls... I cannot return what has already been lost."
    dragon "..."
    dragon "Or perhaps you were aware, and yet still raced against not just time but your own body. All for the sake of a sweet soul that longed so heavy, the scent of its wish for you to stay with it for but even a day clings to you."
    dragon "Some may call it noble. Perhaps it is."
    dragon "But all the same, you know the truth. You are too late."
    g "No… no! It can't... I couldn't have-!"
    dragon "It is as I said. Your selflessness shall only cause grief, and it has many times over now. But it is not my place to confer judgement."
    dragon "I am only here to grant you a wish, one your heart aches for. And despite knowing its end, you still want to save your kin."
    dragon "..."
    dragon "There is very little I can do to help in the present. But perhaps I can assuage the grief through the past."
    dragon "Try again, little trialgoer, and may you be less blind in this next attempt."

    python:
        resetVariables()
        room.unoccupy(store.gray_sprite.x, store.gray_sprite.y)
        room_name = "gray_house"
                
        room = getattr(store, room_name)
        store.gray_sprite.x = 11
        store.gray_sprite.y = 1
        room.occupy(11, 1, store.gray_sprite)
    jump beginning