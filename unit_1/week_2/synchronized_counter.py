import threading
import time

contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    with lock:
        temporal = contador
        print(f"Hilo {threading.current_thread().name} leyó: {temporal}")
        time.sleep(0.1)
        temporal += 1
        contador = temporal
        print(f"Hilo {threading.current_thread().name} escribió: {temporal}")

hilo1 = threading.Thread(target=incrementar, name="Hilo-1")
hilo2 = threading.Thread(target=incrementar, name="Hilo-2")

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(f"\nValor final del contador: {contador} (debería ser 2)")