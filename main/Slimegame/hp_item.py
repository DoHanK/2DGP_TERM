from pico2d import *
import game_world
import game_framework
import sever

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class ITEM:
    image=None
    def __init__(self):
        if ITEM.image==None:
            ITEM.image=load_image("item.png")

        self.x=300
        self.y=300
        self.frame_x=0
        self.frame_y=0

    def get_bb(self):
        return self.x - 15-sever.camera_x, self.y - 30, self.x + 15-sever.camera_x, self.y + 30

    def update(self):
        self.frame_x= (int)(self.frame_x + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) %4
        if(self.frame_x==0):
            self.frame_y=(self.frame_y+1)%3
    def draw(self):
        self.image.clip_draw(83*self.frame_x,  85*self.frame_y, 83,  85,  self.x-sever.camera_x,  self.y,  30,  60)
        draw_rectangle(*self.get_bb())

    def handle_collision(self,other,massage):
        if massage=='eat':
            game_world.remove_object(self)
