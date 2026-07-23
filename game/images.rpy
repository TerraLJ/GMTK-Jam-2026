#the image animation goes here! and if we want specific naming conventions
image pink happy = "pink_healthy_happy.png"

#default direction facing is front
default g_dir = "front"

#how offset we need to be for the sprite to be in the right space
define g_offset = 0

image gray = "gray [g_dir]"

#the numbers are the timing delay between animation frames
image gray front:
    "gray_healthy_front_1"
    0.15
    "gray_healthy_front_2"
    0.2
    "gray_healthy_front_3"
    0.15
    "gray_healthy_front_4"
    0.2
    repeat

image gray back:
    "gray_healthy_back_1"
    0.15
    "gray_healthy_back_2"
    0.2
    "gray_healthy_back_3"
    0.15
    "gray_healthy_back_4"
    0.2
    repeat