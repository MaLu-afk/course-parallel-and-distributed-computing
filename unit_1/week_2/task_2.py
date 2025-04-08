import threading
import time

def descarga_concurrente():
    time.sleep(1)

def descarga_secuencial(num_descargas):
    start = time.time()
    for i in range(1, num_descargas+1):
        print(f'Descargando archivo: {i} ...')
        time.sleep(1)
    end = time.time()
    tiempo_total = end - start
    print(f'El tiempo total de descarga es: {tiempo_total}.')
    print(f'Descarga completa de los {num_descargas} archivos.')
    
cantidad_archivos = 5

hilos = []
for i in range(cantidad_archivos):
    hilo = threading.Thread(target=descarga_concurrente)
    hilos.append(hilo)
    
start = time.time()
for hilo in hilos:
    hilo.start()
for hilo in hilos:
    hilo.join()
end = time.time()
tiempo_total = end - start
print(f'El tiempo total de descarga es: {tiempo_total}.')
print(f'Descarga completa de los {cantidad_archivos} archivos.')
print("------------------------------------------")
descarga_secuencial(cantidad_archivos)