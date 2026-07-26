# For scenes at the Blacksmith's

define bs = Character("Blacksmith", color = "#ffffff")

label blacksmithMenu:
    scene blacksmith with fastFade
    bs "Hey kiddo. What brings someone like you to my forge?"
    jump blacksmithMenu2

label blacksmithMenu2:
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
        bs "I can tell something's bothering you, kid, and you don't look like the type to be using the sort of weapons I work on."
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
                    bs "This’ll do you fine for dealing with the rougher things in that cave."
                    bs "But if you ever find yourself in need of a stronger weapon, I can forge you one if you’d bring me the resources for it."


                "No.":
                    "."
        else:
            # not enough crystals
            bs "Even if it isn’t gold, I still gotta be getting something, kid."
            bs "..."
            bs "But that wooden sword of yours’ll keep you safe enough if you’re just gathering a few crystals."

        jump blacksmithMenu2

    if swordLevel == 1:
        if not hasShopkeepSwordItem or numShards < 1:
            player "You had said something about a stronger sword?"
            bs "Well, I haven't forged it yet, but yes! I'm just missing the right materials for it."
            bs "It’s nothing too crazy. Some horn shards from those pesky monsters in the cave, and…"
            bs "Well, I’m running low on some leather for the grips, but the shopkeep’s got some stashed somewhere in that little store of his. You just gotta talk to him and put up with his mouth."

        else:
            # have everything you need for the Wishmaker's Blade
            "."
            bs "Forging isn’t all that quick, especially if you want something that’ll last. And sometimes, it’s real boring work."
            bs "Say, since I’m doing you a favor making you something that’ll usually cost a pretty penny in exchange for just a few errands, you should stick around and chat with me while I work."
            g "(I suppose she has a point…)"

            menu:
                "> Trade Leather and 1x Monster Shards for the Wishmaker's Blade? You have [actionsLeft] actions left."

                "Yes. (Takes 1 action.)":
                    g "(As the Blacksmith began her work, she struck up a conversation with me.)"
                    g "(I ended up spending a lot of time with her.)"
                    bs "So, kid. Why do you want this blade, anyway?"
                    bs "Like I said, you don’t really look like the sort to be using these kinds of weapons, but if you’re desperate enough to use one anyway to get an audience with the Wishgranter…"
                    bs "Well, you gotta have some sort of story going on."

                    menu:
                        bs "Well, you gotta have some sort of story going on."

                        "I need it to help my sister.":
                            bs "Ah. I get you. Trying to help family’ll drive you to some wild places, won’t they?"

                        "I’d rather not talk about it.":
                            bs "Cagey, aren’t you?"
                            bs "But that’s alright. You don’t have to tell me. It’s all just an old lady’s curiosity making her ask some personal questions anyway."

                    bs "Regardless… the thing is, I took the trial years ago. Probably wasn’t much older than you at the time, too."
                    bs "I don’t care much for talking about what happened back then myself. But if you’re going to be going down there, I figure I might as well offer some insight."
                    bs "The trial isn’t really much about the fighting. You can’t be weak, sure. The things down there would gladly maul you alive given the chance."
                    bs "But any swordsman worth their salt’ll have no issue taking them down, nor would someone like you with this kind of sword."
                    bs "It’s just the onslaught. They’re everywhere, they won’t give you time to breathe. But you gotta just keep making your way through the cave."
                    bs "It’ll confuse you. You’ll lose your way. But just keep on going."
                    bs "The trial’s about enduring hardship and having the will to through even when all hope seems lost. The Wishgranter wants to see only the most determined."
                    bs "And for that, it can grant you almost any wish."
                    bs "..."
                    bs "There’s just a limit."
                    g "(...?)"
                    bs "It can’t help with what’s already dead. Not directly, anyway."
                    bs "So… just keep that in mind when you’re down there. If you happen to be racing against the clock, there won’t be much to hope for if you don’t make it in time."
                    g "I… I see. Thank you for the warning, I suppose."
                    bs "No need for that. It’s just a bit of info to share between adventurers."
                    bs "And… good luck on the Wishgranter’s Trial, kid. Hope you get what you’re searching for."

                    python:
                        swordLevel += 1
                        numShards -= 1
                        actionsLeft -= 1
                    if actionsLeft <= 0:
                        jump endOfDay
        jump blacksmithMenu2
    
    if swordLevel == 2:
        bs "Good luck in the Wishgranter's Trial, kid. Hope you get what you're searching for."
        jump blacksmithMenu2
        