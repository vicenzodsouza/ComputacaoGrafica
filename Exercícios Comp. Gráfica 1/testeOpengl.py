import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Posição inicial do objeto (centralizado na tela)
x = 0 
y = 0 
r = 0

# Escala inicial do polígono
ex = 2 
ey = 2 
ez = 2 

# Variável de controle de profundidade da câmera (zoom)
zoom = -6 

def init():
    # Define a cor de fundo da janela como branco (R, G, B, Alpha)
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 640/480, 0.1, 100)
    
    glMatrixMode(GL_MODELVIEW)

def draw():
    glLoadIdentity()
    
    # Aplica a translação levando em conta a posição XYZ e o zoom atual
    glTranslatef(x, y, zoom)

    # Rotação apenas no eixo X (descomente para girar verticalmente)
    # glRotatef(r, 1, 0, 0)  
    
    # Rotação simultânea nos eixos X e Y (giro diagonal)
    glRotatef(r, 1, 1, 0)  

    glScalef(ex, ey, ez)
    glBegin(GL_TRIANGLES)

    # Define a cor do triângulo como preta
    glColor3f(0, 0, 0)  

    # Mapeamento dos vértices do triângulo
    glVertex3f(0, 2, 0)
    glVertex3f(-2, -2, 0)
    glVertex3f(2, -2, 0)

    glEnd()

def main():
    pygame.init()
    pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)
    init()

    global x, y, r, ex, ey, ez, zoom

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                
                # Controles de translação com movimentação horizontal invertida
                if event.key == K_a:
                    x += 0.2  # Direita
                if event.key == K_d:
                    x -= 0.2  # Esquerda
                if event.key == K_w:
                    y += 0.2
                if event.key == K_s:
                    y -= 0.2
                
                # Controles de profundidade (Câmera)
                if event.key == K_z:
                    zoom += 0.2  # Aproxima o objeto
                if event.key == K_x:
                    zoom -= 0.2  # Afasta o objeto
            
            # Controles de escala pelo scroll do mouse
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 4:
                    ex += 0.2
                    ey += 0.2
                    ez += 0.2
                if event.button == 5:
                    ex -= 0.2
                    ey -= 0.2
                    ez -= 0.2
                    
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw()

        pygame.display.flip()
        pygame.time.wait(10)

        # Incrementa o ângulo para rotação contínua no sentido anti-horário
        r -= 10 

    pygame.quit()

if __name__ == "__main__":
    main()