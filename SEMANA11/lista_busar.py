#Creamos la lista b
lista = [
    [1,2,3],
    [5,6,7],
    [8,9,10]
    ]

#Declaramos la funcion buscar con párametros x
def buscar(l,x):

    for i  in range(len(lista)):  #Iterador i recorre
        for j in range(len(lista[i])) : #Iterador j recorre las columnas
          if lista[i][j]  == x :  #Comparamos si la la iteración es igual al numero

              return i,j # retornamos ambos iteradores

    return None  # si no encuentra el numero que estamos buscando en la lista retorna None

print(lista)
numero = int(input("Que numero desea buscar: "))
print("El numero esta en la posición ",buscar(lista,numero))  #Imprimimos
#Fin