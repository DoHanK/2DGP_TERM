from pico2d import *
import game_world
import game_framework
import random
import server


class SUNMONSTER:

    sunpic = None
    def __init__(self, x , y):
        if SUNMONSTER.sunpic == None:
            SUNMONSTER.sunpic = load_image("./resourceimg/sunmonster.png")
        self.x = x
        self.y = y
        self.frame_x = 5
        self.time = 0
        self.camera_x = 0
        self.prepos_x = 0

    def update(self):
            self.time += game_framework.frame_time
            if self.time > 1:
                self.frame_x = random.randint(0,12)
                self.time = 0

    def draw(self):
             self.sunpic.clip_draw(self.frame_x * 50, 0, 50, 35, self.x - server.camera_x, self.y, 50, 50)
             draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20 - server.camera_x , self.y - 20 , self.x + 20 - server.camera_x , self.y + 20

    def handle_collision(self , other , massage):
         if massage == 'bullet::monster':
                 game_world.remove_object(self)

