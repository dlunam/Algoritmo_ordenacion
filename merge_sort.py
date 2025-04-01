import timeit

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    print(f"Lista dividida en izquierda: {leftHalf} y derecha: {rightHalf}")

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

'''
esta funcion se encarga de unir las diferentes sublistas(izquierda-L y la derecha-R), comparando el 1º elemento del la una sublista L 
con el 1º de la otra sublista-R. Se añade el elemento que sea menor (por ejemplo de la sublista-R) y se compara el elemento que no se 
ha escogido (sublista-L) con el 2º elemento de la sublista del que se añadido (sublista-R). Asi sucesivamente. 
'''
def merge(left, right): 
    print(f"Unificando {left} y {right}")
    result = []
    i = j = 0  #indican los indices de los elementos de la lista 

    while i < len(left) and j < len(right): #mientras haya al menos un elemento por recorrer en cada lista
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:]) #en el caso de que haya elementos por recorrer en UNA sola lista, se añaden al final
    result.extend(right[j:])

    print(f"Resultado de la unificación: {result}")

    return result

#Casos de prueba
unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
orderedArr = [-13, -10, 3, 6, 7, 15, 23.5, 55]
reversedArr = [55, 23.5, 15, 7, 6, 3, -10, -13]

# Medir el tiempo de ejecución para cada caso utilizando timeit
times = {}

# Caso 1: Lista aleatoria
print("\nCaso 1: Lista aleatoria")
time_unsorted = timeit.timeit(lambda: mergeSort(unsortedArr), number=1)
times["Lista aleatoria"] = time_unsorted

# Caso 2: Lista ordenada
print("\nCaso 2: Lista ordenada")
time_ordered = timeit.timeit(lambda: mergeSort(orderedArr), number=1)
times["Lista ordenada"] = time_ordered

# Caso 3: Lista invertida
print("\nCaso 3: Lista invertida")
time_reversed = timeit.timeit(lambda: mergeSort(reversedArr), number=1)
times["Lista invertida"] = time_reversed

# Al final, imprimir los tiempos
print("\nTiempos de ejecución finales:")
for case, time in times.items():
    print(f"{case}: {time:.6f} segundos")