# Place to keep all variables and flags so they don't get redefined elsewhere

# player 0 is Grey, player 1 is Pink
default player = 0
default curseTransferCompleted = False

# Variables that are shared across both characters because they reset
default swordLevel = 0
default magicLevel = 0
default curseTransferObtained = False

# Discovery flags are not reset across runs
default g_curseTransferDiscovered = False
default g_curseBreakDiscovered = False
default p_curseTransferDiscovered = False
default p_curseBreakDiscovered = False

# Day and action related variables
default day = 1
default actionsLeft = 5
default extraAction = False
# ^ Split extraAction into two variables for Day 2 and 3? So Pink/Grey
# can have extra comments on if you're taking care of yourself?

# Progression of interactions with Pink/Gray
default lovedOneProgression = 0

init python:
    def resetVariables():
        # Function to easily reset variables
        swordLevel = 0
        magicLevel = 0
        curseTransferObtained = False
        # discoveries persist between runs
        day = 1
        actionsLeft = 5
        extraAction = False
        lovedOneProgression = 0
        return

    def newDay():
        # sets up variables for the next day
        day += 1
        if day == 2:
            actionsLeft = 3
        elif day == 3:
            actionsLeft = 1
        else:
            actionsLeft = 0
        if extraAction:
            actionsDone += 1
        extraAction = False