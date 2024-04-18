import numpy as np
import matplotlib.pyplot as plt

# Supongamos que tenemos una imagen en escala de grises representada como una matriz
imagen = np.array([[10, 20, 30, 40],
                   [15, 25, 35, 45],
                   [20, 30, 40, 50],
                   [25, 35, 45, 55]])

# Calculamos la Descomposición en Valores Singulares (SVD) de la imagen
U, s, Vt = np.linalg.svd(imagen)

# Reconstruimos la imagen utilizando diferentes cantidades de componentes principales (valores singulares)
num_componentes = [1, 2, 3, 4]
reconstrucciones = []

for k in num_componentes:
    reconstruccion = np.dot(U[:, :k], np.dot(np.diag(s[:k]), Vt[:k, :]))
    reconstrucciones.append(reconstruccion)

# Visualizamos las reconstrucciones de la imagen
plt.figure(figsize=(12, 6))
for i in range(len(num_componentes)):
    plt.subplot(2, 2, i + 1)
    plt.imshow(reconstrucciones[i], cmap='gray')
    plt.title(f'Componentes principales = {num_componentes[i]}')
    plt.axis('off')

plt.tight_layout()
plt.show()
#aplicamos la Descomposición en Valores Singulares (SVD) para descomponerla en componentes principales.
#Luego, reconstruimos la imagen utilizando diferentes cantidades de componentes principales
#permite ver cómo la calidad de la imagen reconstruida varía con el número de componentes principales utilizados. 
#permitiendo reducir su dimensionalidad mientras se conserva la mayor cantidad posible de información visual.
