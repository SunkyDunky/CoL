# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#setting
default hp = 15
default haveAndrew = False

# defining characters
define J = Character("Julia",color="#F400FF")
define R = Character("Renee", color= "#FF8700")
define Q = Character("Quol", color="#0094FF")
define A = Character("Andrew", color= "#ff0000")
define LQ = Character("Lenorra", color="#00ff11")
define G1 = Character("Agent1",color="#cacaca")
define G2 = Character("Agent2",color="#cacaca")
define A1 = Character("Audience1",color="#cacaca")
define A2 = Character("Audience2",color="#cacaca")
define L = Character("Lars",color="#fcff2e")
define Z = Character("A spectator?",color="#6303ff")

# define character sprites
image Renee :   
    "characters/Renee.png"
    zoom 0.49
image Renee worried:   
    "characters/Renee worried.png"
    zoom 0.49  
image Renee smile:   
    "characters/Renee smile.png"
    zoom 1.59
image Renee alt:   
    "characters/Renee alt.png"
    zoom 0.49       
image Renee alt smile:   
    "characters/Renee alt smile.png"
    zoom 0.49    
image Renee alt worried:   
    "characters/Renee alt worried.png"
    zoom 0.49       
image Julia :   
    "characters/Julia-half.png"
    zoom 0.2
image Julia nervious:   
    "characters/Julia-half nervious.png"
    zoom 0.2    
image Julia traumatized:   
    "characters/Julia-half traumatized.png"  
    zoom 0.2
image Julia exhausted:   
    "characters/Julia-half exhausted.png"  
    zoom 0.2
image Quol :   
    "characters/Quol.png"
    zoom 1.59
image Quol Angry:   
    "characters/Quol Angry.png"
    zoom 1.78
image Lenorra:   
    "characters/Lenorra.png"
    zoom 0.5  
image Andrew:   
    "characters/Andrew.png"
    zoom 0.5    
image Agent1:   
    "characters/Agent.png"
    zoom 0.5
image Agent2:   
    "characters/Agent.png"
    zoom 0.5
# defining bgs
image bg entrance = im.Scale("backgrounds/bg_entrance.png", config.screen_width, config.screen_height)
image bg entrance_ticket = im.Scale("backgrounds/bg_entrance_ticket.png", config.screen_width, config.screen_height)
image bg stage = im.Scale("backgrounds/stage.png", config.screen_width, config.screen_height)
image bg greenroom = im.Scale("backgrounds/greenroom.png", config.screen_width, config.screen_height)
image bg toilet = im.Scale("backgrounds/toilet1.png", config.screen_width, config.screen_height)
image bg ReneeBedroom = im.Scale("backgrounds/ReneeBedroom.jpg", config.screen_width, config.screen_height)
image bg Hotelalley = im.Scale("backgrounds/HotelAlley.png", config.screen_width, config.screen_height)
image bg black = im.Scale("backgrounds/black.png", config.screen_width, config.screen_height)

# define other images
image Renee bag :   
    "Renee bag.png"
    zoom 0.3

#transform
transform right_center_lower:
    xalign 0.75
    ypos 0.15
transform left_center_lower:
    xalign 0.25
    ypos 0.15
transform center_lower:
    xalign 0.5
    ypos 0.15
transform textbox_over:
    xalign 1
    ypos 0.54


#disclaimer
label splashscreen:
        show text """Disclaimer

        This demo of Concert of Liberation is a work in progress and intended solely as a test of concept. Please be aware that all content within this demo is unfinished and may not represent the final quality or features of the intended game. Bugs, glitches, and incomplete elements are expected. Your feedback and insights are highly appreciated as they will help us improve and shape the final product. Thank you for participating in this early stage of development."""with dissolve 
        pause 5.0
        hide text with dissolve
        return


#selection screen
image bg entrance_ticket_dark = im.Scale("backgrounds/bg_entrance_ticket_dark.png", config.screen_width, config.screen_height)
screen character_selection:
    vbox:
        xalign 0.5
        yalign 0.5
        hbox spacing 40:  # Add space between each option
            imagebutton:
                idle Transform("ticket_Renee.png", size=(config.screen_width / 5, config.screen_height * 2 / 3), zoom=1.0)
                hover Transform("ticket_Renee.png", zoom=1.1)
                action Jump("Sorry")
            imagebutton:
                idle Transform("ticket_Julia.png", size=(config.screen_width / 5, config.screen_height * 2 / 3), zoom=1.0)
                hover Transform("ticket_Julia.png", zoom=1.1)
                action Jump("Julia_Start")
            imagebutton:
                idle Transform("ticket_Quol.png", size=(config.screen_width / 5, config.screen_height * 2 / 3), zoom=1.0)
                hover Transform("ticket_Quol.png", zoom=1.1)
                action Jump("Sorry")
    text "{b}Choose a Character{/b}" size 40 align (0.5, 0.93)  # Add title at the bottom of the screen


#timer
default downer = 0

screen timerDown(rangeD, missed_event):
    on "show" action SetVariable("downer", rangeD)
    frame:
        xalign 0.5
        yalign 0.1
        hbox:
            timer 0.1 action If(0 < downer, true = SetVariable("downer", downer - 0.1), false = [Hide("timerDown"), Jump(missed_event)]) repeat True
            hbox:
                xalign 0.5
                bar:
                    value AnimatedValue(value=downer, range=rangeD, delay= 0.1)
                    yalign 0.0
                    xmaximum 500
                    bar_invert True
                    right_bar "gui/bar/left.png"
                    left_bar "gui/bar/right.png"
                    ysize 10  # Adjust this value to change the thickness of the bar
                bar:
                    value AnimatedValue(value=downer, range=rangeD, delay= 0.1)
                    yalign 0.0
                    xmaximum 500
                    ysize 10  # Adjust this value to change the thickness of the bar
                    



# QTE choice screen
screen qte_choice(items):
    style_prefix "qte"
    zorder 1
    for i in items:
        frame:
            xalign i[2]  # Adjust this to move the box horizontally
            yalign i[3]  # Adjust this to move the box vertically
            has vbox:
                textbutton "{size=-10}" + i[0] + "{/size}"xalign 0.5 action [Hide("timerDown"), Jump(i[1])] style "qte_button"

#temp hp screen
screen display_hp:
    text "HP: [hp]" xpos 0.1 ypos 0.1


#Illustrations
image JS1FS = im.Scale("JS1/JS1FS.png", config.screen_width, config.screen_height)



# The game starts here.

label start:
    show bg entrance
    pause 2.0
    scene bg entrance_ticket_dark with Dissolve (3.0)
    pause 0.5
    call screen character_selection
    with Fade(1.0,0.0,1.0)
    return

label Sorry:
    "sorry this character isn't available for now, Julia is available though."
    jump Julia_Start
    return

label Julia_Start:
    window hide 
    pause 1.0 
    play music "Audio/Athena.mp3"
    play movie "images/opening.webm"
    show bg stage
    pause 1.0 
    window show
    show Julia at textbox_over
    $ renpy.pause(23, hard=True)
    J"(In the crowded and noisy venue, I find myself standing above the stage, my fingers absentmindedly gripping the neck of my guitar.)"

    stop music fadeout 20.0

    J"""(The vibrant lights and pulsating music create a whirlwind of sensory overload around me, but my senses are suddenly numbed as my gaze lands on a familiar figure.)

    (Standing at the back of the venue are two enigmatic individuals, dressed in sleek white suits, their presence sending a jolt of disbelief through my core.)"""

    hide Julia

    # Fade in the new music over 5 seconds
    play music "StageBGM.mp3" fadein 10.0

    show Agent1 at left_center_lower with Dissolve(0.5)
    show Agent2 at right_center_lower with Dissolve(0.5)
    show Lenorra at Transform (yalign=5.5, xalign=0.5) with Dissolve(0.5)

   
    J"""(I can barely comprehend what I'm seeing.)

    (The agents from NewFutures Institute have infiltrated this concert.)

    (The music continues to blast through the air, but the sounds fade into the background as my focus narrows solely on the ominous figures before me.)

    (Everything seems to move in slow motion as the spotlight illuminates the agents.)

    (Their presence looms over the crowd, casting a shadow of unease and uncertainty within me.)

    (Emotionally stunned, I struggle to find my footing.)

    (Thoughts race through my mind, but clarity eludes me.)

    (This isn't a good sign.)"""

    hide Agent1
    hide Agent2
    hide Lenorra
    show Julia exhausted at textbox_over
    menu:
        J"(What should I do?)"
        "Warn my bandmates about them":
            hide Julia
            Z"That option is unavailable...for now."
            show Julia exhausted at textbox_over
            jump J2
        "Ignore them and hope it doesn't worsen the situation":
            jump J2

    return

label J1:
    J"""I should tell them about this.
    
    Who should I warn first though..."""
    show Julia at textbox_over
    "a"
    show Julia nervious at textbox_over
    "a"
    show Julia traumatized at textbox_over
    "a"
    show Renee at center_lower
    "a"
    show Renee worried at center_lower
    "a"
    show Renee smile at center_lower
    "a"
    show Quol at center_lower
    "a"
    show Quol Angry at center_lower
    "a"

    show screen timerDown(3, "missedit")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Timed choice 1", "choice1", 0.2, 0.3),  # xpos and ypos for choice 1
        ("Timed choice 2", "choice2", 0.8, 0.7)   # xpos and ypos for choice 2
    ])
    return

label missedit:
    "I missed it..."
    jump finished

label choice1:
    "I picked choice 1. It was ok I guess."
    jump finished

label choice2:
    "I picked choice 2. It was ok I guess."
    jump finished

label finished:
    "And we're done"
    return
    menu:
        J"Who should I warn first though..."
        "Quol":
            jump JQ0
        "Renee":
            jump JR0


#J2-Julia self routes
label J2:
    show Julia nervious at textbox_over
    J"""(I ignore the agents, not wanting to deal with any confrontations.)

    I should just ignore them...

    (I mutter to myself, trying to convince myself that everything will be fine if I simply pretend they're not there.)"""
    hide Julia

    show Agent1 at center_lower with Dissolve(0.3)
    pause 0.5
    hide Agent1 with Dissolve(0.3)

    show Julia traumatized at textbox_over

    J"""(But as one of the agents takes a step closer, my heart leaps into my throat, and my previous confidence wavers.)

    They... they are coming closer...

    (I stammer, my voice barely above a whisper.)

    (Panic starts to grip me, and my mind races, desperately searching for a solution.)

    I should do something... right?"""


    menu:
        J"What do I do.."
        "Stand my ground, don't move a muscle..":
            jump JS0
        "I have to leave, I have to go!":
            jump JH0

label JS0:
    # agent tries dragging her
    show Julia nervious at textbox_over
    J"(As I was frozen in fear, I was caught off guard by the agent suddenly lunging at me from below the stage)"
    hide Julia
    show Agent1 at Transform(xalign=0.5, yalign=0.1, zoom=1.5)
    
    J"""(Panic courses through my veins as their grip tightens around my leg, threatening to drag me off the stage.)
    
    {b}{i}Aaaah!{/i}{/b}

    (My instinct kicks in, overriding my initial shock.)

    (With every ounce of strength I can muster, I fight against the agent's grip, desperately wriggling and twisting in an attempt to break free.)

    "I have to back up! I have to back up!"

    (With a blend of panic and a hint of newfound determination, I felt a surge of adrenaline.)

    (It fuels my movements as I manage to loosen the agent's hold.)

    (Stumbling backwards, I narrowly escape being pulled off the stage, my heart pounding in my chest.)"""

    hide Agent1 with Dissolve(0.3)

    show Julia traumatized at textbox_over

    J"""(The sudden commotion disrupted the liveliness of the concert, a deafening silence)

    (The crowd errupted as people were panicking from the chaotic scene unfolding before them.)"""
    hide Julia
    A1"It's The Institute!"
 
    A2"Wha- Why would The Institute be here?"

    show Julia nervious at textbox_over

    J"""(Amidst the confusion, I strain to catch snippets of their conversations, hoping to glean some understanding of the situation.)

    (However, before I can piece together the puzzle, the agents, realizing that their presence has been exposed, yells out to the audience.)"""

    hide Julia

    show Agent1 at center_lower with Dissolve(0.3)

    G1"{b}CIVILLIANS, PLEASE EXIT THE VENUE!!!{/b}"

    hide Agent1 with Dissolve(0.3)

    show Julia exhausted at textbox_over
    
    J"""(The audience, rushes and funnels out the exit like a frantic river, leaving us alone with the agents in the hall.)

    What... what just happened? 

    (Sweat trickles down my forehead, my hands trembling uncontrollably.)"""

    hide Julia

    show Quol Angry at left_center_lower with Dissolve(0.3)
    show Renee worried at right_center_lower with Dissolve(0.3)

    J"(Quol and Renee, tightly grasping their instruments, finally speaks up)"

    R "I...It's them, I did everything they wanted, why are they here?"

    J"(Her voice trembling mildly, her hands shakingly reaches for her whip.)"

    Q"These fuckers again!!"
    
    J"(Quol barked at the infiltrators in frustration)"
    
    Q"Don't you DARE lay a finger on any of us!"

    J"""(Her voice now raspy and laced with anger, she pulls up her sleeves in preperation.)

    (I find myself at the back of the stage, overwhelmed and at a loss for words.)

    (My eyes darted between the chaotic scene unfolding before me and the unwavering bravery of Quol.)

    (It's in this moment, that I realise I must do something other than stay in this vulnerable position.)"""

    menu:
        J"I'm hyperventilating.."
        "I should snap out of it":
            jump JS1
        "Run..I have to leave!":
            hide Renee
            hide Quol
            jump JH0

label JH0:
    show bg stage 
    show Julia traumatized at textbox_over
    J"""(As panic grips my racing mind, I sprint towards the backstage area, my breath coming in ragged gasps.)

    (The urgency of the situation propels me forward, my heart pounding in my chest.)

    (Two options dominate my thoughts like beacons of fleeting respite: the green room or the toilets.)

    (I must make a swift decision.)"""

    menu:
        J"where...where should I go.."
        "Green Room":
            J"I have to go, I have to go!"
            jump JS2
        "Toilet":
            jump JH1    

label JH1:
    play music "Fear_And_Terror.mp3"
    show bg toilet 
    show Julia at textbox_over with Dissolve(0.3)
    J"""huff...huff...

    I'm safe...aren't I?

    What can I do now...what do I do??"""

    menu:
        "Go find Andrew":
            hide Julia
            jump JS2
        "Rush and help your friends":
            hide Julia
            show bg stage with fade
            jump jhfs5
        "Don't go outside":
            hide Julia
            jump JH2



label JS1:
    hide Quol with Dissolve(0.3)
    hide Renee with Dissolve(0.3)
    show Julia at textbox_over
    J"""(As the chaos ensues and my initial shock begins to fade, a fire ignites within me.)

    (Seeing as my bandmates valiantly defending me from the agents' onslaught, a surge of determination courses through my veins.)"""

    menu:
        J"Calm down...calm down..."
        "I need to help my friends":
            jump JS1FS
        "I have to do something!":
            jump JS1FS
        "I can't just stand and do nothing!":
            jump JS1FS        

label JS1FS:
    show Julia nervious at textbox_over
    J"""(I can't stand idly while they put themselves in harm's way. I need to help them.)

    (With a deep breath, I snap out of my daze, focusing my attention on the unfolding fight.) 

    (My eyes quickly scan the area, searching for anything that could aid me in this sudden battle for survival.)"""
    
    hide Renee with Dissolve(0.3)
    hide Quol with Dissolve(0.3)
    show Renee bag at Transform(xalign=0.5, yalign=0.4) with Dissolve(0.3)

    J"""(And then I spot it ... my trusty bat, safely tucked inside Renee's bag.)

    (But before I can fully process my next move, my attention is abruptly diverted.)"""

    hide Renee bag
    show JS1FS
    show screen display_hp
    J"(An agent charges towards me, wielding a baton and swinging it with force.)"
    menu:
        J"gasp!"
        "Try to dodge the attack":
            hide JS1FS
            show Agent1 at center_lower with Dissolve(0.3)
            jump js1fsa
        "Scream":
            $ hp -= 3
            if hp <= 0:
                # If hp is 0, jump to the game_over label
                jump game_over
            hide JS1FS
            show Agent1 at center_lower with Dissolve(0.3)
            jump js1fsb
        "Reach for my bat":
            $ hp -= 1
            if hp <= 0:
                # If hp is 0, jump to the game_over label
                jump game_over
            hide JS1FS
            hide Julia
            show Agent1 at center_lower with Dissolve(0.3)
            jump js1fsc

# fight scene JS1
label js1fsa:
    # Julia dodges attack
    # No hp lost
    
    J"(Instinct kicks in, and I rely on my reflexes and agility.)"
    play sound "SFX/JS1FS/batonswoosh1.mp3" volume 4
    J"""(I lean to the side, narrowly dodging the incoming strike.)
    
    (I stare in disbelief as I try to process how close I was to being hit.)
    
    (But my relief is short-lived. The agent, undeterred by the missed strike, quickly regains their composure.)"""
    
    jump js1fsd

label js1fsb:
    # Julia gets struck with the baton
    $hp -= 3
    
    J"""(I'm overcome with shock and instinctively let out a loud, piercing scream.)
    
    (The sound reverberates through the air, momentarily filling the space with my alarm and surprise.)
    
    (I react instinctively, raising my arms in a desperate attempt to shield myself. In a split second, my forearms form an X-shaped barrier, intercepting the full impact of the baton.)"""
    pause 0.5
    play sound "SFX/JS1FS/batonhit.mp3" volume 4
    pause 1.0
    Q"Julia! are you alright?!?"
    
    J"(Quol's voice cuts through the chaos)"
    
    Q"I'll be there! Hang on Julia! Fight back!"
    
    J"(I gather up myself and endure the pain, then look upwards at the agent.)"
    
    jump js1fsd

label js1fsc:
    # Julia gets her bat but gets hit in the leg(?)
    $hp -= 1
    
    J"(As I swiftly dash towards Renee's bag, my eyes fixated on retrieving my bat, a sudden impact jolts through my leg.)"

    play sound "SFX/JS1FS/batonhit.mp3" volume 5
    
    J"""(The agent's swinging baton connects with my lower leg, causing an intense burst of pain to surge through my body.)
    
    (The force of the blow sends me off balance, causing me to stumble and stagger in my attempt to reach the bag.)
    
    (However, I manage to snatch my bat from Renee's bag)"""
    
    menu:
        J"and next, I'll.."
        "Block":
            jump js1fse
        "Hit him back":
            jump js1fsf

label js1fsd:
    J"(He quickly recovers himself and prepares for another hit)"
    
    menu:
        J"What do I do..?"
        "Scream":
            jump js1fsg
        "Try to dodge the attack":
            jump js1fsh
        "Reach for your bat":
            jump js1fsi

label js1fsg:
    J"""{b}AAAAAH!{/b}
    
    (I let out a startled cry.)
    
    (Voice trembling with fear and frustration, as well as an overwhelming hopelessness.)"""

    hide Agent1
    show Quol at center_lower with Dissolve(0.3)

    "(However, before the baton makes contact with me, Quol swiftly intervenes.)"
    
    play sound "SFX/JS1FS/impactkick.mp3" volume 3

    J"""(With a swift kick, she delivers a powerful blow to the agent, sending them crashing to the ground, unconscious.)
    
    (Afterwards, she extends a hand towards me, her voice filled with concern.) """
    
    Q"You alright, Julia?"
    
    J"""(I nod in response.)
    
    Thank...Thank you..."""
    
    Q"Better fight back next time."
    
    J"(I silently watched as she goes over to Renee's bag and pulls out my bat, then tosses it to me.)"
    
    Q"Better keep it in your hands at all times."
    
    jump js1fsafter



label js1fsh:
    J"""I'll dodge, it'll be fin-
    
    Ah!"""
    
    pause 0.5
    play sound "SFX/JS1FS/batonwoosh2.mp3" volume 5
    pause 0.5

    J"(Just as I gather my resolve to evade the agent's attack, I stumble over my own feet)"
    
    play sound "SFX/JS1FS/batonhitbat2.mp3" volume 4

    J"""(I collide with the ground, as pain shoots through my body)
    
    Ouch!
    
    (The impact leaves me momentarily disoriented, my breath catching in my throat.)
    
    (Frustration and fear wells up within me as I watch the baton swinging down towards me.)"""
    
    hide Agent1
    show Quol at center_lower with Dissolve(0.3)

    "(However, before the baton makes contact with me, Quol swiftly intervenes.)"
    
    play sound "SFX/JS1FS/impactkick.mp3" volume 3

    J"""(With a swift kick, she delivers a powerful blow to the agent, sending them crashing to the ground, unconscious.)
    
    (Afterwards, she extends a hand towards me, her voice filled with concern.) """
    
    Q"You alright, Julia?"
    
    J"""(I nod in response.)
    
    Thank...Thank you..."""
    
    Q"Better not trip next time."
    
    J"(I silently watched as she goes over to Renee's bag and pulls out my bat, then tosses it to me.)"
    
    Q"Better keep it in your hands at all times."
    
    jump js1fsafter

label js1fsi:
    J"""(As the agent lunges towards me, their baton poised to strike, I gathered the courage to finally reach for my bat.)
    
    (Pouncing backwards, I land next to Renee's bag, and lifted my bat out of it.)
    
    (My grip tightens around the bat, my knuckles whitening as I prepare to meet the agent's attack head-on.)
    
    (The agent's baton hurtles towards me, and I brace myself for the impact.)"""

    play sound "SFX/JS1FS/batonwoosh2.mp3" volume 7

    pause 0.5

    play sound "SFX/JS1FS/batonhitbat1.mp3" volume 5


    J"(I skillfully parry the agent's attempts to strike back.)"
    
    play sound "SFX/JS1FS/batonhitbat2.mp3" volume 3

    J"(I block again)"
    
    play sound "SFX/JS1FS/batonhit2.mp3" volume 3

    hide Agent1 with Dissolve(0.3)

    J"(and finally deliver a hard blow, knocking the agent out cold.)"
    
    show Quol at center_lower with Dissolve(0.3)

    Q"Good job!"

    hide Quol with Dissolve(0.3)
    
    J"(Quol compliments my resolve.)"
    
    jump js1fsafter

label js1fse:
    J"I should block him"
    
    play sound "SFX/JS1FS/batonhitbat2.mp3" volume 3

    J"""(As the agent launches their attack, I swiftly raise my bat, positioning it as a shield against the incoming strike.)
    
    (In the brief moment following the block, my mind races, preparing for the next move.)
    
    And then..I'll hit him back!"""
    
    jump js1fsf

label js1fsf:
    J"AAuaAGGGGHHHH!"
    
    play sound "SFX/JS1FS/batonhit.mp3" volume 5

    J"""(With a surge of energy, I propel myself forward, As I channel a powerful swing towards the agent.)
    
    (I watch as the agent staggers backward, shaking with disbelief.)
    
    (Moments later, they collapse to the ground.)"""
    
    jump js1fsafter

label js1fsafter:
    
    hide Quol
    hide Agent1
    hide screen display_hp

    show Julia exhausted at textbox_over

    J"""At least we have one less to deal with now...

    (I let out a tired sigh as I cast a glance at the fallen body, sprawled on the ground.)

    (The defeated foe lay motionless, a testament to our hard-won triumph.)

    (With a heavy heart, I shifted my focus to assess the state of my companions.)"""

    hide Julia

    show Renee worried at right_center_lower with Dissolve(0.3)

    R "Look! There's still more of them coming in from the entrance."

    J"""(I observed Renee, her face etched with her unyielding will, desperately fending off two agile Agents.)

    (With lightning-fast reflexes, she deftly swung her whip, each crack of the lash a symphony of defiance against overwhelming odds.)"""

    R "I can't hold this up forever!"

    show Quol at left_center_lower with Dissolve(0.3)

    Q"Same!"

    J"""(Quol, standing her ground nearby, fought off two relentless Agents of her own.)
    
    (They lunged at her, attempting to subdue her, but she fought back with a flurry of kicks and quick dodges.)"""

    Q"Get away from us or you'll end up like your fucking friend!"

    J"""(The determination in Quol's voice echoed through the chaos as she unleashed her own brand of defiance, refusing to yield to their onslaught.)

    (Watching them fight, I could feel a powerful momentum building within me, an irresistible urge to join the fight.)

    I want to help..

    (But who should I help first?)"""

    menu:
        J"I want to help.."
        "Help Quol first":
            jump JS11
        "Help Renee first":
            jump JS12    


label JS11:
    hide Renee
    hide Quol

    show Julia traumatized at textbox_over

    J"I'll help Quol first!"

    hide Julia

    show Agent1 at center_lower with Dissolve(0.3)

    J"""(Without hesitation, I propelled myself forward, instantly closing the distance between me and the Agent.)

    (Gripping my bat firmly, I swung it with all my might, delivering a powerful blow that connected with the Agent's body.)"""

    hide Agent1 with Dissolve(0.3)

    show Julia exhausted at textbox_over

    play sound "SFX/JS1FS/batonhit2.mp3" volume 3
    
    J"(The force of impact sent them sprawling to the ground, momentarily stunned.)"

    hide Julia

    show Quol at center_lower with Dissolve(0.3)

    J"""(Quol's eyes widened briefly in surprise, but a grateful smile quickly spread across her face. )

    (She wasted no time, using the opening I had created to knock down the second Agent with a kick swiftly.)

    (The air crackled with a mix of adrenaline and relief as Quol, and I stood side by side, our united front a testament to our shared resolve.)

    (The tides of battle seem to have shifted in our favour, even if just for a moment.)"""

    hide Quol with Dissolve(0.3)

    show Julia traumatized at textbox_over

    J"""(However, I turned my head towards the direction of Renee and witnessed her arm getting hit by the baton of one of the agents and tumbling to the floor.)

    (My heart skipped a beat.)

    (The sight sent a surge of worry coursing through me, momentarily overshadowing the triumph of our successful attack on the Agents.)"""

    hide Julia

    show Renee worried at center_lower with Dissolve(0.3)

    J"""(Without a second thought, I rushed to her side, my concern overriding any other consideration.)

    Renee, are you alright?

    (I was trembling and had no idea what to do.)

    (As panic threatened to consume me, my mind raced, desperately searching for a solution.)"""

    hide Renee with Dissolve(0.3)
   
    J"(And then, in that moment of uncertainty, a vivid memory flashed in my mind—a scene I had shared with Renee not too long ago.)"

    show bg ReneeBedroom
    play music "Calm_After_the_Storm.mp3"

    J"""(Renee's room was bathed in soft, warm light as she and I sat side by side on the edge of the bed.)

    (It had been a long and challenging day, and we sought solace in this quiet moment of respite.)"""
   
    show Renee alt at center_lower with Dissolve(0.3)

    J"""(I looked at Renee, her presence a comforting anchor in the storm of uncertainty that swirled within me.)

    (The weight of the future pressed heavily on my mind, filling me with a sense of unease.)

    (I couldn't help but express my concerns.)

    Renee...

    I'm...uncertain about the future...
    
    It's like..like as if I'm standing at a crossroads, not knowing which path to take..

    I'm scared... that I would make wrong choices or I would not live up to my potential.

    (Renee turned to me, her eyes filled with a mixture of understanding and compassion.)

    (After a brief silence, she touched my shoulder gently.)"""

    R """Julia.

    I kind of understand that feeling. 

    You see... there was a time when I was near death when everything seemed lost. 

    But surviving taught me the value of life and each moment's preciousness."""

    J"(Her words resonated deep within me, stirring a renewed perspective.)"

    show Renee alt smile at center_lower

    R """Being alive allows for endless possibilities, Julia. 

    It opens doors to discovering the meaning of our existence and the roles we want to play in this world. 

    It's not about finding all the answers right away, but about embracing the journey and exploring what truly matters to us."""

    J"""(Her words held a profound truth, reminding me to cherish the gift of life and find solace in the process of self-discovery.)

    (Renee's unwavering belief in the importance of protecting one another echoed in my heart, reminding me of the bond we shared.)

    (Moved by her sincerity, I nodded, gratitude and determination shining in my eyes.)

    Thank you... Renee.

    (Renee smiled warmly, her gaze filled with trust and camaraderie.)"""

    R "I wouldn't want to see my best friends being in pain, would I?"


    play music "StageBGM.mp3"
    hide Renee with Dissolve(0.3)
    show bg stage with fade

    J"""(I snapped back to reality and held my bat tightly as I knocked down the agent who injured Renee.)

    (I realised that I had to protect everyone.)"""

    jump JS13

label JS12:
    hide Renee
    hide Quol
    J"I'll help Renee first."

    show Agent1 at center_lower with Dissolve(0.3)

    J"""(Swiftly, I closed the distance between Renee and her assailant.)

    (As I approached, I noticed an opening—a split second where my approach momentarily diverted the Agents' attention.)

    (Seizing the opportunity, I gripped my bat firmly.)

    (I swung it with all my might, delivering a powerful blow that connected with the Agent's body.)"""

    play sound "SFX/JS1FS/batonhit2.mp3" volume 3

    hide Agent1 with Dissolve(0.3)

    J"(The force of impact sent them sprawling to the ground, momentarily stunned.)"

    show Renee at center_lower with Dissolve(0.3)

    J"""(Fueled by my unexpected intervention, Renee swiftly took advantage of the moment.)

    (Her whip cracked through the air, striking the other Agent with a resounding crack.)

    (The enemy stumbled backwards, defeated and unconscious.)

    (A mixture of relief and determination washed over us. Renee's eyes met mine, gratitude and understanding passing between us in that fleeting moment.)"""

    hide Renee with Dissolve(0.3)

    J"""(However, I turned my head towards the direction of Quol and witness her leg getting hit by the baton of one of the agents and tumbling to the floor.)

    (My heart skipped a beat.)

    (The sight sent a surge of worry coursing through me, momentarily overshadowing the triumph of our successful attack on the Agents.)"""

    show Quol at center_lower with Dissolve(0.3)

    J"""(Without a second thought, I rushed to her side, my concern overriding any other consideration.)

    Quol, are you alright?

    (I was trembling and had no idea what to do.)

    (As panic threatened to consume me, my mind raced, desperately searching for a solution.)"""

    hide Quol with Dissolve(0.3)

    J"(And then, in that moment of uncertainty, a vivid memory flashed in my mind—the scent of rain and mud..)"

    show bg Hotelalley with fade
    play music "Anxiety_Shows.mp3"

    J"""(A few weeks after I escaped from the NewFutures Institute and first meeting Quol.)

    (We tried to stay low, trying our hardest to scrape by, with the anxiety of being caught constantly looming over my mind.)

    (I had contacted someone who works for my family-run hotel, the only person who agreed to risk themselves and help me out.)
    
    (I was waiting in a dark alleyway behind the hotel with Quol beside me, I kept fiddling my thumbs)
    
    (This is a bad idea, this is a bad idea...)
    
    (The rain falling deafeningly on the hood of my raincoat, as the backdoor of the hotel swings open.)"""
    
    L"""Sorry to keep you all out in the rain, today's a hectic shift.
    
    I can't be out here for too long or they'd realize I'm gone, since you left this place became like The Institute's personal playground.
    
    There's that one girl from The Institute, Lenorra. 
    
    She acts all nice and dutiful when her boss is looking, but as soon as the Head Scientist turns around she'd just order us around like we are her personal servant or somethi-"""
    
    show Quol at center_lower with Dissolve(0.3)

    J"(Quol glares at Lars in annoyance)"
    
    hide Quol with Dissolve(0.3)

    L" Aha- Sorry, yeah, that's all I could gather before they would start asking questions."

    J"(Lars quickly hands me a bag of supplies, filled with canned foods, hygiene items and a few pieces of clothes.)"
    
    L"""I have to return to my shift now, I have more orders to deal with otherwise I'm in deep trouble. 
    
    Take care and be careful."""
    
    J"(Lars returns to the hotel, closing the door behind him.)"

    show Quol at center_lower with Dissolve(0.3)
    stop music fadeout 5.0

    Q"Let's go back now before someone sees us."

    J"""(I nod in response, swiftly zipping the bag shut.)

    (I sling the bag over my shoulder, taking a deep breath of relief.)

    (I scan the dimly lit alleyway, hoping that no one is around to see us. I turned towards Quol, who was ready to leave.)"""

    hide Quol with Dissolve(0.3)
    play music "Fear_And_Terror.mp3"
    
    J"""(As I was about to take my step, something caught my attention. From the corner of my eye, I spot a silhouette of a man holding a few trash bags, frozen in place, his gaze locked onto us.)
   
    (Being caught off guard, I instinctively freeze, feeling my heartbeat undergo a sudden shift.)
    
    (The man drops the trash bags he was carrying and in a panic dashes away.)
    
    (Oh no! Are we gonna get caught?!)"""

    show Quol Angry at center_lower with Dissolve(0.3)
    
    J"""(I turn to Quol and without hesitation, she bolts into action in pursuing him.)

    (I stand there, paralyzed and uncertain, unable to shake off the initial shock as I watch Quol chase after the fleeing figure.)
    
    (With a burst of speed, Quol closes the gap. In a sudden, precise movement, she tackles the figure, pinning him down as he struggles to escape.)
    
    (It all happened so fast, my head couldn't wrap itself around the sudden turn of events.)
    
    (In one swift, powerful movement, Quol hits the man with a heavy bash to his head, knocking him out cold.)
    
    (She turns to me, her expression dead serious.)"""

    Q"""... We can't keep him alive.

    ... We have to get rid of him.

    ...
    
    Julia."""

    J"""(Quol wants me to do it...)

    (My body shakes in anxiety and fear, should I really do it?)

    (... Can I do it?)"""

    menu:
        "Yes":
            pause 0.0000001
        "...":
            pause 0.0000001

    hide Quol

    J"(I clutch my bat tightly, hesitantly walking towards the guy.)"

    Q"""Your life is yours to shape, Julia.

    You have to learn to take control of it."""

    J"""(I look at the man, then my bat...)

    (My breath is short and fast, my hands trembling. The sound of the rain seems to intensify around me.)

    (I take a moment, closing my eyes, holding my bat tightly and taking a deep breath.)

    (...)

    (... This is the moment. The sound of the rain becoming quiet.)

    (I raise my bat over my head...)
    
    (and...)"""
    show bg black with fade
    pause 0.8

    play sound "SFX/JS1FS/falltofloor.mp3" volume 7

    pause 1
    show bg Hotelalley with fade

    J"""(I lift my bat back up... the smell of rusted metal lined my bat...)

    (The sound of the rain returns to its deafening tone.)

    (I did it.)

    (...)"""
    show Quol at center_lower with Dissolve(0.3)
    J"(I turn to Quol. She gives me a smile and a nod of admiration.)"

    Q"You did well, Julia."   

    hide Quol with Dissolve(0.3)
    play music "StageBGM.mp3"
    show bg stage with fade

    J"""(I snapped back, with moments to spare, I swung with all my might, my bat knocked down the agent who injured Quol.)

    (I realised that I had to protect my friends at all cost..)"""

    jump JS13

label JS13:
    J"Fighting off all the agents, it seemed like they got backup."

    menu:
        J"What will I decide on.."
        "I should keep fighting!":
            jump js42fs
        "I should tell everyone to back up to the backstage":
            jump JS3

label JS3:
    J"""We should go to the back!
    
    (We ran towards the back entrance, Quol a little more hesistant than me or Renee but she also came along.)

    (Adrenaline fueled our every step as we sprinted, desperately seeking an escape route from the perilous situation we found ourselves in.)

    (Reaching the backdoor, a glimmer of hope ignited within us. )

    (With a surge of anticipation, we swung the door open, expecting to find a path to freedom. )
    
    (However, our hopes were shattered as we were met with an unexpected sight:) 

    (Six agents, standing in a calculated formation, blocking our way.)"""

    show Renee worried at right_center_lower with Dissolve(0.3)

    R "It's an ambush!"

    show Quol at left_center_lower with Dissolve(0.3)

    Q"Go back!"

    J"""(I was stunned at this scene and before I knew it, an agent has already grabbed my arm.)
    
    (Renee and Quol noticed and tried to pull me away from the agents)
    
    (But it was too late)
    
    (After a moment of stuggle, all three of us were apprehended.)"""
    hide Renee
    hide Quol
    jump badend




#JS2
label JS2:
    show bg greenroom with fade
    play music "GreenBGM.mp3"
    J"""I burst into the green room, slamming the door open and gasping for air. 

    It awakened the only person who was in the room, who was lying comfortably on the sofas, and he was shocked when I rushed in with such an expression, and while creating such a loud noise."""
    hide Julia
    $ haveAndrew = True
    show Andrew at center_lower with Dissolve(0.3)
    A"""Holy mother of–

    Jeez it's just you, Julia.

    Concert done already? How does it feel like debuting?

    You're drenched in sweat already, I get how tense it is!"""

    J"I....I..."
    menu:
        J"Andrew.."
        "I left them behind..":
            jump JS21
        "Can you come to the front stage now?...please?":
            jump JS22   

label JS21:
    J"They are here for us ... the institute.."

    J"(I bury my face deep into my hands.)"

    J"(My thoughts... it's spiraling back and forth between the present and the past.)"
    
    A"They're here...?"

    J"i don't know anything.."

    J"I don't know anything!"

    J"... iam weak. Compared to who I was..."

    A"Julia. What are you talking about? Your past self? Pull yourself together!"

    J"(Andrew gently grabs my shoulders, as my hands slowly fall from my face, revealing my teary eyes.)"

    J"I was really dissatisfied, with my life...I..."

    J"I have to keep running away..."

    J"do I have to keep running away? from my past? F-from...them?"

    A"Everyone feels that way, Julia. It's fine."

    A"while pursuited, there's a point where it feels like there's no end to it. I think that's more reason for you to find more happiness in small things. I'd say you already did a great job."

    J"...I don't get it. What did...I do?"

    A"Julia. Why did you join this band in the first place?"

    J"..."

    A"Any small, atomic efforts are already admirable. Have some self respect for yourself Julia. You might be better than you think you are right now. And you should realize that sooner."

    A"your initiative of agreeing to join the band is already an effort to have great little things in your journey. Alongside people that you can share moments and grow with."

    J"""(...I think I do get it now.)

    (My friends... I should be more thankful to them. Leaving them behind just like that was a mistake. I frown and look down to the floor, feeling heavy guilt deep within my chest, I can hardly speak up.)"""
    jump JS23

label JS22:
    A"Huh..?"

    A"What happened? is there a problem? or someone wants my autograph? Ehhe.."

    A"..."

    J"(I bury my face deep into my hands.)"

    J"(My thoughts... it's spiraling back and forth between the present and the past.)"

    A"...So... somethin' wrong then."

    J"i dont know anything.."

    J"I don't know anything!"

    A"H-hey! Julia! Calm down..."

    J"the institute..."

    A"I know... Julia. Everyone feels the same way too."

    J"h-how long... how long do we have to keep running away..? From the past ... from them..."

    J"i wish I could be stronger as who I was...but at the same time I... dont like it... the past... i... I don't ..."

    J"(My breath gets heavier.)"

    J"(Andrew gently grabs my shoulders, as my hands slowly fall from my face, revealing my teary eyes.)"

    J"I am scared...scared of whatever happened back then, whatever I did back then, whatever that haunts us! I don't know what to do! Who I was?! Who were we?! I–"

    A"Julia."

    J"(Andrew shook my shoulders lightly as he stares at me, genuine concern is visible on his face, but encouragement is vivid in his eyes.)"

    A"Does that matter now?! All we need to do is to just... face whatever the present gives us on the way, hangin' too much back there will get you nowhere and keep being there!"

    J"B...But–"

    A"Snap out of it, okay? Whatever happened, whatever it was, I don't want to hear if's and but's! What's happening is now! And that's what matters!"

    J"...Andrew... but..."

    J"...would you...even understand?...i..."

    A"Trust me. I have my own history too. Everyone does."

    A"And the only thing that matters now is what you want to do now, and what you choose to be."

    J"..."

    J"(...I think I get what he's saying.)"

    jump JS23

label JS23:
    J"I got my spirits up after talking with Andrew."

    

    menu:
        "what should we do?"
        "Return to our friends":
            hide Andrew
            show bg stage
            jump js42fs
        "Exit through the backdoor":
            jump JS25    

label JS25:
    J"""(We decided to run towards the backdoor, our hearts pounding with a mix of fear and resolve. )

    (Adrenaline fueled our every step as we sprinted, desperately seeking an escape route from the perilous situation we found ourselves in.)

    (Reaching the backdoor, a glimmer of hope ignited within us. )

    (With a surge of anticipation, we swung the door open, expecting to find a path to freedom. )
    
    (However, our hopes were shattered as we were met with an unexpected sight:) 

    (Six agents, standing in a calculated formation, blocking our way.)
    
    AH-
    
    (Andrew immedately grabbed my arm and attempted to run the opposite direction, but their hands were already grabbing my arm tight.)
    
    (After a moment of stuggle, both of us were apprehended.)"""
    hide Andrew with Dissolve(0.3)
    jump badend


label JH2:
    hide Julia
    J"Without hesitation, I stepped inside and locked the door behind her. The silence enveloped me, and tears welled up in her eyes. She collapsed onto the cold, tiled floor, her sobs echoing in the confined space."
    show Julia at center_lower
    J"She is here to get me...She is here to get me...She is here to get me...She is here to get me...She is here to get me...She is here to get me...She is here to get me...She is here to get me..."
    show bg Julia_toilet
    "I..."




label js42fs:
    show screen display_hp
    J"(Four agents approched us)"
    if haveAndrew == True:
        jump js42fsa
    else:
        jump js42fsb

label js42fsa:
    J"""(Without hesitation, Renee sprang into action, her movements swift and precise as she lunged towards one of the agents.)
    
    (In a blur of motion, Quol followed suit, her agility and strength on full display as she engaged another agent.)

    (Layon looked at the two, shrugged, and pulled up his sleeves as he dashes towards the third agent)

    (My heart raced as I realized that there is one agent left, their attention now squarely focused on me.

    How should I approach this?"""
    menu:
        J"How should I approach this?"
        "Go for the kill":
            jump js42fsi
        "Play it defensively":
            jump js42fsj

label js42fsb:
    show Julia exhausted at textbox_over with Dissolve(0.3)

    J"""(Without hesitation, Renee sprang into action, her movements swift and precise as she lunged towards one of the agents.)
    
    (In a blur of motion, Quol followed suit, her agility and strength on full display as she engaged another agent.)
    
    (My heart raced as I realized that two agents still remained, their attention now squarely focused on me. )
    
    (Fear mingled with determination within me as I braced myself for the impending confrontation.)
    
    (One of the agents, slightly taller than the others, took a strong stance.)

    (He confidently threw his baton on the floor and came charging at me in full speed.)
    
    (Who should I focus on first?)"""
    
    menu:
        J"(Who should I focus on first?)"
        "Agent with a baton":
            jump js42fsc
        "Agent without a baton":
            jump js42fsd

label js42fsc:
    show Julia nervious at textbox_over
    J"(As the agent with the baton closed in, I mustered all my strength and swung my weapon towards them.)"
    
    show screen timerDown(3, "misseditJS42FSc1")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Swing left", "choice1JS42FSc1", 0.2, 0.5),  # xpos and ypos for choice 1
        ("Swing right", "choice2JS42FSc1", 0.8, 0.5)   # xpos and ypos for choice 2
    ])
    return
    
    label misseditJS42FSc1:
        $ hp -= 1
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        show Julia traumatized at textbox_over
        J"(I got hit in the arm because I was not quick enough to react.)"
        jump finishedJS42FSc1
    
    label choice1JS42FSc1:
        J"(I swung left, and it blocked the baton.)"
        jump finishedJS42FSc1
    
    label choice2JS42FSc1:
        J"(I swung right, and it blocked the baton.)"
        jump finishedJS42FSc1
    
    label finishedJS42FSc1:
        J"(The agent is temportarily off guard.)"
        
    show screen timerDown(3, "misseditJS42FSc2")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Strike downwards", "choice1JS42FSc2", 0.5, 0.3),  # xpos and ypos for choice 1
    ])
    return
    
    label misseditJS42FSc2:
        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        J"(I got hit on the waist, then came to my senses and attacked his head out of reflexes.)"
        
        J"(They immedately fell on the ground motionless)"
        show Julia exhausted at textbox_over
        jump finishedJS42FSc2
    
    
    label choice1JS42FSc2:
        show Julia exhausted at textbox_over
        J"(I striked down on the Agent and they immediately fell on the ground motionless.)"
        jump finishedJS42FSc2
    
    label finishedJS42FSc2:
        J"""(He is down.)
        
        (My relief was short lived, as the other agent then tried to jump on me.)
        
        (What should I do?)"""
       
    menu:
        J"(What should I do?)"
        "Go for the kill":
            jump js42fsl
        "Play it defensively":
            jump js42fsm

label js42fsd:
    J"""(The agent without the baton approached rapidly, I see that he is trying to directly jump on me.()
    
    (I held tight my bat, and decided on my next move)"""
    
    menu:
        "Go for the kill":
            jump js42fsg
        "Play it defensively":
            jump js42fsh

label js42fsg:
    J"""(I decided to go for the kill)
    
    (I prepared my swing and gluped)
    
    (However, I lost my train of thought and when I came to my senses was when my back hits the ground.)
    
    (The agent has swiftly took my bat away from my hands and threw it away, while pinning me to the ground.)"""
    
    jump game_over

label js42fsh:
    J"(I decided to get defensive and held my bat tight.)"
    
    show screen timerDown(3, "misseditJS42FSc5")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Block Horizontally", "choice1JS42FSc5", 0.2, 0.5),  # xpos and ypos for choice 1
        ("Block Vertically", "choice2JS42FSc5", 0.8, 0.5)   # xpos and ypos for choice 2
    ])
    return
    
    label misseditJS42FSc5:
        $ hp -= 1
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        J"(I stumbled backwards mildly.)"
        jump finishedJS42FSc5

    label choice1JS42FSc5:
        J"(I held my bat horizontally, and it blocked the baton.)"
        jump finishedJS42FSc5

    label choice2JS42FSc5:
        J"(I held my bat vertically, and it blocked the baton.)"
        jump finishedJS42FSc5

    label finishedJS42FSc5:
        J"""(I then swing towards his torso, making sure he fainted off.)

    (The other sees that I've knocked down his comrade, and approches me.)

    (As the agent with the baton closed in, I mustered all my strength and swung my weapon towards them.)"""

    show screen timerDown(3, "misseditJS42FSc3")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Swing left", "choice1JS42FSc3", 0.2, 0.5),  # xpos and ypos for choice 1
        ("Swing right", "choice2JS42FSc3", 0.8, 0.5)   # xpos and ypos for choice 2
    ])
    return

    label misseditJS42FSc3:
        $ hp -= 1
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        J"(I got hit in the arm because I was not quick enough to react.)"
        jump finishedJS42FSc3

    label choice1JS42FSc3:
        J"(I swung left, and it blocked the baton.)"
        jump finishedJS42FSc3

    label choice2JS42FSc3:
        J"(I swung right, and it blocked the baton.)"
        jump finishedJS42FSc3

    label finishedJS42FSc3:
        J"(The agent is temportarily off guard.)"
        
    show screen timerDown(3, "misseditJS42FSc4")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Strike downwards", "choice1JS42FSc4", 0.5, 0.3),  # xpos and ypos for choice 1
    ])
    return

    label misseditJS42FSc4:
        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        J"(I got hit on the waist, then came to my senses and attacked his head out of reflexes.)"
        
        J"(They immedately fell on the ground motionless)"
        jump finishedJS42FSc4


    label choice1JS42FSc4:
        J"(I striked down on the Agent and they immedately fell on the ground motionless.)"
        jump finishedJS42FSc4

    label finishedJS42FSc4:
        jump js42fsafter

    label js42fsi:
        J"""(I decided to go for the kill.)
        
        (I prepared my swing and gluped.)
        
        (However, I lost my train of thought and when I came to my senses was when my back hits the ground.)
        
        (The agent has swiftly took my bat away from my hands and threw it away, while pinning me to the ground.)"""
        
        jump game_over

label js42fsj:
    J"(I decided to get defensive and held my bat tight.)"
    
    show screen timerDown(3, "misseditJS42FSc6")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Block Horizontally", "choice1JS42FSc6", 0.2, 0.5),  # xpos and ypos for choice 1
        ("Block Vertically", "choice2JS42FSc6", 0.8, 0.5)   # xpos and ypos for choice 2
    ])
    return
    
    label misseditJS42FSc6:
        $ hp -= 1
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        J"(I stumbled backwards mildly.)"
        jump finishedJS42FSc6
    
    label choice1JS42FSc6:
        J"(I held my bat horizontally, and it blocked the baton.)"
        jump finishedJS42FSc6
    
    label choice2JS42FSc6:
        J"(I held my bat vertically, and it blocked the baton.)"
        jump finishedJS42FSc6
    
    label finishedJS42FSc6:
        J"""(I then swing towards his torso, making sure he fainted off.)

        Another agent who was combating Andrew decided to run towards me to attempt to strike me
        
        But Andrew swipes his leg under him in time to trip him down.
        
        He then ends it by stomping on his face and then walking over him."""
        show Andrew at center_lower with Dissolve(0.3)
        A"You seem fine now right, Julia?"

        J"He giggles"
        hide Andrew with Dissolve(0.3)

        jump js42fsafter

label js42fsl:
    J"""(I decided to go for the kill.)
    
    (I prepared my swing and gluped.)
    
    (However, I lost my train of thought and when I came to my senses was when my back hits the ground.)
    
    (The agent has swiftly took my bat away from my hands and threw it away, while pinning me to the ground.)"""
    
    jump game_over

label js42fsm:
    $ hp -= 1
    if hp <= 0:
        # If hp is 0, jump to the game_over label
        jump game_over
    J"""(I held my bat horizontally to block the agent as he jumps on me.)
    
    (He hits my shoulder mildly, but I manage to swing him off and throw him on the ground.)
    
    (I then swing towards his torso, making sure he fainted off.)"""
    
    jump js42fsafter

label js42fsafter:
    hide screen display_hp
    J"(All the agents have passed out, and we all had a sigh of relief.)"
    jump cliff



label jhfs5:
    show Julia traumatized at textbox_over
    show screen display_hp
    J"""(As I reach the front stage, a sinking feeling settles in the pit of my stomach.) 
    
    (I glance behind me and discover that two agents have been tailing me, closing in on the stage. )
    
    (Panic courses through my veins.)
    
    (I cannot go back now)
    
    (Quol and Renee looked towards me and recongizes the issue)"""
    hide Julia
    show Quol Angry at left_center_lower with Dissolve(0.3)
    Q "We can take down all of them! They can't just keep coming at us forever!"
    
    show Renee worried at right_center_lower with Dissolve(0.3)

    R "No..no! we have to back up! Lets not get oursleves too hurt!"
    
    J"""(Caught between these conflicting viewpoints, my mind races.)"""

    hide Quol with Dissolve(0.3)
    hide Renee with Dissolve(0.3)

    show Julia nervious at textbox_over
    J"(What should I do?)"
    
    menu:
        J"(What should I do?)"
        "Fight them":
            jump jhfs5a
        "Make an escape for it":
            jump jhfs5b

label jhfs5a:
    J"(I decided that we have to fight them)"

    show Renee bag at Transform(xalign=0.5, yalign=0.4) with Dissolve(0.3)
    
    J"""(In the midst of the chaos, I catch sight of my weapon—a bat sticking out of Renee's bag, carefully placed behind the drum set.)

    (Without hesitation, I dash towards the bag, swiftly grabbing it.)"""
    
    hide Renee bag

    J"(I notice that the two agents behind are preparing to strike)"
    
    show screen timerDown(3, "misseditJHFS5a1")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Go offensive", "choice1JHFS5a1", 0.2, 0.3),  # xpos and ypos for choice 1
        ("Go defensive", "choice2JHFS5a1", 0.8, 0.7)   # xpos and ypos for choice 2
    ])
    return
    
    label misseditJHFS5a1:
        J"""(I faltered and couldn't decide)
        
        (One of the agents swing towards me and I got hit)"""
        $ hp -= 4
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        jump finishedJHFS5a1
    
    label choice1JHFS5a1:
        J"""(With a surge of adrenaline, I decide to go on the offensive.) 
        
        (I swiftly pivot on my heel, channeling my momentum into a powerful swing of the bat.) 
        
        (The first agent lunges forward, and I time my strike perfectly, hitting his arm.) 
        
        (The crack of impact fills the air as the agent staggers backward, momentarily stunned.)
        
        (But he quickly regains his composure.)"""
        jump finishedJHFS5a1
    
    label choice2JHFS5a1:
        J"""(Feeling a pang of caution, I opt for a defensive strategy.) 
        
        (As the first agent lunges, I quickly sidestep their attack, narrowly evading their grasp.) 
        
        (With a calculated move, I position myself for a swift counter.) 
        
        (The second agent moves in, but I remain focused on evasion, waiting for the opportune moment to strike.)"""
        
        jump finishedJHFS5a1
    
    label finishedJHFS5a1:
        J"(I quickly access the situation and do my next move.)"
        
        show screen timerDown(3, "misseditJHFS5a2")  # seconds, label to jump on fail
        call screen qte_choice([
            ("Strike", "choice1JHFS5a2", 0.2, 0.3),  # xpos and ypos for choice 1
            ("Retreat", "choice2JHFS5a2", 0.8, 0.7)   # xpos and ypos for choice 2
        ])
        return
    
    label misseditJHFS5a2:
        J"""(I faltered and couldn't decide)
        
        (One of the agents swing towards me and I got hit)"""
        $ hp -= 4
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        jump finishedJHFS5a2
    
    label choice1JHFS5a2:
        J"""(Seizing the opportunity, I decide to press the advantage.) 
        
        (With a surge of confidence, I prepare to deliver a powerful strike to the agent.)
        
        (Unfortunately I missed my swing and the agents are unharmed.)
        
        (I leaped backwards and tried to give myself some space.)"""
        jump finishedJHFS5a2
    
    label choice2JHFS5a2:
        J"""(I choose to prioritize my safety.)
        
        (Recognizing that the second agent is closing in, I decide to disengage temporarily and create some distance.)
        
        (I leaped backwards and tried to regroup with my team.)"""
        jump finishedJHFS5a2
    
    label finishedJHFS5a2:
        J"""(I scanned around the stage to see that my comrades are all each fighting aganist an agent, whilst I am fending off two)
        
        (What should I do?)"""
    
    menu:
        "Keep fighting them":
            jump jhfs5d
        "Call for help":
            jump jhfs5e


label jhfs5b:
    J"""lets make the run to it!
    
    I started to dash towards the entrance. 
    
    Renee and Quol notices and follows suit
    
    The agents reacted to our escape attempt and tries to intercept us."""
    show screen timerDown(3, "misseditjhfs5b1")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Dodge left", "choice1jhfs5b1", 0.2, 0.5),  # xpos and ypos for choice 1
    ])
    return

    label misseditjhfs5b1:
        $ hp -= 2
        "I bumped into an agent mildly and kept running"
        jump finishedjhfs5b1

    label choice1jhfs5b1:
        "I swiftly dodged one of the agents"
        jump finishedjhfs5b1

    label finishedjhfs5b1:
        "Another agent comes from the right, tring to swing down at me"
        show screen timerDown(3, "misseditjhfs5b2")  # seconds, label to jump on fail
        call screen qte_choice([
        ("Block", "choice1jhfs5b2", 0.8, 0.5),  # xpos and ypos for choice 1
        ])
        return

    label misseditjhfs5b2:
        "I got hit heavily."
        $ hp -= 5
        "I sluggishly try to keep going."
        jump finishedjhfs5b2

    label choice1jhfs5b2:
        "I block the attack and continuse running."
        jump finishedjhfs5b2

    label finishedjhfs5b2:
        "When i looked back forward, I see an agent right in front of my path, I dash towards him and.."
        show screen timerDown(3, "misseditjhfs5b3")  # seconds, label to jump on fail
        call screen qte_choice([
        ("Hit him", "choice1jhfs5b3", 0.5, 0.3),  # xpos and ypos for choice 1
        ])
        return

    label misseditjhfs5b3:
        "I smash right into the Agent as I mess up my swing."
        $hp -= 5
        jump finishedjhfs5b3

    label choice1jhfs5b3:
        "I swing right on his head, bringing him down with a powerful blow."
        jump finishedjhfs5b3

    label finishedjhfs5b3:
        "We were halfway to our distination"
        jump cliff

label jhfs5d:
    J"""I am strong, I can fend them all!
    
    (As the two agents rapidly approach, I tighten my grip on the bat, ready to face them head-on.)
    
    (I have to choose who I should target first.)"""
    
    menu:
        "The one on the right":
            jump jhfs5i
        "The one on the left":
            jump jhfs5j

label jhfs5e:
    J"""(I decided that i should call my teammates for help)
    
    (who should I call?)"""
    menu:
        "Quol":
            jump jhfs5l
        "Renee":
            jump jhfs5m

label jhfs5i:
    J"""(I choose to strike the agent on the right, aiming to catch them off guard.)
    
    (but to my surprise, they skillfully block my attack.)"""
    
    show screen timerDown(3, "misseditJHFS5i1")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Block", "choice1JHFS5i1", 0.2, 0.3),  # xpos and ypos for choice 1
    ])
    return
    
    label misseditJHFS5i1:
        "(I get striked by the agent)"
        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        jump finishedJHFS5i1
    
    label choice1JHFS5i1:
        "(I block the agent.)"
        jump finishedJHFS5i1
    
    
    label finishedJHFS5i1:
        show screen timerDown(3, "misseditJHFS5i2")  # seconds, label to jump on fail
        call screen qte_choice([
            ("Parry", "choice1JHFS5i2", 0.2, 0.3),  # xpos and ypos for choice 1
        ])
        return
    
    label misseditJHFS5i2:
        "(I get striked by the Agent)"
        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        jump finishedJHFS5i2
    
    label choice1JHFS5i2:
        "(I parry the agent's strike.)"
        jump finishedJHFS5i2
    
    
    label finishedJHFS5i2:
        show screen timerDown(3, "misseditJHFS5i3")  # seconds, label to jump on fail
        call screen qte_choice([
            ("Dodge", "choice1JHFS5i3", 0.2, 0.3),  # xpos and ypos for choice 1
        ])
        return
    
    label misseditJHFS5i3:
        "(I get striked by the agent)"
        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        jump finishedJHFS5i3
    
    label choice1JHFS5i3:
        "(I dodge the agent's strike.)"
        jump finishedJHFS5i3
    
    
    label finishedJHFS5i3:
        """(Amidst the flurry of blows, I spot a brief opening—a split second where the agent's guard wavers.)
        
        S(eizing the opportunity, I deliver a powerful swing, channeling all my strength into the strike. )
        
        T(he bat connects with a resounding impact, sending the agent sprawling to the ground.)
        
        (As I try to turn my attention to the Second Agent, I found out Quol has already taken care of him)"""
    jump jhfs5k

label jhfs5j:
    """(I choose to strike the agent on the left, aiming to catch them off guard.)
    
    (The bat strikes the Agent, and he seems to be stunned)
    
    (He swings at me sluggishly, trying to hit me down)"""
    
    show screen timerDown(3, "misseditJHFS5j1")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Block", "choice1JHFS5j1", 0.2, 0.3),  # xpos and ypos for choice 1
    ])
    return
    
    label misseditJHFS5j1:
        "(I get striked by the agent)"
        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        jump finishedJHFS5j1
    
    label choice1JHFS5j1:
        "(I block the agent.)"
        jump finishedJHFS5j1
    
    
    label finishedJHFS5j1:
        show screen timerDown(3, "misseditJHFS5j2")  # seconds, label to jump on fail
        call screen qte_choice([
            ("Swing", "choice1JHFS5j2", 0.2, 0.3),  # xpos and ypos for choice 1
        ])
        return
    
    label misseditJHFS5j2:
        J"(I miss the swing.)"
        jump finishedJHFS5j2
    
    label choice1JHFS5j2:
        J"(I striked the Agent and he falls down on the floor.)"
        jump finishedJHFS5j3
    
    
    label finishedJHFS5j2:
        show screen timerDown(3, "misseditJHFS5j3")  # seconds, label to jump on fail
        call screen qte_choice([
            ("Swing again", "choice1JHFS5j3", 0.2, 0.3),  # xpos and ypos for choice 1
        ])
        return
    
    label misseditJHFS5j3:
        J"(I get striked by the agent)"

        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
         
        """(From a distance, a thin string appears in front of my eyes, violently hitting the agent down)
         
        (Renee assisted me in taking him down)"""
        jump finishedJHFS5j3
    
    label choice1JHFS5j3:
        J"(I striked the Agent and he falls down on the floor.)"
        jump finishedJHFS5j3
    
    
    label finishedJHFS5j3:
        J"(I try to turn my attention to the Second Agent, I found out Renee has already taken care of him)"
    
    jump jhfs5k

label jhfs5k:
    show Julia exhausted at textbox_over
    hide screen display_hp
    J"We have managed to knock out all the agents in the venue"
    jump cliff

label jhfs5l:
    J"""(I call out for Quol)
    
    Quol! Please help me here..!
    
    (Quol, ever vigilant and quick to respond, turns their attention toward me.)"""

    hide Julia with Dissolve(0.3)
    Q"Coming!"
    
    show Quol Angry at center_lower with Dissolve(0.3)
    J"""(Their eyes meet mine, and without hesitation, they rush to my aid.) 
     
    (With a swift and powerful roundhouse kick, Quol unleashes an force upon the agent, targeting their head with precision.) 
    
    (The impact reverberates through the air as the agent's body crumples under the sheer force of the blow.)"""
    
    Q"Finish off the last one, Julia. I have my own agent to beat up."
    
    hide Quol with Dissolve(0.3)

    jump jhfs5o

label jhfs5o:
    J"(Taking the hint, I raised my bat high.)"
    
    show screen timerDown(3, "misseditJHFS5o")  # seconds, label to jump on fail
    call screen qte_choice([
        ("SLAM", "choice1JHFS5o", 0.5, 0.5),  # xpos and ypos for choice 1
    ])
    return
    
    label misseditJHFS5o:
        show Julia traumatized at textbox_over
        J"""I hesitated and missed my shot.

        The agent hits my shoulder"""

        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over

        J"""Renee notices and swings her whip towards the agent's legs, while Quol does the final blow
        
        Their eyes gleam with a mix of understanding and dissappointment."""
        jump finishedJHFS5o
    
    label choice1JHFS5o:
        J"I striked down at the last agent, delivering a fatal blow."
        jump finishedJHFS5o
    
    label finishedJHFS5o:
    jump jhfs5k

label jhfs5m:
    J"""(I call out for Renee)
    
    Renee! Please help me here..!
    
    (Without hesitation, Renee responds to my plea, her eyes locking onto the remaining agent.) """
    hide Julia with Dissolve(0.3)
    R "Alright! Stay back!"
    show Renee at center_lower with Dissolve(0.3)
    J"""(She swiftly maneuvers her whip, seamlessly striking with precision.)
    
    (With a deft flick of her wrist, the whip cracks through the air, its tip finding its mark.) 
     
    (In a dazzling display of skill, Renee incapacitates the agent, rendering them unable to continue their assault.) 
    
    (The agent's movements falter, and they crumble to the ground, immobilized by the force of the whip.)"""
    
    R "I'll help you more later, I'm taking on another agent as well! Try manage the last one yourself!"

    hide Renee with Dissolve(0.3)
    
    jump jhfs5o

label cliff:
    J"""We all stared at our target- the entrance of the concert
    
    As quick as our legs can take us, we sprinted towards it."""

    hide Julia

    show Lenorra at center_lower with Dissolve(0.3)

    LQ"Not so fast, traitors."

    J"We immediately halted and braced oursleves for combat."

    "..."
    hide Lenorra with Dissolve(0.3)
    show bg black with fade
    "..."

    Z"""I haven't finished writing the best part yet!
    
    You guys are here too early!
    
    oh well credits roll."""
    window hide
    call screen credits
    return



label game_over:
    hide Julia
    hide Quol
    hide Renee
    hide Lenorra
    hide Andrew
    hide Agent1
    show bg black with fade
    show text "{size=100}{color=#ff0000}BAD END{/color}{/size}\n{size=30}{color=#ffffff}you died{/color}{/size}" at truecenter with dissolve
    pause 5.0
    hide text with dissolve
    Z"""Huh, you're down
    
    that wasn't fun.

    Not a great way to end a story, is it?

    let's try this again."""
    $ hp == 15
    return


label badend:
    show bg black with fade
    show text "{size=100}{color=#ff0000}BAD END{/color}{/size}\n{size=30}{color=#ffffff}you were caught{/color}{/size}" at truecenter with dissolve
    pause 5.0
    hide text with dissolve

    Z"""Ah, what a tragedy.
    
    However.. it's quite a brillant show.

    What a shame it ends this way.
    
    Let's restart this play, shall we?"""

    return
