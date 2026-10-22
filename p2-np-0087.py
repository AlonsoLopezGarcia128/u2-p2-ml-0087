import numpy as np
# Alonso Lopez garcia NC = 0087 | Fecha 20/10/2026
# Ejemplos de numpy Numerical Python
print("---- Espaciado linealmente en array ---- 0087")
arre = np.linspace(start= 0, stop=1, num=5 )
print(arre)

print(" ")
print("---- matriz identidad en 2D array ---- 0087")
matriz = np.eye(3)
print(matriz)

print(" ")
print("---- Generar numeros al azar (aleatorios) en 2D array ---- 0087")
numale = np.random.random((3,4)) #  Genera 12 numeros aleatorios
print(numale)
print("----Generar 9 numeros aleatorios entre 0 y 1---- 0087")
numale = np.random.random((3,3)) #  Genera doce numeros aleatorios
print(numale)
# como generar nueve numeros aleatorios comprendidos entre 1 y 20 
# con numpy en un arreglo de 3x3 
print("----Generar 9 numeros aleatorios entre 1 y 20---- 0087")
arre = np.random.randint(1, 21, size=9).reshape(3,3)

print(arre)

print(" ")
print("Alonso Lopez garcia NC = 0087 | Fecha 20/10/2026")
