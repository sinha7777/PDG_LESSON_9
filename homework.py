import pgzrun
import random

HEIGHT = 600
WIDTH = 800
TITLE = ("Tree_Axe")

START_SPEED = 10
ITEMS = ["axe"]

FINAL_LEVEL = 6
current_level = 1

game_over = False
game_complete = False

items = []
animations = []

def draw():
    global items, current_level, game_complete, game_over
    screen.clear()
    screen.blit("bground", (0, 0))

    if game_over:
        display_message("GAME OVER", "Try again.")
    elif game_complete:
        display_message("YOU WON.", "Good job.")
    else:
        for item in items:
            item.draw()

def display_message(heading, subheading):
    screen.draw.text(heading, fontsize=60, center=(400,300), color="black")
    screen.draw.text(subheading, fontsize=30, center=(400,330), color="black")

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create = ["tree"]
    for i in range(0, number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
        item = Actor(option)
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    pass

def animate_items(items_to_animate):
    pass

pgzrun.go()