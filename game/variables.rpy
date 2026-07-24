# Place to keep all variables and flags so they don't get redefined elsewhere

# player variable points to either the character g or p
default player = g
default curseTransferCompleted = False

# Variables that are shared across both characters because they reset
default swordLevel = 0
default magicLevel = 0
default timesMagicPracticed = 0
default curseTransferObtained = False

# Discovery flags are not reset across runs
default g_curseTransferDiscovered = False
default g_curseBreakDiscovered = False
default p_curseTransferDiscovered = False
default p_curseBreakDiscovered = False

# Day and action related variables
default day = 1
default actionsLeft = 3
default breakfast = False

# Progression of interactions with Pink/Gray
default lovedOneProgression = 0

init python:
    def resetVariables():
        # Function to easily reset variables
        global swordLevel
        global magicLevel
        global timesMagicPracticed
        global curseTransferObtained
        global day
        global actionsLeft
        global breakfast
        global lovedOneProgression

        swordLevel = 0
        magicLevel = 0
        timesMagicPracticed = 0
        curseTransferObtained = False
        # discoveries persist between runs
        day = 1
        actionsLeft = 3
        breakfast = False
        lovedOneProgression = 0
        return

    def updateMagic():
        # returns True if level up occurred
        global timesMagicPracticed
        global magicLevel

        timesMagicPracticed += 1
        if timesMagicPracticed == 1 and magicLevel < 1:
            magicLevel += 1
            return True
        elif timesMagicPracticed == 3 and magicLevel < 2:
            magicLevel += 1
            return True
        elif timesMagicPracticed == 6 and magicLevel < 3:
            magicLevel += 1
            return True
        return False
