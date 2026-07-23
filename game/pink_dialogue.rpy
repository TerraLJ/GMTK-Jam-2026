# dialogue for interacting with Pink as Grey
label pink_interaction:
    # decides which conversation to jump to for Pink
    if day == 1 and not extraAction:
        jump p_restfulDay1
    elif day == 2 and not extraAction:
        jump p_restfulDay2
    elif lovedOneProgression == 0:
        jump p_convo1
    # TODO: the rest of these

label p_restfulDay1:
    #

label p_restfulDay2:
    #

label p_sweetsQuestStart:
    #

label p_sweetsQuestDeliver:
    #

label p_libraryQuestStart:
    #

label p_libraryQuestDeliver:
    #

label p_caveQuestStart:
    #

label p_caveQuestDeliver:
    #

label p_convo1:
    #

label p_convo2:
    #

label p_convo3:
    #