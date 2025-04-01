import random

def bogo_sort(lista):
    # Función para verificar si la lista está ordenada
    def esta_ordenada(lista):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                return False
        return True

    # Se repite hasta que la lista esté ordenada
    intentos = 0  # Contador para los intentos
    while not esta_ordenada(lista):
        random.shuffle(lista)  # Reordena aleatoriamente la lista
        intentos += 1
        print(f"Intento {intentos}: {lista}")  # Muestra cada intento
    
    return lista  # Devuelve la lista ya ordenada

# Lista con 8 elementos
mi_lista = [5, 3, 8, 6, 1, 7, 2, 4]

print("Resultado final:", bogo_sort(mi_lista))
