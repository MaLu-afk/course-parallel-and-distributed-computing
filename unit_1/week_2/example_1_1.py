import threading

contador = 0
num_hilos = 16
iteraciones = 10000

lock = threading.Lock()

def incrementar_sin_lock():
    global contador
    
    for _ in range(iteraciones):
        temp = contador
        [x for x in range(50)]
        contador = temp +1

def incrementar_con_lock():
    global contador
    
    for _ in range(iteraciones):
        with lock:
            temp = contador 
            [x for x in range(50)]
            contador = temp +1

def ejecutar_prueba(con_lock):
    global contador
    contador = 0
    
    hilos = []
    for _ in range(num_hilos):
        target = incrementar_con_lock if con_lock else incrementar_sin_lock
        hilo = threading.Thread(target=target)
        hilos.append(hilo)
        hilo.start()
        
    for hilo in hilos:
        hilo.join()
        
    numero_esperado = num_hilos * iteraciones
    
    print(f'{"CON LOCK" if con_lock else "SIN LOCK"}')
    print(f'Valor esperado: {numero_esperado}')
    print(f'Valor obtenido: {contador}')

print("DEMOSTRACIÓN DE CONDICIÓN DE CARRERA")
print("====================================")

ejecutar_prueba(con_lock=False)
ejecutar_prueba(con_lock=True)

    