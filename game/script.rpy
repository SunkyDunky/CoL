# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#setting
default hp = 15
default havelayon = False

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
define Z = Character("A spectator?",color="#6303ff")

# define character sprites
image Renee :   
    "characters/Renee.png"
    zoom 0.5
image Julia :   
    "characters/Julia-half.png"
    zoom 0.2
image Quol :   
    "characters/Quol.png"
    zoom 0.5
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


#Illustrations
image JS1FS = im.Scale("JS1/JS1FS.png", config.screen_width, config.screen_height)



# The game starts here.

label start:
    show bg entrance
    pause 4.0
    show bg black
    with Dissolve(2.0)
    # Show your screen
    scene bg entrance_ticket_dark
    call screen character_selection
    with Fade(1.0,0.0,1.0)
    return

label Sorry:
    "sorry this character isn't available for now, Julia is available though."
    call screen credits
    jump Julia_Start
    return

label Julia_Start:
    window hide 
    pause 1.0 
    scene black with fade
    text """Disclaimer
    
    This demo of Concert of Liberation is a work in progress and intended solely as a test of concept. Please be aware that all content within this demo is unfinished and may not represent the final quality or features of the intended game. Bugs, glitches, and incomplete elements are expected. Your feedback and insights are highly appreciated as they will help us improve and shape the final product. Thank you for participating in this early stage of development.""" xalign 0.5 yalign 0.5
    pause 5  # Pause for 5 seconds to let the player read the text
    hide text with dissolve
    pause 0.5 
    $ renpy.movie_cutscene("images/opening.webm")
    show bg stage
    pause 1.0 
    window show
    show Julia at textbox_over

    J"""(In the crowded and noisy venue, I find myself standing above the stage, my fingers absentmindedly gripping the neck of my guitar.)

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
    J"""(I ignore the agents, not wanting to deal with any confrontations.)

    I should just ignore them

    (I mutter to myself, trying to convince myself that everything will be fine if I simply pretend they're not there.)"""


    show Agent1 at center_lower with Dissolve(0.3)
    pause 0.5
    hide Agent1 with Dissolve(0.3)

    J"""(But as one of the agents takes a step closer, my heart leaps into my throat, and my previous confidence wavers.)

    They... they are coming closer...

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

    {b}{i}Aaaah!{/i}{/b}

    (My instinct kicks in, overriding my initial shock.)

    (With every ounce of strength I can muster, I fight against the agent's grip, desperately wriggling and twisting in an attempt to break free.)

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
    hide Quol with Dissolve(0.3)
    hide Renee with Dissolve(0.3)
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
    J"(An agent charges towards me, wielding a baton and swinging it with force.)"
    menu:
        J"gasp!"
        "Try to dodge the attack":
            hide JS1FS
            jump js1fsa
        "Scream":
            $ hp - 3
            hide JS1FS
            show Agent1 at center_lower with Dissolve(0.3)
            jump js1fsb
        "Reach for my bat":
            $ hp - 1
            hide JS1FS
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
    J"""he's down at least.

    (I let out a tired sigh as I cast a glance at the fallen body, sprawled on the ground.)

    (The defeated foe lay motionless, a testament to our hard-won triumph.)

    (With a heavy heart, I shifted my focus to assess the state of my companions.)"""


    show Renee at right_center_lower with Dissolve(0.3)

    R "There's quite a horde of them."

    J"""(I observed Renee, her face etched with determination, desperately fending off two agile Agents.)

    (With lightning-fast reflexes, she deftly swung her whip, each crack of the lash a symphony of defiance against overwhelming odds.)"""

    R "Trying to hold them back, but it's getting intense."

    show Quol at left_center_lower with Dissolve(0.3)

    Q"Same."

    J"""(Quol, standing her ground nearby, fought off two relentless Agents of her own.)
    
    (They lunged at her, attempting to immobilize her, but she fought back with a flurry of kicks and evasive maneuvers.)"""

    Q"I'm not letting them get the upper hand!"

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
    J"I'll help Quol first!"

    show Agent1 at center_lower with Dissolve(0.3)

    J"""(Without hesitation, I propelled myself forward, instantly closing the distance between me and the Agent.)

    (Gripping my bat firmly, I swung it with all my might, delivering a powerful blow that connected with the Agent's body.)"""

    hide Agent1 with Dissolve(0.3)
    
    J"(The force of impact sent them sprawling to the ground, momentarily stunned.)"

    show Quol at center_lower with Dissolve(0.3)

    J"""(Quol's eyes widened briefly in surprise, but a grateful smile quickly spread across her face. )

    (She wasted no time, using the opening I had created to knock down the second Agent with a swift kick swiftly.)

    (The air crackled with a mix of adrenaline and relief as Quol, and I stood side by side, our united front a testament to our shared resolve.)

    (The tides of battle seem to have shifted in our favour, even if just for a moment.)"""

    hide Quol with Dissolve(0.3)

    J"""(However, I turned my head towards the direction of Renee and witnessed her arm getting hit by the baton of one of the agents and tumbling to the floor.)

    (My heart skipped a beat.)

    (The sight sent a surge of worry coursing through me, momentarily overshadowing the triumph of our successful attack on the Agents.)"""

    show Renee at center_lower with Dissolve(0.3)

    J"""(Without a second thought, I rushed to her side, my concern overriding any other consideration.)

    Renee, are you alright?

    (I was trembling and had no idea what to do.)

    (As panic threatened to consume me, my mind raced, desperately searching for a solution.)"""

    hide Renee with Dissolve(0.3)

    J"(And then, in that moment of uncertainty, a vivid memory flashed in my mind—a scene I had shared with Renee not too long ago.)"

    "Show flashback"

    J"""(My room was bathed in soft, warm light as Renee and I sat side by side on the edge of the bed.)

    (It had been a long and challenging day, and we sought solace in this quiet moment of respite.)

    (I looked at Renee, her presence a comforting anchor in the storm of uncertainty that swirled within me.)

    (The weight of the future pressed heavily on my mind, filling me with a sense of unease.)

    (I couldn't help but express my concerns.)

    Renee...

    I'm...uncertain about the future...
    
    It's like..like as if I'm standing at a crossroads, not knowing which path to take..

    I'm scared... that I would make wrong choices or not I would not live up to my potential.

    (Renee turned to me, her eyes filled with a mixture of understanding and compassion.)

    (After a brief silence, she touched my shoulder gently.)"""

    R """Julia.

    I kind of understand that feeling. 

    You see... there was a time when I was near death when everything seemed lost. 

    But surviving taught me the value of life and each moment's preciousness."""

    J"(Her words resonated deep within me, stirring a renewed perspective.)"

    R """Being alive allows for endless possibilities, Julia. 

    It opens doors to discovering the meaning of our existence and the roles we want to play in this world. 

    It's not about finding all the answers right away, but about embracing the journey and exploring what truly matters to us."""

    J"""(Her words held a profound truth, reminding me to cherish the gift of life and find solace in the process of self-discovery.)

    (Renee's unwavering belief in the importance of protecting one another echoed in my heart, reminding me of the bond we shared.)

    (Moved by her sincerity, I nodded, gratitude and determination shining in my eyes.)

    Thank you... Renee.

    (Renee smiled warmly, her gaze filled with trust and camaraderie.)"""

    R "I wouldn't want to see my best friends being in pain, would I?"

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

    (I swung it with all my might, delivering a powerful blow that connected with the Agent's body."""

    hide Agent1 with Dissolve(0.3)

    J"(The force of impact sent them sprawling to the ground, momentarily stunned.)"

    show Renee at center_lower with Dissolve(0.3)

    J"""(Fueled by my unexpected intervention, Renee swiftly took advantage of the moment.)

    (Her whip cracked through the air, striking the other Agent with a resounding crack.)

    (The enemy stumbled backwards, defeated and temporarily stunned.)

    (A mixture of relief and determination washed over us. Renee's eyes met mine, gratitude and understanding passing between us in that fleeting moment.)"""

    hide Renee with Dissolve(0.3)

    J"""(However, I turned my head towards the direction of Quol and witness her leg getting hit by the baton of one of the agents and tumbling to the floor.)

    (My heart skipped a beat.)

    (The sight sent a surge of worry coursing through me, momentarily overshadowing the triumph of our successful attack on the Agents.)"""

    show Quol at center_lower with Dissolve(0.3)

    J"""(Without a second thought, I rushed to her side, my concern overriding any other consideration.)

    Quol, are you alright?

    (I was trembling and had no idea what to do.)

    (As panic threatened to consume me, my mind raced, desperately searching for a solution.)

    (And then, in that moment of uncertainty, a vivid memory flashed in my mind—a scene I had shared with Quol not too long ago.)"""

    hide Quol with Dissolve(0.3)

    J"""(It was 2 days after I ran away from Newfutures Institute, I was sitting near the stack of cargo containers, starving and getting worried of my scarred leg.)

    (Suddenly, a person with distinct blue hair approached me.)"""

    Q"""Julia!

    "It's me, Quol! I can't believe I found you here!"""

    J"""Quol...?

    Who...are you?

    (Quol's expression faltered for a moment, a flicker of disappointment passing across hrt face.)"""

    Q"""I-I'm sorry.

    You really don't remember me...I see.. We were friends during the Brookcastle incident."""

    J"""(My confusion deepened as I stared at her face, trying to search for any instances where she had appeared in any of my memories.)

    (But my mind drew a blank, leaving me feeling disoriented and uncertain.)

    I... I don't remember.

    ...

    I don't understand what's happening... Why can't I remember? What happened during the Brookcastle Incident?

    (Quol's face softened, and they offered a reassuring smile.)""" 

    Q"""It's okay, Julia.

    Nobody remembers what happened during the Brookcastle incident; only I do really, and I'll explain it all to you in due time."""

    J"""(As we stood there, confusion swirling within me, Quol's face glimpsed a confident smirk as she stood up.)

    (They reached into a bag slung over their shoulder and pulled out a small loaf of bread.)"""

    Q"Here."

    J"(Quol extended the bread towards me.)"

    Q"Take this. It might help you feel better."

    J"""(I accepted the bread, grateful for their kindness and willingness to help.)

    (As I nibbled on the bread, Quol began recounting our supposed shared experiences.)

    (They spoke of an adventure through lands, through villages, rivers, and valleys.)

    (The journey of a young girl named Julia as she gathers strength and fortitude to end the Brookcastle event, developing from a frightened, shy kid to one who swings and fights for herself.)

    (As Quol spoke, a sense of determination ignited within me.)

    (Even though I couldn't remember our past, I felt a connection, an unspoken bond that made me let my guard down a little.)

    I may not remember you, or my past,
    
    but I want to be like the Julia you described...

    (Quol's eyes brightened with a mixture of relief and pride.)
    
    (She ripped off part of her shirt, and kneeled down in front of me.)"""

    Q"""Then let's start by taking care of that injured leg.

    We'll face the challenges together, Julia, and hopefully, you will grow as strong as you had back then."""

    J"""(As Quol began to tend to my injured leg using the cloth, I couldn't help but feel a glimmer of hope.)
    
    (Though my confusion remained, I was determined to embrace this new chapter, starting a new life.)

    (I snapped back to reality and held my bat tightly as I knocked down the agent who injured Quol.)

    (I realised that I had to fight for myself.)"""

    jump JS13

label JS13:
    "Fighting off all the agents, it seemed like they got backup."
    jump js42fs


#JS2
label JS2:
    show bg greenroom with fade
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


label js42fs:
    "Four agents approched us"
    if havelayon == True:
        jump js42fsa
    else:
        jump js42fsb

label js42fsa:
    menu:
        "JS42FSi":
            jump js42fsi
        "JS42FSj":
            jump js42fsj

label js42fsb:
    J"""Without hesitation, Renee sprang into action, her movements swift and precise as she lunged towards one of the agents
    
    In a blur of motion, Quol followed suit, her agility and strength on full display as she engaged another agent
    
    My heart raced as I realized that two agents still remained, their attention now squarely focused on me. 
    
    Fear mingled with determination within me as I braced myself for the impending confrontation.
    
    I noticed one of the agents accidentally slipped their baton out of their hand as they approached
    "
    Who should I focus on first?"""
    
    menu:
        "Agent with a baton":
            jump js42fsc
        "Agent without a baton":
            jump js42fsd

label js42fsc:
    J"As the agent with the baton closed in, I mustered all my strength and swung my weapon towards them."
    
    show screen timerDown(3, "misseditJS42FSc1")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Swing left", "choice1JS42FSc1", 0.2, 0.5),  # xpos and ypos for choice 1
        ("Swing right", "choice2JS42FSc1", 0.8, 0.5)   # xpos and ypos for choice 2
    ])
    return
    
    label misseditJS42FSc1:
        $hp - 1
        J"I got hit in the arm because I was not quick enough to react"
        jump finishedJS42FSc1
    
    label choice1JS42FSc1:
        J"I swang left, and it blocked the baton."
        jump finishedJS42FSc1
    
    label choice2JS42FSc1:
        J"I swang right, and it blocked the baton."
        jump finishedJS42FSc1
    
    label finishedJS42FSc1:
        J"The agent is temportarily off guard"
        
    show screen timerDown(3, "misseditJS42FSc2")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Strike downwards", "choice1JS42FSc2", 0.5, 0.3),  # xpos and ypos for choice 1
    ])
    return
    
    label misseditJS42FSc2:
        J"I got hit on the waist, then came to my senses and attacked his head out of reflexes"
        
        J"They immedately fell on the ground motionless"
        jump finishedJS42FSc2
    
    
    label choice1JS42FSc2:
        J"I striked down on the Agent and they immedately fell on the ground motionless"
        jump finishedJS42FSc2
    
    label finishedJS42FSc2:
        J"""He is down.
        
        My relief was short lived, as the other agent then tried to jump on me
        
        what should I do?"""
       
    menu:
        "go for the kill":
            jump js42fsl
        "Play it defensively":
            jump js42fsm

label js42fsd:
    J"""With the agent without the baton closed in, I see that it is trying to directly jump on me
    
    I held tight my bat, and decided on my next move"""
    
    menu:
        "go for the kill":
            jump js42fsg
        "JPLay it defensively":
            jump js42fsh

label js42fsg:
    J""" I decided to go for the kill
    
    I prepared my swing and gluped
    
    however, I lost my train of thought and when I came to my senses was when my back hits the ground.
    
    The agent has swiftly took my bat away from my hands and threw it away, while pinning me to the ground."""
    
    jump game_over

label js42fsh:
    J"I decided to get defensive and held my bat tight"
    
    show screen timerDown(3, "misseditJS42FSc5")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Block Horizontally", "choice1JS42FSc5", 0.2, 0.5),  # xpos and ypos for choice 1
        ("Block Vertically", "choice2JS42FSc5", 0.8, 0.5)   # xpos and ypos for choice 2
    ])
    return
    
    label misseditJS42FSc5:
        $hp - 1
        J"I stumbled backwards mildly"
        jump finishedJS42FSc5

    label choice1JS42FSc5:
        J"I held my bat horizontally, and it blocked the baton."
        jump finishedJS42FSc5

    label choice2JS42FSc5:
        J"I held my bat vertically, and it blocked the baton."
        jump finishedJS42FSc5

    label finishedJS42FSc5:
        J"""I then swing towards his torso, making sure he fainted off

    The other sees that I've knocked down his comrade, and approches me

    As the agent with the baton closed in, I mustered all my strength and swung my weapon towards them."""

    show screen timerDown(3, "misseditJS42FSc3")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Swing left", "choice1JS42FSc3", 0.2, 0.5),  # xpos and ypos for choice 1
        ("Swing right", "choice2JS42FSc3", 0.8, 0.5)   # xpos and ypos for choice 2
    ])
    return

    label misseditJS42FSc3:
        $hp - 1
        J"I got hit in the arm because I was not quick enough to react"
        jump finishedJS42FSc3

    label choice1JS42FSc3:
        J"I swang left, and it blocked the baton."
        jump finishedJS42FSc3

    label choice2JS42FSc3:
        J"I swang right, and it blocked the baton."
        jump finishedJS42FSc3

    label finishedJS42FSc3:
        J"The agent is temportarily off guard"
        
    show screen timerDown(3, "misseditJS42FSc4")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Strike downwards", "choice1JS42FSc4", 0.5, 0.3),  # xpos and ypos for choice 1
    ])
    return

    label misseditJS42FSc4:
        J"I got hit on the waist, then came to my senses and attacked his head out of reflexes"
        
        J"They immedately fell on the ground motionless"
        jump finishedJS42FSc4


    label choice1JS42FSc4:
        J"I striked down on the Agent and they immedately fell on the ground motionless"
        jump finishedJS42FSc4

    label finishedJS42FSc4:
        jump js42fsafter

    label js42fsi:
        J""" I decided to go for the kill
        
        I prepared my swing and gluped
        
        however, I lost my train of thought and when I came to my senses was when my back hits the ground.
        
        The agent has swiftly took my bat away from my hands and threw it away, while pinning me to the ground."""
        
        jump game_over

label js42fsj:
    J"I decided to get defensive and held my bat tight"
    
    show screen timerDown(3, "misseditJS42FSc6")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Block Horizontally", "choice1JS42FSc6", 0.2, 0.5),  # xpos and ypos for choice 1
        ("Block Vertically", "choice2JS42FSc6", 0.8, 0.5)   # xpos and ypos for choice 2
    ])
    return
    
    label misseditJS42FSc6:
        $hp - 1
        J"I stumbled backwards mildly"
        jump finishedJS42FSc6
    
    label choice1JS42FSc6:
        J"I held my bat horizontally, and it blocked the baton."
        jump finishedJS42FSc6
    
    label choice2JS42FSc6:
        J"I held my bat vertically, and it blocked the baton."
        jump finishedJS42FSc6
    
    label finishedJS42FSc6:
        J"""I then swing towards his torso, making sure he fainted off
    
        The other sees that I've knocked down his comrade, and approches me
        
        As the agent with the baton closed in, I mustered all my strength and swung my weapon towards them."""
        
        jump js42fsafter

label js42fsl:
    J""" I decided to go for the kill
    
    I prepared my swing and gluped
    
    however, I lost my train of thought and when I came to my senses was when my back hits the ground.
    
    The agent has swiftly took my bat away from my hands and threw it away, while pinning me to the ground."""
    
    jump game_over

label js42fsm:
    $hp - 1
    J""" I held my bat horizontally to block the agent as he jumps on me
    
    He hits my shoulder mildly, but I manage to swing him off and throw him on the ground
    
    I then swing towards his torso, making sure he fainted off"""
    
    jump js42fsafter

label js42fsafter:
    "All the agents have passed out, and we all had a sigh of relief"





label game_over:
    show bg black
    Z"""Huh, you're down
    
    that wasn't fun.

    Not a great way to end a story, is it?

    let's try this again."""
    return