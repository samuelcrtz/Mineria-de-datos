import matplotlib.pyplot as plt
import numpy as np

datos_x = [162, 212, 220, 206, 152, 183, 167, 175, 156, 186, 183, 163, 163, 172, 194,
           168, 161, 164, 188, 187, 162, 192, 184, 206, 175, 154, 187, 212, 195, 205]
datos_y = [68.78, 74.11, 71.73, 69.88, 67.25, 68.78, 68.34, 67.01, 63.45, 71.19, 67.19, 65.80, 64.30, 67.97, 72.18,
           65.27, 66.09, 67.51, 70.10, 68.25, 67.89, 68.14, 69.08, 72.80, 67.42, 68.49, 68.61, 74.03, 71.52, 69.18]

plt.scatter(x=datos_x , y=datos_y, marker='o', c='black', s=5)
plt.title("Gráfico de puntos y estimación de la recta de regresión simple")
plt.xlabel("Altura")
plt.ylabel("Peso")
plt.show()

array_x = np.array(datos_x)
array_y = np.array(datos_y)

n = len(array_x)
sum_x = sum(array_x)
sum_y = sum(array_y)
sum_xy = sum(array_x*array_y)
sum_xx = sum(array_x*array_x)

s_xy = sum_xy-(1/n)*sum_x*sum_y
s_xx = sum_xx-(1/n)*sum_x**2

beta_1 = s_xy / s_xx
beta_0 = (1/n)*sum_y - beta_1*(1/n)*sum_x

print("La estimación de los parámetros para el modelo de regresión son: ")
print("beta1: ",(beta_1))
print("beta0: ",(beta_0))

plt.scatter(x=datos_x , y=datos_y, marker='o', c='black', s=5)
plt.plot(array_x, beta_0 + beta_1 * array_x, '-', c='red')
plt.title("Gráfico de puntos y estimación de la recta de regresión simple")
plt.xlabel("Altura")
plt.ylabel("Peso")
plt.show()