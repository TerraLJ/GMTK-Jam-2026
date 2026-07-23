#Grid/Tile Based
#character is centered, map moves
#interact key = item interact
#items are obstacles

init python:

    class LandMap:
        def __init__(self, map, img):
             self.map = map
             self.img = img

    class MapTile:
        def __init__(self, occupant=None):
                self.occupant = occupant

    house_map = []

    #number of rows
    for i in range(12):
        new_row = []

        #number of columns
        for j in range (19):
             new_row.append(MapTile)
        house_map.append(new_row)

        gray_house = LandMap(house_map, "gray house indoors.png")