from pico2d import *
import game_world
import game_framework
import random


class SUNMONSTER:
    sunpic=None
    def __init__(self):
        if SUNMONSTER.sunpic==None:
            self.sunpic=load_image("sunmonster.png")
        self.x=400
        self.y=250
        self.frame_x=5
        self.time=0
        self.ableflag=1
    def update(self):
        if self.ableflag==1:
            self.time+=game_framework.frame_time
            if self.time>1:
                self.frame_x=random.randint(0,12)
                self.time=0
    def draw(self):
        if self.ableflag==1:
             self.sunpic.clip_draw(self.frame_x*50,0,50,35,self.x,self.y,50,50)
             draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self,other,massage):
         if(massage=='attack'):
             self.ableflag=0
             # game_world.remove_object(self)
