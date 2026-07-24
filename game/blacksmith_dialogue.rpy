# For scenes at the Blacksmith's

define bs = Character("Blacksmith", color = "#ffffff")

label blacksmithMenu:
    scene blacksmith inside with fastFade
    bs "Hey kiddo."
    scene black with fastFade
    call screen map_screen with fastFade