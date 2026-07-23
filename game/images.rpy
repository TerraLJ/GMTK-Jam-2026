#the image animation goes here! and if we want specific naming conventions

#default direction facing is front
default g_dir = "front"
default move = ""

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

image gray = "gray [g_dir][move]"

image gray front = "gray_front_1"
image gray back = "gray_back_1"
image gray left = "gray_left_1"
image gray right = "gray_right_1"

#the numbers are the timing delay between animation frames
image gray front_move:
    "gray_front_1"
    0.15
    "gray_front_2"
    0.2
    "gray_front_3"
    0.15
    "gray_front_4"
    0.2
    repeat

image gray back_move:
    "gray_back_1"
    0.15
    "gray_back_2"
    0.2
    "gray_back_3"
    0.15
    "gray_back_4"
    0.2
    repeat

#TODO: add left and right
image gray left_move:
    "gray_front_1"
    0.15
    "gray_front_2"
    0.2
    "gray_front_3"
    0.15
    "gray_front_4"
    0.2
    repeat

image gray right_move:
    "gray_back_1"
    0.15
    "gray_back_2"
    0.2
    "gray_back_3"
    0.15
    "gray_back_4"
    0.2
    repeat