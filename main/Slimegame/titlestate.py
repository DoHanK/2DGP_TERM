from pico2d import *
import game_framework
import groundbackground
import game_world


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

image = None
button = None
draw_flag = 0
bgm = None
def enter():
    global image , button ,bgm
    image = load_image('./resourceimg/gametittle.png')
    button = load_image('./resourceimg/pressbutton.png')
    bgm = load_music('./sound/startsound.mp3')
    bgm.set_volume(32)
    bgm.repeat_play()

def exit():
    global image,bgm
    del bgm
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_world.clear()
            game_framework.change_state(groundbackground)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def draw():
    global draw_flag
    clear_canvas()
    image.clip_draw(0, 0 , 1890 , 1417 , 400 , 300 , 800 , 600)
    if 1 > draw_flag > 0:
        button.clip_draw(0 , 0 , 1890 , 1417 , 400 , 100 , 800 , 400)
    update_canvas()


def update():
    global draw_flag
    draw_flag += game_framework.frame_time
    if draw_flag > 1:
        draw_flag = -1


def pause():
    pass


def resume():
    pass