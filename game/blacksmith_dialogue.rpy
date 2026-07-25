# For scenes at the Blacksmith's

define bs = Character("Blacksmith", color = "#ffffff")

label blacksmithMenu:
    scene blacksmith inside with fastFade
    bs "Hey kiddo. What brings someone like you to my forge?"
    menu:
        "> You have [actionsLeft] actions left."

        "Ask about sword upgrades.":
            jump swordUpgrade

        "Leave the Blacksmith's.":
            bs "See you."
            scene black with fastFade
            call screen map_screen with fastFade

label swordUpgrade:
    if swordLevel == 0:
        # TODO: i dunno if we wanna rewrite this
        player "Do you happen to have any swords for sale? My current one is... Rather ineffective."
        player "(It was only ever meant to be a toy, and having a proper weapon on hand might prove useful in breaking the curse.)"
        bs "A flimsy wooden stick like that? Ha, I can imagine."
        bs "Waving that around might scare off an animal or two, but it's not gonna help you in any proper fight."
        bs "Lucky for you, I've got this iron sword already up for sale!"
        bs "It's nothing special, but'll get the job done."
        bs "..."
        bs "I can tell something's bothering you, kid, and you don't look like the adventuring type that I'd expect to see showing up in here."
        bs "Something tells me you don't have much gold on you, either."
        player "I... I don't, no."
        player "(Most of what we have has gone toward our lodgings...)"
        player "(Weaponry tends to be expensive, but I thought I'd at least look around...)"
        bs "I'll cut you a deal, okay?"
        player "You- you will!?"
        bs "Like I said, I can tell something's troubling you. And I'm not gonna up and abandon a kid in need."
        bs "That big cave to the west is filled with monsters, but it's also got a bunch of crystals in it that I sometimes use for my work."
        bs "Bring me four of them, and I'll trade you this iron sword."
        if numCrystals >= 4:
            menu:
                "> Trade 4 Gleaming Crystals for the Iron Sword?"

                "Yes.":
                    python:
                        swordLevel += 1
                        numCrystals -= 4
                    "."
                    "> You obtained the Iron Sword! On top of collecting crystals, you can now choose to hunt monsters in the cave."
                    bs "yapping about how she can make a stronger sword but needs the materials for it"

                "No.":
                    "."
        else:
            # not enough crystals
            bs "something about how the wooden sword should still keep you safe enough to gather crystals, just don't try to get into any fights"
        jump blacksmithMenu

    if swordLevel == 1:
        if not hasShopkeepSwordItem or numShards < 1:
            player "You had said something about a stronger sword?"
            bs "Well, I haven't forged it yet, but yes! I'm just missing the right materials for it."
            # TODO continue
        else:
            # have everything you need for the Wishmaker's Blade
            "."
            bs "You'll need to wait"
            menu:
                "> Trade (UNNAMED SHOPKEEPER ITEM) and 1x Monster Shards for the Wishmaker's Blade? You have [actionsLeft] actions left."

                "Yes. (Takes 1 action.)":
                    g "(As the Blacksmith began her work, she struck up a conversation with me.)"
                    g "(I ended up spending a lot of time with her.)"
                    # TODO: more
                    python:
                        swordLevel += 1
                        numShards -= 1
                        actionsLeft -= 1
                    if actionsLeft <= 0:
                        jump endOfDay
        jump blacksmithMenu
    
    if swordLevel == 2:
        bs "Good luck in the Wishgranter's Trial, kid. Hope you get what you're searching for."
        jump blacksmithMenu
        