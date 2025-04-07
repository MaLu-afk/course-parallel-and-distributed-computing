import threading
import time
import random
from collections import deque

# Cola compartida y condición para sincronizar
cola = deque()
condicion = threading.Condition()

def productor():
    for i in range(10):
        time.sleep(random.uniform(0.5, 1.5))
        with condicion:
            item = f'item-{i}'
            cola.append(item)
            print(f'Productor produjo: {item}')
            condicion.notify()

def consumidor():
    for i in range(10):
        with condicion:
            while not cola:
                condicion.wait()
            item = cola.popleft()
            print(f'Consumidor consumió: {item}')
        time.sleep(random.uniform(0.5, 1))

hilo_prod = threading.Thread(target=productor)
hilo_cons = threading.Thread(target=consumidor)

hilo_prod.start()
hilo_cons.start()

hilo_prod.join()
hilo_cons.join()