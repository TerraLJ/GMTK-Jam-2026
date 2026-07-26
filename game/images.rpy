#the image animation goes here! and if we want specific naming conventions

#default direction facing is front
default g_dir = "front"
default p_dir = "right"
default sprite_player = "gray"
default sprite_sibling = "pink"
default move = ""

python:
    if (player == g):
        sprite_player = "gray"
        sprite_sibling = "pink"
    else:
        sprite_player = "pink"
        sprite_sibling = "gray"

#how offset we need to be for the sprite to be in the right space
define g_offset = -10

init python:
    def getFacingTile():
        if g_dir == "front":
            return (gray_sprite.x, gray_sprite.y + 1)

        elif g_dir == "back":
            return (gray_sprite.x, gray_sprite.y - 1)

        elif g_dir == "left":
            return (gray_sprite.x - 1, gray_sprite.y)

        else:
            return (gray_sprite.x + 1, gray_sprite.y)

    def grayInteracts ():
        x, y = getFacingTile()

        room.triggerInteraction (x, y)

#These two names are actually misleading. they're player (gray) and sibling (pink)
#buttttt i'm lazy so i'm not changing it. good luck future me
image gray = ConditionSwitch(
    "g_dir == 'front' and move == '_move'", "gray front_move",
    "g_dir == 'front'", "gray front",
    "g_dir == 'back' and move == '_move'", "gray back_move",
    "g_dir == 'back'", "gray back",
    "g_dir == 'left' and move == '_move'", "gray left_move",
    "g_dir == 'left'", "gray left",
    "g_dir == 'right' and move == '_move'", "gray right_move",
    "g_dir == 'right'", "gray right",
)

image pink = ConditionSwitch(
    "p_dir == 'front'", "pink front",
    "p_dir == 'back'", "pink back",
    "p_dir == 'left'", "pink left",
    "p_dir == 'right'", "pink right",
)

image gray front = "[sprite_player]_front_1"
image gray back = "[sprite_player]_back_1"
image gray left = "[sprite_player]_left_1"
image gray right = "[sprite_player]_right_1"

image pink front = "[sprite_sibling]_front_1"
image pink back = "[sprite_sibling]_back_1"
image pink left = "[sprite_sibling]_left_1"
image pink right = "[sprite_sibling]_right_1"

image gray front_move:
    "[sprite_player]_front_2" with None
    0.2
    "[sprite_player]_front_3" with None
    0.2
    repeat

image gray back_move:
    "[sprite_player]_back_2" with None
    0.2
    "[sprite_player]_back_3" with None
    0.2
    repeat

image gray left_move:
    "[sprite_player]_left_2" with None
    0.15
    "[sprite_player]_left_3" with None
    0.15
    repeat

image gray right_move:
    "[sprite_player]_right_2" with None
    0.15
    "[sprite_player]_right_3" with None
    0.15
    repeat