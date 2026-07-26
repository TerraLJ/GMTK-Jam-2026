# dialogue for interacting with Pink as Grey
label pink_interaction:
    # decides which conversation to jump to for Pink
    if day == 1 and not ate_breakfast1:
        jump p_breakfast1
    elif day == 2 and not ate_breakfast2:
        jump p_breakfast2
    elif day == 3 and lovedOneProgression < 5:
        jump p_day3
    elif lovedOneProgression == 0:
        jump p_convo1
    elif lovedOneProgression == 1:
        jump p_sweetsQuestDeliver
    elif lovedOneProgression == 2:
        jump p_convo2
    elif lovedOneProgression == 3:
        jump p_libraryQuestStart
    elif lovedOneProgression == 4:
        jump p_libraryQuestDeliver
    else:
        # lovedOneProgression == 5
        jump p_comfortEndingInitiate

label p_breakfast1:
    # TODO: IMPLEMENT PORTRAITS AND EXPRESSION CHANGES
    if not left_home and not declined_breakfast:
        p "Oh, I..."
        p "I really thought you were just going to head out immediately again."
        p "But this is good! We could have some breakfast together before you go!"

    else:
        p "We can still have a meal together, you know…!"

    p "..."
    p "Please..?"
    menu:
        "> You have [actionsLeft] actions left."

        "Eat breakfast with [p]. (This will take 1 action.)":
            g "...I suppose it's been some time since I last had a meal..."
            p "What?!"
            p "When's the last time you ate?"
            g "..."
            g "You know I've been busy."
            p "So busy you can't eat??"
            p "Don't be like that, [g]! You're the one who always told me we need to rest and eat to be able to do other things!" 
            p "I know you're worried about the curse, but it's only going to get harder to do things if you keep neglecting yourself!"
            g "But-"
            p "Nuh-uh! Not hearing it right now!"
            p "Let's get some food in the both of us, okay?"
            # fade to black, sound effects of dishes clinking and such? breakfast getting set up
            g "(...This is nice.)"
            g "(I've hardly any time recently for such... frivolities. But just the same...)"
            g "(I can't recall the last time I was able to share a meal with her, since the curse.)"
            g "(...)"
            g "(She looks so happy.)"
            p "..!"
            p "What's up? You're looking at me all serious."
            p "..."
            p "...If it's about having to spend extra time doing the dishes, I'll do them, don't worry..!"
            p "Go ahead and go out into town and do... Do your research stuff!"
            p "..."
            p "But, um... thanks. For having breakfast with me."
            p "I really missed it."
            "> You have gained 1 action for the day."
            $ ate_breakfast1 = True

        "I don't have time.":
            g "I'm sorry, [p]. There's just too little time left, with the curse."
            g "But I promise we will after I have an answer for it."
            p "..."
            p "...Okay."
            p "Um... good luck in town, then..!"
            $ declined_breakfast = True
    # back to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label p_breakfast2:
    if left_home or declined_breakfast:
        # If [Gray] leaves the building and returns OR after denying the meal
        p "I don't really want to have this if you don't have some, too."
    
    else:
        p "Good morning…! "
        p "I, um… I made food for the both of us again."

        if not ate_breakfast1:
            # If breakfast wasn’t eaten yesterday
            g "(...I don't think that's true. Only one of the plates is steaming, and the one in front of her isn't.)"
            g "(It might be my uneaten meal from yesterday. She set the warm one out for me.)"
            p "I just thought that maybe you'd be really hungry now, so... I gave you some extra!"
        
    p "So, [g]... could you please eat with me?"

    menu:
        "> You have [actionsLeft] actions left."

        "Eat breakfast with [p]. (This will take 1 action.)":
            p "..!" 
            p "Thank you! I really hope you enjoy it. And I'll handle the dishes today too, so don't worry…!"

            # If not on track for the comfort end: TODO
            if lovedOneProgression < 10:
                g "(...She looks like she wants to say more.)"
                g "(I wish I could ask what's on her mind, but I really can't afford to waste any more time.)"
                g "(Still… It is the least I can do, to offer gratitude.)"
                g "Thank you for the meal."
                g "(She nods and smiles, but I can tell it's strained. Maybe she'll be able to relax once I've found the answer.)"

            # Otherwise:
            else:
                g "I appreciate it."
                p "And I appreciate that you're hanging out with me! "
                p "I know you'd probably like to go back to researching how to get rid of the curse, but... As I said, this means a lot to me."

            g "(We ate the rest of our meal in silence. And afterward...)"
            p "Don't you feel better now that you ate? You even {i}look{/i} a little better, too!"
            g "(I suppose I do feel a little more refreshed.)"
            "> You have gained 1 action for the day."
            $ ate_breakfast2 = True

        "I don't have time.":
            g "I'm sorry, truly, but there just isn't-"
            p "Time. There just isn't time. I know..."
            p "Maybe... Maybe later, then."
            $ declined_breakfast = True
    # back to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label p_convo1:
    #If [Gray] has left the house but came back TODO
    if left_home:
        p "[g]! Hi!"
        p "..."
        p "Um... you're back early. Is everything okay?"

    # If [Gray] has not left after breakfast
    else:
        p "...Is everything okay?"

    menu:
        "> You have [actionsLeft] actions left."

        "I just want to talk with you. (This will take 1 action.)":
            jump p_sweetsQuestStart

        "Everything's fine.":
            p "Oh, okay! I'll just, um..."
            p "I'll just be here if you need me, then!"

        "I just wanted to check on you.":
            p "..!"
            p "..."
            p "...Aw, that's sweet! And, uh... Thanks for asking. I'm doing okay, promise!"
    # back to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label p_sweetsQuestStart:
    p "Oh! Um, was there something you wanted to talk about? "
    g "Not especially. I just wanted to listen to you speak for a while. "
    p "Ah, well..."
    p "I hadn't had the time to do much yet today--or at least, nothing you wouldn't already know about!"
    p "But I can't even begin to tell you just how much it meant to me that you agreed to have a meal with me."
    p "It's kinda been hard, you know? Watching you {i}work{/i} and {i}work{/i} and {i}research{/i} until you're about to fall asleep on your feet."
    p "I just don't like seeing you so... Drained! So even if you're not going to rest, 'cause I know you won't right now, knowing you had at least some food now makes me feel a lot better."
    p "And, um... I'm sorry if this sounds really selfish of me, but... It also gets really lonely when you're out. So getting to spend even a little bit of time with you right now helps that feeling a lot."

    menu:
        p "And, um... I'm sorry if this sounds really selfish of me, but... It also gets really lonely when you're out. So getting to spend even a little bit of time with you right now helps that feeling a lot."

        "I'm glad it's helping you.":
            p "And I'm glad it's helping the both of us!"
            p "I hope we'll have the time to have more meals together, too. I know you'll probably be busy for the rest of the day, but..."
            p "Maybe we can have one tomorrow, at least?"

            menu:
                p "Maybe we can have one tomorrow, at least?"

                "Of course.":
                    p "..!"
                    p "Well! I'll hold you to it, then! I'll even make your favorites so it's even harder to forget!"

                "I don't know...":
                    p "We can figure out if it works later..."
                    p "But there's got to be a little time to spare... Especially since food will give you more energy to spend on all your research stuff!"
                    p "So just... Give it a thought, okay?"

        "I'm sorry to leave you alone so much.":
            p "..."
            p "It's okay! I know why you're doing it. Breaking the curse is really important."
            p "And, if anything... I just wish I could help you more. I know you're really worried that something would happen to me if I did, but..."
            p "We were {i}both{/i} adventurers before this. And just because we had a bad run-in doesn't mean you need to be afraid for me."
            p "..."
            p "But I know you're just a worrywart, so... I understand why you want me here, where it's safe."

    p "Anyway... I dunno! That's about all I can really think of talking about right now. What about you?"
    g "I suppose… if it might soothe you a little more, is there anything I might be able to get you?"
    p "Oh..!"
    p "Well... I guess so? But it's nothing big or anything. It's not even that important."
    p "But if you find yourself at the shop, could you maybe grab me some sweets?"
    p "Or... Or anything, really, if it's something we can share later!"
    g "I see. If I'm able, I will, then."
    p "Yay!"
    $ lovedOneProgression += 1
    $ sweetsQuestProgression = 1
    $ actionsLeft -= 1
    if actionsLeft <= 0:
        jump endOfDay
    # back to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label p_sweetsQuestDeliver:
    if sweetsQuestProgression < 3:
        # dialogue chain reminding you about the quest
        p "You really don't have to go get any candy, though, if it's too much trouble! I'll see if I can find what I need to get some myself later."
    else:
        #delivering the sweets and the crystal
        p "Oh, you're back!"
        menu:
            "> You have [actionsLeft] actions left."
            
            "Deliver the sweets. (This will take 1 action.)":
                p "You got them? You really got them?"
                p "Oh, thank you, [g]! Thank you!!"
                p "..."
                p "I, um... I wasn't worried that you wouldn't, exactly. It was just a little favor and all."
                p "But... I didn't feel sure you would, you know?"
                p "You've just been really... Focused recently, so..."
                p "..."
                p "I guess all it is, really, is... Is that I didn't know if this was too far off your path to be worth handling right now. It is pretty trivial, after all."
                g "But I asked if you wanted anything, and you gave me an answer. Did you think after that, I'd neglect to fulfill the promise implicitly made?"
                p "I guess not! It's not really like you to do that."
                g "Exactly. Though perhaps I… do have something of a surprise for you, still."
                g "(I pulled out the second crystal I had gathered from the cave.)"
                p "Oh, that's so pretty. Where'd you get it?"
                g "The shopkeeper was kind enough to let me trade the crystals from the cave for goods. I had a little more than I needed, though, and thought perhaps you might find some joy in having it."
                p "The... Cave? As in the one west of here rumored to house the Wishgranter?"
                g "That one, yes."
                p "But that had to have..."
                p "..."
                p "Um, nevermind."
                p "Anyway, uh... This kinda reminds me! While you were gone, I had my own little adventure!"
                g "..!"
                p "Before you worry, it wasn't much, I promise. I just went out to spend some time by the river."
                p "I don't think it's all that interesting to talk about, since it is just the same old river as the one we crossed when we first arrived… but there's more dragonflies buzzing around there than back then!"
                p "Maybe the little baby dragonflies are all starting to grow up now that the weather's warmer?"
                p "But anyway, a lot of them liked to land on me. Their feet kinda tickle, by the way, though I don't think I mind! It was kinda nice, actually."
                p "Maybe we can go walk along it together later..?"
                g "Another time, perhaps? It's... Been something of a long day."
                p "Another time. But I'm holding you to it!"
                p "For now, though... go get some rest, okay?"
                python:
                    lovedOneProgression += 1
                    numCrystals -= 1
                    sweetsQuestProgression = 4
                    actionsLeft -= 1
                if actionsLeft <= 0:
                    jump endOfDay
            
            "Hold off for now.":
                g "(...Maybe I'll give this to her a little later...)"
                p "Um... Be safe out there..!"
    # back to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label p_convo2:
    #+If [Gray] has left the house but came back
    if left_home:
        p "Welcome back!"
    #+ If [Gray] has not left after breakfast
    else:
        p "You know, I'm glad you're still hanging around. It's nice."
        p "But, um..."

    p "What's up?"
    menu:
        "> You have [actionsLeft] actions left."

        "I just want to talk with you. (This will take 1 action.)":
            p "..."
            p "I... I don't know if I have much to talk about. I don't even know if I'll have much to talk about tonight, either."
            p "There's just not a lot going on for me. And, um... honestly, I think the stress is starting to get to me, too."
            p "But I'm sure it'll be fine! It does mean going out to the river again sounds like a lot, though."
            p "I'm thinking I'll do something calm at home today. Like, um… knitting. Or reading."

            menu:
                p "I'm thinking I'll do something calm at home today. Like, um… knitting. Or reading."

                "I didn't know you could knit.":
                    p "Haha! Yeah, um... I don't. But trial by fire, you know? Best way to learn!"

                "There aren't many books here.":
                    p "I know. But there's nothing wrong with rereading old favorites!"

            g "...But there is also a library nearby. It... Might not be too strenuous for you to visit and find something of value."
            g "I could even walk you there."
            p "..!"
            p "..."
            p "I... I appreciate the offer. I really do. But I think I'll be fine with what we have here. I mean, you... Um..."
            p "You really do keep a lot of your old beginner casting books. Why have you toted them around for this long?"
            g "...I suppose for not a particularly good reason, but... It was in the case you ever needed to learn. Had you ever chosen to, it would have been very simple to pass them down to you."
            p "But I never..."
            g "...I know. But, as I said, it was in case you ever did need to do so."
            p "Well... I still don't need to, but... Maybe I'll learn it anyway. There's not much better to do..!"
            g "It can be rather dull."
            p "I can handle that, silly. A little bit of textbook reading never killed anyone, and... And I think it's better to read that sort than lay around and waste the day away entirely."
            g "...That is... Decidedly true."
            p "See? It'll be fine! So don't worry about me and just... Do what you need to do, okay?"
            $ lovedOneProgression += 1
            $ actionsLeft -= 1
            if actionsLeft <= 0:
                jump endOfDay

        "Nothing.":
            p "That's good, I think! Better to have nothing of note going on, with all the stuff already weighing on you."
    # back to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label p_libraryQuestStart:
    # [FOR REGULAR ROUTES ONLY]
    if lovedOneProgression < 3:
        # unreachable. whatever
        p "Oh, don't worry about me feeling bored! If it really gets that bad, I'll..."
        p "..."
        p "...I'll go get it myself! Yeah!"

    else:
        p "Is there… something else you wanted to say to me?"
        menu:
            p "Is there… something else you wanted to say to me?"

            "Would you like me to bring you a book from the library?":
                p "I mean, I guess I kinda do? I just... I dunno. I don't want to bother you."
                p "..."
                p "..But it would be very nice. When we first arrived, the librarian had recommended I check out this one about the cats and the sun."
                p "Just don't go out of your way to get me that, okay?"
                #[BOOK QUEST START]
                $ lovedOneProgression += 1

            "Not especially. I wanted to check in on you.":
                p "Oh. Alright! And, um... I'm doing okay."
    # back to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label p_libraryQuestDeliver:
    if bookQuestProgression < 2:
        # dialogue chain reminding you about the quest
        g "(She looks tired. Maybe that's why she didn't even suggest she's going to try and get one herself.)"
        g "(...)"
        g "(I should really go over there and find something for her to read.)"
    else:
        #delivering the book
        p "What's up?"
        menu:
            "> You have [actionsLeft] actions left."

            "Deliver the library book. (This will take 1 action.)":
                p "..!"
                g "(Ah… I should have realized that regardless of what she said, she would get upset by such an act when she declined to go herself. She's too headstrong to suggest she could not do it herself.)"
                g "[p], I-"
                p "...Thank you."
                g "What?"
                p "Thank you for bringing me a book. And for taking the time out of your research to try and make me happy."
                p "I know you've been wanting to focus on finding an answer or cure or... Something, for this curse. A part of me wants that, too."
                p "But I've watched you struggle up until yesterday, and... I don't know. I think with the way we've been going, we would have {i}both{/i} ended up dead."
                p "And I really don't think that trying to save me is worth driving yourself into an early grave."

                menu:
                    p "And I really don't think that trying to save me is worth driving yourself into an early grave."
                    
                    "It's worth it if it could save you.":
                        p "If that meant losing my big sibling and having to deal with that life all alone, I don't know if it is."
                        p "And even if it was… I think you and I both know saving me isn't really your goal anymore. Otherwise, you'd probably not even be talking to me right now."
                        p "Don't worry, though. I think that's the best course of action, too."

                    "I realized there might be something more important.":
                    p "..."
                    p "...Yeah. I guess you must've, huh?"

                p "But anyway... We still have a whole day tomorrow, and... Well, I know you got it for me to read today, but if you'd be up for it... Maybe we could read the book together then?"
                g "How will you spend the rest of today, then?"
                p "Um… just talking to you, I guess! There's something I wanted to ask since yesterday, anyway."
                p "Did you really go into the cave adventurers were known to die in without any weapons?"
                g "...I wasn't truly weaponless. Even besides the minor spells I know, I..."
                g "I brought the old training sword you had."
                p "That toy? That thing could hardly scare off a rat, let alone anything that could really hurt you!"
                p "If you ever go back there again, you should really try and get some better equipment first. Doesn't this town even have a blacksmith?"
                g "I was hardly at risk. I only needed to grab the crystals."
                g "But... I will keep that in mind, if I do indeed return there."
                p "Good. That's good."
                p "..."
                p "...Thinking about that sword makes me miss adventuring again, though. I killed my first monster with that thing. Even if said monster was just... Kind of an overgrown rodent."
                p "But that was also far from home. Do you still remember that, and how we were lost for weeks? I think it's that kind of joy of exploration and discovery that I really miss."
                p "..."
                p "...And the thrill of fighting things that might curse you, too, I guess. Haha..."
                p "But, um... I guess it's kind of late now already, isn't it?"
                p "Let's get some rest so we can try and enjoy as much of tomorrow as we can, okay?"
                #[BOOK QUEST COMPLETE]
                $ lovedOneProgression += 1
                $ bookQuestProgression = 3
                $ actionsLeft -= 1
                if actionsLeft <= 0:
                    jump endOfDay
            
            "Not now.":
                g "Nevermind, it's nothing."
                p "Oh... Okay."
                g "(...Maybe I'll give this to her a little later...)"
    # back to rpg mode
    scene black with fastFade
    call screen map_screen with fastFade

label p_comfortEndingInitiate:
    g "(I can grieve later. For now... I should just spend what time we have left together with her.)"
    menu:
        "> Spend the rest of the day with [p]?"

        "Yes.":
            jump comfortEnding
        
        "No.":
            # back to rpg mode
            scene black with fastFade
            call screen map_screen with fastFade

label comfortEnding:
    g "Good morning, [p]."
    p "Morning..!"
    g "(...Oh. She's stumbling.)"
    p "Did you get to look outside yet? It looks really nice! The skies are clear, and there's a breeze..."
    p "Maybe we could go have a little... Picnic or something? And read the book together while we're out there?"

    menu:
        p "Maybe we could go have a little... Picnic or something? And read the book together while we're out there?"

        "That sounds nice.":
            p "Yay! I'll go get everything we need, don't worry!"
            g "..."
            g "Perhaps we can do this faster if I help, [p]?"
            p "Well... I guess I would appreciate the help!"
            #[FOLLOWING BGS ARE ALL OUTSIDE] TODO

        "I'm not sure we should do that.":
            g "(She just doesn't look like she's in any state to go out right now.)"
            p "...You mean we shouldn't go outside at all?"
            g "(...)"
            g "(But she looks so miserable.)"
            g "...Perhaps we could read in here for a while, and head outside later if you're steadier then?"
            p "Okay..! Okay... I can accept that."
            #[FOLLOWING BGS ARE ALL INSIDE UNTIL STATED OTHERWISE]

    # [rustling noises of cloth? load in appropriate cg based on location] TODO

    p "Okay! I think we can read now."
    p "..."
    p "...Hey... Um, maybe this is going to sound really silly, but..."
    p "Instead of us both trying to read it... Do you think you could maybe read it out loud for me?"
    g "(Read it aloud…? I hadn't done anything like that for her since she was a child.)"
    g "(Though I suppose it might be something a little more reminiscent of a storybook, with all its cats.)"
    g "(And it is the last day I have with her. Surely I can oblige this little request.)"
    g "Alright."
    g "Let's see..."
    g "(...Oh.)"
    g "(This is not anything like a children's storybook.)"
    g "(She seems excited to hear the story, though, so... I suppose regardless of the themes, I'll still read it to her.)"
    g "(...)"
    g "(But the more I read this tale, the more it feels morbidly relevant. Just as the sun blazes its way across the sky toward the horizon like a countdown to nightfall, they too are helpless to stop the impending tragedy.)"
    g "(Perhaps the same was always true for us, too. Perhaps a happy ending was never in the cards, no matter what I could have tried.)"
    g "(...)"
    g "(...!)"
    g "(...She's crying.)"
    g "[p]?"
    p "S-sorry... It just..."
    p "The ending just made me think of you. Of… of what will happen when I'm gone."
    g "..."
    p "...But that's too sad to talk about right now. There's still a good bit of time before moonhigh, and I don't want it to be all sad."

    #+ If they are not outside TODO
    # Hoping this doesn't need a separate variable? But idk
    p "Though... maybe now it'd be a good time to go out?"

    p "I... I mean, the sunset's gonna be pretty, and… maybe you can talk about the stars again?"
    p "Like when you used to tell me all about the stories behind those constellations?"
    p "No reason for all of that to be a downer because we talked about… stuff, right..?"
    g "..."
    g "I suppose so, yes."
    g "(Even if perhaps I don't agree it won't be weighed by sadness regardless.)"
    g "(...)"
    g "(...But she is right. The sunset is beautiful over the river.)"
    g "(The stars are, too. I don't think we've spent this long staring up at them since we were both little.)"
    g "(She hasn't changed much in that way. Yet again it's been hours, and she hadn't seemed to have looked away even once, as if she wanted to burn them to memory.)"
    g "(...)"
    p "The stars seem extra sparkly tonight."
    g "...They do, don't they?"
    p "I'm glad I got to see them before... Before..."
    p "..."
    jump comfortEnding2

label comfortEnding2:
    p "...Hey, [g]?"
    g "Yes?"
    p "You know, I'm... I'm still scared. I don't {i}want{/i} to die."
    p "But I think I accepted it was gonna happen a few days ago. "
    p "That's why I wanted to spend all this time with you. So maybe we could both end today not needing to regret the fact we didn't spend these last moments together."
    p "And I'm really glad we could! I missed being able to hang out with you."
    p "But... can I ask you for one more thing?"
    g "..."
    g "...I can do my best, but there's really not much I can give before midnight. There's just so little time."
    p "It's nothing big, I swear. You don't even have to get up."
    p "I just... I just want you to promise me something."
    p "Just promise me you'll take care of yourself when I'm gone."
    menu:
        p "Just promise me you'll take care of yourself when I'm gone."

        "...":
            p "Please? I... I'm worried you'll just let yourself wither away."
            p "Ever since it happened, you've not been taking care of yourself like you used to."
            p "And I'm scared that after tonight, you'll just... let go entirely."

            menu:
                p "And I'm scared that after tonight, you'll just... let go entirely."

                "...":
                    p "I just don't want you to die, too. I don't want you to die because you let your guilt eat you alive."
                    p "I know you tried your best. I {i}watched{/i} you work yourself to the bone. I just didn't realize just how badly you were doing that until you told me you couldn't remember the last time you ate."
                    p "You were neglecting yourself. And, looking back now... I think maybe you were about to start neglecting to spend time with me. And even if you had done that... I don't know if that would have made things any better."
                    p "Maybe there could have been an answer. But if there weren't... what then? It'd still end like these, but we wouldn't have gotten to have these last few days, either."
                    p "This way, at least I have a few more happy memories to die with, instead of..."
                    p "..."
                    p "...Instead of dying alone, just because my sibling was too focused on trying to find a cure to realize I wanted to spend time with them."
                    p "You did all you could. There's nothing for you to regret, I promise."
                    p "And I know there's a bright future waiting somewhere. I won't be able to see it, but I know you can."
                    p "So please, {i}live{/i}. Live for the both of us, okay?"
                    p "Can you promise me that? Please?"
                
                "I promise.":
                    jump promiseAccept

label plead:
    menu:
        p "Can you promise me that? Please?"

        "...":
            p "{i}Please?{/i} "
            jump plead
        
        "I promise.":
            jump promiseAccept

label promiseAccept:
    p "Thank you."
    # [cg of [Gray] looks at the sky. The moon is almost at its zenith]
    g "(...)"
    # [cg of [Pink] looking up with them.]
    p "Oh... it really is almost time, huh?"
    p "Haha..."
    p "..."
    p "I almost don't feel scared anymore. Just… sad to be going away."
    # [cg of her leaning against [Gray]? maybe?]
    p "But I guess this means goodbye."
    menu:
        g "(...)"

        "...Yeah.":
            p "Haha..! Just a \"yeah\"?"
            p "I guess you weren't ever really all that good with these kinds of things, but…"
            p "Well, it's okay. I know what you mean."
            p "But, um, I hope... I hope you remember..."

        "...Goodbye, [p].":
            p "...Bye, [g]."
            p "Remember your promise to take care of yourself, 'cause if there's an afterlife… I don't want to see you there for a long, long while."
            p "Because that means you're still okay here."
            p "And... And remember, um..!"
    menu:
        "..."

        "I love you.":
            p "...I love you too."
            p "Thank you for being there for me. Thank you for trying so hard to save me."
            p "I'm glad I got to be your sister."
            p "And... I hope you always, always remember... no matter what happens..."
    p "..."
    p "...Remember that I'll always love you."
    # [FIN: grave and bouquet? In memory of a sister loved]
    jump gameOver

label p_day3:
    g "(She looks weak...)"
    g "(I {i}will{/i} have a solution before moonhigh. There is no other option.)"
    p "...[g]?"
    scene black with fastFade
    call screen map_screen with fastFade