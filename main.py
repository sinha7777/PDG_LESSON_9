import pgzrun
import random

HEIGHT = 600
WIDTH = 800
TITLE = ("Earth_day")

START_SPEED = 10
ITEMS = ["bag","battery","bottle","chips"]

FINAL_LEVEL = 6
current_level = 1

game_over = False #You lost

game_complete = False #You won

items = []
animations = []

def draw ():
    global items,current_level,game_complete,game_over
    screen.clear()
    screen.blit("bground",(0,0))
    if game_over :
        display_message("GAME OVER","Try again.")
    elif game_complete :
        display_message("YOU WON.","Good job.")
    else :
        for item in items :
            item.draw()

def display_message (heading,subheading):
    screen.draw.text(heading,fontsize=60,center=(400,300),color="black")
    screen.draw.text(subheading,fontsize=30,center=(400,330),color="black")

def update ():
    global items
    if len(items) == 0:
        items = make_items(current_level)

#Make items
#1.get the options from ITEMS list - random
#2.Create actors and add it to items list
#3.Layout items - display them with equal spacing
#4.Animations - move the objects down

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create (number_of_extra_items):
    items_to_create = ["paper"]
    for i in range(0,number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
        item = Actor(option + "img")
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    no_of_gaps = len(items_to_layout)+1
    gap_size = WIDTH/no_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
        new_x_pos = (index + 1) * gap_size
        item.x = new_x_pos

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration = START_SPEED - current_level
        animation=animate(item,duration=duration,on_finished=handle_game_over,y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global items
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
            else:
                handle_game_over()
def handle_game_complete():
    global current_level,items,animations,game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level += 1
        items = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()




pgzrun.go()