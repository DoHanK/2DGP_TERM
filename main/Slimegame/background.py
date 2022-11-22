import random

from pico2d import*
import sever

class BACKGROUND:
    flag=1
    def __init__(self):
        if BACKGROUND.flag:
            self.tree1_img=load_image('tree.png')
            self.tileset_img=load_image('tilesetgrass.png')
            self.sky_img=load_image('sky.png')
            self.bush_img=load_image("bush.png")
            BACKGROUND.flag=0
        self.pic1pos=[5,5,86,27] #잔디있는거
        self.pic2pos=[5,5,86,16]
        self.colum=32
        self.raw=12
        #앞가 위치 뒤에가 크기
        self.tree_pos=[ (random.randint(0,1),random.randint(0,20)) for x in range(10)]
        self.prepos_x=0
        self.onegen=1
        #1은 잔디있는 땅
        # self.ninoblock=[   [[0,1,0],[0,2,0],[1,2,1]], [[0,0,1],[0,1,0],[1,0,0]], [[1,1,1],[0,0,2],[0,0,2]], [[0,1,0],[1,0,1],[0,0,0]], [[1,1,1],[2,0,2],[2,2,2]], [[1,1,1],[0,0,2],[0,0,2]], [[1,1,1],[0,0,2],[0,0,2]]]
        self.grid=[
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [0, 0, 1, 1, 0, 0, 0, 0, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                   [0, 0, 0, 0, 1, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   ]
    def draw(self):

        # 하늘
        self.sky_img.clip_composite_draw(0, 0,self.sky_img.w,self.sky_img.h,0 , '',400,300,800,600)
        for x in range(10):
            x1,y=self.tree_pos[x]
            self.tree1_img.draw_to_origin(x*(160+x1)-sever.camera_x,40,200+y,200+y)

        for y in range(0,self.raw):
            for x in range(0,self.colum):
                if(self.grid[y][x]==1 ):
                    self.tileset_img.clip_composite_draw(self.pic1pos[0] ,self.pic1pos[1] ,self.pic1pos[2] ,self.pic1pos[3] ,0,' ',50*x+25 -sever.camera_x,50*(11-y)+25,50,50)
                    draw_rectangle(*self.get_bb(x,y) )
                elif self.grid[y][x]==2 :
                    self.tileset_img.clip_composite_draw(self.pic2pos[0], self.pic2pos[1], self.pic2pos[2], self.pic2pos[3], 0, ' ', 50 * x + 25 - sever.camera_x, 50 * (11 - y) + 25, 50, 50)
                    draw_rectangle(*self.get_bb(x, y))

    def update(self):
        # if self.onegen:
        #     for y in range(0, self.raw):
        #         for x in range(0, self.colum):
        #             if random.randint(0,10)==0:
        #                 num=random.randint(0,6)
        #                 for y1 in range (0,3):
        #                     for x1 in range(0,3):
        #                         if x+3<32 and y+3<10:
        #                             self.grid[y+y1][x+x1]=self.ninoblock[num][y1][x1]
        #     self.onegen=0

        pass
    def get_bb(self,x,y):
        return 50*x-sever.camera_x, 50*(11-y), 50*x+50-sever.camera_x,50*(11-y)+50
    def handle_collision(self,other,massage):
        #점프에 대한 충돌 처리
       pass






def test_self():
    while not(get_events()==SDLK_DOWN):
      background=BACKGROUND()
      print(type(background))
      background.draw()
      pico2d.update_canvas()
    # pico2d.clear_canvas()


if __name__ == '__main__':
    test_self()