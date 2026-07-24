# dialogue for interacting with Pink as Grey
label pink_interaction:
    # decides which conversation to jump to for Pink
    if day == 1 and not breakfast:
        jump p_breakfast1
    elif day == 2 and not breakfast:
        jump p_breakfast2
    elif lovedOneProgression == 0:
        jump p_convo1
    elif lovedOneProgression == 1:
        jump p_sweetsQuestStart
    elif lovedOneProgression == 2:
        jump p_sweetsQuestDeliver
    elif lovedOneProgression == 3:
        jump p_libraryQuestStart
    elif lovedOneProgression == 4:
        jump p_libraryQuestDeliver
    elif lovedOneProgression == 5:
        jump p_convo2
    else:
        jump p_comfortEndingInitiate


label p_breakfast1:
    p "something something eat some breakfast"
    menu:
        "Eat breakfast with [p]? This will take 1 action."

        "Sure.":
            g "Sure,"
            #TODO continue
            g "()"
            "> You have gained 1 action for the day."

        "I don't have time.":
            g "Sorry, but I don't have time for that today."
            # sad pink noises
    # back to rpg mode

label p_breakfast2:
    p "something something eat some breakfast but again. you look exhausted"
    menu:
        "Eat breakfast with [p]? This will take 1 action."

        "Sure.":
            g "Sure,"
            #TODO continue
            p "You're looking better already!"
            g "(I suppose I do feel a little more refreshed.)"
            "> You have gained 1 action for the day."

        "I don't have time.":
            g "Sorry, but I don't have time for that today."
            # sad pink noises
    # back to rpg mode

label p_sweetsQuestStart:
    $ lovedOneProgression += 1
    # back to rpg mode

label p_sweetsQuestDeliver:
    if not hasSweets:
        # dialogue chain reminding you about the quest
    else:
        #delivering the sweets and the crystal
        $ lovedOneProgression += 1
    # back to rpg mode

label p_libraryQuestStart:
    $ lovedOneProgression += 1
    # back to rpg mode

label p_libraryQuestDeliver:
    if not hasPinkBook:
        # dialogue chain reminding you about the quest
    else:
        #delivering the book
        $ lovedOneProgression += 1
    # back to rpg mode

label p_convo1:
    $ lovedOneProgression += 1
    # back to rpg mode

label p_convo2:
    $ lovedOneProgression += 1
    # back to rpg mode

label p_comfortEndingInitiate:
    g "()"
    menu:
        "> Spend the rest of the day with [p]?"

        "Yes":
            jump comfortEnding
        
        "No":
            # back to rpg mode

label comfortEnding:
    # aaa
    jump gameOver