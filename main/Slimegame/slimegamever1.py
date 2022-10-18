import math

from pico2d import *
import random
import pdb
width=800
height=600

open_canvas(width,height)
background= load_image('backgrond.png')
'''==================================함수 정의============================='''

class item:
    def __init__(self):
        self.image=load_image("item.png")
        self.frame_x=0
        self.frame_y=0

    def update(self):
        self.frame_x=(self.frame_x+1)%4
        if(self.frame_x==0):
            self.frame_y=(self.frame_y+1)%3
    def draw(self):
        self.image.clip_draw(83*self.frame_x,85*self.frame_y,83,85,300,200,35,35)

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
#총알 객체 생성
bullets=[]
class SLIME:
    def __init__(self):
        self.dir_x=0
        self.dir_y=0
        self.pos_x=100
        self.pos_y= 35
        self.frame_x=0
        self.frame_y=0
        self.slime_walk_pic = load_image('slimepic.png')
        self.attack_effect_pic=load_image('deadsprite.png')
        self.attack_frame=0
        self.attacking=0
        self.hp=80
        self.jump_height = 16
        self.jumping=0
        self.flying=0
        self.y_velocity=self.jump_height
        self.y_gravity=2
        self.top_jump_point=0

    def update(self):
    #점프 관련 업데이트
        if self.jumping==0: #점프인지 아닌지 확인하는 조건문
             if self.dir_x!=0:
                 self.frame_x = (self.frame_x + 1) % 13
             else:
                 if self.frame_y%2==0:
                     self.frame_y = 6
                 else:
                     self.frame_y=5
                     self.frame_x= 0
        else:
                 if not self.dir_x == 0:        #점프하면서 오른쪽왼쪽으로 이동
                    if self.flying==1:
                        if self.frame_y % 2 == 0:
                            self.frame_y = 0
                        else:
                            self.frame_y = 1

                    else:
                        if self.frame_y % 2 == 0:
                             self.frame_y = 2
                        else:
                            self.frame_y = 3

                 if self.y_velocity ==self.jump_height:
                    self.top_jump_point=self.pos_y


                #점프 구현 중력 가속도

                 if(self.y_velocity>=0):
                     self.pos_y += self.y_velocity
                     self.y_velocity -= self.y_gravity
                 else:
                     if self.flying:  # flying 기능 구현
                         if(self.flying==2):
                             self.pos_y-=8
                         else:
                             self.pos_y -= 2
                     else:
                         self.pos_y += self.y_velocity
                         self.y_velocity -= self.y_gravity


              #점프하는 동시에 이동할때 이미지
                 if(self.y_velocity>self.jump_height-7): # 0에서 최고 높이까지 갈때 스프라이트 맞춰주기

                     if self.dir_x == 0:
                         self.frame_x = (self.frame_x + 1) % 7
                     else:
                         self.frame_x = (self.frame_x + 1) % 6

                 elif(self.y_velocity<self.jump_height-6) and (self.y_velocity>0): #최고높이일때
                     if self.dir_x == 0:
                         self.frame_x = 7
                     else:
                         self.frame_x = (self.frame_x + 1) % 4 + 4

                 else:  #날라가는 모션 취하기

                     if self.dir_x == 0: #점프하면서 이동하지않을때
                             self.frame_x = 0
                     else: #점프하면서 이동할때
                         if self.flying == 1:
                            self.frame_x = (self.frame_x +1)%2+7
                         else:
                            self.frame_x = (self.frame_x +1)%4+4

                 if(self.pos_y<self.top_jump_point):##y축으로의 이동속도가 점프보다 낮을때
                      self.pos_y =self.top_jump_point
                      print(self.top_jump_point)
                      print("        ")
                      print(self.pos_y)
                      self.jumping =False
                      self.y_velocity=self.jump_height
                      self.top_jump_point=0
                      if self.frame_y % 2 == 0:
                          self.frame_y = 6
                      else:
                          self.frame_y = 7
                      self.frame_x = 0
    #공격 임펙트
        if self.attacking:
           self.attack_frame= (self.attack_frame+1)%10
           if self.attack_frame==0:
               self.attacking=0


        delay(0.05)
        self.pos_x += 8*self.dir_x


        #총알 관리

        for bullet in bullets:
            if bullet.update():
                bullets.remove(bullet)
            bullet.draw()



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
                    if self.jumping:
                        self.frame_y =2
                    else:
                         self.frame_y=6


                elif event.key==SDLK_LEFT:
                    self.dir_x-=1
                    if self.jumping:
                        self.frame_y=3
                    else:
                        self.frame_y=7

                if event.key==SDLK_UP:
                    if not self.jumping:
                        self.dir_y+=1
                        if self.frame_y%2==0:
                           self.frame_y = 4
                        else:
                           self.frame_y=5
                        self.jumping = 1
                if event.key==SDLK_SPACE: ##체력 감소
                    self.attacking=1
                    self.makebullet()
                    self.hp-=1
                if event.key==SDLK_LCTRL:
                    self.flying=1
                    self.frame_x=7
                elif event.key == SDLK_ESCAPE:
                    running = False




            elif event.type == SDL_KEYUP:
                if event.key==SDLK_RIGHT:
                    self.dir_x-=1
                elif event.key==SDLK_LEFT:
                    self.dir_x+=1
                if event.key==SDLK_LCTRL:
                    self.flying=2

    def makebullet(self):
        bullets.append(BULLET())
        if(self.frame_y%2==0):
            bullets[-1].state ='right'
            bullets[-1].pos_y= self.pos_y
            bullets[-1].pos_x = self.pos_x
        else:
            bullets[-1].state = "left"
            bullets[-1].pos_y = self.pos_y
            bullets[-1].pos_x = self.pos_x

    def draw(self):
        if self.attacking:
            self.attack_effect_pic.clip_draw(self.attack_frame * 50, 0, 50, 35, self.pos_x, self.pos_y, 6 * self.hp / 5,
                                             6 * self.hp / 5)
        self.slime_walk_pic.clip_draw(self.frame_x * 50, self.frame_y * 35, 50, 35, self.pos_x, self.pos_y, 2*self.hp ,self.hp)




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






slime=SLIME()
sun=SUNMONSTER()
item=item()


'''변수 선언들'''
running=True




# SDL_IntersectRect()

while(running):

    clear_canvas()

    background.clip_draw(0,0,800,600,400,300)
    item.update()
    item.draw()
    slime.update()
    slime.draw()
    slime.slime_handle()
    sun.update()
    sun.draw()
    update_canvas()





close_canvas()

