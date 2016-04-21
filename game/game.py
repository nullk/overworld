import pyglet
from pyglet import clock
from pyglet.window import key
from pyglet.gl import *

# Game settings

settings = {
    'width':1024,
    'height':768,
    'title':'game'
}
batch = pyglet.graphics.Batch()

background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

keys = key.KeyStateHandler()

# Initialize window

window = pyglet.window.Window(
    settings['width'],
    settings['height'],
    settings['title']
)
window.push_handlers(keys)

# Game components

import tilemap
from player import Player
from camera import Camera

pyglet.clock.set_fps_limit(60)

player = Player()
player.load_sprite('assets/pug.png', 4, 3)

camera = Camera()

palette = {
    # green
    0:(96, 155, 64),
    # cyan
    1:(30, 155, 64)
}
overworld = tilemap.Overworld(32, 'assets/textures.png', palette, 'assets/overworld.png')
_map = overworld.read_map()
overworld.gen_map(_map)

# Handle window events

@window.event
def on_draw():
    window.clear()
    glClear(GL_COLOR_BUFFER_BIT)

    camera.translate(player, window)

    if keys[key.TAB]:
        camera.panout(player, window)

    batch.draw()

# Main loop

if quit != True:
    pyglet.clock.schedule_interval(player.update, 1/120.0)
    pyglet.app.run()
