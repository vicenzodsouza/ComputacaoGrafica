import numpy as np

P = np.array([-2, 4, 1, 1])

Mt = np.array([
    [1, 0, 0, 5],
    [0, 1, 0, 2],
    [0, 0, 1, 3],
    [0, 0, 0, 1]
])

P_linha = np.dot(Mt, P)

print("-" * 10)
print("EXERCÍCIO: TRANSFORMAÇÃO GEOMÉTRICA 3D")
print("-" * 20)
print("Matriz de Translação (Mt):")
print(Mt)
print("\nPonto Original (P):", P)
print("Ponto Transladado (P'):", P_linha)
print("-" * 30)
