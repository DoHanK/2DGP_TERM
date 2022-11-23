from pico2d import *
import game_world
import game_framework
import sever


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 1

class SLIDE:
    image=None
    def __init__(self,):
        if SLIDE.image==None:
            SLIDE.image=load_image("water_slide.png")

        self.x=575
        self.y=25
        self.frame_x=0
        self.frame_y=0

    def get_bb(self):
        return self.x - 25-sever.camera_x, self.y -50, self.x + 25-sever.camera_x, self.y -51

    def update(self):


        self.frame_y=(self.frame_y +1 ) %10

    def draw(self):
        self.image.clip_draw(0,  50*self.frame_y+100, 60,  50,  self.x-sever.camera_x,  self.y, 80,  50)
        draw_rectangle(*self.get_bb())

    def handle_collision(self,other,massage):
        if massage=='slime::slide':

            pass
