import threading

contador = 0

def incrementar():
    global contador
    temporal = contador
    print(f"Hilo {threading.current_thread().name} leyó: {contador}\n")
    for _ in range(100000):
        temporal += 1
    contador = temporal
    print(f"Hilo {threading.current_thread().name} escribió: {contador}\n")


hilos = []
for i in range(1,5):
    hilo = threading.Thread(target=incrementar, name=i)
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print(f"\nValor final del contador: {contador} (debería ser {len(hilos)*100000})")