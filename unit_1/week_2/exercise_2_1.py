import threading
import numpy as np
import time

def multiplicar_submatriz(A, B, C, fila_inicio, fila_fin, tiempos, idx):
    inicia = time.time()
    for i in range(fila_inicio, fila_fin):
        for j in range(B.shape[1]):
            C[i, j] = sum(A[i, k] * B[k, j] for k in range(A.shape[1]))
    termina = time.time()
    tiempos[idx] = termina - inicia
    print(f'{threading.current_thread().name} ha terminado. Tiempo: {tiempos[idx]} segundos\n')
    
def principal(A, B, C, numero_hilos):
    hilos = []
    tiempos = [0] * numero_hilos 

    if (numero_hilos <= f_ma) and (f_ma % numero_hilos == 0):
        lista_inicio_fin = []
        num_div = f_ma // numero_hilos
        for i in range(numero_hilos):
            lista_inicio_fin.append((i * num_div, (i + 1) * num_div))

        for i in range(numero_hilos):
            hilo = threading.Thread(
                target=multiplicar_submatriz,
                name=f'Hilo {i}',
                args=(A, B, C, lista_inicio_fin[i][0], lista_inicio_fin[i][1], tiempos, i))
            hilos.append(hilo)

        start = time.time()
        for hilo in hilos:
            hilo.start()

        for hilo in hilos:
            hilo.join()
        end = time.time()

        print(f"\nTiempo total de ejecución: {end - start} segundos")
        for i, t in enumerate(tiempos):
            print(f"Tiempo del Hilo {i}: {t} segundos")
    else:
        print("¡El número de hilos no es posible porque excede el número de filas!")
        print("o")
        print("¡No se puede dividir el número de filas entre el número de hilos de manera uniforme!")


f_ma = 80
c_ma = 80
f_mb = c_ma
c_mb = 80
numero_hilos_a = 1
numero_hilos_b = 8


print(f'Tamaño matriz: {f_ma}x{c_mb}')
print(f'Número de hilos a: {numero_hilos_a}')
print(f'Número de hilos b: {numero_hilos_b}')


A = np.random.randint(0, 10, (f_ma, c_ma))
B = np.random.randint(0, 10, (f_mb, c_mb))
C = np.zeros((f_ma, c_mb), dtype=int)

print("--------------------------------")
print("Prueba en a:")
principal(A, B, C, numero_hilos_a)
print("--------------------------------")
print("Prueba en b:")
principal(A, B, C, numero_hilos_b)
