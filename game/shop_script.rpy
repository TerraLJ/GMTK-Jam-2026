label shopMenu:
    scene shop inside with fastFade
    #mostly for learning purposes
    image shopkeep happy = "shopkeep happy.png"
    image shopkeep embarrassed = "shopkeep embarrassed.png"
    define shopkeep = Character("Shopkeeper", color = "#3239c8")

    show shopkeep happy
    shopkeep "Hey buddy, what's up?"
    shopkeep "I haven't seen you since.... gosh, how long has it been?"
    shopkeep "How's your sister?"
    scene black with fastFade
    call screen map_screen with fastFade