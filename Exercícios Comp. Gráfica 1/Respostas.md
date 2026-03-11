# Entrega de Atividades: Computação Gráfica - Prática 03

Este documento apresenta a documentação das modificações implementadas no script `TesteOpenGl.py`, cobrindo as 10 etapas solicitadas no exercício.

---

### Questão 1: Cor de Fundo
* **Ação:** Substituição de `glClearColor(0.0, 0.0, 0.0, 1.0)` por `glClearColor(1.0, 1.0, 1.0, 1.0)`.
* **Efeito prático:** A área de fundo da renderização mudou de preto para totalmente branco.

### Questão 2: Modificação do Eixo de Giro (Y para X)
* **Ação:** Alteração da chamada de `glRotatef(r, 0, 1, 0)` para `glRotatef(r, 1, 0, 0)`.
* **Efeito prático:** O movimento do polígono mudou de um giro em torno do próprio eixo horizontal para um movimento de tombamento frontal/traseiro.

### Questão 3: Rotação Diagonal (Eixos X e Y)
* **Ação:** Atualização da função de rotação para `glRotatef(r, 1, 1, 0)`.
* **Efeito prático:** O triângulo agora gira utilizando ambos os eixos simultaneamente, criando uma rotação contínua em um ângulo de 45º.

### Questão 4: Preenchimento do Triângulo
* **Ação:** Modificação da função de cor de `glColor3f(1, 1, 0)` para `glColor3f(0, 0, 0)`.
* **Efeito prático:** A cor interna do objeto passou de amarelo para preto, destacando-se no novo fundo branco.

### Questão 5: Redimensionamento dos Vértices
* **Ação:** As coordenadas de desenho passaram de `(0, 1, 0)`, `(-1, -1, 0)`, `(1, -1, 0)` para coordenadas de raio maior: `(0, 2, 0)`, `(-2, -2, 0)`, `(2, -2, 0)`.
* **Efeito prático:** A geometria base do triângulo foi dobrada de tamanho no momento do desenho.

### Questão 6: Aceleração e Inversão de Rotação
* **Ação:** Substituição do incremento `r += 3` por um decremento maior `r -= 10`.
* **Efeito prático:** A animação ficou bem mais rápida e a direção do giro foi invertida para o sentido horário.

### Questão 7: Alinhamento Inicial
* **Ação:** A variável global `x` foi inicializada com `0` ao invés de `-1.5`.
* **Efeito prático:** O polígono não aparece mais deslocado no canto esquerdo ao iniciar o script, surgindo perfeitamente no centro.

### Questão 8: Ampliação da Escala Base
* **Ação:** As variáveis tridimensionais de escala (`ex`, `ey`, `ez`) receberam o valor `2` inicial.
* **Efeito prático:** Além do aumento dos vértices, o fator de escala da matriz também inicia dobrado.

### Questão 9: Inversão do Eixo X no Teclado
* **Ação:** Troca matemática nas condições das teclas `A` e `D`. 
* **Efeito prático:** Pressionar `A` agora soma ao eixo X (`x += 0.2`, movendo para a direita) e `D` subtrai do eixo X (`x -= 0.2`, movendo para a esquerda).

### Questão 10: Adição do Sistema de Zoom
* **Ação:** Declaração da variável `zoom = -6` aplicada na função `glTranslatef(x, y, zoom)`. Adição dos inputs `Z` (`zoom += 0.2`) e `X` (`zoom -= 0.2`).
* **Efeito prático:** Criação de controles de câmera de profundidade, permitindo aproximar ou afastar o plano visual usando o teclado.

---
## Script Completo Atualizado

> Aluno: [Seu Nome Aqui]
> Data: 11/03/2026

```python
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Posicionamento de tela (Eixo X centralizado)
x = 0 
y = 0 
r = 0

# Multiplicadores de escala definidos em 2x nativamente
ex = 2 
ey = 2 
ez = 2 

# Controle de profundidade para a câmera
zoom = -6 

def init():
    # Define o fundo da aplicação como branco absoluto
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
    
    # Translação do objeto considerando X, Y e o recuo da câmera (Zoom)
    glTranslatef(x, y, zoom)

    # Rotação apenas no eixo X
    # glRotatef(r, 1, 0, 0)  
    
    # Rotação mesclando os eixos X e Y
    glRotatef(r, 1, 1, 0)  

    glScalef(ex, ey, ez)
    glBegin(GL_TRIANGLES)

    # Define o desenho do objeto com a cor preta
    glColor3f(0, 0, 0)

    # Construção do triângulo com vértices expandidos
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
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    
                # Teclas de movimento (Horizontal invertido)
                if event.key == K_a:
                    x += 0.2 
                if event.key == K_d:
                    x -= 0.2 
                if event.key == K_w:
                    y += 0.2
                if event.key == K_s:
                    y -= 0.2
                
                # Teclas de profundidade / Câmera
                if event.key == K_z:
                    zoom += 0.2 
                if event.key == K_x:
                    zoom -= 0.2 
                    
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

        # Alteração de velocidade e sentido (Horário)
        r -= 10 

    pygame.quit()

if __name__ == "__main__":
    main()
