from pico2d import *
import game_framework
import play_state
import game_world


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

image = None
button=None
drawflag=0
import os

path = "./resoureimg"
file_list = os.listdir(path)

print ("file_list: {}".format(file_list))
def enter():
    global image,button
    image = load_image('./resoureimg/gametittle.png')
    button = load_image('./resoureimg/pressbutton.png')


def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_world.clear()
            game_framework.change_state(play_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
    pass


def draw():
    global drawflag
    clear_canvas()
    image.clip_draw(0, 0, 1890,1417, 400, 300,800,600)
    if 1>drawflag>0:
        button.clip_draw(0, 0, 1890,1417, 400, 100,800,400)
    update_canvas()


def update():
    global drawflag
    drawflag+=game_framework.frame_time
    if drawflag>1:
        drawflag=-1

    pass


def pause():
    pass


def resume():
    pass