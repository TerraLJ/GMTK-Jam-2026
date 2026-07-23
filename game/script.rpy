# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pink")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room
    $commentFlag = False
    $rpg = True
    $room = gray_house

    window auto

    #put the before-rpg stuff here
    "."

    #find a way to disable and enable it
    if (rpg == True):
        show screen map_screen(room)

        # Freeze progression until commentFlag is True
        while not commentFlag:
            $ renpy.pause(0.1, hard=True)


    #show pink happy

    #put vn stuff here?
    else:
        "."

    return
