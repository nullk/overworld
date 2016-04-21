import pyglet
from pyglet.window import key
from pyglet.gl import *

from game import batch, keys, window

class Player(object):
    def __init__(self):
        # Velocity caps
        self.xvel = 100.0
        self.yvel = 100.0

    def check_bounds(self):
        if self.sprite.x >= window.width - self.sprite.width:
            self.sprite.x = window.width - self.sprite.width
        if self.sprite.x <= 0:
            self.sprite.x = 0
        if self.sprite.y >= window.height - self.sprite.height:
            self.sprite.y = window.height - self.sprite.height
        if self.sprite.y <= 0:
            self.sprite.y = 0

    def check_collision(self):
        for tile in cyan_tiles:
            if (self.sprite.x - tile.x)**2 + (self.sprite.y - tile.y)**2 < (self.sprite.width/2 + tile.width/2)**2:
                print 'collided with %s' % tile

    def load_sprite(self, path, rows, columns):
        # This function assumes the grid is 4x3

        self.image = pyglet.image.load(path)
        self.image_grid = pyglet.image.ImageGrid(self.image, rows, columns)

        self.anim_up = pyglet.image.Animation.from_image_sequence(
            self.image_grid[:2], 0.33)
        self.anim_down = pyglet.image.Animation.from_image_sequence(
            self.image_grid[9:11], 0.33)
        self.anim_left = pyglet.image.Animation.from_image_sequence(
            self.image_grid[6:8], 0.33)
        self.anim_right = pyglet.image.Animation.from_image_sequence(
            self.image_grid[3:5], 0.33)

        # Current player frame
        self.frame = self.image_grid[0]

        self.sprite = pyglet.sprite.Sprite(self.frame,
            x=window.width//2, y=window.height//2, batch=batch)

    def update(self, dt):
        self.check_bounds()
        #self.check_collision()

        if keys[key.W]:
            self.sprite.y += self.yvel * dt
            self.frame = self.anim_up
        if keys[key.A]:
            self.sprite.x -= self.xvel * dt
            self.frame = self.anim_left
        if keys[key.S]:
            self.sprite.y -= self.yvel * dt
            self.frame = self.anim_down
        if keys[key.D]:
            self.sprite.x += self.xvel * dt
            self.frame = self.anim_right

        self.sprite.image = self.frame
        #print self.xvel
        #print self.yvel
