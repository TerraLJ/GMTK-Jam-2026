#snippy comments

label bridgeText:
    "There's nothing of value across the river."
    $ global commentFlag
    $ commentFlag = False

    return

label churchText:
    "Praying never helped before."
    "It won't help now."
    $ global commentFlag
    $ commentFlag = False

    return


label npc1Chat:
    "Hey, have you heard that there's this weird door in the mountains?"
    "I think it somehow got lost..."
    "I wonder if it's invisible now? Maybe the person who left it there came back for it?"
    "Must be a really goofy person to misplace it that far out of reach..."
    $ global commentFlag
    $ commentFlag = False

    return

label npc2Chat:
    "Did someone take all our crops???? Where did they go"
    $ global commentFlag
    $ commentFlag = False

    return

label shelfInspect:
    "You look at the books on the shelves."
    "You pull out a battered book with cats on the cover."
    "It clearly is well-loved and much read."
    $ global commentFlag
    $ commentFlag = False

    return

label cupboardInspect:
    "The dishes are where you always leave them."
    "You look at the numerous patterned mugs collected there for a bit longer."
    "She always preferred to use the one you got for free..."
    $ global commentFlag
    $ commentFlag = False

    return

label pinkBed:
    "The bed is neatly made, with the stuffed animals sitting nicely next to the pillow."
    $ global commentFlag
    $ commentFlag = False

    return

label grayBed:
    "The sheets are rumpled."
    $ global commentFlag
    $ commentFlag = False

    return