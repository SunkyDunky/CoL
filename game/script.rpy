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
define G = Character("Agent",color="#cacaca")

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
    J"""Aren't those agents?
    
    what are they doing here??"""

    hide Julia

    show Agent at left with Dissolve(0.5)
    pause 0.5
    hide Agent with Dissolve(0.5)
    pause 0.5
    show Agent at right with Dissolve(0.5)
    pause 0.5
    hide Agent with Dissolve(0.5)
    pause 0.5
    show Agent at center_lower with Dissolve(0.5)
    pause 0.5
    hide Agent with Dissolve(0.5)
   
    show Julia at center_lower
    J"""This isn't a good sign..

    what should I do?"""

    menu:
        J"what should I do?"
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
    J"""I should ignore them...
    
    I think it would be okay, right?"""

    hide Julia worried

    show Agent at center_lower with Dissolve(0.3)
    pause 0.5
    hide Agent with Dissolve(0.3)
    show Agent at center_lower with Dissolve(0.3)
    pause 0.5
    hide Agent with Dissolve(0.3)

    J"""They... they are coming closer..
    
    I should do something...right?
    
    what do I do.."""

    menu:
        J"what do I do.."
        "Stand my ground, don't move a muscle..":
            jump JS0
        "I have to leave, I have to go!":
            jump JH0

label JS0:
    # agent tries dragging her
    show Agent at Transform(xalign=0.5, yalign=0.1, zoom=1.5)

    J"{b}'Aaaah!'{/b}"
    J"I have to back up I have to back up!!"
    hide Agent
    pause 2.0

    J"What...what just happened.."
    J"I'm hyperventilating.."

    menu:
        J"I'm hyperventilating.."
        "I should snap out of it":
            jump JS1
        "Run..I have to leave!":
            jump JH0

label JH0:
    show bg stage 
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

    menu:
        J"Calm down...calm down..."
        "I need to help my friends":
            jump JS1FS
        "I have to do something!":
            jump JS1FS
        "I can't just stand and do nothing!":
            jump JS1FS        

label JS1FS:
    J"where...where is my bat?"
    pause 0.5
    show Renee bag at center_lower
    J"Oh..oh I remember! It's in Renee's bag!"
    hide Renee bag
    J"It's just behind me, I have to get i-"
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