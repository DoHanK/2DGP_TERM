from pico2d import *
import game_world



class BULLET:
    def __init__(self):
        self.l_pic=load_image("L_bullet.png")
        self.r_pic=load_image("R_bullet.png")
        self.pos_x=0
        self.pos_y=0
        self.state="right"
    def update(self):
        if self.state == "right":
           self.pos_x+=15
           if self.pos_x >width:
               return True
        elif self.state == "left":
           self.pos_x-=15
           if self.pos_x<0:
               return True

    def draw(self):
        if self.state=="right":
          self.r_pic.clip_draw(0,0, 50, 35, self.pos_x, self.pos_y, 30, 15)
        elif self.state=="left":
            self.l_pic.clip_draw(0, 0, 50, 35, self.pos_x, self.pos_y, 30, 15)