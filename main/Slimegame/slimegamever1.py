from pico2d import *
import random
height=800
width=600

open_canvas(height,width)
background= load_image('backgrond.png')
'''==================================함수 정의============================='''

class SLIME:
    def __init__(self):
        self.dir_x=0
        self.dir_y=0
        self.pos_x=100
        self.pos_y=35
        self.frame_x=0
        self.frame_y=0
        self.slime_walk_pic = load_image('slimepic.png')
        self.upflag=0
        self.hp=0
    def update(self):

        if self.upflag==0: #점프인지 아닌지 확인하는 조건문
             if self.dir_x!=0:
                 self.frame_x = (self.frame_x + 1) % 13
             else:
                 self.frame_x=0
        else:
            delay(0.03) #점프 구현
            self.frame_x = (self.frame_x + 1) % 13
            if self.frame_x==7 or self.frame_x==8:
                self.pos_y += 25
            if self.frame_x == 0:
                self.upflag=0



        delay(0.05)
        self.pos_x += 8*self.dir_x

    '''  frame y  
          7    왼쪽으로 이동
          6    오른쪽으로 이동
          5    왼쪽방향보면서 점프
          4    오른쪽 방향 보면서 점프
          3    왼쪽방향 공격
          2    오른쪽 방향 공격
          1     위로 이동
          0     아래로 이동    
          '''

    def slime_handle(self):
        global running
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                 running = False
            elif event.type == SDL_KEYDOWN:
                if event.key==SDLK_RIGHT:
                    self.dir_x+=1
                    self.frame_y=6
                elif event.key==SDLK_LEFT:
                    self.dir_x-=1
                    self.frame_y =7
                elif event.key==SDLK_UP:
                    self.dir_y+=1
                    if self.frame_y%2==0:
                        self.frame_y = 4
                    else:
                        self.frame_y=5
                    self.upflag=1
                elif event.key == SDLK_ESCAPE:
                    running = False




            elif event.type == SDL_KEYUP:
                if event.key==SDLK_RIGHT:
                    self.dir_x-=1

                elif event.key==SDLK_LEFT:
                    self.dir_x+=1
                elif event.key == SDLK_UP:
                    self.dir_y -= 1

    def draw(self):
        self.slime_walk_pic.clip_draw(self.frame_x*50,self.frame_y*35,50,35,self.pos_x,self.pos_y,100,50)

class SUNMONSTER:
    def __init__(self):
        self.sunpic=load_image("sunmonster.png")
        self.pos_x=300
        self.pos_y=400
        self.frame_x=5
    def update(self):

        self.frame_x=random.randint(0,12)
    def draw(self):
        self.sunpic.clip_draw(self.frame_x*50,0,50,35,self.pos_x,self.pos_y,100,50)

# def handle_events():
#     global running
#     global slime
#     events=get_events()
#     for event in events:
#         if event.type ==SDL_QUIT:
#             running=False
#         elif event.type==SDL_KEYDOWN:
#             if event.type==SDLK_LEFT:
#                 slime.dir_x -= 1
#                 slime.frame_y = 0
#             elif event.type==SDLK_RIGHT:
#                 slime.dir_x+=1
#                 slime.frame_y=1
#




slime=SLIME()
sun=SUNMONSTER()



'''변수 선언들'''
running=True






while(running):

    clear_canvas()

    background.clip_draw(0,0,800,600,400,300)
    slime.update()
    slime.draw()
    slime.slime_handle()
    sun.update()
    sun.draw()
    update_canvas()





close_canvas()

