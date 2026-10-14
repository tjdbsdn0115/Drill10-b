from pico2d import *
import random


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

class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10  # Assuming the sprite sheet has 10 frames
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height, self.x, self.y, frame_width//2, frame_height//2)

class Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
    def draw(self):
        self.image.draw(400, 400)
    def update(self):
        pass

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

    zombie = Zombie()
    world.append(zombie)

    ball = Ball()
    world.append(ball)

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
