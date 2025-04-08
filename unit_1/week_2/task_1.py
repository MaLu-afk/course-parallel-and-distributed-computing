import threading

contador = 0
lock = threading.Lock()

def incrementar(lock_activado):
    global contador
    print("Ejecutando hilo ...")
    for _ in range(100000):
        if lock_activado:
            with lock:
                temp = contador
                [i for i in range(1)]
                temp +=1
                contador = temp
        else:
            temp = contador
            [i for i in range(1)]
            temp +=1
            contador = temp
            
usar_lock = True
        
hilo1 = threading.Thread(target=incrementar, args=(usar_lock,))
hilo2 = threading.Thread(target=incrementar, args=(usar_lock,))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(f'Valor del contador: {contador}')
