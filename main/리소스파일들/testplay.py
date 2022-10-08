from pico2d import *
open_canvas()

character = load_image('walkupsprite.png')

x = 0

frame=0
while(x<800):
    clear_canvas()

    character.clip_draw(frame*50,0,50,35,400,90)
    update_canvas()
    frame= (frame+1)%13
    delay(0.01)
    get_events()



close_canvas()

