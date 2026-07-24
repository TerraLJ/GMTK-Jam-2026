#default is (4,3) for no reason
#center_x (pixels) = tile_size * 4.5
#center of the screen 1920/2 = 960
#xpos = center of screen - center_x
#center_y (pixels) = tile_size * 3.5
#center of the screen 1080/2 = 540
#ypos = center of screen - center_y

transform plane_3d:
    perspective True
    matrixanchor (960, 540)
    matrixtransform RotateMatrix(15, 0, 0) * OffsetMatrix(0, 50, -200)

screen map_screen ():
    add "#000"

    $ map_cols = len(room.map[0]) if len(room.map) > 0 else 1
    $ map_rows = len(room.map)

    $ screen_half_w = 1920.0 / 2.0
    $ screen_half_y = 1080.0 / 2.0

    if (map_cols * tile_size) <= 1920:
        $ offset_x = screen_half_w - ((map_cols * tile_size) / 2.0)
        $ cam_x = map_cols / 2.0
    else:
        $ min_camera_x = screen_half_w / tile_size
        $ max_camera_x = map_cols - (screen_half_w / tile_size)
        $ cam_x = max(min_camera_x, min(room.center_x + 0.5, max_camera_x))
        $ offset_x = screen_half_w - (tile_size * cam_x)

    if (map_rows * tile_size) <= 1080:
        $ offset_y = screen_half_y - ((map_rows * tile_size) / 2.0)
        $ cam_y = map_rows / 2.0
    else:
        $ min_camera_y = screen_half_y / tile_size
        $ max_camera_y = map_rows
        $ cam_y = max(min_camera_y, min(room.center_y + 0.5, max_camera_y))
        $ offset_y = screen_half_y - (tile_size * cam_y)

    fixed:
        at plane_3d

        fixed:
            pos (int(offset_x), int(offset_y))
            add room.img

        python:
            active_denizens = []
            for row in room.map:
                for tile in row:
                    if tile.occupant is not None:
                        if hasattr(tile.occupant, "sort_y") and hasattr(tile.occupant, "img"):
                            active_denizens.append(tile.occupant)

            active_denizens.sort(key=lambda d: d.sort_y)

        for denizen in active_denizens:
            $ offx, offy = denizen.getOffset()
            
            if (map_cols * tile_size) <= 1920:
                $ sprite_render_x = offset_x + (tile_size * denizen.x)
            else:
                $ sprite_render_x = screen_half_w + (tile_size * (denizen.x - cam_x))
                
            if (map_rows * tile_size) <= 1080:
                $ sprite_render_y = offset_y + (tile_size * denizen.y)
            else:
                $ sprite_render_y = screen_half_y + (tile_size * (denizen.y - cam_y))

            fixed:
                pos (int(sprite_render_x + offx), int(sprite_render_y + offy))
                
                at transform:
                    matrixanchor (tile_size // 2, tile_size)
                    
                    matrixtransform RotateMatrix(-15, 0, 0)
                
                add denizen.img

    vbox:
        xalign 0.05
        yalign 0.05
        spacing 10

        text "Day [day]":
            text_align 0.0

        text "[actionsLeft] actions left":
            text_align 0.0
                
    if (rpg == True and commentFlag == False):
        key "keydown_K_UP" action SetVariable("moving_up", True)
        key "keydown_K_DOWN" action SetVariable("moving_down", True)
        key "keydown_K_LEFT" action SetVariable("moving_left", True)
        key "keydown_K_RIGHT" action SetVariable("moving_right", True)

        key "keyup_K_UP" action [SetVariable("moving_up", False), SetVariable("move", "")]
        key "keyup_K_DOWN" action [SetVariable("moving_down", False), SetVariable("move", "")]
        key "keyup_K_LEFT" action [SetVariable("moving_left", False), SetVariable("move", "")]
        key "keyup_K_RIGHT" action [SetVariable("moving_right", False), SetVariable("move", "")]

        $ move_state = handle_character_input()

        # 2. Execute the appropriate single timer based on the state
        if move_state:
            if move_state[0]:
                timer repeat_input repeat True action [
                Function(room.movePlayerDenizen, move_state[1], move_state[2]), 
                SetVariable("move", "_move")
            ]
        
            else:
                timer repeat_input repeat False action SetVariable("g_dir", move_state[3])
                
        key "K_RETURN" action Function(grayInteracts)