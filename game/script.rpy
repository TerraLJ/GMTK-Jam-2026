# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pink", color = "#ff7afb")
define g = Character("Gray", color = "#3d383d")

default commentFlag = False
default shopFlag = False
default rpg = True
default room_name = "gray_house"
default room = None

#TODO: placeholder
default max_countdown = 5
default countdown = max_countdown

# The game starts here.

label start:
    jump beginning

label rpg_section:
    # disable rollback because i kept accidentally rolling back. allow save scumming though
    $ renpy.block_rollback()
    $ room = getattr(store, room_name)
    while rpg:
        call screen map_screen
    return
