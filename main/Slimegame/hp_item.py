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
