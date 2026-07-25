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