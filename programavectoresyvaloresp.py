import numpy as np

# Definimos una matriz de ejemplo simétrica
A = np.array([[6, 2, 1],
              [2, 3, 1],
              [1, 1, 1]])

# Calculamos los valores propios y los vectores propios utilizando np.linalg.eig()
eigenvalues, eigenvectors = np.linalg.eig(A)

# Imprimimos los resultados utilizando np.linalg.eig()
print("Valores propios (np.linalg.eig()):")
print(eigenvalues)
print("\nVectores propios (np.linalg.eig()):")
print(eigenvectors)

# Calculamos los valores propios y los vectores propios utilizando np.linalg.eigh() para matrices simétricas
eigenvalues_symm, eigenvectors_symm = np.linalg.eigh(A)

# Imprimimos los resultados utilizando np.linalg.eigh()
print("\nValores propios (np.linalg.eigh()):")
print(eigenvalues_symm)
print("\nVectores propios (np.linalg.eigh()):")
print(eigenvectors_symm)
