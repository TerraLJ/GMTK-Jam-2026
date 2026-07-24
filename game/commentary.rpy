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