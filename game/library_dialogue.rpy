label library:
    # shared start for entering library
    if curseTransferObtained and magicLevel >= 3:
        "I have everything I need now. I think I can cast the spell to transfer the curse..."
        menu:
            "...Should I do it?"

            "Yes.":
                $ curseTransferCompleted = True
                # TODO
                jump curseTransferEnding

            "No.":
                if player == 0:
                    jump library_g
                else:
                    jump library_p

label library_g:
    # library scenes when playing as Grey
    if not curseBreakDiscovered:
        "bweh"

    "I'm still not good enough to break the curse... Should I practice my magic?"

label library_p:
    # library scenes when playing as Pink

label curseTransferEnding:
    "placeholder."