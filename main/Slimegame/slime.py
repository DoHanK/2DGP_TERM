from pico2d import *
import game_world
import game_framework


'''==================================함수 정의============================='''



# class SLIME:
#     def __init__(self):
#         self.dir_x=0
#         self.dir_y=0
#         self.pos_x=100
#         self.pos_y= 35
#         self.frame_x=0
#         self.frame_y=0
#         self.slime_walk_pic = load_image('slimepic.png')
#         self.attack_effect_pic=load_image('deadsprite.png')
#         self.attack_frame=0
#         self.attacking=0
#         self.hp=80
#         self.jump_height = 16
#         self.jumping=0
#         self.flying=0
#         self.y_velocity=self.jump_height
#         self.y_gravity=2
#         self.top_jump_point=0
#
#     def update(self):
#     #점프 관련 업데이트
#         if self.jumping==0: #점프인지 아닌지 확인하는 조건문
#              if self.dir_x!=0:
#                  self.frame_x = (self.frame_x + 1) % 13
#              else:
#                  if self.frame_y%2==0:
#                      self.frame_y = 6
#                  else:
#                      self.frame_y=5
#                      self.frame_x= 0
#         else:
#                  if not self.dir_x == 0:        #점프하면서 오른쪽왼쪽으로 이동
#                     if self.flying==1:
#                         if self.frame_y % 2 == 0:
#                             self.frame_y = 0
#                         else:
#                             self.frame_y = 1
#
#                     else:
#                         if self.frame_y % 2 == 0:
#                              self.frame_y = 2
#                         else:
#                             self.frame_y = 3
#
#                  if self.y_velocity ==self.jump_height:
#                     self.top_jump_point=self.pos_y
#
#
#                 #점프 구현 중력 가속도
#
#                  if(self.y_velocity>=0):
#                      self.pos_y += self.y_velocity
#                      self.y_velocity -= self.y_gravity
#                  else:
#                      if self.flying:  # flying 기능 구현
#                          if(self.flying==2):
#                              self.pos_y-=8
#                          else:
#                              self.pos_y -= 2
#                      else:
#                          self.pos_y += self.y_velocity
#                          self.y_velocity -= self.y_gravity
#
#
#               #점프하는 동시에 이동할때 이미지
#                  if(self.y_velocity>self.jump_height-7): # 0에서 최고 높이까지 갈때 스프라이트 맞춰주기
#
#                      if self.dir_x == 0:
#                          self.frame_x = (self.frame_x + 1) % 7
#                      else:
#                          self.frame_x = (self.frame_x + 1) % 6
#
#                  elif(self.y_velocity<self.jump_height-6) and (self.y_velocity>0): #최고높이일때
#                      if self.dir_x == 0:
#                          self.frame_x = 7
#                      else:
#                          self.frame_x = (self.frame_x + 1) % 4 + 4
#
#                  else:  #날라가는 모션 취하기
#
#                      if self.dir_x == 0: #점프하면서 이동하지않을때
#                              self.frame_x = 0
#                      else: #점프하면서 이동할때
#                          if self.flying == 1:
#                             self.frame_x = (self.frame_x +1)%2+7
#                             pass
#                          else:
#                             self.frame_x = (self.frame_x +1)%4+4
#
#                  if(self.pos_y<self.top_jump_point):##y축으로의 이동속도가 점프보다 낮을때
#                       self.pos_y =self.top_jump_point
#                       print(self.top_jump_point)
#                       print("        ")
#                       print(self.pos_y)
#                       self.jumping =False
#                       self.y_velocity=self.jump_height
#                       self.top_jump_point=0
#                       if self.frame_y % 2 == 0:
#                           self.frame_y = 6
#                       else:
#                           self.frame_y = 7
#                       self.frame_x = 0
#     #공격 임펙트
#         if self.attacking:
#            self.attack_frame= (self.attack_frame+1)%10
#            if self.attack_frame==0:
#                self.attacking=0
#
#
#         delay(0.05)
#         self.pos_x += 8*self.dir_x
#
#
#         #총알 관리
#
#         for bullet in bullets:
#             if bullet.update():
#                 bullets.remove(bullet)
#             bullet.draw()
#
#
#
#     '''  frame y
#           7    왼쪽으로 이동
#           6    오른쪽으로 이동
#           5    왼쪽방향보면서 점프
#           4    오른쪽 방향 보면서 점프
#           3    왼쪽방향 공격
#           2    오른쪽 방향 공격
#           1     위로 이동
#           0     아래로 이동
#           '''
#
#     def slime_handle(self):
#         global running
#         events = get_events()
#         for event in events:
#             if event.type == SDL_QUIT:
#                  running = False
#             elif event.type == SDL_KEYDOWN:
#
#                 if event.key==SDLK_RIGHT:
#                     self.dir_x+=1
#                     if self.jumping:
#                         self.frame_y =2
#                     else:
#                          self.frame_y=6
#
#
#                 elif event.key==SDLK_LEFT:
#                     self.dir_x-=1
#                     if self.jumping:
#                         self.frame_y=3
#                     else:
#                         self.frame_y=7
#
#                 if event.key==SDLK_UP:
#                     if not self.jumping:
#                         self.dir_y+=1
#                         if self.frame_y%2==0:
#                            self.frame_y = 4
#                         else:
#                            self.frame_y=5
#                         self.jumping = 1
#                 if event.key==SDLK_SPACE: ##체력 감소
#                     self.attacking=1
#                     self.makebullet()
#                     self.hp-=1
#                 if event.key==SDLK_LCTRL:
#                     self.flying=1
#                     self.frame_x=7
#                 elif event.key == SDLK_ESCAPE:
#                     running = False
#
#
#
#
#             elif event.type == SDL_KEYUP:
#                 if event.key==SDLK_RIGHT:
#                     self.dir_x-=1
#                 elif event.key==SDLK_LEFT:
#                     self.dir_x+=1
#                 if event.key==SDLK_LCTRL:
#                     self.flying=2
#
#     def makebullet(self):
#         bullets.append(BULLET())
#         if(self.frame_y%2==0):
#             bullets[-1].state ='right'
#             bullets[-1].pos_y= self.pos_y
#             bullets[-1].pos_x = self.pos_x
#         else:
#             bullets[-1].state = "left"
#             bullets[-1].pos_y = self.pos_y
#             bullets[-1].pos_x = self.pos_x
#
#     def draw(self):
#         if self.attacking:
#             self.attack_effect_pic.clip_draw(self.attack_frame * 50, 0, 50, 35, self.pos_x, self.pos_y, 6 * self.hp / 5,
#                                              6 * self.hp / 5)
#         self.slime_walk_pic.clip_draw(self.frame_x * 50, self.frame_y * 35, 50, 35, self.pos_x, self.pos_y, 2*self.hp ,self.hp)


#1 : 이벤트 정의
RD, LD, RU, LU,JD= range(5)
event_name=['RD','LD','RU','LU','JD']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN,SDLK_SPACE):JD
}

#  frame y
#           7    왼쪽으로 이동
#           6    오른쪽으로 이동
#           5    왼쪽방향보면서 점프
#           4    오른쪽 방향 보면서 점프
#           3    왼쪽방향 공격
#           2    오른쪽 방향 공격
#           1     위로 이동
#           0     아래로 이동


#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.face_dir=self.dir
        self.dir=0
        self.frame_x = 0

    @staticmethod
    def exit(self,event):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        pass



    @staticmethod
    def draw(self):

        if self.face_dir > 0:
            self.slime_walk_pic.clip_draw(self.frame_x * 50, 6*35, 50, 35, self.x, self.y,self.hp,self.hp)
        else:
            self.slime_walk_pic.clip_draw(self.frame_x * 50, 7*35, 50, 35, self.x, self.y,self.hp,self.hp)
        draw_rectangle(*self.get_bb())

class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self,event):
        print('EXIT RUN')



    def do(self):
        print(game_framework.frame_time)
        self.frame_x =(self.frame_x + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 13
        self.x += self.dir*RUN_SPEED_PPS*game_framework.frame_time
        self.x = clamp(0, self.x, 800)
    def draw(self):
        if self.dir > 0:
            self.slime_walk_pic.clip_draw(int(self.frame_x) * 50, 6 * 35, 50, 35, self.x, self.y,self.hp,self.hp)
        else:
            self.slime_walk_pic.clip_draw(int(self.frame_x)* 50, 7 * 35, 50, 35, self.x, self.y,self.hp,self.hp)
        draw_rectangle(*self.get_bb())


next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE},
}


PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  #m/m
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0) # m/s
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# Slime Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class SLIME:

    def __init__(self):
        self.x,self.y=800//2,90
        self.frame_x=0
        self.dir, self.face_dir=1,1
        self.slime_walk_pic = load_image('slimepic.png')
        self.attack_effect_pic=load_image('deadsprite.png')

        self.event_que=[]
        self.cur_state=IDLE
        self.cur_state.enter(self,None)

        self.hp=100
        self.jump_height = 16
        self.jumping=0
        self.flying=0
        self.j_velocity=self.jump_height
        self.j_gravity=2


    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event=self.event_que.pop()
            self.cur_state.exit(self,event)

            try:
                self.cur_state=next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__} Event{event_name[event]}')
            self.cur_state.enter(self,event)


    def draw(self):
        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f'Face Dir: {self.face_dir},dir:{self.dir}')

    def add_event(self,event):
        self.event_que.insert(0,event)


    def handle_event(self,event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def  get_bb(self):
        return self.x-self.hp/2+10,    self.y-self.hp/2 +15,     self.x+self.hp/2-10,     self.y+self.hp/2-15
