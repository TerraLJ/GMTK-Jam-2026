label shopMenu:
    scene shop inside with fastFade
    #mostly for learning purposesx
    image shopkeep happy = "shopkeep happy.png"
    image shopkeep embarrassed = "shopkeep embarrassed.png"
    define shopkeep = Character("Shopkeeper", color = "#3239c8")

    show shopkeep happy
    shopkeep "Hey buddy, what's up?"
    shopkeep "I haven't seen you since.... gosh, how long has it been?"
    shopkeep "How's your sister?"

    player "(...I have a feeling that attempting to talk to him will take up a lot of my time, whether I like it or not.)"

    jump shopHub
    # scene black with fastFade
    # call screen map_screen with fastFade

label shopHub:
    shopkeep "What can I get for ya?"
    menu:
        "> You have [actionsLeft] actions left."

        "Ask about his wares. (This will take 1 action.)":
            shopkeep "The yapperrrrrrrrr"
            python:
                g_curseTransferDiscovered = True
                actionsLeft -= 1
            if actionsLeft <= 0:
                jump endOfDay
        
        "Ask about sweets." if sweetsQuestProgression > 0:
            jump buySweets
        
        "Ask about the spellbook." if g_curseTransferDiscovered:
            jump buySpellbook

        "Ask about the (UNNAMED MATERIAL).":
            # TODO: if statement
            jump buySwordItem
        
        "Leave the shop.":
            shopkeep "Please come again!"
            scene black with fastFade
            call screen map_screen with fastFade

label buySweets:
    "."

label buySpellbook:
    if curseTransferObtained:
        player "Thank you again for this spellbook."
        shopkeep "No no, thank YOU for the lovely trade! Take good care of it now!"
        shopkeep "If I might pry, what do you want it for, anyway? An aspiring mage?"
        player "...You could say that, I suppose."
        jump shopHub
    shopkeep "some yapping"
    shopkeep "Says he'll trade for 2 Gleaming Crystals"
    if numCrystals >= 2:
        menu:
            "> Trade 2 Gleaming Crystals for the Shopkeeper's Spellbook?"

            "Yes.":
                shopkeep "Pleasure doing business with you!"
                player "(Go my internal monologue)"
                python:
                    numCrystals -= 2
                    curseTransferObtained = True
                jump shopHub
            
            "No.":
                player "...I'll pass for now."
                shopkeep "Really? I'm offering you quite the deal here, you know!"
                shopkeep "But, well, just come back if you ever change your mind."
                jump shopHub
    else:
        jump lowCrystals

label buySwordItem:
    "."

label lowCrystals:
    player "Ah... I don't have enough of those on me."
    shopkeep "Those crystals grow all over that cave to the northwest!"
    shopkeep "Of course, you've gotta watch out for the little beasties roaming around in there too."
    # ^ edit this dialogue I think it could use more, or just. something
    jump shopHub