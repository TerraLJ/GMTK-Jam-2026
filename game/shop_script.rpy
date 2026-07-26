label shopMenu:    
    define shopkeep = Character("Shopkeeper", color = "#ffffff")
    scene shop with fastFade

    if not visited_shop:
        shopkeep "Don't think I've seen your face around here before! What can I get ya?"
        player "(...I have a feeling that attempting to talk to him will take up a lot of my time, whether I like it or not.)"
        g "(But... there is something I do have to ask.)"
        g "Pardon the bizarre question, but I am unfortunately tight on money. Is there perhaps anything you'd be willing to accept in lieu of gold?"
        shopkeep "Hmm...!"
        shopkeep "Well, not typically, but there's been an awfully big demand from the city for some of the crystals from the cave west of here! If you bring some of those, I'll gladly take that as a fair trade."

        $ visited_shop = True
    else:
        shopkeep "Ah, welcome back!"

    jump shopHub
    # scene black with fastFade
    # call screen map_screen with fastFade

label shopHub:
    scene shop with fastFade
    shopkeep "What can I get for ya?"
    menu:
        "> You have [actionsLeft] actions left."

        "Ask about his wares. (This will take 1 action.)" if not g_curseTransferDiscovered:
            shopkeep "Oh, we have everything an aspiring adventurer could ever want. If there's a supply you need-rope, torches, candles, knives, canteens, wire, rations... you name it, we got it!"
            shopkeep "And if somehow we don't, we'll happily send out an order to our sister locations in the city to bring some in within the week."
            g "(I hope I won't need anything that isn't already here, then. Anything of that sort would likely take too long to arrive to be of any use to me.)"
            shopkeep "Then, of course, we got some limited goods. These curiosities were traded in by the wonderful folk like you just passin' through!"
            shopkeep "We don't really have the means to test if they're free of curses or anything of that sort here, so we're willing to offer some of the more suspect ones for, ah... cheap."
            shopkeep "But what are the chances of a brooch like this being cursed? Or this-"
            g "(...)"
            g "(...he's been prattling on for ages now. And for every trivial trinket he's mentioned thus far...)"
            g "(Well, the chances of them being cursed is surprisingly high, unfortunately.)"
            g "(I don't see a reason for me to care about those, though.)"
            shopkeep "-and then there's this lovely spellbook. Just a few months ago, one of those fancy mages from the city seemed to be in a bit of a pinch when it came to money, so they sold theirs to us! It's got all sorts of spellcasting instructions, including something about..."
            shopkeep "I believe they said a spell that would be able to transfer any sort of ailment from one to another? Certainly something that could be used for incredible good or evil, that's for sure!"
            g "(...wait, what?)"
            g "(A spellbook with a spell that can transfer any ailment?)"
            g "You said {i}any{/i} ailment? Even curses?"
            shopkeep "Well, I wouldn't know personally, not being a spellcaster! But the fella did say something of the sort, yep!"
            g "I see..."
            g "Then, this book... would a similar book happen to be in this town's library as well?"
            shopkeep "Doubt it! Even though they told me it largely contained intermediate difficulty spells when it came to casting, they also said most of them were exceptionally niche."
            shopkeep "Our library only has spellbooks covering the more well-known sorts of spell, even if they're absurdly difficult."
            shopkeep "Anyway, anything else I can help you with?"
            
            python:
                g_curseTransferDiscovered = True
                actionsLeft -= 1
            jump shopHub

            if actionsLeft <= 0:
                g "No, but thank you for telling me about your wares. I may stop by tomorrow to purchase something."
                shopkeep "Hope to see you soon, then!"
                jump endOfDay
        
        "Ask about the spellbook." if g_curseTransferDiscovered:
            jump buySpellbook
        
        "Ask about sweets." if sweetsQuestProgression > 0:
            jump buySweets

        "Ask about the leather." if wishSwordStarted:
            jump buySwordItem
        
        "Leave the shop.":
            shopkeep "Please come again!"
            scene black with fastFade
            call screen map_screen with fastFade

label buySweets:
    scene shop with fastFade
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
        
        g "Do you happen to carry any sweets?"
        shopkeep "'Course I do! It'd hardly be a worthwhile shop if we didn't have some goodies to sell, would it?"
        shopkeep "I even have a bag right here ready to go for... oh, I dunno, just one crystal. How's that sound?"

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
    scene shop with fastFade
    if curseTransferObtained:
        player "Thank you again for this spellbook."
        shopkeep "No no, thank YOU for the lovely trade! Take good care of it now!"
        shopkeep "If I might pry, what do you want it for, anyway? An aspiring mage?"
        player "...You could say that, I suppose."
        jump shopHub
    
    g "About that spellbook you mentioned..."
    shopkeep "Oh, caught your attention, did it?"
    shopkeep "Well, it's a mighty fine thing to have for a spellcaster, I'm sure, but those are rather rare in town! For all the time it's been here, no one's ever thought much of it until you."
    shopkeep "So, since it's eating up inventory space and is still considered of uncertain curse status itself... how does two of those crystals sound for a price?"

    if numCrystals >= 2:
        menu:
            "> Trade 2 Gleaming Crystals for the Shopkeeper's Spellbook?"

            "Yes.":
                shopkeep "Pleasure doing business with you!"
                g "Likewise."
                g "(And a pleasure indeed! This seems to have been some sort of textbook for medical magic, but more... experimental than what I'd ever seen before. No wonder it's covered in annotations.)"
                g "(Just paging through it, I can tell there's a lot of information I could find use for someday.)"
                g "(But most importantly... there's that transfer spell the shopkeeper mentioned. And the annotations do indeed say it can be used for curses.)"
                g "(Not that the previous owner thought it was usually a good idea, given the curse will simply carry on as before in its new host, but...)"
                g "(It might be just what I need.)"

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
    scene shop with fastFade
    if hasShopkeepSwordItem:
        player "Thank you for the leather."
        shopkeep "I'm always happy to be of service!"
    else:
        player "The Blacksmith said you carry leather?"
        shopkeep "I sure do! Did she send you to help her restock?"
        player "Not... Exactly."

        shopkeep "I see! I'll continue with our usual trades, then. How do two crystals sound for it?"
        if numCrystals >= 2:
            menu:
                "> Trade 2 Gleaming Crystals for the Leather?"

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
    scene shop with fastFade
    player "Ah... I don't have enough of those on me."
    shopkeep "Those crystals grow all over that cave to the northwest!"
    shopkeep "Of course, you've gotta watch out for the little beasties roaming around in there too."
    shopkeep "But so long as you don't go in too deep, even a child with their first training sword could fend those things off long enough to grab a few of those crystals."

    jump shopHub

label firstPurchase:
    $ hasPurchased = True
    # something here where grey and the shopkeep set up the crystal exchange deal for the first time
    # This exists now but currently nothing jumps to it
    jump shopHub