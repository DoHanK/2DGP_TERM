from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 120.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  #m/m
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0) # m/s
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class BULLET:
    bullet=None
    def __init__(self, x,y, dir):
        if BULLET.bullet==None:
            BULLET.bullet=load_image("./resoureimg/R_bullet.png")
        self.pos_y=y
        self.pos_x=x
        self.state=dir

    def update(self):
            if self.state == 1:
                 self.pos_x+=RUN_SPEED_PPS*game_framework.frame_time
            elif self.state == -1:
                 self.pos_x-=RUN_SPEED_PPS*game_framework.frame_time
            if self.pos_x < 25 or self.pos_x > 800 - 25:
                game_world.remove_object(self)

    def handle_collision(self, other, massage):
        if massage =="bullet::monster":
                game_world.remove_object(self)

        if massage =="bullet::background":
                game_world.remove_object(self)

        pass
    def get_bb(self):
        return self.pos_x -15, self.pos_y-7.5 , self.pos_x+15 ,  self.pos_y+7.5
    def draw(self):
            if self.state==1:
                self.bullet.clip_draw(0,0, 50, 35, self.pos_x, self.pos_y, 30, 15)
            elif self.state==- 1:
                  self.bullet.clip_composite_draw(0, 0, 50, 35,0,'h' ,self.pos_x, self.pos_y, 30, 15)
            draw_rectangle(*self.get_bb())