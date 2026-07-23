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
            if not tile.occupant is None:
                $offx, offy = tile.occupant.getOffset()
                $tile_lc_x = tile_size * j + offset_x
                $tile_lc_y = tile_size * i + offset_y
                add tile.occupant.img:
                    pos (tile_lc_x + offx, tile_lc_y + offy)