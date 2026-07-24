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
    # fade from black
    "> The curse will take effect at midnight. You must enact a solution before then."

    # check for comfort ending prereqs, prompt it if fulfilled

    # check for trial ending prereqs, prompt it if fulfilled

    # check for magic ending prereqs, prompt it if fulfilled

    # else, jump to rpg mode

label outOfTime:
    # TODO

label gameOver:
    menu:
        "> You have failed to break the curse."

        "Try again.":
            "> And so it begins again."
            $ resetVariables()
            jump beginning
        
        "Give up. (This will take 1 action.)":
            "> You do not have any actions left."
            jump gameOver