init python:

    #that's me??? only add something if it's funny
    def self_op(denizen):
        pass

    #i'm not interacting with you
    def no_op(denizen):
        pass

    #i'm not interacting with you
    def disappear(denizen):
        #TODO: keep track of the right room
        gray_house.unoccupy (denizen.x, denizen.y)