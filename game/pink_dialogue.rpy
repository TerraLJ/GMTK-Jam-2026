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
    # TODO: IMPLEMENT PORTRAITS AND EXPRESSION CHANGES
    p "Oh, I..."
    p "I really thought you were just going to head out immediately again."
    p "But this is good! We could have some breakfast together before you go!"
    p "..."
    p "Please..?"
    menu:
        "> Eat breakfast with [p]? This will take 1 action."

        "Eat breakfast.":
            g "...I suppose it's been some time since I last had a meal..."
            p "What?!"
            p "When's the last time you ate?"
            g "..."
            g "You know I've been busy."
            p "So busy you can't eat??"
            p "Don't be like that, [g]! You're the one who always told me we need to rest and eat to be able to do other things!" 
            p "I know you're worried about the curse, but it's only going to get harder to do things if you keep neglecting yourself!"
            g "But-"
            p "Nuh-uh! Not hearing it right now!"
            p "Let's get some food in the both of us, okay?"
            # fade to black, sound effects of dishes clinking and such? breakfast getting set up
            g "(...This is nice.)"
            g "(I've hardly any time recently for such... frivolities. But just the same...)"
            g "(I can't recall the last time I was able to share a meal with her, since the curse.)"
            g "(...)"
            g "(She looks so happy.)"
            p "..!"
            p "What's up? You're looking at me all serious."
            p "..."
            p "...If it's about having to spend extra time doing the dishes, I'll do them, don't worry..!"
            p "Go ahead and go out into town and do... Do your research stuff!"
            p "..."
            p "But, um... thanks. For having breakfast with me."
            p "I really missed it."
            "> You have gained 1 action for the day."

        "I don't have time.":
            g "I'm sorry, [p]. There's just too little time left, with the curse."
            g "But I promise we will after I have an answer for it."
            p "..."
            p "...Okay."
            p "Um... good luck in town, then..!"
    # back to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label p_breakfast2:
    p "something something eat some breakfast but again. you look exhausted"
    menu:
        "> Eat breakfast with [p]? This will take 1 action."

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