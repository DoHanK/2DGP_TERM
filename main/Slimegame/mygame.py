import game_framework
import pico2d
import titlestate
import play_state

pico2d.open_canvas()
game_framework.run(titlestate)
pico2d.close_canvas()