import pygame

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

pos_x = -1.5
pos_y = 0
angulo = 0

esc_x = 1
esc_y = 1
esc_z = 1

def iniciar():
    glClearColor(0, 0, 1, 1)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 640/480, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)

def desenhar():
    glLoadIdentity()

    glTranslatef(pos_x, pos_y, -6)
    glRotatef(angulo, 0, 1, 0)
    glScalef(esc_x, esc_y, esc_z)

    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 1, 0)
    glVertex3f(-1, -1, 0)
    glVertex3f(1, -1, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex3f(2, 1, 0)
    glVertex3f(1, -1, 0)
    glVertex3f(3, -1, 0)
    glEnd()

def principal():
    pygame.init()
    pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)
    iniciar()

    global pos_x, pos_y, angulo, esc_x, esc_y, esc_z

    ativo = True
    while ativo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ativo = False
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    ativo = False
                if evento.key == K_a:
                    pos_x -= 0.2
                if evento.key == K_d:
                    pos_x += 0.2
                if evento.key == K_w:
                    pos_y += 0.2
                if evento.key == K_s:
                    pos_y -= 0.2
            if evento.type == MOUSEBUTTONDOWN:
                if evento.button == 4:
                    esc_x += 0.2
                    esc_y += 0.2
                    esc_z += 0.2
                if evento.button == 5:
                    esc_x -= 0.2
                    esc_y -= 0.2
                    esc_z -= 0.2

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        desenhar()
        pygame.display.flip()
        pygame.time.wait(10)
        angulo += 3

    pygame.quit()

if __name__ == "__main__":
    principal()