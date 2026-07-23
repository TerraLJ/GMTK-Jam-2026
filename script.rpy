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

    show screen map_screen(gray_house)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show pink happy

    # These display lines of dialogue.

    "."

    #p "You've created a new Ren'Py game."

    #p "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
