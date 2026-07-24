#default is (4,3) for no reason
#center_x (pixels) = tile_size * 4.5
#center of the screen 1920/2 = 960
#xpos = center of screen - center_x
#center_y (pixels) = tile_size * 3.5
#center of the screen 1080/2 = 540
#ypos = center of screen - center_y

transform plane_3d:
    # Enable perspective projection
    perspective True
    # Anchor the matrix to the center of your game window (assuming 1920x1080)
    matrixanchor (960, 540)
    # Tilt the grid back 25 degrees and move the camera view to simulate height
    matrixtransform RotateMatrix(15, 0, 0) * OffsetMatrix(0, 50, -200)

screen map_screen ():
    add "#000"

screen map_screen ():
    add "#000"

    # 1. Fetch exact grid row/col counts safely
    $ map_cols = len(room.map[0]) if len(room.map) > 0 else 1
    $ map_rows = len(room.map)

    # 2. Calculate half screen metrics in real pixels
    $ screen_half_w = 1920.0 / 2.0
    $ screen_half_y = 1080.0 / 2.0

    # 3. Handle Horizontal Camera Alignment & Tracking Point
    if (map_cols * tile_size) <= 1920:
        $ offset_x = screen_half_w - ((map_cols * tile_size) / 2.0)
        # For small rooms, the camera tracking center is just the middle of the room
        $ cam_x = map_cols / 2.0
    else:
        $ min_camera_x = screen_half_w / tile_size
        $ max_camera_x = map_cols - (screen_half_w / tile_size)
        $ cam_x = max(min_camera_x, min(room.center_x + 0.5, max_camera_x))
        $ offset_x = screen_half_w - (tile_size * cam_x)

    # 4. Handle Vertical Camera Alignment & Tracking Point
    if (map_rows * tile_size) <= 1080:
        $ offset_y = screen_half_y - ((map_rows * tile_size) / 2.0)
        $ cam_y = map_rows / 2.0
    else:
        $ min_camera_y = screen_half_y / tile_size
        $ max_camera_y = map_rows
        $ cam_y = max(min_camera_y, min(room.center_y + 0.5, max_camera_y))
        $ offset_y = screen_half_y - (tile_size * cam_y)

    # 5. Render World Viewport
    fixed:
        at plane_3d

        # Draw background map
        add room.img:
            pos (int(offset_x), int(offset_y))

        # Extract all visual objects currently present on the active map
        $ active_denizens = []
        for row in room.map:
            for tile in row:
                if tile.occupant is not None:
                    if isinstance(tile.occupant, (MapDenizen, MapBuilding)):
                        $ active_denizens.append(tile.occupant)

        # SORTING FIX: Sort everything together using the new visual baseline attribute
        $ active_denizens.sort(key=lambda d: d.sort_y)

        # Render everything relative to the exact same camera baseline
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
                    matrixtransform RotateMatrix(-25, 0, 0) 
                
                add denizen.img

    # --- ENGINE CONTROLS (Kept flat/untransformed) ---
    if (rpg == True and commentFlag == False):
        key "keydown_K_UP" action SetVariable("moving_up", True)
        key "keydown_K_DOWN" action SetVariable("moving_down", True)
        key "keydown_K_LEFT" action SetVariable("moving_left", True)
        key "keydown_K_RIGHT" action SetVariable("moving_right", True)

        key "keyup_K_UP" action [SetVariable("moving_up", False), SetVariable("move", "")]
        key "keyup_K_DOWN" action [SetVariable("moving_down", False), SetVariable("move", "")]
        key "keyup_K_LEFT" action [SetVariable("moving_left", False), SetVariable("move", "")]
        key "keyup_K_RIGHT" action [SetVariable("moving_right", False), SetVariable("move", "")]

        if moving_up:
            timer 0.075 repeat True action [Function(room.movePlayerDenizen, 0, -1), SetVariable("g_dir", "back"), SetVariable("move", "_move")]
        elif moving_down:
            timer 0.075 repeat True action [Function(room.movePlayerDenizen, 0, 1), SetVariable("g_dir", "front"), SetVariable("move", "_move")]
        elif moving_left:
            timer 0.075 repeat True action [Function(room.movePlayerDenizen, -1, 0), SetVariable("g_dir", "left"), SetVariable("move", "_move")]
        elif moving_right:
            timer 0.075 repeat True action [Function(room.movePlayerDenizen, 1, 0), SetVariable("g_dir", "right"), SetVariable("move", "_move")]

        key "K_RETURN" action Function(grayInteracts)