import pyglet
from pyglet.gl import *

from game import window

class Camera(object):
    def __init__(self):
        pass

    def translate(self, player, window):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0.0, window.width//2, 0.0, window.height//2)

        self.cam_x = -player.sprite.x + window.width//4
        self.cam_y = -player.sprite.y + window.height//4

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glTranslatef(self.cam_x, self.cam_y, 0)

    def panout(self, player, window):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0.0, window.width*1.5, 0.0, window.height*1.5)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glTranslatef(window.width//4, window.height//4, 0)
