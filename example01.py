from xengine import *
from OpenGL.GL import * # pip install PyOpenGL
from math import sqrt

def setup(window):
    a = 480
    h = a * sqrt(3) / 2

    A = Point(-a/2, -h/2,   0, RED)
    B = Point(a/2,  -h/2,   0, GREEN)
    C = Point(0,    h/2,    0, BLUE)

    T = Triangle(A, B, C)
    T.adapt_to_window(window)
    T.draw()

def loop(window):
    glDrawArrays(GL_TRIANGLES, 0, 3)

window = Window(720, 480, setup_function=setup, loop_function=loop)
