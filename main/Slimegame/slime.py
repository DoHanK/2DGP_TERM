from pico2d import *
import game_world
import game_framework
from bullet import BULLET
import sever
'''==================================함수 정의============================='''
RD, LD, RU, LU,JD,SPACE= range(6)
event_name=['RD','LD','RU','LU','JD','SPACE']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN,SDLK_UP):JD,
    (SDL_KEYDOWN,SDLK_SPACE):SPACE
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

        self.dir=0
        self.frame_x = 0
        if event == JD:
            if self.jump_flag == 0:
                self.jumping()
                self.jumping_update()
    @staticmethod
    def exit(self,event):

        if event == SPACE:
            self.shoot_bullet()
    @staticmethod
    def do(self):
        self.jumping_update()
        pass



    @staticmethod
    def draw(self):
        if self.attacked_delay>1:
            if self.face_dir > 0:
                  self.slime_walk_pic.clip_draw(self.frame_x * 50, 6*35, 50, 35, self.x, self.y,self.hp,self.hp)
            else:
                  self.slime_walk_pic.clip_draw(self.frame_x * 50, 7*35, 50, 35, self.x, self.y,self.hp,self.hp)
        else:
            if self.attacked_draw%2==0:
              if self.face_dir > 0:
                  self.slime_walk_pic.clip_draw(self.frame_x * 50, 6 * 35, 50, 35, self.x, self.y, self.hp, self.hp)
              else:
                 self.slime_walk_pic.clip_draw(self.frame_x * 50, 7 * 35, 50, 35, self.x, self.y, self.hp, self.hp)
        draw_rectangle(*self.get_bb())

class RUN:
    def enter(self, event):

        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        self.face_dir = self.dir
        if event == JD:
            if self.jump_flag == 0:
                self.jumping()
                self.jumping_update()
    def exit(self,event):

        self.face_dir=self.dir
        if event == SPACE:
            self.shoot_bullet()


    def do(self):

        self.jumping_update()
        self.frame_x =(self.frame_x + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 13
        self.x += self.dir*RUN_SPEED_PPS*game_framework.frame_time
        self.x = clamp(0, self.x, 800)
    def draw(self):
        if self.attacked_delay > 1:
            if self.face_dir > 0:
                self.slime_walk_pic.clip_draw(int(self.frame_x) * 50, 6 * 35, 50, 35, self.x, self.y, self.hp, self.hp)
            else:
                self.slime_walk_pic.clip_draw(int(self.frame_x) * 50, 7 * 35, 50, 35, self.x, self.y, self.hp, self.hp)
        else:
            if self.attacked_draw % 2 == 0:
                if self.face_dir > 0:
                    self.slime_walk_pic.clip_draw(int(self.frame_x)* 50, 6 * 35, 50, 35, self.x, self.y, self.hp, self.hp)
                else:
                    self.slime_walk_pic.clip_draw(int(self.frame_x) * 50, 7 * 35, 50, 35, self.x, self.y, self.hp, self.hp)
        draw_rectangle(*self.get_bb())


next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN,JD:IDLE,SPACE:IDLE},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, JD:RUN,SPACE:RUN},
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
    slime_walk_pic= None
    def __init__(self):
        self.x,self.y=50,100
        self.frame_x=0
        self.dir, self.face_dir=1,1
        if SLIME.slime_walk_pic==None:
            SLIME.slime_walk_pic = load_image('slimepic.png')
            self.attack_effect_pic=load_image('deadsprite.png')
        self.background=None
        self.event_que=[]
        self.cur_state=IDLE
        self.cur_state.enter(self,None)
        self.hp=100
        self.jump_height = 6.5
        self.jump_flag=1
        self.flying=0
        self.j_velocity=0
        self.j_gravity=0.15
        self.attacked_delay=10
        self.attacked_draw=0
        self.monster=None
        self.bullets=[]
        self.attack_delay=0.2


    def update(self):
        self.attack_delay -= game_framework.frame_time
        self.attacked_delay+=game_framework.frame_time
        self.attacked_draw +=1
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
        return self.x-self.hp/2+220/800*self.hp,    self.y-self.hp/2 +100/800*self.hp,     self.x+self.hp/2-220/800*self.hp,     self.y+self.hp/2-100/800*self.hp
    def handle_collision(self,other,massage):
        #점프에 대한 충돌 처리
        if massage=='crush':
                self.x -= self.face_dir * RUN_SPEED_PPS * game_framework.frame_time
        elif massage=='g':
            if self.jump_flag==1:
                 self.y -= self.j_velocity * RUN_SPEED_PPS * game_framework.frame_time
                 self.jump_flag=0
            elif self.jump_flag==0:
                 self.y +=RUN_SPEED_PPS*game_framework.frame_time
        if massage =='eat':
                self.hp+=200
        if massage =='attacked':
            if self.attacked_delay>1:
                self.hp -=10
                self.attacked_delay=0
                self.attacked_draw =0

        pass


    def jumping(self):
        self.jump_flag=1
        self.j_velocity = self.jump_height

        pass
    def jumping_update(self):
        if self.jump_flag==1:

            self.y+=self.j_velocity*RUN_SPEED_PPS*game_framework.frame_time
            self.j_velocity-=self.j_gravity
        elif self.jump_flag==0:
            self.y-=RUN_SPEED_PPS*game_framework.frame_time

    def shoot_bullet(self):
        if self.attack_delay<0:
            self.hp -=1
            bullets=BULLET( self.x ,self.y ,self.face_dir )

            game_world.add_object(bullets,1)

            game_world.add_collision_pairs(bullets, None, "bullet::background")
            game_world.add_collision_pairs(bullets, None, "bullet::monster")
            self.attack_delay=0.2
            # print(game_world.collision_group)
