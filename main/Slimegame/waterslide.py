from pico2d import *
import game_world
import game_framework
import server


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 1

class SLIDE:

    image=None

    def __init__(self,x,y):
        if SLIDE.image == None:
            SLIDE.image = load_image("./resourceimg/water_slide.png")

        self.x = x
        self.y = y
        self.frame_x = 0
        self.frame_y = 0

    def get_bb(self):
        return self.x - 25-server.camera_x , self.y - 50 , self.x + 25 - server.camera_x , self.y - 51

    def update(self):
        self.frame_y = (self.frame_y + 1 ) % 10

    def draw(self):
        self.image.clip_draw(0, 50 * self.frame_y + 100, 60, 50, self.x - server.camera_x, self.y, 80, 50)
        draw_rectangle(*self.get_bb())

    def handle_collision(self , other , massage):
        if massage == 'slime::slide':
            pass
