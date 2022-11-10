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
