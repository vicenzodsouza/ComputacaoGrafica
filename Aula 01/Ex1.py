import math

def calculaTamanho(x, y, z):
  return math.sqrt(x*x + y*y + z*z)

def normalizaVetor(x, y, z):
  tam = calculaTamanho(x, y, z)
  if tam == 0:
    return 0.0, 0.0, 0.0
  return x/tam, y/tam, z/tam

def adicionaVetor(x1, y1, z1, x2, y2, z2):
  return x1 + x2, y1 + y2, z1 + z2

def subtraiVetor(x1, y1, z1, x2, y2, z2):
  return x1 - x2, y1 - y2, z1 - z2

def multiplicaVetor(x, y, z, scalar):
  return x * scalar, y * scalar, z * scalar

def divideVetor(x, y, z, scalar):
  if scalar == 0:
    print("Não é possível dividir por zero.")
    return x, y, z
  return x / scalar, y / scalar, z / scalar

x=float(input("Digite o valor de x: "))
y=float(input("Digite o valor de y: "))
z=float(input("Digite o valor de z: "))

op = 0

while(op != 7):
  print("\nEscolha uma operação:")
  print("1. Calcular o tamanho do vetor")
  print("2. Normalizar o vetor")
  print("3. Adicionar outro vetor")
  print("4. Subtrair outro vetor")
  print("5. Multiplicar o vetor por um escalar")
  print("6. Dividir o vetor por um escalar")
  print("7. Sair")

  try:
    op=int(input("Digite a opção desejada: "))
  except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
    continue

  if op == 1:
    tam = calculaTamanho(x,y,z)
    print(f"O tamanho do vetor é: {tam:.2f}")
  elif op == 2:
    nx, ny, nz = normalizaVetor(x, y, z)
    print(f"O vetor normalizado é: ({nx:.2f}, {ny:.2f}, {nz:.2f})")
  elif op == 3:
    try:
      x2 = float(input("Digite o valor de x para o segundo vetor: "))
      y2 = float(input("Digite o valor de y para o segundo vetor: "))
      z2 = float(input("Digite o valor de z para o segundo vetor: "))
      ax, ay, az = adicionaVetor(x, y, z, x2, y2, z2)
      print(f"A soma dos vetores é: ({ax:.2f}, {ay:.2f}, {az:.2f})")
      x, y, z = ax, ay, az
      print(f"O vetor atual agora é: ({x:.2f}, {y:.2f}, {z:.2f})")
    except ValueError:
      print("Entrada inválida. Por favor, digite um número.")
  elif op == 4:
    try:
      x2 = float(input("Digite o valor de x para o segundo vetor: "))
      y2 = float(input("Digite o valor de y para o segundo vetor: "))
      z2 = float(input("Digite o valor de z para o segundo vetor: "))
      sx, sy, sz = subtraiVetor(x, y, z, x2, y2, z2)
      print(f"A subtração dos vetores é: ({sx:.2f}, {sy:.2f}, {sz:.2f})")
      x, y, z = sx, sy, sz
      print(f"O vetor atual agora é: ({x:.2f}, {y:.2f}, {z:.2f})")
    except ValueError:
      print("Entrada inválida. Por favor, digite um número.")
  elif op == 5:
    try:
      scalar = float(input("Digite o valor escalar para multiplicação: "))
      mx, my, mz = multiplicaVetor(x, y, z, scalar)
      print(f"O vetor multiplicado é: ({mx:.2f}, {my:.2f}, {mz:.2f})")
      x, y, z = mx, my, mz
      print(f"O vetor atual agora é: ({x:.2f}, {y:.2f}, {z:.2f})")
    except ValueError:
      print("Entrada inválida. Por favor, digite um número.")
  elif op == 6:
    try:
      scalar = float(input("Digite o valor escalar para divisão: "))
      dx, dy, dz = divideVetor(x, y, z, scalar)
      if scalar != 0:
        print(f"O vetor dividido é: ({dx:.2f}, {dy:.2f}, {dz:.2f})")
        x, y, z = dx, dy, dz
        print(f"O vetor atual agora é: ({x:.2f}, {y:.2f}, {z:.2f})")
    except ValueError:
      print("Entrada inválida. Por favor, digite um número.")
  elif op == 7:
    print("Saindo do programa.")
  else:
    print("Opção inválida. Por favor, escolha uma opção entre 1 e 7.")
