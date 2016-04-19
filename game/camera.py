import pyglet
from pyglet.gl import *

class Camera(object):
    def __init__(self):
        pass

    def translate(self, player, window):
        self.cam_x = -player.sprite.x + window.width//4
        self.cam_y = -player.sprite.y + window.height//4

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glTranslatef(self.cam_x, self.cam_y, 0)

    def panout(self, window):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0.0, window.width, 0.0, window.height)
