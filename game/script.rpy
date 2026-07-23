# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pink", color = "#ff7afb")
define g = Character("Gray", color = "#3d383d")
default commentFlag = False
default shopFlag = False
default rpg = True
default room_name = "gray_house"

# The game starts here.

label start:
    $ resetVariables()

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    #put the before-rpg stuff here
    jump beginning

    label rpg_section:
        #find a way to disable and enable it
        if (rpg == True):
            $ room = getattr(store, room_name)
            call screen map_screen(room)

    return
