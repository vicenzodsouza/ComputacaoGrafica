# Respostas aos Exercícios de Computação Gráfica

---

## EX11)

**Pergunta:** Ao pressionar as teclas de movimento, o que acontece com os dois triângulos? Por que eles se movem em sincronia?

**Resposta:** Ao acionar os comandos de direção (W, A, S, D), nota-se que ambos os triângulos realizam o deslocamento de forma **conjunta**. Esse comportamento ocorre porque a função de translação (`glTranslatef(x, y, -6)`) é inserida logo após o `glLoadIdentity()`, agindo sobre a matriz de modelagem global antes de qualquer geometria ser renderizada. 

Como o OpenGL funciona como uma máquina de estados, essa transformação aplicada no início do ciclo de desenho afeta todos os elementos subsequentes. Sem o uso de comandos para isolar as matrizes (como `glPushMatrix` e `glPopMatrix`), os dois objetos acabam compartilhando o mesmo referencial de coordenadas, resultando nesse movimento "travado" entre eles.

---

## EX13)

**Pergunta:** O que aconteceu? Qual a diferença entre o giro dos triângulos?

**Resposta:** Neste cenário, cada triângulo passou a responder a uma variável de rotação distinta, com taxas de incremento diferentes (como `r += 3` e `r2 += 2`). O resultado visual é que os objetos agora giram em **velocidades dessincronizadas**, com um completando a volta mais rápido que o outro. 

Isso prova que, ao resetar a matriz com `glLoadIdentity()` entre os desenhos e utilizar variáveis exclusivas para cada entidade, conseguimos definir comportamentos individuais de animação para cada peça da cena.

---

## EX14)

**Pergunta:** O que acontece consigo controlar cada triângulo separadamente agora?

**Resposta:** Exatamente. Agora que cada objeto possui seu próprio bloco de transformações isolado e variáveis de estado dedicadas (para posição, rotação, escala e zoom), os triângulos tornaram-se **entidades independentes** no espaço 3D. 

A principal mudança é a autonomia: as ações realizadas em um triângulo (como o movimento pelas teclas WASD ou o zoom pelo mouse) não interferem nas propriedades do outro (controlado por IJKL ou C/V). Essa estrutura é fundamental para organizar cenas complexas, permitindo que cada elemento gráfico seja manipulado como um "objeto" único, com vida própria dentro do ambiente virtual.
