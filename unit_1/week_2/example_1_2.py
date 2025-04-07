import threading
import time

sem = threading.Semaphore(3)

def tarea_con_recurso(id_tarea):
    print(f'Tarea {id_tarea} esperando para acceder al recurso ...\n')
    with sem:
        print(f'Tarea {id_tarea} accediendo al recurso.\n')
        time.sleep(2)
        print(f'Tarea {id_tarea} liberando recurso.\n')

num_hilos = 6
hilos = [threading.Thread(target=tarea_con_recurso, args=(i,)) for i in range(num_hilos)]
for hilo in hilos:
    hilo.start()
for hilo in hilos:
    hilo.join()