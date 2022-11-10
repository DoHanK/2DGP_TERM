from pico2d import*
pico2d.open_canvas()

class BACKGROUND:
    def __init__(self):
        self.tree1_img=load_image('tree.png')
        self.tileset_img=load_image('tilesetgrass.png')
        self.sky_img=load_image('sky.png')
        self.bush_img=load_image("bush.png")
        self.pic1pos=[5,5,86,27] #잔디있는거
        self.pic2pos=[5,5,86,16]
        self.colum=32
        self.raw=12
        #1은 잔디있는 땅
        self.grid=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   ]
    def draw(self):
        # 하늘
        self.sky_img.clip_composite_draw(0, 0,self.sky_img.w,self.sky_img.h,0 , '',400,300,800,600)
        self.tree1_img.draw_to_origin(0,0,400,400)

        for y in range(0,self.raw):
            for x in range(0,self.colum):
                if(self.grid[y][x]==1 ):
                    self.tileset_img.clip_composite_draw(self.pic1pos[0],self.pic1pos[1],self.pic1pos[2],self.pic1pos[3],0,' ',50*x+25,50*(11-y)+25,50,50)
                    draw_rectangle(*self.get_bb(x,y) )

    def update(self):
        pass
    def get_bb(self,x,y):
        return 50*x, 50*(11-y),50*x+50,50*(11-y)+50
def test_self():
    while not(get_events()==SDLK_DOWN):
      background=BACKGROUND()
      background.draw()
      pico2d.update_canvas()
    # pico2d.clear_canvas()


if __name__ == '__main__':
    test_self()