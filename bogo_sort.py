import random

def bogo_sort(lista):
    # Función para verificar si la lista está ordenada
    def esta_ordenada(lista):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                return False
        return True

    # Se repite hasta que la lista esté ordenada
    while not esta_ordenada(lista):
        random.shuffle(lista)  # Reordena aleatoriamente la lista
    
    return lista  # Devuelve la lista ya ordenada

# Usamos un nombre distinto a 'list' para evitar confusión
mi_lista = [5, 3, 8, 6, 1, 7]

print(bogo_sort(mi_lista))
