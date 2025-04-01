import random
import timeit

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

# Función para medir el tiempo de ejecución de bogo_sort
def medir_tiempo():
    mi_lista = [5, 3, 8, 6, 1, 7, 2, 4]  # Lista con 8 elementos
    bogo_sort(mi_lista)

# Medir el tiempo de ejecución usando timeit
tiempo = timeit.timeit('medir_tiempo()', globals=globals(), number=1)

print(f"\nTiempo de ejecución del BogoSort: {tiempo} segundos")

