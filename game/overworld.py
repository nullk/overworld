import pyglet
from pyglet.gl import *

from game import batch, background, foreground

#32/24 -> number of pixels in overworld image

overworld_img = pyglet.image.load('assets/overworld.png')
overworld = overworld_img.get_image_data()
overworld_map = overworld.get_data('RGB', overworld.width*3)

palette = {
    'green':(96, 155, 64),
    'cyan':(30, 155, 64)
}

# Tiles
TILE_SIZE = 32
tiles = []

spritesheet = pyglet.image.load('assets/textures.png')
textures = pyglet.image.ImageGrid(spritesheet, 1, 2)

# Grass
GREEN = textures[0]
green_tiles = []
# Water
CYAN = textures[1]
cyan_tiles = []

def read_map(overworld):
    _map = []
    iter = False
    for r in overworld[0::3]:
        for g in overworld[1::3]:
            # Check if already iterated through green
            # value in the current pixel
            if iter:
                iter = False
                break
            for b in overworld[2::3]:
                # Identify color
                for key, value in palette.iteritems():
                    # Convert rgb values of selected pixel to integers
                    # using python's ord function and convert the result
                    # to a tuple to see if it equals one of the colors
                    # in the color palette
                    if tuple(map(ord, (r,g,b))) == value:
                        _map.append(key)

                iter = True
                break
    return _map

def gen_world(_map, TILE_SIZE):
    x = -1
    y = 0
    for pixel in _map:
        x += 1
        if x >= TILE_SIZE:
            x = 0
            y += 1
        if pixel == 'green':
            green_tiles.append(pyglet.sprite.Sprite(GREEN, x=x*TILE_SIZE, y=y*TILE_SIZE, batch=batch, group=background))
        if pixel == 'cyan':
            cyan_tiles.append(pyglet.sprite.Sprite(CYAN, x=x*TILE_SIZE,
                y=y*TILE_SIZE, batch=batch, group=background))

_map = read_map(overworld_map)

