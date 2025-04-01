def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

'''
esta funcion se encarga de unir las diferentes sublistas(izquierda-L y la derecha-R), comparando el 1º elemento del la una sublista L 
con el 1º de la otra sublista-R. Se añade el elemento que sea menor (por ejemplo de la sublista-R) y se compara el elemento que no se 
ha escogido (sublista-L) con el 2º elemento de la sublista del que se añadido (sublista-R). Asi sucesivamente. 
'''
def merge(left, right):
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

    return result

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)