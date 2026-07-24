label beginning:
    #initialize your sprites here
    image pink happy = "pink_healthy_happy.png"

    #this is the text bit :)
    show pink happy
    p "Hey there?"
    hide pink happy

    "> The curse will take effect in three days at midnight. You must enact a solution before then."
    #blease leave this thank you <3
    jump rpg_section

label endOfDay:
    "(I'm exhausted... I don't think I can keep going today.)"
    # fade to black?
    $ day += 1
    # TODO: something here to make sure you're at home the next time the game switches to rpg mode
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
    # fade from black
    "> The curse will take effect in two days at midnight. You must enact a solution before then."
    # TODO
    scene black with fastFade
    call screen map_screen with fastFade

label startOfDay3:
    # fade from black
    "> The curse will take effect at midnight. You must enact a solution before then."

    # check for curse transfer ending prereqs, prompt it if fulfilled
    if curseTransferObtained and magicLevel >= 2:
        player "(I have everything I need now. I think I can cast the spell to transfer the curse...)"
        player "(...Should I do it?)"
        menu:
            "> This will take 1 action."

            "Transfer the curse.":
                $ curseTransferCompleted = True
                # TODO
                jump curseTransferEnding

            "Do not.":
                player "(I still need to think about this...)"
                "> If you would like to transfer the curse, visit the library."
                scene black with fastFade
                call screen map_screen with fastFade

    # check for comfort ending prereqs, prompt it if fulfilled
    elif lovedOneProgression == 6:
        player "(something about maybe just spending this last day with [p])"
        player "(maybe even multiple lines about it)"
        player "(kind of out of time now anyway soo)"
        menu:
            "> Spend the rest of the day with [p]?"

            "Yes":
                jump comfortEnding
            
            "No":
                player "(some thought about how they can talk to pink if they change their mind on this)"
                # back to rpg mode
                scene black with fastFade
                call screen map_screen with fastFade

    # check for trial ending prereqs, prompt it if fulfilled
    elif swordLevel == 3:
        player "(With this new sword, I'm sure I can pass the Wishgranter's Trial.)"
        menu: 
            "> Attempt the trial?"

            "Yes":
                "> You make your way to the cave."
                # fade to black?
                jump trialEnding
            
            "Not now":
                player "(I can visit the cave later today. I should prepare first.)"
                scene black with fastFade
                call screen map_screen with fastFade

    # check for magic ending prereqs, prompt it if fulfilled
    elif timesMagicPracticed == 5:
        player "(I'm so close... Just a little more practice, and I'm sure I'll be able to break the curse with my magic.)"
        menu:
            "> Go to the library?"

            "Yes":
                # fade to black?
                jump library

            "Not now":
                player "(Maybe later today. I need to be quick, though: I'm running out of time.)"
                scene black with fastFade
                call screen map_screen with fastFade

    # else, jump straight to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label outOfTime:
    # TODO
    "some internal monologue from Grey about how Pink is so fucking dead"
    "and them rushing home maybe"
    "and how they never felt like they even got close to finding a solution"
    jump gameOver

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