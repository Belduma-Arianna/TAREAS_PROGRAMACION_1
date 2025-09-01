def bubble_sort(fila):
    n = len(fila)  # calculo cuántos elementos tiene la fila
    for i in range(n): # Recorro la fila
        for j in range(0, n - i - 1):  # En cada pasada comparo los elementos que aún no están en su lugar
            if fila[j] > fila[j + 1]:# Si el número actual es mayor que el siguiente, están mal ordenados
                fila[j], fila[j + 1] = fila[j + 1], fila[j] # los intercambio

def ordenar_fila(matriz, i):
    # Ordena la fila i de la matriz m
    if 0 <= i < len(matriz): # Verifico que el número de fila esté dentro del rango válido
        bubble_sort(matriz[i]) # Ordeno la fila usando bubble_Sort
    else:
        print("Índice fuera del rango.")

# Definición de la matriz 3x3
lista = [
    [9, 2, 5],
    [3, 8, 1],
    [6, 7, 4]
]
#Imprimo la matriz original
print("Matriz original:")
for fila in lista:
    print(fila)

# Ordenar la fila 1 (segunda fila)
ordenar_fila(lista, 1)

# Vuelvo a imprimir la matriz para ver el resultado después de ordenar la fila
print("\nMatriz con la fila 1 ordenada:")
for fila in lista:
    print(fila)

#Fin