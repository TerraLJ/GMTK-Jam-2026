label shopMenu:
    scene shop inside with fastFade
    #mostly for learning purposesx
    image shopkeep happy = "shopkeep happy.png"
    image shopkeep embarrassed = "shopkeep embarrassed.png"
    define shopkeep = Character("Shopkeeper", color = "#ffffff")

    show shopkeep happy
    if not visited_shop:
        shopkeep "Don't think I've seen your face around here before! What can I get ya?"
        player "(...I have a feeling that attempting to talk to him will take up a lot of my time, whether I like it or not.)"
        $ visited_shop = True
    else:
        shopkeep "Ah, welcome back!"

    jump shopHub
    # scene black with fastFade
    # call screen map_screen with fastFade

label shopHub:
    shopkeep "What can I get for ya?"
    menu:
        "> You have [actionsLeft] actions left."

        "Ask about his wares. (This will take 1 action.)" if not g_curseTransferDiscovered:
            shopkeep "The yapperrrrrrrrr"
            python:
                g_curseTransferDiscovered = True
                actionsLeft -= 1
            if actionsLeft <= 0:
                jump endOfDay
        
        "Ask about the spellbook." if g_curseTransferDiscovered:
            jump buySpellbook
        
        "Ask about sweets." if sweetsQuestProgression > 0:
            jump buySweets

        "Ask about the (UNNAMED MATERIAL)." if wishSwordStarted:
            jump buySwordItem
        
        "Leave the shop.":
            shopkeep "Please come again!"
            scene black with fastFade
            call screen map_screen with fastFade

label buySweets:
    if sweetsQuestProgression == 4:
        # Quest completed
        player "My little sister really enjoyed those sweets I bought from you. Thank you."
        shopkeep "Oh, that's wonderful to hear! I'll be restocking them next week, so you should come by again sometime then!"
        player "...Right..."
        jump shopHub
    if sweetsQuestProgression == 3:
        # Sweets acquired, not given to Pink yet
        player "Thank you for these, I'm sure my sister will love them."
        shopkeep "Of course! I sell only the best, after all!"
        player "(...I should get these home to [p] before he starts rambling again.)"
        jump shopHub
    if sweetsQuestProgression == 2:
        # Aware of sweets, not purchased yet.
        player "About those sweets..."
        shopkeep "Still interested? I'll trade 'em to you for one of those crystals from that cave!"
    if sweetsQuestProgression == 1:
        # Has never asked about sweets before
        $ sweetsQuestProgression = 2
        player "PLACEHOLDER ASKS SOMETHING ABOUT SWEETS" # TODO
        shopkeep "PLACEHOLDER PART TWO"
    if numCrystals >= 1:
        menu:
            "> Trade 1 Gleaming Crystal for the sweets?"

            "Yes.":
                shopkeep "Wonderful! I do hope you enjoy them!"
                player "(I should get these back to [p] as soon as I can.)"
                python:
                    numCrystals -= 1
                    sweetsQuestProgression = 3
                jump shopHub
            
            "No.":
                shopkeep "Ah... What a shame."
                shopkeep "Well, the offer's still open if you change your mind!"
                jump shopHub
    else:
        jump lowCrystals

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
    if hasShopkeepSwordItem:
        player "Thank you for ()."
        shopkeep "I'm always happy to be of service!"
    else:
        player "The Blacksmith said you carry (ITEM NAME)?"
        shopkeep "I sure do! Did she send you to help her restock?"
        player "Not... Exactly."
        shopkeep "I see! I'll continue with our usual trades, then. How do two crystals sound for it?"
        if numCrystals >= 2:
            menu:
                "> Trade 2 Gleaming Crystals for the (UNNAMED ITEM)?"

                "Yes.":
                    shopkeep "Here you are, then!"
                    $ numCrystals -= 2
                    $ hasShopkeepSwordItem = True
                    jump shopHub

                "No.":
                    shopkeep "."
                    jump shopHub
        else:
            jump lowCrystals

label lowCrystals:
    player "Ah... I don't have enough of those on me."
    shopkeep "Those crystals grow all over that cave to the northwest!"
    shopkeep "Of course, you've gotta watch out for the little beasties roaming around in there too."
    # ^ edit this dialogue I think it could use more, or just. something TODO
    jump shopHub

label firstPurchase:
    $ hasPurchased = True
    # something here where grey and the shopkeep set up the crystal exchange deal for the first time
    # This exists now but currently nothing jumps to it
    jump shopHub