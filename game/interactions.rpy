init python:

    #that's me??? only add something if it's funny
    def self_op(denizen):
        pass

    #i'm not interacting with you
    def no_op(denizen):
        pass

    #i'm not interacting with you
    def disappear(denizen):
        room.unoccupy (denizen.x, denizen.y)

    def self_op(denizen): pass
    def no_op(denizen): pass
    def disappear(denizen): room.unoccupy (denizen.x, denizen.y)
    def shop (denizen): renpy.jump("shopMenu")
    def library (denizen): pass
    def blacksmith (denizen): pass

    def leave_room (denizen):
        global room_name
        global room
        teleport_x = 0
        teleport_y = 0

        store.moving_up = False
        store.moving_down = False
        store.moving_left = False
        store.moving_right = False
        store.move = ""

        if room is not None:
            room.unoccupy(store.gray_sprite.x, store.gray_sprite.y)

        if (room_name == "gray_house"):
            room_name = "town"
            teleport_x = 23
            teleport_y = 17
        else:
            room_name = "gray_house"
            teleport_x = 9
            teleport_y = 5

        room = getattr(store, room_name)
        
        # FIX: Relocate the sprite position and map arrays correctly
        store.gray_sprite.x = teleport_x
        store.gray_sprite.y = teleport_y
        room.occupy(teleport_x, teleport_y, store.gray_sprite)
        
        # FIX: Align the room camera onto the fresh spawn coordinate location
        room.center_x = teleport_x
        room.center_y = teleport_y

        return True

    def shop (denizen):
        renpy.jump("shopMenu")

    def library (denizen):
        pass

    def blacksmith (denizen):
        pass

    def leave_rpg (denizen):
        global rpg
        rpg = False

        renpy.Return() 
