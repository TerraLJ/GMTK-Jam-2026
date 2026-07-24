label beginning:
    #initialize your sprites here
    image pink happy = "pink_healthy_happy.png"

    #this is the text bit :)
    show pink happy
    p "Hey there?"
    hide pink happy

    #blease leave this thank you <3
    jump rpg_section

label endOfDay:
    player "(I'm exhausted... I don't think I can keep going today.)"
    # fade to black?
    $ newDay()
    if day == 2:
        jump startOfDay2
    elif day == 3:
        jump startOfDay3
    else:
        jump outOfTime

label startOfDay2:
    # Fade from black
    
    # Pink asks you to eat breakfast with her
    # game says that it costs one action, but if you agree then you gain that action back
    # and Pink says that you're looking a little healthier
    # TODO

label startOfDay3:
    # Fade from black
    "> The curse will take effect at midnight. You must enact a solution before then."

    # If you have the Level 3 Sword, you'll be prompted to attempt the Cave Trial
    # If you are one practice away from Level 3 Magic, you'll be prompted to study at the library
    # If you have the Shopkeeper's Spellbook and Level 2 Magic, you'll be prompted to perform the transfer spell

    # Otherwise, Pink asks you to eat breakfast with her
    # game says that it costs one action, but if you agree then you gain that action back
    # and Pink says that you're looking a little healthier
    # TODO

label outOfTime:
    # TODO