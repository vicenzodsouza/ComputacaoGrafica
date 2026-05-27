# Aplicação modificada de OpenGL renderizando formas em novas posições e cores
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

# Renomeação de variáveis globais
janela_principal = None
vao_forma_quadrada = None
vao_forma_triangular = None

programa_shader_quadrado = None
programa_shader_triangulo = None

LARGURA_TELA = 1000
ALTURA_TELA = 800

def callback_redimensionar(window, w, h):
    global LARGURA_TELA, ALTURA_TELA
    LARGURA_TELA = w
    ALTURA_TELA = h

def configurar_opengl():
    global janela_principal, LARGURA_TELA, ALTURA_TELA

    glfw.init()

    # Criação da janela com novo título
    janela_principal = glfw.create_window(LARGURA_TELA, ALTURA_TELA, "OpenGL - Novas Formas e Cores", None, None)
    if not janela_principal:
        glfw.terminate()
        exit()

    glfw.set_window_size_callback(janela_principal, callback_redimensionar)
    glfw.make_context_current(janela_principal)

    print("Placa de vídeo: ", glGetString(GL_RENDERER))
    print("Versão do OpenGL: ", glGetString(GL_VERSION))

def configurar_shaders_quadrado():
    global programa_shader_quadrado

    codigo_vertex = """
    #version 400
    layout(location = 0) in vec3 posicao_vertice;
    layout(location = 1) in vec3 cor_vertice;
    out vec3 cor_fragmento;
    void main() {
        cor_fragmento = cor_vertice;
        gl_Position = vec4(posicao_vertice, 1.0);
    }
    """

    codigo_fragment = """
    #version 400
    in vec3 cor_fragmento;
    out vec4 cor_final;
    void main() {
        cor_final = vec4(cor_fragmento, 1.0);
    }
    """

    vs = OpenGL.GL.shaders.compileShader(codigo_vertex, GL_VERTEX_SHADER)
    fs = OpenGL.GL.shaders.compileShader(codigo_fragment, GL_FRAGMENT_SHADER)
    programa_shader_quadrado = OpenGL.GL.shaders.compileProgram(vs, fs)

def configurar_shaders_triangulo():
    global programa_shader_triangulo

    codigo_vertex = """
    #version 400
    layout(location = 0) in vec3 posicao_vertice;
    layout(location = 1) in vec3 cor_vertice;
    out vec3 cor_fragmento;
    void main() {
        cor_fragmento = cor_vertice;
        gl_Position = vec4(posicao_vertice, 1.0);
    }
    """

    codigo_fragment = """
    #version 400
    in vec3 cor_fragmento;
    out vec4 cor_final;
    void main() {
        cor_final = vec4(cor_fragmento, 1.0);
    }
    """

    vs = OpenGL.GL.shaders.compileShader(codigo_vertex, GL_VERTEX_SHADER)
    fs = OpenGL.GL.shaders.compileShader(codigo_fragment, GL_FRAGMENT_SHADER)
    programa_shader_triangulo = OpenGL.GL.shaders.compileProgram(vs, fs)

def carregar_triangulo():
    global vao_forma_triangular

    vao_forma_triangular = glGenVertexArrays(1)
    glBindVertexArray(vao_forma_triangular)

    # Modificado: Triângulo movido para a esquerda e invertido (de cabeça para baixo)
    coordenadas = [
         -0.2, -0.5, 0.0,
         -0.8, -0.5, 0.0,
         -0.5,  0.5, 0.0
    ]

    # Modificado: Paleta de cores alterada (tons frios e roxos)
    cores_rgb = [
         0.0, 1.0, 1.0,  # Ciano
         0.5, 0.0, 1.0,  # Roxo/Plum
         1.0, 0.0, 0.5   # Magenta escuro
    ]

    coordenadas = np.array(coordenadas, dtype=np.float32)
    cores_rgb = np.array(cores_rgb, dtype=np.float32)

    vbo_pos = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_pos)
    glBufferData(GL_ARRAY_BUFFER, coordenadas, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    vbo_col = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_col)
    glBufferData(GL_ARRAY_BUFFER, cores_rgb, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def carregar_quadrado():
    global vao_forma_quadrada

    vao_forma_quadrada = glGenVertexArrays(1)
    glBindVertexArray(vao_forma_quadrada)

    # Modificado: Quadrado movido para o lado direito e ligeiramente deslocado para cima
    coordenadas = [
        # TRIÂNGULO 1
         0.1,  0.7, 0.0,
         0.9,  0.7, 0.0,
         0.1, -0.3, 0.0,

        # TRIÂNGULO 2
         0.9,  0.7, 0.0,
         0.9, -0.3, 0.0,
         0.1, -0.3, 0.0
    ]

    # Modificado: Nova distribuição RGB nas diagonais do quadrado
    cores_rgb = [
         0.0, 0.8, 0.4,  # Verde menta
         0.1, 0.2, 0.6,  # Azul escuro
         1.0, 0.4, 0.0,  # Laranja aceso

         0.1, 0.2, 0.6,  # Azul escuro
         0.9, 0.9, 0.1,  # Amarelo lima
         1.0, 0.4, 0.0   # Laranja aceso
    ]

    coordenadas = np.array(coordenadas, dtype=np.float32)
    cores_rgb = np.array(cores_rgb, dtype=np.float32)

    vbo_pos = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_pos)
    glBufferData(GL_ARRAY_BUFFER, coordenadas, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    vbo_col = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_col)
    glBufferData(GL_ARRAY_BUFFER, cores_rgb, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def loop_renderizacao():
    global janela_principal

    # Fundo de tela alterado sutilmente para um cinza azulado muito escuro
    glClearColor(0.08, 0.12, 0.16, 1.0)

    while not glfw.window_should_close(janela_principal):
        glClear(GL_COLOR_BUFFER_BIT)

        # Renderiza o Quadrado modificado à direita
        glUseProgram(programa_shader_quadrado)
        glBindVertexArray(vao_forma_quadrada)
        glDrawArrays(GL_TRIANGLES, 0, 6)

        # Renderiza o Triângulo modificado à esquerda
        glUseProgram(programa_shader_triangulo)
        glBindVertexArray(vao_forma_triangular)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.poll_events()
        glfw.swap_buffers(janela_principal)

    glfw.terminate()

def main():
    configurar_opengl()

    carregar_quadrado()
    carregar_triangulo()

    configurar_shaders_quadrado()
    configurar_shaders_triangulo()

    loop_renderizacao()

if __name__ == "__main__":
    main()