from pico2d import *
import game_framework
import game_world
from slime import SLIME
from background import BACKGROUND
from hp_item import ITEM
from sunmonster import SUNMONSTER
import sever
from door import DOOR
width=800
height=600



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            sever.slime.handle_event(event)


# 초기화
def enter():
    sever.monster = [SUNMONSTER()]
    sever.items = ITEM(270,80)
    sever.background = BACKGROUND()
    sever.slime = SLIME()
    sever.door=DOOR()
    game_world.add_objects(sever.monster, 1)
    game_world.add_object(sever.items, 1)
    game_world.add_object(sever.background, 0)
    game_world.add_object(sever.slime,1)
    game_world.add_object(sever.door,0)

    game_world.add_collision_pairs(sever.slime,sever.door,"slime::door" )
    game_world.add_collision_pairs(sever.slime, sever.background, 'g')
    game_world.add_collision_pairs(sever.slime, sever.background, 'crush')
    game_world.add_collision_pairs(sever.slime, sever.items, 'eat')
    game_world.add_collision_pairs(sever.slime,sever.monster, 'attacked')
    game_world.add_collision_pairs(None, sever.background, "bullet::background")
    game_world.add_collision_pairs(None, sever.monster, "bullet::monster")
# 종료
def exit():
  game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a , b , group in game_world.all_collision_pairs():
        if collide(a,b,group):
            a.handle_collision(b,group)
            b.handle_collision(a,group)

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

def collide(a,b,group):

            if type(b) is BACKGROUND:  #background 전체에 대한 충돌 처리
                left_a, bottom_a, right_a, top_a = a.get_bb()
                for y in range(0,b.raw):
                    for x in range(0,b.colum):
                        if b.grid[y][x]==1 or b.grid[y][x]==2:
                            left_b, bottom_b, right_b, top_b = b.get_bb(x,y)
                            if left_a > right_b: continue
                            if right_a<left_b:continue
                            if top_a < bottom_b: continue
                            if bottom_a > top_b: continue
                            else:return True
                        else:continue
                return False
            else:  #기본 object와의 충돌 처리
                    left_a, bottom_a, right_a, top_a = a.get_bb()
                    left_b,bottom_b,right_b,top_b=b.get_bb()
                    if left_a> right_b: return False
                    if right_a<left_b: return False
                    if top_a<bottom_b:return False
                    if bottom_a>top_b:return False
                    return True






def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas(800,600)
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__': # 단독 실행이면
    test_self()
