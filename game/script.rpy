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
    "characters/Julia-half.png"
    zoom 0.2
image Quol :   
    "characters/Quol.png"
    zoom 1.7
image Quol Angry:   
    "characters/Quol Angry.png"
    zoom 1.7
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
    show Julia at textbox_over

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
    
    J"(Quol out of frustration, swears towards the infiltrators)"

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
    show Julia at center_lower with Dissolve(0.3)
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
    show Renee bag at center with Dissolve(0.3)
    J"""(And then I spot it ... my trusty bat, safely tucked inside Renee's bag.)

    (But before I can fully process my next move, my attention is abruptly diverted.)"""

    hide Renee bag
    J"(An agent charges towards me, wielding a baton and swinging it with force.)"
    show Agent1 at center_lower with Dissolve(0.3)
    menu:
        J"gasp!"
        "Try to dodge the attack":
            hide Agent
            jump js1fsa
        "Scream":
            $ hp - 3
            jump js1fsb
        "Reach for my bat":
            $ hp - 1
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
    $hp - 3
    
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
    $hp - 1
    
    J"(As I swiftly dash towards Renee's bag, my eyes fixated on retrieving my bat, a sudden impact jolts through my leg.)"

    play sound "SFX/JS1FS/batonhit.mp3" volume 4
    
    J"""(The agent's swinging baton connects with my lower leg, causing an intense burst of pain to surge through my body.)
    
    (The force of the blow sends me off balance, causing me to stumble and stagger in my attempt to reach the bag.)
    
    (However, I manage to snatch my bat from Renee's bag)"""
    
    menu:
        "and next, I'll.."
        "Block":
            jump js1fse
        "Hit him back":
            jump js1fsf

label js1fsd:
    J"(He quickly recovers himself and prepares for another hit)"
    
    menu:
        "What do I do..?"
        "Scream":
            jump js1fsg
        "Try to dodge the attack":
            jump js1fsh
        "Reach for your bat":
            jump js1fsi

label js1fsg:
    J"""{b}AAAAAH!{/b}
    
    (I let out a startled cry.)
    
    (Voice trembling with fear and frustation, as well as an overwhelming hopelessness.)"""

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
    
    J"(I sliently watched as she goes over to Renee's bag and pulls out my bat, then tosses it to me.)"
    
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
    
    J"(I sliently watched as she goes over to Renee's bag and pulls out my bat, then tosses it to me.)"
    
    Q"Better keep it in your hands at all times."
    
    jump js1fsafter

label js1fsi:
    J"""(As the agent lunges towards me, their baton poised to strike, I gatrthered the courage to finally reach for my bat.)
    
    (Pouncing backwards, I land next to Renee's bag, and lifted my bat out of it.)
    
    (My grip tightens around the bat, my knuckles whitening as I prepare to meet the agent's attack head-on.)
    
    (The agent's baton hurtles towards me, and I brace myself for the impact.)"""

    play sound "SFX/JS1FS/batonwoosh2.mp3" volume 5

    pause 0.5

    play sound "SFX/JS1FS/batonhitbat1.mp3" volume 3


    J"(I skillfully parry the agent's attempts to strike back.)"
    
    play sound "SFX/JS1FS/batonhitbat2.mp3" volume 3

    J"(I block again)"
    
    play sound "SFX/JS1FS/batonhit2.mp3" volume 3

    J"(and finally deliver a hard blow, knocking the agent out cold.)"
    
    Q" Good job!"
    
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
    
    (I watch as the agent staggers backward, their eyes wide with disbelief.)
    
    (Moments later, they collapse to the ground.)"""
    
    jump js1fsafter

label js1fsafter:
    
    hide Quol
    hide Agent1

    J"he's down at least."
    show Renee at right_center_lower with Dissolve(0.3)
    R "There are quite a lot of them."

    R "Trying to hold them back."
    show Quol at left_center_lower with Dissolve(0.3)
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
    J"""I burst into the green room, slamming the door open and gasping for air. 

    It awakened the only person who was in the room, who was lying comfortably on the sofas, and he was shocked when I rushed in with such an expression, and while creating such a loud noise."""
    show Layon with Dissolve(0.3)
    L"""Holy mother of–

    Jeez it's just you, Julia.

    Concert done already? How does it feel like debuting?

    You're drenched in sweat already, I get how tense it is!"""

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


