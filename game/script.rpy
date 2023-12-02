# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#setting
default hp = 15

# defining characters
define J = Character("Julia",color="#F400FF")
define R = Character("Renee", color= "#FF8700")
define Q = Character("Quol", color="#0094FF")
define L = Character("Layon", color= "#ff0000")
define LQ = Character("Lenorra", color="#00ff11")
define G1 = Character("Agent1",color="#cacaca")
define G2 = Character("Agent2",color="#cacaca")
define A1 = Character("Audience1",color="#cacaca")
define A2 = Character("Audience2",color="#cacaca")

# define character sprites
image Renee :   
    "characters/Renee.png"
    zoom 1.5
image Julia :   
    "characters/Julia.png"
    zoom 1.5
image Quol :   
    "characters/Quol.png"
    zoom 1.7
image Quol Angry:   
    "characters/Quol Angry.png"
    zoom 1.7

# defining bgs
image bg entrance = im.Scale("backgrounds/bg_entrance.png", config.screen_width, config.screen_height)
image bg entrance_ticket = im.Scale("backgrounds/bg_entrance_ticket.png", config.screen_width, config.screen_height)
image bg stage = im.Scale("backgrounds/stage.png", config.screen_width, config.screen_height)
image bg greenroom = im.Scale("backgrounds/greenroom.png", config.screen_width, config.screen_height)
image bg toilet = im.Scale("backgrounds/toilet1.png", config.screen_width, config.screen_height)

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



# The game starts here.

label start:
    show bg entrance
    pause 4.0
    scene bg entrance_ticket
    with Dissolve(2.0)
    # Show your screen
    scene bg entrance_ticket_dark
    call screen character_selection
    with Fade(1.0,0.0,1.0)
    return

label Sorry:
    "sorry this character isn't available for now, Julia is available though."
    jump Julia_Start
    return

label Julia_Start:
    window hide 
    pause 0.5 
    $ renpy.movie_cutscene("images/opening.webm")
    show bg stage
    pause 1.0 
    window show
    show Julia at center_lower

    J"""(In the crowded and noisy venue, I find myself squished within the audience, my fingers absentmindedly gripping the neck of my guitar.)

    (The vibrant lights and pulsating music create a whirlwind of sensory overload around me, but my senses are suddenly numbed as my gaze lands on a familiar figure.)

    (Standing at the back of the venue are two enigmatic individuals, dressed in sleek white suits, their presence sending a jolt of disbelief through my core.)"""

    hide Julia
    
    play music "StageBGM.mp3"
    show Agent1 at left_center_lower with Dissolve(0.5)
    show Agent2 at right_center_lower with Dissolve(0.5)
    show Lenorra at center_lower with Dissolve(0.5)
   
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

    menu:
        J"(What should I do?)"
        "Warn my bandmates about them":
            jump J1
        "Ignore them and hope it doesn't worsen the situation":
            jump J2

    return

label J1:
    J"""I should tell them about this.
    
    Who should I warn first though..."""
    menu:
        J"Who should I warn first though..."
        "Quol":
            jump JQ0
        "Renee":
            jump JR0


#J2-Julia self routes
label J2:
    J"""(I ignore the agents, not wanting to deal with any confrontations.)

    I should just ignore them

    (I mutter to myself, trying to convince myself that everything will be fine if I simply pretend they're not there.)"""


    show Agent at center_lower with Dissolve(0.3)
    pause 0.5
    hide Agent with Dissolve(0.3)

    J"""(But as one of the agents takes a step closer, my heart leaps into my throat, and my previous confidence wavers.)

    They... they are coming closer

    (I stammer, my voice barely above a whisper.)

    (Panic starts to grip me, and my mind races, desperately searching for a solution.)

    I should do something... right?"""


    menu:
        J"what do I do.."
        "Stand my ground, don't move a muscle..":
            jump JS0
        "I have to leave, I have to go!":
            jump JH0

label JS0:
    # agent tries dragging her
    J"(As I stand there, frozen in fear, the agent's sudden lunge towards me catches me off guard.)"

    show Agent1 at Transform(xalign=0.5, yalign=0.1, zoom=1.5)
    
    J"""(Panic courses through my veins as their grip tightens around my leg, threatening to drag me off the stage.)

    (In that moment, a scream erupts from deep within me, piercing the air and reverberating throughout the venue, carrying a raw mixture of terror and desperation.)

    {b}Aaaah!{/b}

    (My instinct kicks in, overriding my initial shock.)

    (With every ounce of strength I can muster, I fight against the agent's grip, desperately wriggling and twisting in an attempt to break free.

    "I have to back up! I have to back up!"

    (Uttering those words repeatedly, a blend of panic and a hint of newfound determination, I summon a surge of adrenaline.)
    (It fuels my movements as I manage to loosen the agent's hold.)

    (Stumbling backwards, I narrowly escape being pulled off the stage, my heart pounding in my chest.)"""

    hide Agent1 with Dissolve(0.3)

    J"""(The sudden commotion disrupts the once-lively concert, casting a hushed silence over the audience.)

    (Whispers and murmurs ripple through the air as people grapple to make sense of the chaotic scene unfolding before them.)"""

    A1"It's NewFutures, why are they here?"
 
    A2"Even a small event like this caught the attention of NewFutures... I wonder why they are here?"

    J"""(Amidst the confusion, I strain to catch snippets of their conversations, hoping to glean some understanding from the fragments of information swirling around.)

    (However, before I can piece together the puzzle, the agents, realizing that their presence has been exposed, yells out to the audience.)"""

    G1"{b}EVERYONE, LEAVE THE VENUE NOW!!!{/b}"

    J"""(The audience obeys their command, and rushes towards the exit.)

    What... what just happened? 

    (Sweat trickles down my forehead, my hands trembling uncontrollably.)"""

    show Quol Angry at left_center_lower with Dissolve(0.3)
    show Renee at right_center_lower with Dissolve(0.3)

    J"(Quol and Renee, my bandmates, also speak up after witnessing the situation.)"

    R "I...It's them, I did everything they wanted, why are they here?"

    J"(her voice trembling mildly, her hands shaking, while grasping her whip tight.)"

    Q"God its them again, goddammit!!"
    
    J"(Quol out of frustration, throws her bass towards the agents as it breaks into pieces upon contact with the floor, causing an echoing loud noise)"

    Q"Fucking GOD!!"
    
    Q"Don't you all DARE lay a finger on any of us!"

    J"""(her voice laced with anger and infuriation roars, as she pulls up her sleeves.)

    (I find myself at the back of the stage, overwhelmed and at a loss for words.)

    (My eyes dart between the chaotic scene unfolding before me and the unwavering support of my bandmates.)

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
    show bg toilet 
    show Julia at center_lower
    J"""huff...huff...

    I'm safe...aren't I?

    What can I do now...what do I do??"""

    menu:
        "Go find layon":
            hide Julia
            jump JS2
        "Rush and help your friends":
            hide Julia
            jump Jh5
        "Don't go outside":
            hide Julia
            jump JH2



label JS1:
    J"""(As the chaos ensues and my initial shock begins to fade, a surge of determination courses through my veins.)

    (The sight of my bandmates valiantly defending me from the agents' onslaught ignites a fire within me.)"""

    menu:
        J"Calm down...calm down..."
        "I need to help my friends":
            jump JS1FS
        "I have to do something!":
            jump JS1FS
        "I can't just stand and do nothing!":
            jump JS1FS        

label JS1FS:
    J"""(I can't stand idly by while they put themselves in harm's way. I need to help them.)

    (With a deep breath, I snap out of my daze, focusing my attention on the unfolding fight.) 

    (My eyes quickly scan the area, searching for anything that could aid me in this sudden battle for survival.)"""
    
    hide Renee
    hide Quol
    show Renee bag at center
    J"""(And then I spot it ... my trusty bat, safely tucked inside Renee's bag.)

    (But before I can fully process my next move, my attention is abruptly diverted.)"""

    hide Renee bag
    J"(An agent charges towards me, wielding a baton and swinging it with force.)"
    show Agent at center_lower
    menu:
        J"gasp!"
        "Try to dodge the attack":
            hide Agent
            jump JS1FSa
        "Scream":
            $ hp - 3
            jump JS1FSb
        "Reach for my bat":
            $ hp - 1
            jump JS1FSc

# fight scene JS1
label JS1FSa:
    J"I have to dodge this!"
    pause 2.0
    show Agent with moveinright
    pause 1.0
    hide Agent with moveoutleft
    J"I dodged him!"
    jump JS1FSd

label JS1FSb:
    J"{b}'AAAAAH'{/b}"
    Q"Whats happening?"
    J"'help!'"
    hide Agent
    pause 1.0
    show Agent at Transform(xalign=0.5, yalign=0.1, zoom=1.5)
    J"'OUCH!!!'"
    hide Agent with moveoutbottom
    jump JS1FSd

label JS1FSc:
    J"I'm getting the bat!"
    pause 1.0
    J"'got it! OW!"
    menu: 
        "Block":
            jump JS1FSe
        "Hit":
            jump JS1FSf    

label JS1FSd:
    show Agent with moveinbottom
    J"he's trying to attack again!"
    menu:
        "Scream":
            jump JS1FSg
        "Dodge":
            jump JS1FSh
        "Get bat":
            jump JS1FSi

label JS1FSe:
    hide Agent
    show Agent at left_center_lower
    show Julia at right_center_lower
    J"I should block him.."
    pause 2.0
    J" and then.."
    menu:
        "and then.."
        "Hit him back!":
            jump JS1FSf

label JS1FSf:
    J"'Uuuugahhhh!'"
    pause 2.0
    J"he's out...cold"
    J"did I hit him a little too hard..?"
    jump JS1FSafter

label JS1FSg:
    J"{b}'AAAAAH'{/b}"
    hide Agent
    show Quol with Dissolve(0.1)
    Q"'You alright Julia?'" 
    J"'Thank...Thank you..'"
    Q"'better fight back yourself next time.'"
    J"'Thanks..Oh, my bat!' "
    Q"'keep it in your hands at all times.'"
    hide Quol
    jump JS1FSafter

label JS1FSh:
    J"I'll dodge, it'll be fin-"
    J"'ah!'"
    J"I tripped over myself..."
    J"'ouch!'"
    $ hp - 2
    hide Agent
    show Quol with Dissolve(0.1)
    Q"'You alright Julia?'" 
    J"'Thank...Thank you..'"
    Q"'better not trip next time.'"
    J"'Thanks..Oh, my bat!'"
    Q"'keep it in your hands at all times.'"
    hide Quol
    jump JS1FSafter

label JS1FSi:
    J"I have to get my bat this time"
    pause 1.0
    J"yes! and I'll defend.."
    pause 1.0
    J"I blocked him!"
    J"It should be fine if I hit back.."
    pause 2.0
    J"he's down"
    jump JS1FSafter

label JS1FSafter:
    J"he's down at least."
    show Renee at right_center_lower
    R "There are quite a lot of them."

    R "Trying to hold them back."
    show Quol at left_center_lower
    Q "Same."

    J"I want to help.."
    menu:
        J"I want to help.."
        "Help Quol first":
            jump JS11
        "Help Renee first":
            jump JS12    

#JS2
label JS2:
    show bg greenroom with wipeleft
    J"Huff.."
    show Layon with fade
    L"Hey what happened? Are you alright?"
    J"I....I..."
    menu:
        J"Layon.."
        "I left them behind..":
            jump JS21
        "Can you come to the front stage now?...please?":
            jump JS22   

label JH2:
    hide Julia
    "Without hesitation, Julia stepped inside and locked the door behind her. The silence enveloped her, and tears welled up in her eyes. She collapsed onto the cold, tiled floor, her sobs echoing in the confined space."
    show Julia at center_lower
    J"She is here to get me...She is here to get me...She is here to get me...She is here to get me...She is here to get me...She is here to get me...She is here to get me...She is here to get me..."
    show bg Julia_toilet
    "I..."


label js5fs:
    menu:
        "JS5FSa":
            jump js5fsa
        "JS5FSb":
            jump js5fsb

label js5fsa:
    menu:
        "JS5FSd":
            jump js5fsd
        "JS5FSe":
            jump js5fse

label js5fsb:

label js5fsd:
    menu:
        "JS5FSi":
            jump js5fsi
        "JS5FSj":
            jump js5fsj

label js5fse:
    menu:
        "JS5FSl":
            jump js5fsl
        "JS5FSm":
            jump js5fsm
        "JS5FSn":
            jump js5fsn

label js5fsi:
    jump js5fsk

label js5fsj:

label js5fsk:

label js5fsl:
    jump js5fso

label js5fsm:
    jump js5fso

label js5fsn:
    jump js5fso
