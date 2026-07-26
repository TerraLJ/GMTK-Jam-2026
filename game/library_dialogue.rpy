image grave gray = "grave-gray.png"
image hug = "hug.png"
image moon gray = "bad.png"

label library:
    # shared start for entering library
    scene library with fastFade

    if curseTransferObtained and magicLevel >= 2:
        player "(I have everything I need now. I think I can cast the spell to transfer the curse...)"
        player "(...Should I do it?)"
        menu:
            "> You have [actionsLeft] actions left."

            "Transfer the curse. (This will take 1 action.)":
                $ curseTransferCompleted = True
                jump curseTransferEnding

            "Do not.":
                # For now, just always jump to library_g
                jump library_g
    # technically not a required line but ummm. I feel better with it there
    jump library_g

label library_g:
    # library scenes when playing as Grey
    if not g_curseBreakDiscovered:
        # Has never studied in the library before
        player "(A library... Perhaps I could find something in here about the curse?)"
        menu:
            "> You have [actionsLeft] actions left."

            "Look around. (This will take 1 action.)":
                player "(I combed through the library's vast collection, desperate for ANYTHING that might help my situation.)"
                player "(And...)"
                player "(I actually found something. An old spellbook, detailing a way to break even the strongest of curses.)"
                player "(It's an advanced spell, unlike anything I've ever tried to cast before.)"
                player "(But... It might be my only hope. I just need to practice, starting now.)"
                "> Time passes..."
                "> Your magical ability leveled up! It is now level 1."
                python:
                    magicLevel = 1
                    timesMagicPracticed = 1
                    g_curseBreakDiscovered = True
                    actionsLeft -= 1
                if actionsLeft <= 0:
                    jump endOfDay

            "Look for [p]'s book." if bookQuestProgression > 0:
                jump getPinkBook
            
            "Leave the library.":
                scene black with fastFade
                call screen map_screen with fastFade

    player "(I'm still not skilled enough to break the curse... Should I practice my magic?)"
    menu:
        "> You have [actionsLeft] actions left."

        "Spend time practicing magic. (This will take 1 action.)":
            player "(I read through the book and practiced my control over casting spells.)"
            if updateMagic():
                player "(I really feel like I'm getting better!)"
                "> Your magical ability leveled up! It is now level [magicLevel]."
            else:
                player "(Progress was slower today. I'm still making some, but... It just never feels like enough.)"
                "> You will need to practice again before you can level up..."
            $ actionsLeft -= 1
            if magicLevel == 3:
                jump spellEnding
            if actionsLeft <= 0:
                jump endOfDay
            else:
                scene black with fastFade
                call screen map_screen with fastFade
        
        "Look for [p]'s book." if bookQuestProgression > 0:
            jump getPinkBook
        
        "Leave the library.":
            scene black with fastFade
            call screen map_screen with fastFade

label getPinkBook:
    if bookQuestProgression == 3:
        # already delivered book
        player "(I already gave [p] her book. I hope she's enjoying it at home...)"
        player "(...I don't need to get her a second one.)"
        jump library_g
    elif bookQuestProgression == 2:
        # have book, not delivered
        player "(I already found the book [p] requested.)"
        player "(I should get it to her quickly.)"
        jump library_g
    else:
        # progression == 1, don't have book yet
        player "(Right, I came here for [p] today.)"
        # fade to black?
        player "(I spent some time searching for that book she asked for...)"
        player "(Fortunately, it wasn't too difficult to find.)"
        # fade background back in?
        player "(I should bring this back home to her.)"
        $ bookQuestProgression = 2
        jump library_g

label spellEnding:
    player "(I think... I think I've finally done it.)"
    player "(I understand the spell completely. I've honed my ability to wield my magic.)"
    player "(I can break the curse.)"
    player "(...)"
    player "-!? (When did it get so late!? I need to get home, now!)"
    # fade to black
    scene black with fastFade
    player "(I dashed out of the library as fast as I could, neglecting even to collect my belongings.)"
    # cg of grey looking up at the moon
    scene moon gray with fastFade
    player "It's... Already moonhigh."
    # fade to black followed by immediate fade out of black? like vision's fading
    scene black with fastFade
    scene moon gray with fastFade
    player "(I... I need to get home.)"
    # fade to black
    scene black with fastFade
    player "{i}[p]!?{/i}"
    player "(It was too late.)"
    player "({i}I{/i} was too late.)"
    player "(The curse had taken effect.)"
    player "([p] lay sprawled across the table in our home. Not moving. Dead.)" #TODO: description of how she's dead as hell
    #she seemed as though she may have been waiting for them. a sibling who never came home in time
    player "(She must have been waiting for me.)"
    player "(And I... I never--)"
    player "([p]...)"
    player "(I'm so sorry. I got so close. Just a little more time, and I {i}know{/i} I could have...)"
    player "(I wasn't enough.)"
    player "(I... I feel weak. I can't...)"
    jump gameOver

label curseTransferEnding:
    g "(It must have worked. I feel as if there is something growing inside my chest, something that wants to wrap my heart and force it still.)"
    g "(...)"
    g "(And it feels... Terrible. To think [p] had been burdened with this for any amount of time, and still kept that smile of hers on...)"
    g "(...No, I've no time to dwell on this. It's too close to moonhigh.)"

    if (room_name == "town"):
    # If not at home
    # TODO Terra help this might rely on map stuff i don't know your variables
        g "(But there's still enough time to go home. To talk to Pink one last time.)"
        
        scene black with fastFade
        scene home-bg with fastFade
    # [fade to black, fade back into home?]

    # else, If at home
    else:
        g "(I should talk to Pink one last time.)"

    g "[p]? Are you well?"
    show pink0004
    p "..."
    p "[g]... what did you do..?"
    g "I enacted a solution. You're free of the curse now, just as I swore you would be."
    show pink0011
    p "..!!"
    p "But what about you?! I'm not dumb, [g]! You were already in poor health putting everything you had into finding that stupid solution, but even then, you look..."
    p "..."
    p "You look like you're going to die soon."
    p "No, it's {i}worse{/i} than that. I suddenly feel so much better, and {i}you{/i} look like you're going to die at moonhigh, just like the curse said I would. [g], what did you {i}do{/i}?!"
    menu:
        p "No, it's {i}worse{/i} than that. I suddenly feel so much better, and {i}you{/i} look like you're going to die at moonhigh, just like the curse said I would. [g], what did you {i}do{/i}?!"

        "I transferred the curse.":
            show pink0004
            p "Why would you do that?!?"
            p "I accepted the fact I would die days ago! I made my peace with it!! And all I wanted was to spend my last moments with you!"
            p "But you were always so busy looking for answers, you never bothered to realize that!"
            p "Maybe it was wrong of me not to say it outright before today, but… I {i}wanted{/i} to hope that all your efforts would be worth it. That I wouldn't die after all."
            p "That… that we'd be able to go back to adventuring together after all of this."
            p "But now you're saying that'll never get to happen."

        "Only keeping the promise I made you.":
            show pink0004
            p "The one to save me?"
            p "Great! You managed to keep one promise, [g], but was it really worth all the time you left me alone to find an answer?! Was it really worth me having to suddenly realize I'm not just going to live, but I'm going to have to do that without the only family I have left?!"
            p "And..."
            p "And what about all the other promises you're going to break because you did this..?"
    p "..."
    show pink0011
    p "You promised we would get to spend all of tomorrow together. You {i}promised{/i}."
    p "[g]... Why did you have to do this?"
    #[note: same response but I think they should get different portraits]
    menu:
        p "[g]... Why did you have to do this?"

        "It was the only option I could find, and it was worth it.":
            show pink0012
            p "..."

        "Because I love you.":
            show pink0011
            p "..."
    p "...You stupid, self-sacrificial dummy..."
    p "Did you ever think I might not want to have to live in a world without you..?"
    menu:
        p "Did you ever think I might not want to have to live in a world without you..?"

        "But you'll manage. I know you will.":
            p "Maybe, but…"

        "I'm sorry.":
            show pink0007
            p "..."
            p "...I'm sorry, too. For snapping. I know you were just trying to save me."

    p "But it's going to be hard, having to face the future you just gave me."
    p "..."
    p "...There's no point in yelling at you about it, though. Not anymore. There's just no time left to waste on that, and I don't want those to be the last words you hear from me."
    # [cg of [Pink] hugging [Gray]?]
    scene hug
    p "Thank you for always trying to help me. No matter if I got mad or frustrated with you, I was always glad to be your sister."
    p "I'm glad to know you loved me so much you were willing to give up everything for me."
    p "I hope you know I love you, too. More than the world. And I'll love you when you're gone, too."
    p "But I'll make it through, even if it's hard. I'll make sure everything you did for me won't be wasted."
    p "So... So rest now, please. You deserve it."
    menu:
        p "So... So rest now, please. You deserve it."

        "Close your eyes.":
            "..."
            # [fade to black, then to ending]
    scene grave gray
    #[FIN: [Pink] kneeling by a gravestone with a bouquet. In memory of a sibling who gave her their all]
    "> You will now be returned to the main menu."
    $ MainMenu(confirm=False)()