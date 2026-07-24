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
    scene black with fastFade
    call screen map_screen with fastFade

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
    scene black with fastFade
    call screen map_screen with fastFade

label p_sweetsQuestStart:
    p "wa"
    g "wawa"
    $ lovedOneProgression += 1
    # back to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label p_sweetsQuestDeliver:
    if not hasSweets:
        # dialogue chain reminding you about the quest
        p "wawa my sweets wawawa"
    else:
        #delivering the sweets and the crystal
        p "yayy my sweets wawawa"
        p "ooo pretty crystal also wowie"
        python:
            lovedOneProgression += 1
            numCrystals -= 1
    # back to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label p_libraryQuestStart:
    p "find my pages but like a whole lot of them because it's a book"
    $ lovedOneProgression += 1
    # back to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label p_libraryQuestDeliver:
    if not hasPinkBook:
        # dialogue chain reminding you about the quest
        p "you did not find my pages :("
    else:
        #delivering the book
        p "My pages!!! :D"
        $ lovedOneProgression += 1
    # back to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label p_convo1:
    p "wawawawa?"
    g "wawawa"
    p "this is just like rain world. our wawas"
    $ lovedOneProgression += 1
    # back to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label p_convo2:
    p "have you heard of the hit game persona 4"
    g "that's not the one that vaguely inspired us tho why are you bringing it up"
    p "ummm. teehee"
    $ lovedOneProgression += 1
    # back to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label p_comfortEndingInitiate:
    g "()"
    menu:
        "> Spend the rest of the day with [p]?"

        "Yes":
            jump comfortEnding
        
        "No":
            # back to rpg mode
            scene black with fastFade
            call screen map_screen with fastFade

label comfortEnding:
    # aaa
    jump gameOver