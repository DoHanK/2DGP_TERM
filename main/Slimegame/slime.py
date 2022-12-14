from pico2d import *
import game_world
import game_framework
from bullet import BULLET
import server
import undergroundbackground
import failstage
from  batmonster import BATMONSTER

RD, LD, RU, LU , JD , SPACE , CTRL_D , CTRL_U = range(8)
event_name=['RD', 'LD' , 'RU' , 'LU' , 'JD' , 'SPACE' , 'CTRL_D' , 'CTRL_U' ]

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN,SDLK_UP): JD,
    (SDL_KEYDOWN,SDLK_SPACE): SPACE,
    (SDL_KEYDOWN,SDLK_LCTRL): CTRL_D,
    (SDL_KEYUP,SDLK_LCTRL): CTRL_U
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
            if self.jump_flag != 'jump':
                self.jumping()
                self.jumping_update()
                self.jump_flag = 'jump'
        if event is CTRL_D:
            self.flying = 'flying'
        if event is CTRL_U:
            self.flying = 'unflying'
            self.j_velocity = 0

    @staticmethod
    def exit(self,event):

        if event == SPACE:
            self.shoot_bullet()

    @staticmethod
    def do(self):
        self.jumping_update()

    @staticmethod
    def draw(self):
        if self.flying == 'flying':
            self.slime_fly_pic.clip_draw(157,7,145,143,self.x,self.y,self.hp,self.hp)

        if self.attacked_delay > 1:
            if self.face_dir > 0:
                  self.slime_walk_pic.clip_draw(self.frame_x * 50, 6*35, 50, 35, self.x, self.y,self.hp,self.hp)

            else:
                  self.slime_walk_pic.clip_draw(self.frame_x * 50, 7*35, 50, 35, self.x, self.y,self.hp,self.hp)

        else:
            if self.attacked_draw%2 == 0:
              if self.face_dir > 0:
                  self.slime_walk_pic.clip_draw(self.frame_x * 50, 6 * 35, 50, 35, self.x, self.y, self.hp, self.hp)

              else:
                 self.slime_walk_pic.clip_draw(self.frame_x * 50, 7 * 35, 50, 35, self.x, self.y, self.hp, self.hp)

        if self.flying == 'flying': #pic비눗방울 디테일
            self.slime_fly_pic.clip_draw(8,8,143,140,self.x,self.y,self.hp,self.hp)
        # draw_rectangle(*self.get_bb())


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
            if self.jump_flag != 'jump':
                self.jumping()
                self.jumping_update()
                self.jump_flag = 'jump'
        if event is CTRL_D:
            self.flying = 'flying'
        if event is CTRL_U:
            self.flying = 'unflying'
            self.j_velocity = 0

    def exit(self,event):

        self.face_dir=self.dir
        if event == SPACE:
            self.shoot_bullet()

    def do(self):

        self.jumping_update()
        self.frame_x = (self.frame_x + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 13
        self.x += self.dir*RUN_SPEED_PPS*game_framework.frame_time
        self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.flying == 'flying':
            self.slime_fly_pic.clip_draw(157,7,145,143,self.x,self.y,self.hp,self.hp)

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

        if self.flying == 'flying': #pic비눗방울 디테일
            self.slime_fly_pic.clip_draw(8,8,143,140,self.x,self.y,self.hp,self.hp)
        # draw_rectangle(*self.get_bb())


next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN,JD:IDLE,SPACE:IDLE,CTRL_U:IDLE, CTRL_D:IDLE},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, JD:RUN,SPACE:RUN,CTRL_U:RUN, CTRL_D:RUN},
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

    slime_walk_pic = None
    attack_effect_pic = None
    slime_fly_pic= None
    def __init__(self):
        if SLIME.slime_walk_pic == None:
            SLIME.slime_walk_pic = load_image('./resourceimg/slimepic.png')
            SLIME.attack_effect_pic=load_image('./resourceimg/deadsprite.png')
            SLIME.slime_fly_pic= load_image('./resourceimg/bubble.png')

        self.x , self.y = 60 , 150
        self.frame_x = 0
        self.dir , self.face_dir = 1 , 1
        self.background = None
        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self,None)
        self.hp = 50

        self.jump_height = 5.5
        self.jump_flag = 'nujump'
        self.j_velocity = 0
        self.j_gravity = 0.10
        self.pre_j_velocity=0

        self.attacked_delay = 1
        self.attacked_draw = 0

        self.flying='unflying'
        self.flying_g=0.3

        self.bullets = []
        self.prepos_x = 0
        self.world_pos = 'ground'

        self.batkill = 0
    def update(self):
        if self.world_pos == 'underground':
            if self.batkill is server.batmonstercount:
                server.door.sound.set_volume(50)
                server.door.sound.repeat_play()
                game_world.add_object(server.door , 0)
                game_world.add_collision_pairs(server.slime, server.door,"slime::door")
                self.batkill += 1

        if self.hp<30:
            game_framework.change_state(failstage)

        server.camera_x += self.x-self.prepos_x
        self.prepos_x = self.x
        self.attacked_delay += game_framework.frame_time
        self.attacked_draw += 1
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

    def get_bb(self):
        return self.x-self.hp/2+220/800*self.hp,    self.y-self.hp/2 +100/800*self.hp,     self.x+self.hp/2-220/800*self.hp,     self.y+self.hp/2-100/800*self.hp

    def handle_collision(self,other,massage):
        #점프에 대한 충돌 처리
        if massage == 'slime::background':
            self.x -= self.face_dir * RUN_SPEED_PPS * game_framework.frame_time
            pass
        elif massage == 'g':
            self.j_velocity = 0
            self.y -= self.pre_j_velocity * RUN_SPEED_PPS * game_framework.frame_time
            self.jump_flag = 'unjump'

        if massage == 'slime::item':
            self.hp += 8
            self.y += 4

        if massage == 'slime::monster':
            if self.attacked_delay>1:
                if type(other) is BATMONSTER:
                    self.hp -= 8
                else:
                    self.hp -= 4
                self.attacked_delay = 0
                self.attacked_draw = 0
        if massage == 'slime::slide':
            # 캐릭터 전위치와 전카메라 위치 담기
            temp=server.slime
            server.sever_init()
            server.slime=temp
            game_world.clear()
            server.slime.x = 400
            server.slime.y = 600
            server.slime.world_pos = 'underground'
            self.prepos_x = 400
            server.camera_x = 400
            game_framework.push_state(undergroundbackground)

    def jumping(self):
            self.j_velocity = self.jump_height


    def jumping_update(self):
        if self.flying == 'unflying':
            self.y += self.j_velocity * RUN_SPEED_PPS * game_framework.frame_time
            self.pre_j_velocity = self.j_velocity
            self.j_velocity -= self.j_gravity
        elif self.flying == 'flying':
            if self.j_velocity > 0:
                self.y += self.j_velocity * RUN_SPEED_PPS * game_framework.frame_time
                self.pre_j_velocity = self.j_velocity
                self.j_velocity -= self.j_gravity
            else:
                self.y -= self.flying_g* RUN_SPEED_PPS * game_framework.frame_time
                self.pre_j_velocity = -self.flying_g
    def shoot_bullet(self):
        self.hp -= 1
        bullets = BULLET( self.x ,self.y ,self.face_dir, self.hp )
        game_world.add_object(bullets,1)
        game_world.add_collision_pairs(bullets, None, "bullet::background")
        game_world.add_collision_pairs(bullets, None, "bullet::monster")
