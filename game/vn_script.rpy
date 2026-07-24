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
    "(I'm exhausted... I don't think I can keep going today.)"
    # fade to black?
    $ day += 1
    if day == 2:
        $ actionsLeft = 2
        jump startOfDay2
    elif day == 3:
        $ actionsLeft = 1
        jump startOfDay3
    else:
        $ actionsLeft = 0
        jump outOfTime

label startOfDay2:
    # TODO

label startOfDay3:
    # TODO

label outOfTime:
    # TODO