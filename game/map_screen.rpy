#default is (4,3) for no reason
#center_x (pixels) = tile_size * 4.5
#center of the screen 1920/2 = 960
#xpos = center of screen - center_x
#center_y (pixels) = tile_size * 3.5
#center of the screen 1080/2 = 540
#ypos = center of screen - center_y

screen map_screen (aMap):

    add "#000"

    $offset_x = 960 - (tile_size * aMap.center_x) + (tile_size//2)
    $offset_y = 540 - (tile_size * aMap.center_y) + (tile_size//2)
    add aMap.img:
        pos(offset_x, offset_y)

    for i in range(len(aMap.map)):
        $row = aMap.map [i]
        for j in range(len(row)):
            $tile = row[j]
            if not tile.occupant is None and isinstance(tile.occupant, MapDenizen):
                $offx, offy = tile.occupant.getOffset()
                $tile_lc_x = tile_size * j + offset_x
                $tile_lc_y = tile_size * i + offset_y
                add tile.occupant.img:
                    pos (tile_lc_x + offx, tile_lc_y + offy)

    # Detect when the key is first pressed down
    key "keydown_K_UP" action SetVariable("moving_up", True)
    key "keydown_K_DOWN" action SetVariable("moving_down", True)
    key "keydown_K_LEFT" action SetVariable("moving_left", True)
    key "keydown_K_RIGHT" action SetVariable("moving_right", True)

    # Detect when the player releases the key
    key "keyup_K_UP" action SetVariable("moving_up", False), SetVariable ("move", "")
    key "keyup_K_DOWN" action SetVariable("moving_down", False), SetVariable ("move", "")
    key "keyup_K_LEFT" action SetVariable("moving_left", False), SetVariable ("move", "")
    key "keyup_K_RIGHT" action SetVariable("moving_right", False), SetVariable ("move", "")

    # A repeating timer that shifts position smoothly if a state is True
    if moving_up:
        timer 0.075 repeat True action [Function (gray_house.moveDenizen, gray_sprite.x, gray_sprite.y, 0, -1), SetVariable ("g_dir", "back"), SetVariable ("move", "_move")]

    elif moving_down:
        timer 0.075 repeat True action [Function (gray_house.moveDenizen, gray_sprite.x, gray_sprite.y, 0, 1), SetVariable ("g_dir", "front"), SetVariable ("move", "_move")]

    elif moving_left:
        timer 0.075 repeat True action [Function (gray_house.moveDenizen, gray_sprite.x, gray_sprite.y, -1, 0), SetVariable ("g_dir", "left"), SetVariable ("move", "_move")]

    elif moving_right:
        timer 0.075 repeat True action [Function (gray_house.moveDenizen, gray_sprite.x, gray_sprite.y, 1, 0), SetVariable ("g_dir", "right"), SetVariable ("move", "_move")]

    key "K_RETURN" action Function (grayInteracts)