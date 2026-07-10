#Birthday Jun 30, 2026
import os

os.environ["TK_SILENCE_DEPRECATION"] = "1"
# Disclaimer: This game cannot be commercially played due to Turtle module limits.
# remember to import pygame for Bold and Gilber(t) sequels
import sys
import random
import time
import turtle
import math
from Tokimon_save_file import save_game, load_game
def creddits():
    stupid_imbeciles = turtle.turtles()
    for _ in stupid_imbeciles:
        _.hideturtle()
        _.clear()
    pen.color("white")
    credits =""" RNG RPG(Tokimon)
            Created by: XXX XXX
            Programmed by: XXX XXX
            Testers: XXX XXX and YYY YYY
            Used resourses:\n os, sys, random, time, turtle, math\nPython 3\nTurtle Graphics(Developed by Lego), Gemini(Google), ChatGPT(Open AI)
            Special thanks to: Python 3(https://docs.python.org/3/), Coding For Kids Python by Adrienne B. Tacke and YOU!
    """
    easter_egg = """""🎵 Happy Birthday to You
Happy Birthhhhday to Tokimon
Happy Birthday to You…

You're 0 years old,
You have a lotta Ego®,
And you smell like one too!"""
    songs = """The Man Who's Running the Game
    Happy Birthday to Tokimon!
    Tokirap
    The Man Who's Running the Game ex.-
    Hold on since when did that song exist
    Since NOW!🎶 said Scaresow, period."""
    the_man_whos_running_the_game = """It's a surprise😮 to me that it's a surprise to you😮...
    Which degree is the argument to whom...
    We could go on and on and on but in the end who are we KIDDING?
    My Divinity is past math.inf...
    AM I GETTING THROUGH?
    Seems our regime is going down fast
    No need to yell if our ideas don't contrast...
    Look at that!
    I put this in your hat!
    💣Oh what a shock!⚡️(using Tikachu)
    Watch where you walk!(You stepped in sticky arena)
    I'm the Ghost I run this game! Scaresow is my name
    Feeling reused, not much news...
    WHAT A FUK-ING SHAME!!!
    Congratulations🎉 all of you players! I'm gonna destroy you so send out your prayers!
    Right step down on the sack my torture now- back on track
    It's your tendency to be blind to see that this twisted mascree is the only place you'll ever be...
    Cuz' I'm the one who's running this game! YEAH!"""
    screen.bgcolor("black")
    map_drawer.clear()
    pen.clear()
    pen.up()
    pen.goto(0, 220)
    pen.write((credits), align="center",font=("Courier", 24, "bold"))
    screen.ontimer(lambda: pen.clear(), 5000)
    screen.ontimer(lambda: pen.write(easter_egg), 5500)
    screen.ontimer(lambda: pen.write(songs), 7000)

round = 1

team, box, progress = load_game()

name = input("What's your name? You will only need the terminal for this part.")
screen = turtle.Screen()
annoying_mac = screen.window_width()
more_annoying_mac = screen.window_height()
screen.setup(annoying_mac, more_annoying_mac)
pen = turtle.Turtle()
pen.color("black")
pen.hideturtle()
Tokimon = "MissingNo"
def battle_text(msg, size=24):
    pen.clear() # Locked pairing frame boundary
    pen.up()
    pen.goto(-annoying_mac/2 + 30, -more_annoying_mac/2 + 60)
    pen.write(msg, font=("Courier", size, "bold"))
global Reasearch_1, Scary, baited, rage_baited, impression, stary, gym_battle, gym_battle_finale, Enemy_Move_Type, Energy_flail
gym_battle_finale = False
Scary = 0
Angry_Tikachu = progress["Angry_Tikachu"]
Defeating_Green = progress["defeating_green"]
Tokicubes = progress["tokicubes"]
current_map = progress["current_map"]
Reasearch_1 = progress["research_1"]
impression = progress["impression"]
tm = progress["tm"]
starter = progress["starter"]
def manual_save():
    progress["starter"] = starter
    progress["Angry_Tikachu"] = Angry_Tikachu
    progress["defeating_green"] = Defeating_Green
    progress["research_1"] = Reasearch_1
    progress["impression"] = impression
    progress["current_map"] = current_map
    progress["tokicubes"] = Tokicubes
    progress["tm"] = tm

    save_game(team, box, progress)
    battle_text("Game saved!")
enemy = "Green"       # 🎯 Dynamic enemy tracker ("Green", "Digetey", or "Ratattle")
player_taunted = False # 🤫 Status tracker for Taunt mechanic
enemy_immune = False   # 🕊️ Block tracker for state immunity frames (Fly)
enemy_flying = False   # ☁️ State lock for two-turn aerial moves
enemy_ar_active = False # 𽳳 Status tracker for Digetey's 1/4 accuracy hack
player_immune = False  # 🛡️ Block tracker for player immunity frames (Fly)
player_flying = False  # ☁️ State lock for player aerial moves
player_flinched = False # 😨 Status tracker for Ratattle's brutal Bite flinch
slot_1_item = False
baited = False
rage_baited = False
stary = False
gym_battle = False
Enemy_Move_Type = "_"
Energy_flail = False
arena = "_"

party_items = ["Berry", "None", "None", "None", "None", "None"] # 🎒 Tracks held items for party slots 0-5
active_slot = 0       # Tracks which party slot (0-5) is currently fighting on field
turn1 = 0            # Tracks enemy's random move choice
green_status = "Normal" # 💤 Tracks enemy's status condition ("Normal", "Sleep", "Confused", or "Burn")
screen.bgcolor("#2e8b57") # SeaGreen hex code (looks like classic 8-bit grass)
# Map drawer configuration
partner_blue_hat_guy = turtle.Turtle()
partner_blue_hat_guy.shape("turtle")
partner_blue_hat_guy.color("blue")
partner_blue_hat_guy.up()
partner_blue_hat_guy.hideturtle()

blue_hat_guy = turtle.Turtle()
blue_hat_guy.shape("turtle")
blue_hat_guy.color("blue")
blue_hat_guy.up()
blue_hat_guy.hideturtle()
blue_hat_guy.goto(10, 0)

partner_Scarmander = turtle.Turtle()
partner_Scarmander.shape("circle")
partner_Scarmander.color("orange")
partner_Scarmander.up()
partner_Scarmander.goto(30, 0)
partner_Scarmander.hideturtle()

Scarmander = turtle.Turtle()
Scarmander.shape("circle")
Scarmander.color("orange")
Scarmander.up()
Scarmander.hideturtle()
Scarmander.goto(30, 0)

partner_Bulbabore = turtle.Turtle()
partner_Bulbabore.shape("square")
partner_Bulbabore.color("green")
partner_Bulbabore.up()
partner_Bulbabore.hideturtle()

Bulbabore = turtle.Turtle()
Bulbabore.shape("square")
Bulbabore.color("green")
Bulbabore.up()
Bulbabore.hideturtle()
Bulbabore.goto(-10, 0)

Tikachu = turtle.Turtle()
Tikachu.shape("triangle")
Tikachu.color("yellow")
Tikachu.hideturtle()
Tikachu.up()


player = turtle.Turtle()
player.shape("turtle")
player.color("red")
player.up()
player.showturtle()
player.goto(0, 0)
player.left(90)

map_drawer = turtle.Turtle()
map_drawer.hideturtle()
map_drawer.speed(0)
map_drawer.up()

# Dialogue pen configuration
pen = turtle.Turtle()
pen.color("black")
pen.hideturtle()
pen.up()

# --- 2. THE SYMMETRIC GRID BUILDER ---
lab_width = 460
lab_height = 320

lab_x = -(lab_width / 2)
lab_y = -(lab_height / 2) + 60 

def Scaresow_tag():
    global round
    if player.distance(real_scaresow) < 25:
        battle_text("Darn...!")
        round += 1
        Scaresow_game()
    if player.distance(hat) < 21:
        manual_save()
        sys.exit()    
    else:
        screen.ontimer(Scaresow_tag, 100)
def BATTLE():
    global enemy, Tokimon
    enemy = "Napsols"
    Tokimon =  "Napsols"
    Tokimon_battle()

def final_mission():
    battle_text("Everyone welcome. I, Broke will prove the hyposissis that Bulbabore can grow like regular plants.")
    screen.ontimer(lambda: battle_text("Oh what ever says one guy WE DON'T CARE IT'S GONNA FAIL ANYWAYS."), 3000)
    screen.ontimer(lambda: battle_text("WELL YOU SHOULD CARE ALL RIGHT! I killed a Chrap and squezzed a Polirode AND Poligirl AND put in Scaresow's compost!"), 6000)
    screen.ontimer(lambda: battle_text("And watch the effect...(A Bulbabore in a pot looking iritated had a BULB growing out of it's bulb.)"), 9000)
    screen.ontimer(lambda: battle_text(" TIKACHU'S HERE AND I HAVE A BAZOOKA!"), 12000)
    screen.ontimer(lambda: battle_text("IS THIS EVEN APPROPIATE FOR CHILDREN?"), 13000)
    screen.ontimer(lambda: battle_text("lNKL>KN>KSJDHKJ! LEGENDARY TIME!"), 14000)
    screen.ontimer(lambda: BATTLE(), 16000)

def countdown():
    global start_farm
    if time.monotonic() - start_farm >= 20:
        battle_text(" Ugh are you going to boring... 😉 Jump scare time...")
        battle_text("")
        pen.color("red")
        pen.goto((-2 * annoying_mac + 40), (-2 * more_annoying_mac + 60))        
        map_drawer.clear()
        pen.write("""
                *   *
                 \__/ 
                  """)
        pen.color("black")
        sys.exit()
    else:
        screen.ontimer(countdown, 1000)  
def delete():
    battle_text("IT WAS.")
    screen.ontimer(lambda: battle_text("HEY YOU JUST DELETED SCRAP METAL HOW DARE YOU?"), 3000)
    screen.ontimer(lambda: battle_text("🎶Not very happy? You think I'm yappy?🔫"), 6000)
    screen.ontimer(lambda: battle_text("Uh where did you get the shotgun heh, heh."), 9000)
    screen.ontimer(lambda: battle_text("Squish Squish Squish😊."), 12000)
    screen.ontimer(lambda: battle_text("CONGRAGUATIONS ALL OF YOU PLAYERS, YOUR DUMB SAVE FILE IS GETTING A CLEANSE!"), 15000)
    screen.ontimer(lambda: battle_text("PERIOD Did you like my little- WAIT WHERE DID YOU GO? and where is the compost?!"), 16000)
    screen.ontimer(lambda: final_mission(), 17000)
    screen.onkey(None, "-")          

def Scaresow_game():
    global rows, colloms, round, real_scaresow,hat, current_map, start_farm, Tokimon
    current_map = "Lab"
    real_scaresow = turtle.Turtle()
    real_scaresow.shape("classic")
    real_scaresow.color("brown")
    hat = turtle.Turtle()
    hat.color("white")
    hat.shapesize(0.5)
    def hat_move():
        global hat_angle
        hat_angle = hat.towards(player)
        hat.setheading(hat_angle)
        hat.forward(5)
        screen.ontimer(hat_move, 100)
    hat.goto(real_scaresow.xcor(), real_scaresow.ycor())
    hat.showturtle()
    for craziness in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
        rows = random.randint(1, 500)           
        colloms = random.randint(1, 500)
        real_scaresow.goto(rows, colloms)
        real_scaresow.stamp()
        craziness += 1    
    if round == 1:   
        battle_text("NOW COME GET ME😂") 
        start_farm = time.monotonic()
    elif round == 2:
        battle_text("😡Well, there's still 2 more rounds")    
        start_farm = time.monotonic()
    elif round == 3:
        battle_text("🤬 CAN'T YOU JUST STAY STILL FOR 4 SECONDS STOP PRESSING THE W,A,S,D!")    
        time.sleep(4)
        start_farm = time.monotonic()
    elif round == 4:
        Tokimon = "Scaresow"
        battle_text("😅😉😈🤬😡🦠I AM THE ONLY ONE WHO CAN BREAK THE FOURTH WALL I CAN ALSO INFULENCE THE DEVELOPER!")
        screen.ontimer(lambda: battle_text("Let's leave before he calls sys.exit() or somethin'!"), 3000)
        screen.ontimer(lambda: battle_text("🎶It's a surprise😮 to me that it's a surprise 😮 to you..."), 6000)
        screen.ontimer(lambda: battle_text("🎶On which degree is the arguement to whom!"), 9000)
        screen.ontimer(lambda: battle_text("\" You should have kept it as WHO instead of Whom because then it would rhyme!\" says Sassy Tokidex."), 12000)
        screen.ontimer(lambda: battle_text("🎶😡 We could go on and on and on and on, but in the end who are f****** kidding?"), 15000)
        screen.ontimer(lambda: battle_text("🎶MY APOSTROPHE IS PAST DEMOCRACY! Am I getting THROUGH🫥?"), 18000)
        screen.ontimer(lambda: battle_text("🎶Seems our regime is plummeting down📉 No need to shout if you don't got a mouth😶"), 21000)
        screen.ontimer(lambda: battle_text("Look at that!👀 Watch what I put in your hat!🧢💣💥"), 24000)
        Tokimon = "Hotomb"
        screen.ontimer(lambda: battle_text("AHHH A HOTOMB!"), 27000)
        screen.ontimer(lambda: battle_text("Oh what a shock!⚡️ Watch where you walk!(Ick you stepped on the Sticky arena)"), 30000)
        screen.ontimer(lambda: battle_text("I'm the ghost I run the place Scare-sow is my name I run the game and that's the same AND IT ISN'T TAME!"), 33000)
        screen.ontimer(lambda: battle_text("That wasn't even a good rhyme."), 36000)
        delete()

        #This is where Scaresow loses his sanity!
        return    
    player.left(130)  
    countdown()
    Scaresow_tag()
    hat_move()
def volcano():
    battle_text("Proffessor Broke says: DIGETEY YOU F****** BRAT! TELL US WHERE IS THAT TIKACHU!")    
    screen.ontimer(lambda: battle_text("COME DIGETEY! You little birdie I know you can hear me! TELL ME WHERE IS THAT TIKACHU! Or else I'LL..."), 3000)
    screen.ontimer(lambda: battle_text("\"Actually better idea get a life\" , interupts The Sassy Tokidex"), 6000)
    screen.ontimer(lambda: battle_text("Digetey screams Look he's on a VOLCANO!"), 9000)
    screen.ontimer(lambda: battle_text("Let's kill him anyway! shouts the Sassy Tokidex"), 12000)
    screen.ontimer(lambda: battle_text("You watch in horror as the Sassy Tokidex comes out of a dresser with a tax filing machine in the metal rectanglish hand where Digetey used to be!"), 15000)
    if "Digetey" in team:
        team.remove("Digetey")
    screen.ontimer(lambda: battle_text(f"Now it's your turn... GO Get em' {name} fight the Legendary Tokimon!"), 18000)
    load_the_island()
    

def Tokimon_battle():
    pen.clear() # Locked pairing frame boundary
    pen.write(f"Green VS. (Which one? {team[0]} Use numbers 1-6 to decide!)", font=("Courier", 24, "bold"))
           

def Get_a_sassy_Tokidex():
    global gym_battle, gym_battle_finale
    gym_battle_finale = False
    gym_battle = False
    battle_text("This works like the original... I like to call it SCRAP METAL for Stupid C*** Rightfully Added With Poorly- BONK!")
    screen.ontimer(lambda: battle_text("You watch in surprise as the Tokidex takes the disk and puts it in his disk holder!(He bonks him on the head)"), 3000)
    volcano()            

def build_room(turt, x, y, w, h, floor_color, wall_color):
    turt.goto(x, y)
    turt.color(wall_color, floor_color)
    turt.down()
    turt.begin_fill()
    for _ in range(2):
        turt.forward(w)
        turt.left(90)
        turt.forward(h)
        turt.left(90)
    turt.end_fill()
    turt.up()
    
    turt.goto(x, y)
    turt.pensize(6)
    turt.down()
    for _ in range(2):
        turt.forward(w)
        turt.left(90)
        turt.forward(h)
        turt.left(90)
    turt.up()
    turt.pensize(1) 

def draw_forest_tree(x, y):
    map_drawer.goto(x - 6, y - 24)
    map_drawer.color("black", "#5c4033")
    map_drawer.down()
    map_drawer.begin_fill()
    for _ in range(2):
        map_drawer.forward(12)
        map_drawer.left(90)
        map_drawer.forward(24)
        map_drawer.left(90)
    map_drawer.end_fill()
    map_drawer.up()
    
    map_drawer.goto(x, y)
    map_drawer.color("black", "#1e5335")
    map_drawer.down()
    map_drawer.begin_fill()
    map_drawer.circle(24)
    map_drawer.end_fill()
    map_drawer.up()

def load_the_woods():
    global current_map
    current_map = "The_Woods"
    pen.clear()
    map_drawer.clear()
    
    blue_hat_guy.hideturtle()
    Scarmander.hideturtle()
    Bulbabore.hideturtle()
    Tikachu.hideturtle()
    
    screen.bgcolor("#2e8b57") 
    
    random.seed(69) 
    for _ in range(20):
        tx = random.randint(-300, 300)
        ty = random.randint(-250, 250)
        if not (-60 <= tx <= 60 and -60 <= ty <= 60):
            draw_forest_tree(tx, ty)
    
    yeet_x = random.randint(-120, 120)
    yeet_y = random.randint(-120, 120)
    
    player.goto(yeet_x, yeet_y)
    if "Blue Hat Guy" in team: partner_blue_hat_guy.goto(yeet_x + 10, yeet_y)
    if "Scarmander" in team: partner_Scarmander.goto(yeet_x + 30, yeet_y)
    if "Bulbabore" in team: partner_Bulbabore.goto(-10, yeet_y)
    
    battle_text("Professor Broke: YEET!!!\n\nYou crashed deep into the untamed woods!", size=16)

def load_the_island():
        global enemy, Tokimon, current_map, Voltoogaidle
        map_drawer.clear()
        screen.bgcolor("sea green")

        map_drawer.goto(0, -370)
        map_drawer.color("black", "sandy brown")
        map_drawer.down()
        map_drawer.begin_fill()
        map_drawer.circle(370)
        map_drawer.end_fill()
        map_drawer.up()
        current_map = "Island"
        Voltoogaidle = turtle.Turtle()
        Voltoogaidle.shape("turtle")
        Voltoogaidle.color("red")
        Voltoogaidle.penup()
        Voltoogaidle.goto(0,0)
        Voltoogaidle.shapesize(150)
        player.goto(0,0)
        enemy = "Voltooga(Idle)"
        Tokimon = "Voltooga(Idle)"
        Tokimon_battle()
        screen.ontimer(lambda: battle_text("Wheeze that didn't go well did it?"), 3000)
        screen.ontimer(lambda: battle_text("Wait why is..."), 3000)
        Voltoogaidle.showturtle()
        voltooga_alive = True

# --- 3. RENDERING THE ENVIRONMENT ---
if current_map == "Lab":
    build_room(map_drawer, lab_x, lab_y, lab_width, lab_height, "#dcdcdc", "black")

    door_width = 40
    door_height = 45
    door_x = -(door_width / 2) 
    door_y = lab_y + lab_height - door_height 

    map_drawer.goto(door_x, door_y)
    map_drawer.color("black", "#8b4513")
    map_drawer.down()
    map_drawer.begin_fill()
    for _ in range(2):
        map_drawer.forward(door_width)
        map_drawer.left(90)
        map_drawer.forward(door_height)
        map_drawer.left(90)
    map_drawer.end_fill()
    map_drawer.up()
elif current_map ==  "The_Woods":
    load_the_woods()
elif current_map == "Island":
    load_the_island()
elif current_map == "Team Socket Landing":
    load_the_woods()
    current_map = "Team Socket Landing"
elif current_map == "Gym":
    build_room(map_drawer, -100, -100, 200, 200, "#e2d5d7", "red")
    screen.ontimer(lambda: battle_text("Professor Broke says: \"I have a need for... Digetey!\""), 1000)
    screen.ontimer(lambda: battle_text("He's a bit of a... thing um you see... HE MIGHT KNOW WHERE IS THAT G******* Tikachu is!"), 3000)
    screen.ontimer(lambda: battle_text("But first gym battle against Pigpen the ground type specilist!"), 5000)
    enemy = "Onieyx"
    Tokimon_battle()
    gym_battle = True
    enemy = "Glooper"
    Tokimon_battle()
    gym_battle_finale = True
    screen.ontimer(lambda: battle_text("HMMM... very intresting... I think you are ready for an upgraded Tokidex or as I like to say DOWNGRADED!"), 3000)
    screen.ontimer(lambda: Get_a_sassy_Tokidex(), 6000)   
else:
    ####"Praise" people who SOMEHOW found a way to get out of bounds when it's technicly impossible#####        
    pen.clear() # Locked pairing frame boundary
    pen.up()
    pen.goto(-annoying_mac/2 + 30, -more_annoying_mac/2 + 60)
    pen.write("Wha- how the f*** did you get into the void? Since you're obviously not a child\n for knowing this I'd say just f*** you\n wait how to turn of censoring ugh!", ("Courier",24,"bold"))



# --- 🌲 CHAOTIC FOREST GENERATOR ---
# --- 🎲 WILD AMBUSH STEP ENGINE ---
def check_forest_encounter():
    global current_map, enemy, Tokimon, player_taunted, enemy_immune, enemy_flying, enemy_ar_active, player_flinched, green_status, player_immune, player_flying
    if current_map != "The_Woods": return
    
    if random.randint(1, 5) != 1:
        screen.onkey(None, "w")
        screen.onkey(None, "s")
        screen.onkey(None, "a")
        screen.onkey(None, "d")
        
        enemy = random.choice(["Digetey", "Ratattle"])
        Tokimon = enemy
        
        if enemy == "Digetey": Tokimon_stats["Digetey"]["HP"] = 90
        elif enemy == "Ratattle": Tokimon_stats["Ratattle"]["HP"] = 150
        
        player_taunted = False 
        enemy_immune = False
        enemy_flying = False
        enemy_ar_active = False
        player_flinched = False
        green_status = "Normal"
        player_immune = False
        player_flying = False
        battle_text(f"A wild {enemy} ambushed you from the canopy!\n\nPress 1-6 to choose your fighter!")

def icky_island_encounter():
    global enemy, Tokimon
    if current_map != "Island":
        return
    else:
        enemy = random.choice(["Magtar", "Fuk", "Slimer", "Ratamate", "Tichu", "Thaichu", "Digetey", "Motom"])
        Tokimon = enemy
        battle_text("ICK no wonder nobody really goes to Hawai!")
        Tokimon_battle()
        screen.ontimer(lambda: battle_text("SOOO famished... What's that smell... it's seafood...?"), 5000)
        screen.ontimer(lambda: battle_text("NOPE! It was a Chrap I mean Trap I mean Chrap Trap!"), 8000)
        enemy = "Chrap"
        Tokimon = "Chrap"
        Tokimon_battle()
        screen.ontimer(lambda: battle_text("One eternity later..."), 3000)
        time.sleep(4)
        Tokimon = "Polirode"
        enemy = "Polirode"
        Tokimon_battle()
        Tokimon = "Poligirl"
        enemy = "Poligirl"
        Tokimon_battle()
        time.sleep(10)
        battle_text("2 eternities later...")
        screen.ontimer(lambda: battle_text("\"You want the CONPOST THEN LET'S PLAY A GAME😈.\" says an invisible voice you think is coming from the scarecrow."), 1000)
        Scaresow_game()
def player_right():
    player.right(45)
    partner_blue_hat_guy.right(45)
    partner_Scarmander.right(45)
    partner_Bulbabore.right(45)
if name == "Charlie" or name == "Ash":
            creddits()
            screen.mainloop()
            sys.exit()
def player_left():
    player.left(45)
    partner_blue_hat_guy.left(45)
    partner_Scarmander.left(45)
    partner_Bulbabore.left(45)

def player_forward():
    player.forward(10)
    partner_blue_hat_guy.forward(10)
    partner_Scarmander.forward(10)
    partner_Bulbabore.forward(10)
    check_forest_encounter()
    icky_island_encounter()

def player_backward():
    player.backward(10)
    partner_blue_hat_guy.backward(10)
    partner_Scarmander.backward(10)
    partner_Bulbabore.backward(10)
    check_forest_encounter()
    icky_island_encounter()

def check_door_collision():
    px, py = player.pos()
    if -20 <= px <= 20 and 175 <= py <= 220:
        if not starter:
            player.right(180)
            player.goto(0, 0) 
            blue_hat_guy.showturtle()
            Scarmander.showturtle()
            Bulbabore.showturtle()
            pen.clear() # Locked pairing frame boundary
            pen.write("You entered the room! Professor Broke offers you to choose between 3 Tokimon!", font=("Courier", 24, "bold"))
        elif Defeating_Green and current_map == "Lab":
            load_the_woods()

def blue_hat_guy_starter(x, y):
    if blue_hat_guy.isvisible() and blue_hat_guy.distance(x, y) < 10:
        global starter
        pen.up()
        pen.goto(-annoying_mac/2, -(more_annoying_mac/2))
        pen.down()
        pen.clear() # Locked pairing frame boundary
        pen.write("You have chosen Blue Hat Guy!", font=("Courier", 24, "bold"))
        blue_hat_guy.hideturtle()
        partner_blue_hat_guy.goto(10, 0)
        partner_blue_hat_guy.showturtle()
        partner_blue_hat_guy.right(90)
        team.append("Blue Hat Guy")
        starter = True

def Scarmander_starter(x, y):
    global starter
    if Scarmander.isvisible() and Scarmander.distance(x, y) < 10:
        pen.up()
        pen.goto(-annoying_mac/2, -(more_annoying_mac/2))
        pen.down()
        pen.clear() # Locked pairing frame boundary
        pen.write("You have chosen Scarmander!", font=("Courier", 24, "bold"))
        Scarmander.hideturtle()
        partner_Scarmander.showturtle()
        partner_Scarmander.right(90)
        team.append("Scarmander")
        starter = True

def Bulbabore_starter(x, y):
    global starter
    if Bulbabore.isvisible() and Bulbabore.distance(x, y) < 10:
        pen.up()
        pen.goto(-annoying_mac/2, -(more_annoying_mac/2))
        pen.down()
        pen.clear() # Locked pairing frame boundary
        pen.write("You have chosen Bulbabore!", font=("Courier", 24, "bold"))
        Bulbabore.hideturtle()
        partner_Bulbabore.showturtle()
        partner_Bulbabore.right(90)
        team.append("Bulbabore")
        starter = True

def partner(x, y):
    blue_hat_guy_starter(x, y)
    Scarmander_starter(x, y)
    Bulbabore_starter(x, y)

pen.up()
pen.goto(-annoying_mac/2, -(more_annoying_mac/2))
pen.down()
pen.clear() # Locked pairing frame boundary
pen.write("You walk up the steps to Professor Broke's lab.", font=("Courier", 24))

def trigger_brokes_intro():
    pen.clear() # Locked pairing frame boundary
    pen.write("Hello, Professor Broke! The Professor is waiting for you. Move to the door with the Tokimon.(Use e to open the door.)", font=("Courier", 24))

screen.ontimer(trigger_brokes_intro, 10000)
screen.listen()
screen.onkey(player_right, "d")
screen.onkey(player_left, "a")
screen.onkey(player_forward, "w")
screen.onkey(player_backward, "s")
screen.onkey(check_door_collision, "e")
screen.onclick(partner)

###Part two: Tokimon Index Templates###
Tokimon_stats = {
    "Tikachu": {"HP": 99, "Attack": 99, "Defense": 99, "Speed": 99, "Special": 99},
    "Bulbabore": {"HP": 100, "Attack": 22, "Defense": 60, "Speed": 45, "Special": 120, "Weight": 90, "Move 1": "Hypnosis", "Move 2": "Confusion", "Move 3": "Life Leaf", "base_level": 5, "Type 1": "Grass", "Type 2": "Psychic"},
    "Scarmander": {"HP": 60, "Attack": 90, "Defense": 40, "Speed": 100, "Special": 10, "Weight": 65, "Move 1": "Take Down", "Move 2": "Fire Blitz", "Move 3": "Close Combat", "base_level": 5, "Type 1": "Fire", "Type 2": "Fighting"},
    "Blue Hat Guy": {"HP": 75, "Attack": 75, "Defense": 75, "Speed": 75, "Special": 75, "Weight": 55, "Move 1": "Hat Throw", "Move 2": "Aqua Ring", "Move 3": "Surf", "base_level": 5, "Type 1": "Water", "Type 2": "_"},
    "Green": {"HP": 102, "Attack": 67, "Defense": 41, "Speed": 58, "Special": 63, "Weight": 60, "Move 1": "Hop", "Move 2": "Tackle", "Move 3": "Flail", "base_level": 5, "Type 1": "_", "Type 2": "_"},
    "Digetey": {"HP": 90, "Attack": 40, "Defense": 40, "Speed": 90, "Special": 50, "Weight": 50, "Move 1": "AR", "Move 2": "Fly", "Move 3": "Taunt", "base_level": 7, "Type 1": "Flying", "Type 2": "Normal"},
    "Digetotto": {"HP": 110, "Attack": 60, "Defense": 60, "Speed": 110, "Special": 90, "Weight": 10, "Move 1": "AR", "Move 2": "Fly", "Move 3": "Taunt", "Move 4": "Gust", "base_level": 18,  "Type 1": "Flying", "Type 2": "Normal"},
    "Digetoet": {"HP": 130, "Attack": 80, "Defense": 80, "Speed": 130, "Special": 120, "Weight": 5, "Move 1": "Huricane", "Move 2": "Fly", "Move 3": "Power Outage", "Move 4": "Gust", "base_level": 27, "Type 1": "Flying", "Type 2": "Normal"},
    "Ratattle": {"HP": 150, "Attack": 120, "Defense": 20, "Speed": 91, "Special": 5, "Weight": 45, "Move 1": "Bite", "Move 2": "Thief", "Move 3": "Trip Rope", "base_level": 7, "Type 1": "Dark", "Type 2": "Normal"},
    "Ratamate": {"HP": 200, "Attack": 150, "Defense": 60, "Speed": 85, "Special": 0, "Weight": 20, "Move 1": "Bite", "Move 2": "Thief", "Move 3": "Trip Rope", "Move 4": "Lick", "base_level": 22, "Type 1": "Dark", "Type 2": "_"},
    "ytmoaW": {"HP": 90, "Attack": 90, "Defense": 90, "Speed": 90, "Special": 90, "Weight": 45, "Move 1": "Go Mad", "Move 2": "Scary Face", "Move 3": "Rage Bait", "base_level": 25, "Type 1": "Normal", "Type 2": "_"},
    "Onieyx": {"HP": 100, "Attack": 150, "Defense": 200, "Speed": 30, "Special": 40, "Weight": 100, "Move 1": "Earthquake", "Move 2": "Bind", "Move 3": "All-out", "base_level": 20, "Type 1": "Rock", "Type 2": "Ground"},
    "Glooper": {"HP": 200, "Attack": -200, "Defense": -200, "Speed": 0, "Special": -50, "Weight": 10000000000000000000000000000000, "Move 1": "Stronger!", "Move 2": "It's Doey the Doughman it's squishy it slimey it's gloopy it's- let's all destroy it with a chainsaw and a refrigerator!", "Move 3": "Stick Stuck", "base_level": 15, "Type 1": "Poison", "Type 2": "Ground"},
    "Pigpen": {"Team 1": "Glooper", "Team 2": "Onieyx"},
    "Voltooga(Idle)": {"HP": 300, "Attack": 100, "Defense": 100, "Speed": 40, "Special": 50, "Weight": 740912387429, "Move 1": "Shell Shock", "Move 2": "Wave Crash", "Move 3": "Rest", "base_level": 50, "Type 1": "Water", "Type 2": "Rock"},
    "Magtar": {"HP": 180, "Attack": 180, "Defense": 50, "Speed": 40, "Special": 180, "Weight": 10, "Move 1": "Tar War", "Move 2": "Lava Sprout", "Move 3": "Explosion", "Type 1": "Fire", "Type 2": "_", "base_level": 180},
    "Slimer": {"HP": 50, "Attack": 10, "Defense": math.inf, "Speed": 0, "Special": 10, "Weight": 0, "Move 1": "Stick Stuck", "Move 2": "Rest", "Move 3": "Trip Rope", "Type 1": "Poison", "Type 2": "_", "base_level": 50},
    "Fuk": {"HP": 200, "Attack": 1000, "Defense": math.inf, "Speed": 0, "Special": 10, "Weight": 100, "Move 1": "Stick Stuck", "Move 2": "Rest", "Move 3": "Trip Rope", "Type 1": "Poison", "Type 2": "_", "base_level": 6741},
    "Tichu": {"HP": 50, "Attack": 5, "Defense": 50, "Speed": 300, "Special": 50, "Weight": 30, "Move 1": "Stick Stuck", "Move 2": "Rest", "Move 3": "Trip Rope", "Type 1": "Poison", "Type 2": "_", "base_level": 30},
    "Motom": {"HP": 80, "Attack": 100, "Defense": 70, "Speed": 90, "Special": 10, "Weight": -10, "Move 1": "Taunt", "Move 2": "Lick", "Move 3": "Lightning", "Type 1": "Eletric", "Type 2": "Ghost", "base_level": 373},
    "Chrap": {"HP": 80, "Attack": 200, "Defense": 70, "Speed": 200, "Special": 10, "Weight": 5, "Move 1": "Lava Sprout", "Move 2": "Plate Smash", "Move 3": "Explosion", "Type 1": "Fire", "Type 2": "Dark", "base_level": 200},
    "Poligirl": {"HP": 50, "Attack": 60, "Defense": 70, "Speed": 80, "Special": 90, "Weight": 100, "Move 1": "Taunt", "Move 2": "Earthquake", "Move 3": "Rest", "Type 1": "Water", "Type 2": "_", "base_level": 5409},
    "Polirode": {"HP": 50, "Attack": 60, "Defense": 70, "Speed": 80, "Special": 90, "Weight": 100, "Move 1": "Taunt", "Move 2": "Earthquake", "Move 3": "Rest", "Type 1": "Water", "Type 2": "_", "base_level": 5409},
    "Napsols": {"HP": 300, "Attack": 20, "Defense": 150, "Speed": 0, "Special": 100, "Weight": 150, "Move 1": "Lightning", "Move 2": "Rest", "Move 3": "Power Outage", "Type 1": "Eletric", "Type 2": "Flying", "base_level": 100}
}

pen.clear() # Locked pairing frame boundary
pen.write("Professor Broke says: \"Here is your Tokimon index: press - to open it, and...\"")

def Tokidex():
    if Tokimon == "Tikachu":
        pen.clear() # Locked pairing frame boundary
        pen.write("Tokimon number 001 the awesomeness Tokimon, but I think he's about as great as cow plops.", font=("Courier", 24, "bold"))
        
        def render_tikachu_stats():
            pen.clear() # Locked pairing frame boundary
            pen.write(str(Tokimon_stats["Tikachu"]), font=("Courier", 24, "bold"))
            screen.ontimer(lambda: pen.clear(), 3000)
            
        screen.ontimer(render_tikachu_stats, 5000)
    
    elif Tokimon == "Digetey":
        AR = random.randint(1, 5)
        if AR == 1:
            pen.clear() # Locked pairing frame boundary
            pen.write("Tokimon number 011 This Tokimon once caused a huge pandemic involving people falling off cliffs and bridges because they aparently wanted to catch a lengendary in a game called \"Tokimon Go\"", font=("Courier", 16, "bold"))
        elif AR == 2:
            pen.clear() # Locked pairing frame boundary
            pen.write("Tokimon number 011 This Tokimon is incredibly dangerous do not be fooled by it's weak pigeon apearence. It *kills* it's foes by tricking them with VR and AR.", font=("Courier", 16, "bold"))
        elif AR == 3:
            pen.clear() # Locked pairing frame boundary
            pen.write("Tokimon number 011 This Tokimon was only stuffed in Route 1 because of a cranky old 80 year old man who hated tech so he did not get tricked.", font=("Courier", 16, "bold"))
        elif AR == 4:
            pen.clear() # Locked pairing frame boundary
            pen.write("Tokimon number 011 This Tokimon is SO common it sometimes, in some places apears more than 6 billion times in a single square mile", font=("Courier", 16, "bold"))
        else:
            pen.clear() # Locked pairing frame boundary
            pen.write("AR and VR are it's special tricks, due to it's small body and weak wings.", font=("Courier", 16, "bold"))
            
    elif Tokimon == "Ratattle":
        pen.clear() # Locked pairing frame boundary
        pen.write("Tokimon number 014 This Tokimon once caused a plauge one way to describe the actions taken is \"Ashes Ashes We all Die Down!\"This Tokimon steals lunch from STUUUUUUUUUUUUUUUUUUUUUPID Players.", font=("Courier", 16, "bold"))
    elif Tokimon == "Ratamate":
        battle_text("No. 15 This Tokimon eats more during mating season... that proably has something to do with the fact that plauge and flu and power outages happen more in mating season.")    
    elif Tokimon == "ytmoaW":
        torture = random.randint(1, 3)
        if torture == 1:
            battle_text("Tokimon No. 016 This Tokimon is hanged by 1 foot.")
        if torture == 2:
            battle_text("Tikachu's favorite victim.")
        if torture == 3:
            battle_text("This is a good guy... but it was driven MAD.")
    elif Tokimon == "Glooper":
        pen.clear() # Locked pairing frame boundary
        pen.write("Tokimon number 18 It is really STUUUUUUUUUPID in competetive play!", font=("Courier", 16, "bold"))        
    elif Tokimon == "Onieyx":
        pen.clear() # Locked pairing frame boundary
        pen.write("Tokimon number 19. It is made of pure rock and soul making it quite absorbent", font=("Courier", 16, "bold"))
    elif Tokimon == "Voltooga(Idle)":
        shell = random.randint(1, 2)
        if shell == 1:
            pen.clear() # Locked pairing frame boundary
            pen.write("If you fail to catch it, you are really STUUUUUUUUUPID!", font=("Courier", 24, "bold"))
        if shell == 2:
            pen.clear() # Locked pairing frame boundary
            pen.write("No. 20 It is a volcano... but it's a turtle... but it's a legendary Tokimon... but nobody has actually encountered it since the last recording from 36 BC.")
    elif Tokimon == "Magtar":
        battle_text('No 21! NO> @!! HOT! IT GOES UP TO 180 DEGREES! !*) DEGREESES!')
    elif Tokimon == "Fuk":
        battle_text("No. 23 The name was made so everyone could swear without any liabilltys yay now I can say in the name of Fuk!")
    elif Tokimon == "Slimer":
        battle_text("No. 22 EWW it was put on a scale of one to ten based on reports and it scored 9.5 right under the corspe flower.") 
    elif Tokimon == "Tichu":
        battle_text(" This is Tokimon No. uhhh WHAT YOU JUST... that's a undiscovered Tokimon!")           
    elif Tokimon == "Motom":
        battle_text("No: 24 This possesses things- that's how I got created... wait you didn't forget I am the sassy Tokidex?")
        time.sleep(4)
        process_whiteout()
    elif Tokimon == "Chrap":
        battle_text("No 25: We're not in Singapore for g***** s***")    
    elif Tokimon == "Polirode" or Tokimon == "Poligirl":
        battle_text("No: 26 and 27: These are gender counterparts of each other, the male(Polirode) is rode, while the girl(Poligirl) takes a break.")    
    elif Tokimon == "Scaresow":
        battle_text("No. 29: This Tokimon destroyed 13 victims in 13 days every 13 months for 13 years where the 13th year ended on a Friday.")
    elif Tokimon == "Hotomb":
        battle_text("No. 31: It's a bomb similar to Motom PERIOD.")        
    elif Tokimon == "Napsols":
        battle_text('No. 32:SLEEPY ELETRIC BIRD.')    

def Tokirap():
    global Angry_Tikachu
    pen.up()
    pen.goto(-annoying_mac/2, -(more_annoying_mac/2))
    pen.down()
    pen.clear()
    pen.write("You're probably very tired...", font=("Courier", 24, "bold"))

    def slide_two_tokirap():
        pen.clear()
        pen.write(
            "Professor Broke says: \"Let's sing some songs to relive you... "
            "Tikachu, Bulbabore, Scarmander, and Blue Hat Guy! "
            "That's it for the Tokirap! My lord that's short!\"",
            font=("Courier", 24, "bold")
        )

    screen.ontimer(slide_two_tokirap, 1500)
    Angry_Tikachu = True
    First_Tokimon_Battle()

def Tikachu_apearance():
    global starter, Tokimon
    if starter == False:
        pen.up()
        pen.goto(-annoying_mac/2, -(more_annoying_mac/2))
        pen.down()
        pen.clear() # Locked pairing frame boundary
        pen.write("You need to get a starter otherwise YOU'LL NEVER become a Tokimon Master! , says Professor Broke",font=("Courier", 24, "bold"))
        screen.ontimer(Tikachu_apearance, 5000)
    else:    
        Tikachu.goto(0, 50)
        Tikachu.showturtle()
        pen.up()
        pen.goto(-annoying_mac/2, -(more_annoying_mac/2))
        pen.down()
        pen.clear() # Locked pairing frame boundary
        pen.write("You should have chose me...", font=("Courier", 24, "bold"))
        Tokimon = "Tikachu"
        screen.ontimer(Tokirap, 3000)
if Defeating_Green == False:
    Tikachu_apearance()        

###Part three: Our First Tokimon Battle!###
def First_Tokimon_Battle():
    if Angry_Tikachu == True:
        def trigger_tikachu_battle_dialogue():
            pen.clear() # Locked pairing frame boundary
            pen.write("Tikachu shouts, \"I AM THE BEST! YOU DON'T CHOOSE ME? WELL GET DESTROYED!\"", font=("Courier", 24, "bold"))
        screen.ontimer(trigger_tikachu_battle_dialogue, 3000)
        screen.ontimer(Tikachu_Green, 6000)

def Tikachu_Green():
    pen.clear() # Locked pairing frame boundary
    pen.write("Tikachu sent out Green The Tokimon Trainer!", font=("Courier", 24, "bold"))
    screen.ontimer(Tokimon_battle, 3000)

def check_green_defeat():
    global Defeating_Green, Tokimon, Tokicubes, player_taunted, enemy_immune, enemy_flying, enemy_ar_active, player_flinched, green_status, player_immune, player_flying
    if Defeating_Green == True:
        battle_text("Tikachu said \"I'll... jetpack!\"")
        Tokimon = "MissingNo" 
        player_taunted = False
        enemy_immune = False
        enemy_flying = False
        player_immune = False
        player_flying = False
        enemy_ar_active = False
        player_flinched = False
        green_status = "Normal"
        
        screen.ontimer(lambda: battle_text("Professor Broke says: \"Uhhh that was not what I expected to be your first Tokimon Battle...\""), 3000)
        screen.ontimer(lambda: battle_text("Neverless, you did well!"), 6000)
        screen.ontimer(lambda: battle_text("So good that I'll have you catch some Tokimon for my research!"), 9000)
        screen.ontimer(lambda: battle_text("You can go out and explore the world!... But first prove you're ready to catch the route 1 Tokimon BEFORE you go crazy."), 12000)
        screen.ontimer(lambda: battle_text("Now although there many Tokimon even in Route 1 I want you to find Ratattle and Digitey first!"), 15000)
        screen.ontimer(lambda: battle_text("Good luck! Here are your Tokicubes! You recieved some Tokicubes!"), 18000)
        
        def award_cubes():
            global Tokicubes
            Tokicubes = 10 
            battle_text(f"Come on get moving I already gave you {Tokicubes} Tokicubes! YEET!\n\n(Walk up to the top door and press 'e' to head out!)")
            screen.onkey(Tokidex, "-")
            
        screen.ontimer(award_cubes, 21000)

### PART FOUR: DAMAGE & ATTACK LOGIC SYSTEM ###




def check_Voltooga():
    if player.distance(Voltoogaidle) < 150:
        process_whiteout()
        return True
    return False

def crazyturtle():
    global voltooga_alive

    if current_map != "Island":
        return

    if check_Voltooga():
        return

    Voltoogaidle.left(random.randint(-40, 40))

    # move a little, then check again
    Voltoogaidle.forward(10)

    if check_Voltooga():
        return

    # repeat soon
    screen.ontimer(crazyturtle, 50)

def Amazed():
    #####Part 5: Is That Supposed To Be A Charlie Brown Reference?#####
    global gym, enemy, Tokimon, gym_battle, gym_battle_finale
    battle_text("I think you're ready...")
    screen.ontimer(lambda: battle_text("...To battle a gym leader!"), 3000)    
    screen.ontimer(lambda: battle_text("how to take advantage of..."), 4000)
    screen.ontimer(lambda: battle_text("You saw nothing! press \"l\""), 5000)
    gym = True
    def secret_room(): 
        global current_map
        current_map = "Gym"
        map_drawer.clear()
        build_room(map_drawer, -100, -100, 200, 200, "#e2d5d7", "red")
        if current_map == "Gym":
            screen.ontimer(lambda: battle_text("Professor Broke says: \"I have a need for... Digetey!\""), 1000)
            screen.ontimer(lambda: battle_text("He's a bit of a... thing um you see... HE MIGHT KNOW WHERE IS THAT G******* Tikachu is!"), 3000)
            screen.ontimer(lambda: battle_text("But first gym battle against Pigpen the ground type specilist!"), 5000)
            enemy = "Onieyx"
            Tokimon_battle()
            gym_battle = True
            enemy = "Glooper"
            Tokimon_battle()
            gym_battle_finale = True
            screen.ontimer(lambda: battle_text("HMMM... very intresting... I think you are ready for an upgraded Tokidex or as I like to say DOWNGRADED!"), 3000)
            screen.ontimer(lambda: Get_a_sassy_Tokidex(), 6000)
    screen.onkey(secret_room, "l")
def Hot_Balloon():
    global current_map
    current_map = "Team Socket Landing"
    battle_text("Score! Now you can impress... WHAT THE HECK!?")
    Team_Socket = turtle.Turtle()
    Team_Socket.shape("circle")
    Team_Socket.color("yellow")
    Team_Socket.hideturtle()
    Team_Socket.goto(0, 0)
    screen.ontimer(Team_Socket.showturtle, 3000)
    screen.ontimer(lambda: battle_text("What is that..."), 6000)
    screen.ontimer(lambda: battle_text("Prepare for trouble..."), 9000)
    screen.ontimer(lambda: battle_text("Uh Cathy the toilet is overflowing!"), 12000)
    screen.ontimer(lambda: battle_text("UGH SHUT UP BOB!"), 15000)
    screen.ontimer(lambda: battle_text("Just give us a shiny, trainer."), 18000)
    screen.ontimer(lambda: battle_text("We don't need a shiny, Bob we just need your..."), 21000)
    screen.ontimer(lambda: battle_text("Digetey AND Ratattle!"), 24000)
    def PREPARE_FOR_TROUBLE():
        global Tokimon, enemy
        enemy = "ytmoaW"
        Tokimon = "ytmoaW"
        Tokimon_battle()
    screen.ontimer(PREPARE_FOR_TROUBLE, 27000)    

def evolve(base_form, evolution):
    Tokimon_stats[base_form].clear()
    Tokimon_stats[base_form].update(evolution)
def display_menu(t):
    global enemy, Tokicubes, slot_1_item, berry
    berry = 0
    if party_items[0] == "berry":
        slot_1_item = True
        berry = 1
    move1 = Tokimon_stats[t].get("Move 1", "Tackle")
    move2 = Tokimon_stats[t].get("Move 2", "Tackle")
    move3 = Tokimon_stats[t].get("Move 3", "Tackle")
    if slot_1_item == True and berry > 0:
        if Tokimon_stats[team[0]]["HP"] <= Tokimon_stats[team[0]]["HP"]/2:
            Tokimon_stats[team[0]]["HP"] += 10
            berry -= 1
            battle_text("That berry boosted him right up I guess you aren't stupid!")
    status_display = f" [{green_status}]" if green_status != "Normal" else ""
    if arena == "sticky":
        if Tokimon_stats[t]["Type 1"] == "Flying" or Tokimon_stats[t]["Type 2"] == "Flying":
            battle_text(f"{t} wasn't affected by the sticky ground!")
        else:
            Tokimon_stats[t]["Speed"] -= 50
            battle_text(f"The ground got stickier!")
    
    if player_flying:
        move_name = "Fly_Desend"

    cube_prompt = f" | c: Throw Cube ({Tokicubes})" if enemy != "Green" else ""
    battle_text(f"Fighter: {t} | HP: {Tokimon_stats[t]['HP']} | {enemy} HP: {Tokimon_stats[enemy]['HP']}{status_display}\nWhich move would you like to use?\n8: {move1} | 9: {move2} | 0: {move3}{cube_prompt}")

def throw_tokicube():
    global Tokicubes, enemy, team, current_map, player_taunted, enemy_immune, enemy_flying, enemy_ar_active, player_flinched, Tokimon, green_status, player_immune, player_flying, gym_battle, box, Reasearch_1
    if enemy == "Green" or gym_battle == True:
        battle_text("You cannot trap another trainer's Tokimon!")
        screen.ontimer(lambda: display_menu(team[active_slot]), 1500)
        return
    if Tokicubes <= 0:
        battle_text("Out of Tokicubes! Go get more from Broke!")
        screen.ontimer(lambda: display_menu(team[active_slot]), 1500)
        return
    if enemy == "ytmoaW" or enemy == "Voltooga(Idle)":
        battle_text("One leap of fate... one cower throw... and you realize the creator's dumb... because you actually caught it!")
        Tokicubes -= 1
        if len(team) >= 6:
            pen.clear() # Locked pairing frame boundary
            pen.write(f"Your team is full! {enemy} was sent to your storage box!", font=("Courier", 16, "bold"))     
            box.append(enemy)
        else:
            team.append(enemy)
        if enemy == "ytmoaW":
            Tokimon_stats["ytmoaW"]["HP"] = 90
        elif enemy == "Voltooga(Idle)":
            ##### Part 5: You know how rare a Hot Spring is?#####
            Tokimon_stats["Voltooga(Idle)"]["HP"] = 300
            battle_text("Na Na Na Boo Boo I'm flying away from my volcano on a JETPACK!")
            screen.ontimer(lambda: battle_text("Well since you're here, how about you find a hot spring?"), 3000)
            screen.ontimer(lambda: battle_text("I'll give you TM Dig or TM 52 as bossy Giovanni says."), 6000)
            tm.append("Dig")
            current_tm = "Dig"
        if enemy == "ytmoaW":
            battle_text("GOTCHA!\n\nWild ytmoaW was permanently appended to your squad!")
            Amazed()        

        return
        
    Tokicubes -= 1
    current_target_hp = Tokimon_stats[enemy]["HP"]
    if green_status == "Sleep":
        battle_text(f"Wild {enemy} is asleep! Tokicube is more effective!")
        catch_chance = max(18, 120 - current_target_hp)
    else:
        catch_chance = max(15, 100 - current_target_hp)

    if random.randint(1, 100) <= catch_chance:
        battle_text(f"GOTCHA!\n\nWild {enemy} was permanently appended to your squad!")
        if enemy == "Ratattle":
            Tokimon_stats["Ratattle"]["HP"] = 150
        elif enemy == "Digetey":
            Tokimon_stats["Digetey"]["HP"] = 90
        if len(team) < 6:
            team.append(enemy)
        else:
            pen.clear() # Locked pairing frame boundary
            pen.write(f"Your team is full! {enemy} was sent to your storage box!", font=("Courier", 16, "bold"))     
            box.append(enemy)
        if "Ratattle" in team and "Digetey" in team and not Reasearch_1:
            Reasearch_1 = True
            Hot_Balloon()
            return    
        player_taunted = False
        enemy_immune = False
        enemy_flying = False
        enemy_ar_active = False
        player_flinched = False
        green_status = "Normal"
        player_immune = False
        player_flying = False
        Tokimon = "MissingNo" 
        
        screen.onkey(player_right, "d")
        screen.onkey(player_left, "a")
        screen.onkey(player_forward, "w")
        screen.onkey(player_backward, "s")
    else:
        battle_text(f"Shoot! Wild {enemy} shredded through the cube and broke free!")
        screen.ontimer(lambda: run_green_counter(team[active_slot], enemy), 1500)

def process_whiteout():
    global current_map, enemy, enemy_immune, enemy_flying, enemy_ar_active, player_taunted, player_flinched, Tokimon, green_status
    battle_text("You blacked out... and woke up back in the Lab!\n If you are being chased by a wild Tokimon to flee!")
    
    for member in ["Bulbabore", "Scarmander", "Blue Hat Guy", "Green", "Digetey", "Ratattle"]:
        if member == "Bulbabore": Tokimon_stats[member]["HP"] = 100
        elif member == "Scarmander": Tokimon_stats[member]["HP"] = 60
        elif member == "Blue Hat Guy": Tokimon_stats[member]["HP"] = 75
        elif member == "Green": Tokimon_stats[member]["HP"] = 102
        elif member == "Digetey": Tokimon_stats[member]["HP"] = 90
        elif member == "Ratattle": Tokimon_stats[member]["HP"] = 100
        
    player_taunted = False
    enemy_immune = False
    enemy_flying = False
    enemy_ar_active = False
    player_flinched = False
    green_status = "Normal"
    Tokimon = "MissingNo" 
    
    current_map = "Lab"
    pen.clear()
    map_drawer.clear()
    
    build_room(map_drawer, lab_x, lab_y, lab_width, lab_height, "#dcdcdc", "black")
    map_drawer.goto(door_x, door_y)
    map_drawer.color("black", "#8b4513")
    map_drawer.down()
    map_drawer.begin_fill()
    for _ in range(2):
        map_drawer.forward(door_width)
        map_drawer.left(90)
        map_drawer.forward(door_height)
        map_drawer.left(90)
    map_drawer.end_fill()
    map_drawer.up()
    
    player.goto(0, 0)
    
    screen.onkey(player_right, "d")
    screen.onkey(player_left, "a")
    screen.onkey(player_forward, "w")
    screen.onkey(player_backward, "s")

def run_green_counter(t, g):
    global turn1, green_status, Defeating_Green, enemy, player_taunted, party_items, active_slot, enemy_immune, enemy_flying, enemy_ar_active, player_flinched, Tokimon, level_up, Scary, arena
    if Tokimon_stats[g]["HP"] <= 0:
        player_taunted = False
        enemy_immune = False
        enemy_flying = False
        enemy_ar_active = False
        player_flinched = False
        player_immune = False
        player_flying = False
        green_status = "Normal"
        Tokimon = "MissingNo" 
        if name == "Charlie" or name == "Ash":
            creddits()
            return
        if g == "Green":
            battle_text("Green -Died-!")    
        elif gym_battle == True and gym_battle_finale == True:
            battle_text("You defeated the gym leader! That was a close one!")
            level_up = (Tokimon_stats[t]["base_level"]/Tokimon_stats[g]["base_level"]) * 100
            Tokimon_stats[t]["base_level"] += level_up/1000
            battle_text(f"{t} leveled up! Gained {level_up} experience points.")
            if "Digetey" in team and Tokimon_stats["Digetey"]["base_level"] >= 18:
                battle_text(f"Digetey evolved into Digetotto!")
                evolve(["Digetey"], ["Digetotto"])
            if "Digetotto" in team and Tokimon_stats["Digetotto"]["base_level"] >= 30:
                battle_text(f"Digetotto evolved into Digetoet!")
                evolve(["Digetotto"], ["Digetoet"])    
            if "Ratattle" in team and Tokimon_stats["Ratattle"]["base_level"] >= 22:
                battle_text(f"Ratattle evolved into Ratattle!")
                evolve(["Ratattle"], ["Ratamate"])
            if "Ratattle" in team and "Digetey" in team:
                Reasearch_1 = True  
                Hot_Balloon()  
                return      
            arena = "_"           
        elif g == "ytmoaW":
            battle_text("You defeated Team Socket!")  
            Scary = 0  
            rage_baited = False
            baited = False
            impression = True
            if impression == True:
                Amazed()
        else:
            battle_text(f"Wild {g} fainted! You win!")
            level_up = (Tokimon_stats[t]["base_level"]/Tokimon_stats[g]["base_level"]) * 100
            Tokimon_stats[t]["base_level"] += level_up/1000
            battle_text(f"{t} leveled up! Gained {level_up} experience points.")
            if "Digetey" in team and Tokimon_stats["Digetey"]["base_level"] >= 18:
                battle_text(f"Digetey evolved into Digetotto!")
                evolve(["Digetey"], ["Digetotto"])
            if "Ratattle" in team and Tokimon_stats["Ratattle"]["base_level"] >= 22:
                battle_text(f"Ratattle evolved into Ratattle!")
                evolve(["Ratattle"], ["Ratamate"])
            if "Ratattle" in team and "Digetey" in team:
                Reasearch_1 = True  
                Hot_Balloon()
            screen.onkey(evolve, "b")    
            screen.onkey(player_right, "d")
            screen.onkey(player_left, "a")
            screen.onkey(player_forward, "w")
            screen.onkey(player_backward, "s")
        return
    elif g == "Voltooga(Idle)":
        battle_text("You big fat dummy! YOU NEED TO CATCH IT!")
        enemy = "Voltooga(Idle)"
        Tokimon = "Voltooga(Idle)"
        Tokimon_battle()
        return team
    elif g == "Napsols":
        creddits()
    
    Scary -= 1

    if green_status == "Sleep":
        if random.randint(1, 2) == 1: 
            green_status = "Normal"
            battle_text(f"{g} woke up!")
        else:
            battle_text(f"{enemy} is fast asleep...")
            screen.ontimer(lambda: display_menu(t), 1500)
            return 
            
    if green_status == "Confused":
        if random.randint(1, 10) in {1, 2, 3}:
            damage = int(20 * (Tokimon_stats[g]["Attack"] / Tokimon_stats[g]["Defense"]))
            Tokimon_stats[g]["HP"] -= damage
            battle_text(f"{g} is confused and hurt itself!\nDealt {damage} damage to itself!")
            
            if Tokimon_stats[g]["HP"] <= 0:
                player_taunted = False
                enemy_immune = False
                enemy_flying = False
                enemy_ar_active = False
                player_flinched = False
                green_status = "Normal"
                Tokimon = "MissingNo"
                if g == "Green":
                    Defeating_Green = True
                    screen.ontimer(check_green_defeat, 1500)
                elif gym_battle == True and gym_battle_finale == True:
                    battle_text("You defeated the gym leader! That was a close one!")
                    level_up = (Tokimon_stats[t]["base_level"]/Tokimon_stats[g]["base_level"]) * 100
                    Tokimon_stats[t]["base_level"] += level_up/1000
                    battle_text(f"{t} leveled up! Gained {level_up} experience points.")
                    if "Digetey" in team and Tokimon_stats["Digetey"]["base_level"] >= 18:
                        battle_text(f"Digetey evolved into Digetotto!")
                        evolve(["Digetey"], ["Digetotto"])
                    if "Digetotto" in team and Tokimon_stats["Digetotto"]["base_level"] >= 30:
                        battle_text(f"Digetotto evolved into Digetoet!")
                        evolve(["Digetotto"], ["Digetoet"])    
                    if "Ratattle" in team and Tokimon_stats["Ratattle"]["base_level"] >= 22:
                        battle_text(f"Ratattle evolved into Ratattle!")
                        evolve(["Ratattle"], ["Ratamate"])
                    if "Ratattle" in team and "Digetey" in team:
                        Reasearch_1 = True  
                        Hot_Balloon()    
                else:
                    screen.ontimer(lambda: battle_text(f"Wild {g} fainted! You win!"), 1500)
                    level_up = (Tokimon_stats[t]["base_level"]/Tokimon_stats[g]["base_level"]) * 100
                    Tokimon_stats[t]["base_level"] += level_up
                    battle_text(f"{t} leveled up! Gained {level_up} experience points.")
                    if "Digetey" in team and Tokimon_stats["Digetey"]["base_level"] >= 18:
                        battle_text(f"Digetey evolved into Digetotto!")
                        evolve(["Digetey"], ["Digetotto"])    
                    screen.onkey(player_right, "d")
                    screen.onkey(player_left, "a")
                    screen.onkey(player_forward, "w")
                    screen.onkey(player_backward, "s")
                    if "Ratattle" in team and Tokimon_stats["Ratattle"]["base_level"] >= 22:
                        battle_text(f"Ratattle evolved into Ratattle!")
                        evolve(["Ratattle"], ["Ratamate"])
                    if "Ratattle" in team and "Digetey" in team:
                        Reasearch_1 = True  
                        Hot_Balloon()        
            else:
                screen.ontimer(lambda: display_menu(t), 1500)
            return
        
    if green_status  == "Paralyzed":
        Tokimon_stats[g]["Speed"] -= 30
        battle_text(f"{g} is {green_status}! It is now slower!")

    # ⚔️ NESTED EXECUTOR SEPARATES ATTACK CONTEXT FLOW FROM CHRONIC BURN TICKS
    def execute_enemy_turn():
        global enemy_flying, enemy_immune, turn1, player_taunted, enemy_ar_active, player_flinched, Scary, green_status, player_immune, player_flying, rage_baited, baited, Energy_flail, arena
        if Tokimon_stats[g]["HP"] <= 0: return

        if arena == "sticky":
            if Tokimon_stats[g]["Type 1"] == "Flying" or Tokimon_stats[g]["Type 2"] == "Flying":
                battle_text(f"{enemy} wasn't affected by the sticky ground!")
            else:
                Tokimon_stats[g]["Speed"] -= 50
                battle_text("The ground got stickier!")    

        if rage_baited == True:
            battle_text(f"{g}'s rage is NEVER ending it's going to last the whole battle!")

        if enemy_flying:
            move_used = "Fly_Descend"
            enemy_flying = False
            enemy_immune = False 
        elif Energy_flail == True:
            power = 0
            Enemy_Move_Type = "_"    
            move_used = "f*** there's no Wi-Fi FOR G**** S*** This \"Pygame\" window is STUPID!"
        else:
            turn1 = random.randint(1, 3)
            move_used = Tokimon_stats[g].get(f"Move {turn1}", "Tackle")
            if move_used == "": move_used = "Tackle"

        power = 0
        is_special = False
        theft_occurred = False
        stolen_item_name = ""

        if move_used == "Tackle": 
            power = 40
            Enemy_Move_Type = "Normal"
        elif move_used == "Hop":
            power = 0
            Enemy_Move_Type = "Normal"
        elif move_used == "Flail":
            power = int((1 / max(1, Tokimon_stats[g]["HP"])) * 100)
            Enemy_Move_Type = "Normal"
        elif move_used == "Bite": 
            power = 80
            Enemy_Move_Type = "Dark"
            if g == "Ratattle":
                player_flinched = True
        elif move_used == "Fly": 
            power = 0 
            Enemy_Move_Type = "Flying"
            if g == "Digetey":
                enemy_immune = True
                enemy_flying = True
        elif move_used == "Fly_Descend":
            power = 75 
            Enemy_Move_Type = "Flying"
        elif move_used == "AR": 
            power = 0 
            is_special = True
            Enemy_Move_Type = "Psychic"
            if g == "Digetey":
                enemy_ar_active = True 
        elif move_used == "Flail":
            power = int((1 / max(1, Tokimon_stats[g]["HP"])) * 100)
            Enemy_Move_Type = "Normal"
        elif move_used == "Thief":
            power = 25
            Enemy_Move_Type = "Dark"
            if active_slot < len(party_items) and party_items[active_slot] != "None":
                stolen_item_name = party_items[active_slot]
                party_items[active_slot] = "None"
                theft_occurred = True
        elif move_used == "Trip Rope":
            target_weight = Tokimon_stats[t].get("Weight", 50)
            power = int(target_weight * 0.4)
            Enemy_Move_Type = "Dark"
        elif move_used == "Go Mad":
            power = 15
            Tokimon_stats[g]["HP"] -= 15
            Tokimon_stats[g]["Attack"] += 40
            Tokimon_stats[g]["Defense"] += 40
            Tokimon_stats[g]["Speed"]  += 40
            Tokimon_stats[g]["Special"] += 40   
            Enemy_Move_Type = "Psychic"
        elif move_used == "Scary Face":
            Tokimon_stats[t]["Speed"] -= 20
            Scary = 3   
        elif move_used == "Rage Bait":
            battle_text("ytmoaW got baited!")
            baited = True
        elif move_used == "Stronger!":
            Tokimon_stats[t]["Attack"] += 200
            Tokimon_stats[t]["Special"] += 200
            Tokimon_stats[t]["Speed"] += 200
            Tokimon_stats[t]["Defense"] += 200   
        elif move_used == "It's Doey the Doughman it's squishy it slimey it's gloopy it's- let's all destroy it with a chainsaw and a refrigerator!":
            Tokimon_stats["Glooper"]["HP"] -= Tokimon_stats["Glooper"]["Attack"] * 20/Tokimon_stats[t]["Defense"]
            power = 60    
        elif move_used == "Stick Stuck":
            arena = "sticky"    
        elif move_used == "Earthquake":
            power = 100
            Enemy_Move_Type = "Ground"
        elif move_used == "Bind":
            power = 0
            Type = "Normal"
            Enemy_Move_Type = "Rock"
            binded = 1
        elif move_used == "All-out":
            power = 150
            Tokimon_stats[g]["HP"] -= Tokimon_stats[g]["Attack"] * 50
            Enemy_Move_Type = "Ground" 
        elif move_used == "Shell Shock":
            power = 100
            Enemy_Move_Type = "Rock"
            Tokimon_stats[t]["Speed"] -= 20
        elif move_used == "Wave Crash":
            power = 150
            Enemy_Move_Type = "Water"
            Tokimon_stats[g]["HP"] -= Tokimon_stats[g]["Attack"] * 50
        elif move_used == "Rest":
            power = 0
            Enemy_Move_Type = "Psychic"
            Tokimon_stats[g]["HP"] = Tokimon_stats[g]["HP"] + 50
            green_status = "Sleep"  
        elif move_used == "Explosion":
            power = 360
            Tokimon_stats[g]["HP"] = 0
            Enemy_Move_Type = "Normal"
        elif move_used == "Lava Sprout":
            power = 180/Tokimon_stats[g]["HP"]
            Enemy_Move_Type = "Fire"
        elif move_used == "Tar War":
            power = 0
            arena = "sticky"
        elif move_used == "Lightning":
            power = 120
            Enemy_Move_Type = "Eletric"
        elif move_used == "Plate Smash":
            power = 0
            player_flinched = True    
        else:
            Enemy_Move_Type = "Normal"

        if Enemy_Move_Type == "Grass" and Tokimon_stats[t]["Type 1"] in ["Flying", "Fire"]:
            Type_matchup3 = 0.5
        elif Enemy_Move_Type == "Psychic" and Tokimon_stats[t]["Type 1"] in ["Dark"]:
            Type_matchup3 = 0    
        elif Enemy_Move_Type == "Psychic" and Tokimon_stats[t]["Type 1"] in ["Fighting"]:
            Type_matchup3 = 2        
        elif Enemy_Move_Type == "Grass" and Tokimon_stats[t]["Type 1"] in ["Water"]:
            Type_matchup3 = 2   
        elif Enemy_Move_Type == "Fire" and Tokimon_stats[t]["Type 1"] in ["Water"]:
            Type_matchup3 = 0.5
        elif Enemy_Move_Type == "Fire" and Tokimon_stats[t]["Type 1"] in ["Grass"]:
            Type_matchup3 = 2
        elif Enemy_Move_Type == "Fighting" and Tokimon_stats[t]["Type 1"] in ["Normal", "Dark"]:
            Type_matchup3 = 2
        elif Enemy_Move_Type == "Fighting" and Tokimon_stats[t]["Type 1"] in ["Flying", "Psychic"]:
            Type_matchup3 = 0.5        
        elif Enemy_Move_Type == "Water" and Tokimon_stats[t]["Type 1"] in ["Fire"]:
            Type_matchup3 = 2
        elif Enemy_Move_Type == "Flying" and Tokimon_stats[t]["Type 1"] in ["Grass", "Fighting"]:
            Type_matchup3 = 2
        elif Enemy_Move_Type == "Dark" and Tokimon_stats[t]["Type 1"] in ["Psychic"]:
            Type_matchup3 = 2
        elif Enemy_Move_Type == "Dark" and Tokimon_stats[t]["Type 1"] in ["Fighting"]:
            Type_matchup3 = 0.5
        elif Enemy_Move_Type == "Ghost" and Tokimon_stats[t]["Type 1"] in ["Psychic"]:
            Type_matchup3 = 2
        elif Enemy_Move_Type ==  "Ghost" and Tokimon_stats[t]["Type 1"] in ["Normal"]:
            Type_matchup3 = 0
        elif Enemy_Move_Type ==  "Ghost" and Tokimon_stats[t]["Type 1"] in ["Dark"]:
            Type_matchup3 = 0.5       
        elif Enemy_Move_Type == "Ground" and Tokimon_stats[t]["Type 1"] in ["Flying"]:
            Type_matchup3 = 0
        elif Enemy_Move_Type == "Ground" and Tokimon_stats[t]["Type 1"] in ["Grass", "Water", "Fire"]:
            Type_matchup3 = 0.5          
        else:
            Type_matchup3 = 1    

        if Enemy_Move_Type == "Grass" and Tokimon_stats[t]["Type 2"] in ["Flying", "Fire"]:
            Type_matchup4 = 0.5
        elif Enemy_Move_Type == "Psychic" and Tokimon_stats[t]["Type 2"] in ["Dark"]:
            Type_matchup4 = 0    
        elif Enemy_Move_Type == "Psychic" and Tokimon_stats[t]["Type 2"] in ["Fighting"]:
            Type_matchup4 = 2        
        elif Enemy_Move_Type == "Grass" and Tokimon_stats[t]["Type 2"] in ["Water"]:
            Type_matchup4 = 2   
        elif Enemy_Move_Type == "Fire" and Tokimon_stats[t]["Type 2"] in ["Water"]:
            Type_matchup4 = 0.5
        elif Enemy_Move_Type == "Fire" and Tokimon_stats[t]["Type 2"] in ["Grass"]:
            Type_matchup4 = 2
        elif Enemy_Move_Type == "Fighting" and Tokimon_stats[t]["Type 2"] in ["Normal", "Dark"]:
            Type_matchup4 = 2
        elif Enemy_Move_Type == "Fighting" and Tokimon_stats[t]["Type 2"] in ["Flying", "Psychic"]:
            Type_matchup4 = 0.5        
        elif Enemy_Move_Type == "Water" and Tokimon_stats[t]["Type 2"] in ["Fire"]:
            Type_matchup4 = 2
        elif Enemy_Move_Type == "Flying" and Tokimon_stats[t]["Type 2"] in ["Grass", "Fighting"]:
            Type_matchup4 = 2
        elif Enemy_Move_Type == "Dark" and Tokimon_stats[t]["Type 2"] in ["Psychic"]:
            Type_matchup4 = 2
        elif Enemy_Move_Type == "Dark" and Tokimon_stats[t]["Type 2"] in ["Fighting"]:
            Type_matchup4 = 0.5
        elif Enemy_Move_Type == "Ghost" and Tokimon_stats[t]["Type 2"] in ["Psychic"]:
            Type_matchup4 = 2
        elif Enemy_Move_Type ==  "Ghost" and Tokimon_stats[t]["Type 2"] in ["Normal"]:
            Type_matchup4 = 0
        elif Enemy_Move_Type ==  "Ghost" and Tokimon_stats[t]["Type 2"] in ["Dark"]:
            Type_matchup4 = 0.5       
        else:
            Type_matchup4 = 1            

        if move_used == "Taunt":
            player_taunted = True
            battle_text(f"{g} used Taunt!\n{t} can no longer use status moves!")
        elif power > 0 or move_used == "Fly":
            if rage_baited == True:
                power = 120
            stat_used = Tokimon_stats[g]["Special"] if is_special else Tokimon_stats[g]["Attack"]
            damage = int((power * (stat_used / Tokimon_stats[t]["Defense"])) * Type_matchup3 * Type_matchup4)
            Tokimon_stats[t]["HP"] = max(0, Tokimon_stats[t]["HP"] - damage)
            
            theft_alert = f"\nRatattle violently stole your held {stolen_item_name}!" if theft_occurred else ""
            fly_alert = f"\n{g} flew high into the sky, gaining total immunity!" if move_used == "Fly" else ""
            descend_alert = f"\n{g} dove out of the clouds with a massive strike!" if move_used == "Fly_Descend" else ""
            flinch_alert = f"\n{t} cowers from the sheer pain of the bite!" if move_used == "Bite" and g == "Ratattle" else ""
            
            display_name = "Fly" if move_used == "Fly_Descend" else move_used
            battle_text(f"{g} used {display_name}!\nDealt {damage} damage to {t}!{theft_alert}{fly_alert}{descend_alert}{flinch_alert}")
                
            if Tokimon_stats[t]["HP"] <= 0:
                Tokimon_stats[t]["HP"] = 0
                screen.ontimer(lambda: battle_text(f"{t} fainted!"), 1500)
                
                squad_alive = False
                for bumbles in team:
                    if Tokimon_stats[bumbles]["HP"] > 0:
                        squad_alive = True
                        
                if squad_alive:
                    screen.ontimer(lambda: battle_text("Send out another party member! (Use keys 1-6)"), 3000)
                else:
                    screen.ontimer(process_whiteout, 3000)
                return
        elif move_used == "AR":
            ar_alert = f"\nAR Matrix initialized! Projections are blinding your sight!"
            battle_text(f"{g} flashed an AR Illusion directly into your mind!{ar_alert}")
        else:
            battle_text(f"{g} used {move_used}!")

        if Tokimon_stats[t]["HP"] > 0:
            screen.ontimer(lambda: display_menu(t), 1500)

    # 🌋 CHRONIC BURN RESOLUTION BLOCKS (1/8th max pool reduction execution)
    if green_status == "Burn":
        base_hp = 100
        if g == "Digetey": base_hp = 90
        elif g == "Ratattle": base_hp = 100
        elif g == "Green": base_hp = 102
        elif g == "Ratamate": base_hp = 200
        elif g == "Digetotto": base_hp = 110
        burn_damage = max(1, int(base_hp / 8))
        Tokimon_stats[g]["HP"] = max(0, Tokimon_stats[g]["HP"] - burn_damage)
        battle_text(f"{g} is hurt by its burn!\nDealt {burn_damage} burn damage!")
        
        if Tokimon_stats[g]["HP"] <= 0:
            player_taunted = False
            enemy_immune = False
            enemy_flying = False
            enemy_ar_active = False
            player_flinched = False
            green_status = "Normal"
            Tokimon = "MissingNo"
            if g == "Green":
                Defeating_Green = True
                screen.ontimer(check_green_defeat, 1500)
            else:
                screen.ontimer(lambda: battle_text(f"Wild {g} fainted! You win!"), 1500)
                screen.onkey(player_right, "d")
                screen.onkey(player_left, "a")
                screen.onkey(player_forward, "w")
                screen.onkey(player_backward, "s")
            return
        else:
            screen.ontimer(execute_enemy_turn, 1500)
    else:
        execute_enemy_turn()

def use_player_move(move_key):
    global Type, active_slot, green_status, Defeating_Green, enemy, player_taunted, enemy_immune, enemy_ar_active, player_flinched, Tokimon, rage_baited, player_immune, player_flying, gym_battle, gym_battle_finale, Energy_flail, arena
    if active_slot >= len(team): return
    
    t = team[active_slot]
    g = enemy
    
    if Tokimon_stats[t]["HP"] <= 0:
        battle_text(f"{t} has already fainted! Press 1-6 to choose a living fighter!")
        return
    if Tokimon_stats[g]["HP"] <= 0:
        battle_text(f"{g} is already defeated!")
        return
        
    if player_flinched:
        player_flinched = False
        battle_text(f"{t} is flinched and too scared to move!")
        screen.ontimer(lambda: run_green_counter(t, g), 1500)
        return
        
    move_name = Tokimon_stats[t][move_key]
    
    if move_name == "Take Down": 
        power = 90
        Type = "Normal"
    elif move_name == "Fire Blitz": 
        power = 120
        Type = "Fire"
    elif move_name == "Close Combat": 
        power = 120
        Type = "Fighting"
    elif move_name == "Hat Throw": 
        hat = random.randint(1, 4)
        if hat in [1, 2, 3]:
            power = 100
        else:    
            power = 50
        Type = "Normal"
    elif move_name == "Aqua Ring": 
        power = 0
        Type = "Water"
    elif move_name == "Confusion":
        power = 50
        Type = "Psychic"
    elif move_name == "Hypnosis": 
        power = 0
        Type = "Psychic"
    elif move_name == "Life Leaf": 
        power = 60
        Type = "Grass"
    elif move_name == "Surf": 
        power = 80
        Type = "Water"
    elif move_name == "Flail":
        power = int((1 / max(1, Tokimon_stats[t]["HP"])) * 100)
        Type = "Normal"
    elif move_name == "Tackle":
        power = 40
        Type = "Normal"
    elif move_name == "Hop":
        power = 0
        Type = "Normal"            
    elif move_name == "Bite":
        power = 80
        Type = "Dark"
    elif move_name == "Thief":
        power = 60
        Type = "Dark"
    elif move_name == "AR": 
        power = 0
        Type = "Psychic" 
    elif move_name == "Fly":
        power = 0
        Type = "Flying"
        player_immune = True
        player_flying = True
    elif move_name == "Fly_Descend":
        power = 75
        Type = "Flying"
        player_immune = False
        player_flying = False    
    elif move_name == "Taunt": 
        power = 0
        Type = "Dark"
    elif move_name == "Trip Rope":
        enemy_w = Tokimon_stats[g].get("Weight", 50)
        power = int(enemy_w * 0.4)
        Type = "Dark"
    elif move_name == "Lick":
        power = 30
        Type = "Ghost"
    elif move_name == "Gust":
        power = 60
        Type = "Flying"    
    elif move_name == "Wave Crash":
        power = 150
        Type = "Water"
    elif move_name == "Shell Shock":
        power = 100
        Type = "Rock"
        Tokimon_stats[g]["Speed"] -= 20
    elif move_name == "Rest":
        power = 0
        Type = "Psychic"
        Tokimon_stats[t]["HP"] = Tokimon_stats[t]["HP"] + 50
        green_status = "Sleep"    
    elif move_name == "Power Outage":
        power = 0
        Type = "Eletric"
        Tokimon_stats[g]["Special"] -= 20
        if Enemy_Move_Type == "Eletric":
            battle_text("Power Outage caused the opponent to run out of energy!")
            Energy_flail = True        
    elif move_name == "Huricane":
        battle_text(f"Looks like {enemy} is in for a dozey!")
        power = 110
        green_status = "Confused"
        Type = "Flying"  
    elif move_name == "Explosion":
        power = 360
        Tokimon_stats[g]["HP"] = 0
        Type = "Normal"
    elif move_name == "Lava Sprout":
        power = 180/Tokimon_stats[g]["HP"]
        Type = "Fire"
    elif move_name == "Tar War":
        power = 0
        arena = "sticky"
    elif move_name == "Lightning":
        power = 120
        Type = "Eletric"
    elif move_name == "Plate Smash":
        power = 0
        green_status = "Flinched"              
    elif move_name == "Earthquake":
        Type = "Ground"
        power = 100    
    else: 
        power = 0
        Type = "_"
        enemy = name
        Tokimon_battle()
        berry = 198459034858793475938
    if Type == "Grass" and Tokimon_stats[g]["Type 1"] in ["Flying", "Fire"]:
        Type_matchup = 0.5
    elif Type == "Psychic" and Tokimon_stats[g]["Type 1"] in ["Dark"]:
        Type_matchup = 0    
    elif Type == "Psychic" and Tokimon_stats[g]["Type 1"] in ["Fighting"]:
        Type_matchup = 2        
    elif Type == "Grass" and Tokimon_stats[g]["Type 1"] in ["Water", "Ground", "Rock"]:
        Type_matchup = 2   
    elif Type == "Fire" and Tokimon_stats[g]["Type 1"] in ["Water", "Ground", "Rock"]:
        Type_matchup = 0.5
    elif Type == "Fire" and Tokimon_stats[g]["Type 1"] in ["Grass"]:
        Type_matchup = 2
    elif Type == "Fighting" and Tokimon_stats[g]["Type 1"] in ["Normal", "Dark", "Rock"]:
        Type_matchup = 2
    elif Type == "Fighting" and Tokimon_stats[g]["Type 1"] in ["Flying", "Psychic"]:
        Type_matchup = 0.5        
    elif Type == "Water" and Tokimon_stats[g]["Type 1"] in ["Fire", "Ground", "Rock"]:
        Type_matchup = 2
    elif Type == "Flying" and Tokimon_stats[g]["Type 1"] in ["Grass", "Fighting"]:
        Type_matchup = 2
    elif Type == "Dark" and Tokimon_stats[g]["Type 1"] in ["Psychic"]:
        Type_matchup = 2
    elif Type == "Dark" and Tokimon_stats[g]["Type 1"] in ["Fighting"]:
        Type_matchup = 0.5
    elif Type == "Ghost" and Tokimon_stats[g]["Type 1"] in ["Psychic"]:
        Type_matchup = 2
    elif Type ==  "Ghost" and Tokimon_stats[g]["Type 1"] in ["Normal"]:
        Type_matchup = 0
    elif Type ==  "Ghost" and Tokimon_stats[g]["Type 1"] in ["Dark"]:
        Type_matchup = 0.5   
    elif Type == "Rock" and Tokimon_stats[g]["Type 1"] in ["Flying","Fire"]:
        Type_matchup = 2
    elif Type == "Rock" and Tokimon_stats[g]["Type 1"] in ["Ground", "Fighting", "Water"]:
        Type_matchup = 0.5        
    else:
        Type_matchup = 1    
    if Type == "Grass" and Tokimon_stats[g]["Type 2"] in ["Flying", "Fire"]:
        Type_matchup2 = 0.5
    elif Type == "Psychic" and Tokimon_stats[g]["Type 2"] in ["Dark"]:
        Type_matchup2 = 0    
    elif Type == "Psychic" and Tokimon_stats[g]["Type 2"] in ["Fighting"]:
        Type_matchup2 = 2        
    elif Type == "Grass" and Tokimon_stats[g]["Type 2"] in ["Water", "Ground", "Rock"]:
        Type_matchup2 = 2   
    elif Type == "Fire" and Tokimon_stats[g]["Type 2"] in ["Water", "Ground", "Rock"]:
        Type_matchup2 = 0.5
    elif Type == "Fire" and Tokimon_stats[g]["Type 2"] in ["Grass"]:
        Type_matchup2 = 2
    elif Type == "Fighting" and Tokimon_stats[g]["Type 2"] in ["Normal", "Dark", "Rock"]:
        Type_matchup2 = 2
    elif Type == "Fighting" and Tokimon_stats[g]["Type 2"] in ["Flying", "Psychic"]:
        Type_matchup2 = 0.5        
    elif Type == "Water" and Tokimon_stats[g]["Type 2"] in ["Fire", "Ground", "Rock"]:
        Type_matchup2 = 2
    elif Type == "Flying" and Tokimon_stats[g]["Type 2"] in ["Grass", "Fighting"]:
        Type_matchup2 = 2
    elif Type == "Dark" and Tokimon_stats[g]["Type 2"] in ["Psychic"]:
        Type_matchup2 = 2
    elif Type == "Dark" and Tokimon_stats[g]["Type 2"] in ["Fighting"]:
        Type_matchup2 = 0.5
    elif Type == "Ghost" and Tokimon_stats[g]["Type 2"] in ["Psychic"]:
        Type_matchup2 = 2
    elif Type ==  "Ghost" and Tokimon_stats[g]["Type 2"] in ["Normal"]:
        Type_matchup2 = 0
    elif Type ==  "Ghost" and Tokimon_stats[g]["Type 2"] in ["Dark"]:
        Type_matchup2 = 0.5
    elif Type == "Rock" and Tokimon_stats[g]["Type 2"] in ["Flying","Fire"]:
        Type_matchup2 = 2
    elif Type == "Rock" and Tokimon_stats[g]["Type 2"] in ["Ground", "Fighting", "Water"]:
        Type_matchup2 = 0.5           
    else:
        Type_matchup2 = 1

    if baited == True and power > 0:
        rage_baited = True
        battle_text(f"{g} fell for the bait!")                

    if player_taunted and power == 0:
        battle_text(f"{t} is taunted and can't use status moves!")
        screen.ontimer(lambda: display_menu(t), 1500)
        return

    if move_name in ["Confusion", "Life Leaf", "AR"]:
        stat_used = Tokimon_stats[t]["Special"]
        defence = "Special"
    else:
        stat_used = Tokimon_stats[t]["Attack"]
        defence = "Defense"

    damage = int((power * (stat_used / Tokimon_stats[g][defence])) * Type_matchup * Type_matchup2)
    
    hit_text = ""
    if move_name == "Hat Throw":
        if random.randint(1, 4) == 1:
            damage *= 2
            hit_text = "\nIt hit 2 times!"
            
    if move_name == "Hypnosis":
        green_status = "Sleep"
        hit_text = f"\n{g} fell asleep!"
    if move_name == "Confusion":
        green_status = "Confused"
        hit_text = f"\n{g} is confused!"
    if move_name == "Fire Blitz":
        green_status = "Burn"
        hit_text = f"\n{g} caught fire! Foe was severely burned!"
    if move_name == "Lick":
        green_status = "Paralyzed"   
        
    recoil_text = ""
    if move_name in ["Take Down", "Fire Blitz"]:
        recoil_damage = int(damage * 0.3)
        Tokimon_stats[t]["HP"] -= recoil_damage
        recoil_text = f"\n{t} took {recoil_damage} recoil damage!"
        
    Stat_Lower = ""
    if move_name == "Close Combat":
        Tokimon_stats[t]["Defense"] = max(1, Tokimon_stats[t]["Defense"] - 10)
        Tokimon_stats[t]["Special"] = max(1, Tokimon_stats[t]["Special"] - 10)
        Stat_Lower = "\nClose Combat lowered your Defense and Special!"    

    if move_name == "Aqua Ring":
        Tokimon_stats[t]["HP"] += 15
        hit_text = "\nAqua Ring restored some HP!"

    if move_name == "Life Leaf":
        Tokimon_stats[t]["HP"] += int(damage * 0.4)
        hit_text = "\nLife Leaf restored part of the damage it dealt as HP!"

    if Tokimon_stats[t]["Speed"] >= Tokimon_stats[g]["Speed"]:
        if g == "Digetey" and enemy_immune:
            battle_text(f"{t} used {move_name}!\nBut wild {g} is flying high and avoided it entirely!")
            screen.ontimer(lambda: run_green_counter(t, g), 1500)
        elif g == "Digetey" and enemy_ar_active and random.randint(1, 4) != 1:
            battle_text(f"{t} used {move_name}!\nBut you swung at a fake projection! The attack missed!")
            screen.ontimer(lambda: run_green_counter(t, g), 1500)
        else:
            if power > 0:
                Tokimon_stats[g]["HP"] = max(0, Tokimon_stats[g]["HP"] - damage)
                battle_text(f"{t} used {move_name}!{hit_text}\nDealt {damage} damage!{recoil_text}{Stat_Lower}")
            else:
                battle_text(f"{t} used {move_name}!{hit_text}")
            
            if Tokimon_stats[g]["HP"] <= 0:
                player_taunted = False
                enemy_immune = False
                enemy_ar_active = False
                player_flinched = False
                green_status = "Normal"
                Tokimon = "MissingNo"
                if g == "Green":
                    Defeating_Green = True
                    screen.ontimer(check_green_defeat, 2500)
                else:
                    screen.ontimer(lambda: battle_text(f"Wild {g} fainted! You win!"), 1500)
                    screen.onkey(player_right, "d")
                    screen.onkey(player_left, "a")
                    screen.onkey(player_forward, "w")
                    screen.onkey(player_backward, "s")
            else:
                screen.ontimer(lambda: run_green_counter(t, g), 1500)
    else:
        run_green_counter(t, g)
        
        if Tokimon_stats[t]["HP"] > 0:
            if player_flinched:
                player_flinched = False
                screen.ontimer(lambda: battle_text(f"Ratattle bit you first! {t} flinched and couldn't strike!"), 1500)
                screen.ontimer(lambda: display_menu(t), 3500)
            elif g == "Digetey" and enemy_immune:
                screen.ontimer(lambda: battle_text(f"{t} tried to use {move_name}!\nBut wild {g} easily soared over it!"), 1500)
            elif g == "Digetey" and enemy_ar_active and random.randint(1, 4) != 1:
                screen.ontimer(lambda: battle_text(f"{t} tried to use {move_name}!\nBut the AR illusion completely blinded your strike!"), 1500)
            else:
                if power > 0:
                    Tokimon_stats[g]["HP"] = max(0, Tokimon_stats[g]["HP"] - damage)
                    screen.ontimer(lambda h=hit_text, r=recoil_text, d=damage: battle_text(f"{t} used {move_name}!{h}\nDealt {d} damage!{r}{Stat_Lower}"), 1500)
                else:
                    screen.ontimer(lambda h=hit_text: battle_text(f"{t} used {move_name}!{h}"), 1500)
                    
                if Tokimon_stats[g]["HP"] <= 0:
                    player_taunted = False
                    enemy_immune = False
                    enemy_ar_active = False
                    player_flinched = False
                    green_status = "Normal"
                    Tokimon = "MissingNo"
                    if g == "Green":
                        Defeating_Green = True
                        screen.ontimer(check_green_defeat, 3500)
                    else:
                        screen.ontimer(lambda: battle_text(f"Wild {g} fainted! You win!"), 3500)
                        screen.onkey(player_right, "d")
                        screen.onkey(player_left, "a")
                        screen.onkey(player_forward, "w")
                        screen.onkey(player_backward, "s")

def use_move_1(): use_player_move("Move 1")
def use_move_2(): use_player_move("Move 2")
def use_move_3(): use_player_move("Move 3")

def Team_1():
    global turn1, active_slot, enemy
    if len(team) < 1: return
    active_slot = 0
    t = team[0]
    g = enemy
    battle_text(f"You sent out {t}!")
    
    if Tokimon_stats[t]["Speed"] >= Tokimon_stats[g]["Speed"]:
        screen.ontimer(lambda: display_menu(t), 1500)
    else:
        screen.ontimer(lambda: run_green_counter(t, g), 1500)

def Team_2():
    global turn1, active_slot, enemy
    if len(team) < 2: return
    active_slot = 1
    t = team[1]
    g = enemy
    battle_text(f"You sent out {t}!")
    
    if Tokimon_stats[t]["Speed"] >= Tokimon_stats[g]["Speed"]:
        screen.ontimer(lambda: display_menu(t), 1500)
    else:
        screen.ontimer(lambda: run_green_counter(t, g), 1500)

def Team_3():
    global turn1, active_slot, enemy
    if len(team) < 3: return
    active_slot = 2
    t = team[2]
    g = enemy
    battle_text(f"You sent out {t}!")
    
    if Tokimon_stats[t]["Speed"] >= Tokimon_stats[g]["Speed"]:
        screen.ontimer(lambda: display_menu(t), 1500)
    else:
        screen.ontimer(lambda: run_green_counter(t, g), 1500)

def Team_4():
    global turn1, active_slot, enemy
    if len(team) < 4: return
    active_slot = 3
    t = team[3]
    g = enemy
    battle_text(f"You sent out {t}!")
    
    if Tokimon_stats[t]["Speed"] >= Tokimon_stats[g]["Speed"]:
        screen.ontimer(lambda: display_menu(t), 1500)
    else:
        screen.ontimer(lambda: run_green_counter(t, g), 1500)

def Team_5():
    global turn1, active_slot, enemy
    if len(team) < 5: return
    active_slot = 4
    t = team[4]
    g = enemy
    battle_text(f"You sent out {t}!")
    
    if Tokimon_stats[t]["Speed"] >= Tokimon_stats[g]["Speed"]:
        screen.ontimer(lambda: display_menu(t), 1500)
    else:
        screen.ontimer(lambda: run_green_counter(t, g), 1500)

def Team_6():
    global turn1, active_slot, enemy
    if len(team) < 6: return
    active_slot = 5
    t = team[5]
    g = enemy
    battle_text(f"You sent out {t}!")
    
    if Tokimon_stats[t]["Speed"] >= Tokimon_stats[g]["Speed"]:
        screen.ontimer(lambda: display_menu(t), 1500)
    else:
        screen.ontimer(lambda: run_green_counter(t, g), 1500)
if Scary <= 0:
    screen.onkey(Team_1, "1")
    screen.onkey(Team_2, "2")
    screen.onkey(Team_3, "3")
    screen.onkey(Team_4, "4")
    screen.onkey(Team_5, "5")
    screen.onkey(Team_6, "6")
    screen.onkey(use_move_1, "8")
    screen.onkey(use_move_2, "9")
    screen.onkey(use_move_3, "0")
    screen.onkey(throw_tokicube, "c") 
else:
    Fright = lambda: battle_text("ERRR") 
    for key in ["1", "2", "3", "4", "5", "6"]:
        screen.onkey(Fright, key) 
     
screen.onkey(manual_save, "r")    
screen.onkey(Tokidex, "-")
def start1():
    screen.listen()
    screen.mainloop()

start1()    