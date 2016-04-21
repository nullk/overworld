import pyglet
from pyglet.gl import *

from game import batch, background, foreground

#32/24 -> number of pixels in overworld image

class Overworld(object):
    def __init__(self, TILE_SIZE, SPRITESHEET, PALETTE, OVERWORLD_IMG):
        # Class parameters
        self.TILE_SIZE = TILE_SIZE
        self.SPRITESHEET = pyglet.image.load(SPRITESHEET)
        self.PALETTE = PALETTE
        self.OVERWORLD_IMG = pyglet.image.load(OVERWORLD_IMG)

        self.overworld = self.OVERWORLD_IMG.get_image_data()
        self.overworld = self.overworld.get_data('RGB', self.overworld.width*3)

        self._map = []
        self.tiles = []

        self.textures = pyglet.image.ImageGrid(self.SPRITESHEET, 1, 2)

    # Read overworld image and create _map
    def read_map(self):
        iter = False
        for r in self.overworld[0::3]:
            for g in self.overworld[1::3]:
                # Check if already iterated through green
                # value in the current pixel
                if iter:
                    iter = False
                    break
                for b in self.overworld[2::3]:
                    # Identify color
                    for key, value in self.PALETTE.iteritems():
                        # Convert rgb values of selected pixel to integers
                        # using python's ord function and convert the result
                        # to a tuple to see if it equals one of the colors
                        # in the color palette

                        if tuple(map(ord, (r,g,b))) == value:
                            self._map.append(key)

                    iter = True
                    break

        return self._map

    # Function to draw each individual tile from the map to the screen
    # with sprites
    def gen_map(self, _map):
        x = -1
        y = 0
        for pixel in _map:
            x += 1
            if x >= self.TILE_SIZE:
                x = 0
                y += 1

            for key, value in self.PALETTE.iteritems():
                if pixel == key:
                    self.tiles.append(pyglet.sprite.Sprite(self.textures[key], x=x*self.TILE_SIZE, y=y*self.TILE_SIZE, batch=batch, group=background))


