from pico2d import *
import game_framework
import game_world
from slime import SLIME
from background import BACKGROUND

width=800
height=600

slime=None
background=None
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            slime.handle_event(event)


# 초기화
def enter():
    global slime,background
    slime=SLIME()
    background=BACKGROUND()
    game_world.add_object(background, 1)
    game_world.add_object(slime,2)

# 종료
def exit():
  game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()
        if collide(slime,background):
            print("collision")


def draw_world():
   for game_object in game_world.all_objects():
       game_object.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass

def collide(a,b):
    # print(type(b))
    if type(b)==type(BACKGROUND()):
        left_a, bottom_a,right_a,top_a=a.get_bb()
        for y in range(0,b.raw):
            for x in range(0,b.colum):
                if b.grid[y][x]==1:
                     left_b, bottom_b, right_b, top_b = b.get_bb(x,y)
                     if left_a > right_b: continue
                     if right_a<left_b:continue
                     if top_a < bottom_b: continue
                     if bottom_a > top_b: continue
                     else:return True
        return False
    else:
          left_a, bottom_a, right_a, top_a = a.get_bb()
          left_b,bottom_b,right_b,top_b=b.get_bb()
          if left_a> right_b: return False
          if top_a<bottom_b:return False
          if bottom_a>top_b:return False
          return True




def test_self():
    import play_state
    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
