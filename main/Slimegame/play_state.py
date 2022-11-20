from pico2d import *
import game_framework
import game_world
from slime import SLIME
from background import BACKGROUND
from bullet import BULLET
from hp_item import ITEM
from sunmonster import SUNMONSTER
width=800
height=600

item=None
slime=None
background=None
sunmonster=None
bullets=None

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
    global slime,background,item,sunmonster,bullets
    item=ITEM()
    sunmonster=SUNMONSTER()
    slime=SLIME()
    background=BACKGROUND()
    bullets=[BULLET() for x in range(6)]

    slime.background=background
    slime.bullets=bullets
    slime.monster=sunmonster

    game_world.add_object(sunmonster, 1)
    game_world.add_object(item, 1)
    game_world.add_object(background, 0)
    game_world.add_object(slime,1)

    for x in bullets:
        game_world.add_object(x, 1)
        game_world.add_collision_pairs(x, sunmonster, 'attack')
        game_world.add_collision_pairs(x, background, 'b')


    game_world.add_collision_pairs(slime, background, 'g')
    game_world.add_collision_pairs(slime, background, 'crush')
    game_world.add_collision_pairs(slime, item, 'eat')
    game_world.add_collision_pairs(slime,sunmonster, 'attacked')
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
    # print(type(b))
    if type(a)==type(BULLET()):
        if a.ableflag == 1:
            if type(b)==type(BACKGROUND()):  #background 전체에 대한 충돌 처리
                left_a, bottom_a, right_a, top_a = a.get_bb()
                for y in range(0,b.raw):
                    for x in range(0,b.colum):
                        if b.grid[y][x]==1:
                            left_b, bottom_b, right_b, top_b = b.get_bb(x,y)
                            if left_a > right_b: continue
                            if right_a<left_b:continue
                            if top_a < bottom_b: continue
                            if bottom_a > top_b: continue
                            else:return True
                        else:continue
                return False
            else:  #기본 object와의 충돌 처리
                if b.ableflag==1:
                    print("충돌 확인")
                    left_a, bottom_a, right_a, top_a = a.get_bb()
                    left_b,bottom_b,right_b,top_b=b.get_bb()
                    if left_a> right_b: return False
                    if right_a<left_b: return False
                    if top_a<bottom_b:return False
                    if bottom_a>top_b:return False
                    return True
        else:
            return
    else:
        if type(b)==type(BACKGROUND()):  #background 전체에 대한 충돌 처리
            left_a, bottom_a, right_a, top_a = a.get_bb()


            for y in range(0,b.raw):
                for x in range(0,b.colum):
                    if b.grid[y][x]==1:
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
    import play_state
    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
