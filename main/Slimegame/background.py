import random

from pico2d import*
import server

class BACKGROUND:
    tree_img = None
    tileset_img = None
    sky_img = None
    bush_img = None
    underground_img = None
    underground_bgm = None
    ground_bgm = None

    def __init__(self,grid):

        if BACKGROUND.sky_img is  None:
            BACKGROUND.underground_img = load_image('./resourceimg/underground.jpg')
            BACKGROUND.tree_img = load_image('./resourceimg/tree.png')
            BACKGROUND.tileset_img=load_image('./resourceimg/tilesetgrass.png')
            BACKGROUND.sky_img=load_image('./resourceimg/sky.png')
            BACKGROUND.bush_img=load_image("./resourceimg/bush.png")
            BACKGROUND.ground_bgm = load_music('./sound/upgroundsound.mp3')
            BACKGROUND.underground_bgm = load_music('./sound/undergroundsound.mp3')
            BACKGROUND.ground_bgm.set_volume(100)
            BACKGROUND.underground_bgm.set_volume(100)


        self.pic1pos = [5,5,86,27] #잔디있는거
        self.pic2pos = [5,5,86,16]
        self.colum = 32
        self.raw = 12
        #앞변수 위치 뒤 변수 크기
        self.tree_pos = [ (random.randint(0,1),random.randint(0,500)) for x in range(10)]
        self.prepos_x = 0
        self.onegen = 1
        #1은 잔디있는 땅

        self.grid=grid

    def draw(self):

        # 하늘
        if server.slime.world_pos=='ground':
            self.sky_img.clip_composite_draw(0, 0,self.sky_img.w,self.sky_img.h,0 , '',400,300,800,600)
            for x in range(10):
                x1,y=self.tree_pos[x]
                self.tree_img.draw_to_origin(x*(160+x1)-server.camera_x,40,200+y,200+y)

        elif server.slime.world_pos=='underground':
            self.underground_img.clip_composite_draw(int(0+server.camera_x),int(self.underground_img.h/2) ,int(self.underground_img.w/4),int(self.underground_img.h/4),0 , '',400,300,800,600)


        for y in range(0,self.raw):
            for x in range(0,self.colum):
                if(self.grid[y][x]==1 ):
                    self.tileset_img.clip_composite_draw(self.pic1pos[0] ,self.pic1pos[1] ,self.pic1pos[2] ,self.pic1pos[3] ,0,' ',50*x+25 -server.camera_x,50*(11-y)+25,50,50)
                    draw_rectangle(*self.get_bb(x,y) )
                elif self.grid[y][x]==2 :
                    self.tileset_img.clip_composite_draw(self.pic2pos[0], self.pic2pos[1], self.pic2pos[2], self.pic2pos[3], 0, ' ', 50 * x + 25 - server.camera_x, 50 * (11 - y) + 25, 50, 50)
                    draw_rectangle(*self.get_bb(x, y))

    def update(self):
        pass

    def get_bb(self,x,y):
        return 50*x - server.camera_x , 50*(11 - y) , 50 * x + 50 - server.camera_x ,50*(11 - y)+50

    def handle_collision(self,other,massage):
        #점프에 대한 충돌 처리
        pass

