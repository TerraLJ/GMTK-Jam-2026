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


label npcChat:
    "Hey, have you heard that there's this weird door in the mountains?"
    "I think it somehow got lost..."
    $ global commentFlag
    $ commentFlag = False

    return

label shelfInspect:
    "You look at the books on the shelves."
    "They haven't changed since the last time you checked."
    $ global commentFlag
    $ commentFlag = False

    return

label cupboardInspect:
    "You open a cabinet and get hit with a blast of cinnamon."
    $ global commentFlag
    $ commentFlag = False

    return