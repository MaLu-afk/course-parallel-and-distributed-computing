import threading
import time

contador = 0
num_hilos = 8

lock = threading.Lock()

def incrementar_sin_lock():
    global contador
    for _ in range(100000):
        contador +=1

def incrementar_con_lock():
    global contador
    with lock:
        for _ in range(100000):
            contador +=1
        
# Ejecución sin lock
hilos_1 = []
for i in range (1,num_hilos+1):
    hilo = threading.Thread(target=incrementar_sin_lock)
    hilos_1.append(hilo)
    hilo.start()
    
for hilo in hilos_1:
    hilo.join()

print(f'Valor sin lock puede ser erroneo: {contador}')

# Ejecución con lock
contador = 0

hilos_2 = []
for i in range (1,num_hilos+1):
    hilo = threading.Thread(target=incrementar_con_lock)
    hilos_2.append(hilo)
    hilo.start()
    
for hilo in hilos_2:
    hilo.join()
    
print("Valor con lock (correcto):", contador)

