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

import overworld
from player import Player
from camera import Camera

pyglet.clock.set_fps_limit(60)

#bg = pyglet.image.load('assets/bg.jpg')
#bg_sprite = pyglet.sprite.Sprite(bg, x=0, y=0, batch=batch, group=background)

player = Player()
player.load_sprite('assets/pug.png', 4, 3)

cam = Camera()

overworld.gen_world(overworld._map, overworld.TILE_SIZE)

# Handle window events

@window.event
def on_draw():
    window.clear()

    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, window.width//2, 0.0, window.height//2)

    cam.translate(player, window)

    if keys[key.TAB]:
        cam.panout(window)

    batch.draw()

# Main loop

if quit != True:
    pyglet.clock.schedule_interval(player.update, 1/120.0)
    pyglet.app.run()
