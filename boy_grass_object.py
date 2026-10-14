from pico2d import *
import random
import math


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)    
    def update(self):pass
    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        
class Ball:
    def __init__(self):
        self.x, self.y = random.randint(50,750), random.randint(100,200)
        self.speed = random.randint(1, 10)
        self.size = random.randint(21, 40)
        self.top_y = get_canvas_height() - self.size / 2 - 5
        self.floating = False
        self.bob_phase = 0.0
        self.bob_amplitude = random.randint(8, 15)
        self.bob_speed = random.uniform(0.08, 0.15)
        self. frame = random.randint(0,20)
        self.image = load_image('ball21x21.png')
    def update(self):
        self.frame = random.randint(0,10)
        if not self.floating:
            self.y = min(self.y + self.speed, self.top_y)
            if self.y >= self.top_y:
                self.floating = True
        else:
            self.bob_phase = (self.bob_phase + self.bob_speed) % math.tau
            self.y = self.top_y - self.bob_amplitude * (1 - math.cos(self.bob_phase))
    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)

def reset_world():
    global running

    # 세계에 존재하는 객체들을 담는 word list를 만든다
    global world
    world = []

    # 땅 객체를 생성하고, world list에 추가한다
    global grass
    world.append(Grass())

    # 팀을 생성하고 , world list에 추가한다
    team = [Boy() for i in range(11)]
    world += team

    ball = [Ball() for i in range(20)]
    world += ball

    running = True
    grass = Grass()

def update_world():
    grass.update()
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    grass.draw()
    for o in world:
        o.draw()
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
