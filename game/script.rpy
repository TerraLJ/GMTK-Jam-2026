# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pink", color = "#ff7afb")
define g = Character("Gray", color = "#3d383d")
define config.rollback_enabled = False

default commentFlag = False
default shopFlag = False
default rpg = True
default room_name = "gray_house"
default room = None
define fastFade = Fade(0.3, 0, 0.3)

#TODO: placeholder
default max_countdown = 5
default countdown = max_countdown

# The game starts here.

label start:
    jump beginning

label rpg_section:
    init python:
        config.keymap['button_select'].remove('K_RETURN')
    $ room = getattr(store, room_name)
    while rpg:
        call screen map_screen with fastFade

    $ config.keymap['button_select'].append('K_RETURN')
    return
