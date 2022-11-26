from pico2d import *
import game_world
import game_framework
import sever

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class DOOR:
    image=None
    def __init__(self):
        if DOOR.image == None:
            DOOR.image = load_image("./resourceimg/watersprite.png")

        self.x = 250
        self.y = 500
        self.frame_x = 0
        self.frame_y = 0

    def get_bb(self):
        return self.x - 15-sever.camera_x , self.y - 30 , self.x + 15 - sever.camera_x , self.y + 30

    def update(self):
        self.frame_x = (int)(self.frame_x +1) %4

    def draw(self):
        self.image.clip_draw(50*self.frame_x,  0, 50,  50,  self.x-sever.camera_x,  self.y,  100,  100)
        draw_rectangle(*self.get_bb())

    def handle_collision (self , other , massage):
        if massage == 'slime::door':
            pass
