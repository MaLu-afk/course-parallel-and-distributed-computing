## ***1. Operaciones limitadas por E/S y por CPU***

```python
import requests

response = requests.get('https://www.example.com/')
items = response.headers.items()
headers = [f'{key}: {header}' for key, header in items]
formatted_headers = '\n'.join(headers) 

with open('unit_1/week_1/headers.txt', 'w') as file:
 file.write(formatted_headers)
```

Este código realiza tres operaciones principales: solicitud
HTTP (I/O-bound), procesamiento de datos (CPU-bound) y escritura 
en un archivo (I/O-bound).

Las operaciones de I/O-bound, como la descarga y la escritura, suelen 
generar esperas, lo que puede ralentizar los programas si el número 
de solicitudes aumenta. El uso de asynchronous I/O-bound permite ejecutar 
otras tareas mientras una operación de I/O-bound está en espera, lo que 
mejora el rendimiento cuando hay múltiples solicitudes o archivos por 
procesar.

En cuanto a CPU-bound, el formateo de datos en este caso es simple, 
ya que solo toma los encabezados y los concatena. El problema surgiría 
si el procesamiento de los encabezados incluyera tareas como parsers 
complejos, compresión u operaciones con matrices. Una alternativa para 
optimizar estos casos sería usar multiprocessing para aprovechar múltiples 
núcleos del procesador.

Este código ayuda a comprender cómo se presentan casos de I/O-bound en 
sitios web y cómo impactan en el rendimiento de la CPU.

---
Ejemplos:

### **Concurrencia:**
Imaginemos que un panadero desea preparar dos pasteles diferentes. 
Primero, debe precalentar el horno, pero no es necesario esperar a 
que termine de precalentarse para comenzar a preparar los pasteles. 
Podemos empezar a mezclar la harina, el azúcar y los huevos mientras 
el horno se calienta.Ahora, tampoco es necesario esperar a que el 
primer pastel termine de hornearse para empezar con el segundo. 
Mientras el primero está en el horno, podemos preparar la masa del 
segundo. Aquí es donde se presenta la concurrencia: se trata de cómo 
varias tareas pueden ejecutarse de manera intercalada, aprovechando 
los tiempos de espera de una tarea para avanzar con otra, pero sin 
necesariamente ejecutarse al mismo tiempo. A esto se le conoce como 
concurrencia.

### **Paralelismo:**
Si hablamos de concurrencia, no nos referimos a que las tareas se 
ejecutan al mismo tiempo. Eso sucede en el paralelismo.
Tomando el mismo caso, imaginemos ahora que tenemos a un segundo 
panadero. Cada uno se dedicaría a preparar su propio pastel y, de 
esa manera, estarían realizando dos tareas al mismo tiempo. A esto 
se le conoce como paralelismo, donde dos o más tareas se ejecutan 
simultáneamente.

### **Diferencia entre concurrencia y paralelismo:**

Cuando hablamos de concurrencia, podemos decir que múltiples tareas
se ejecutan independientemente una de otra. Podemos tener concurrencia
en una CPU de un solo núcleo, ya que la operación empleará 
multitarea preventiva para cambiar entre tareas. Sin embargo, 
paralelismo ejecuta dos o más tareas al mismo tiempo. En máquinas 
con un solo núcleo, esto es imposible. Para hacerlo posible, se
necesita una CPU con múltiples núcleos para ejecutar tareas juntas. 

Mientras paralelismo implica concurrencia, la concurrencia no siempre
implica paralelismo. 

### **Multitarea:**

#### 1. Multitarea preventiva: 
- En este modelo, permitimos que el sistema operativo decida cómo cambiar 
las tareas en ejecución mediante un proceso llamado segmentación temporal
(time slicing). Cuando el sistema operativo realiza el cambio, lo llamamos 
expropiación (preempting). Todo el funcionamiento interno depende del 
sistema operativo. Se implementa los llamados múltiples hilos (threads) o 
múltiples procesos. 
#### 2. Multitarea cooperativa:
- En este modelo, ya no se depende del sistema operativo por completo para 
cambiar entre tareas, se programa puntos explícitos en la aplicación
donde se permite que otras se ejecuten. Las tareas operan bajo el esquema
de cooperación, donde se indica explícitamente: "Pauso mi tarea por un 
momento; pueden ejecutar otras tareas".

### **Comprensión de procesos, subprocesos, multihilos y multiprocesamiento**

#### 1. Procesos:
- Se trata de una aplicación que se ejecuta en su propio espacio de memoria, 
al que otras aplicaciones no tienen acceso. Varios procesos pueden ejecutarse 
en un mismo equipo; por ejemplo, si utilizamos una CPU con varios núcleos, 
podemos ejecutar múltiples procesos simultáneamente. En el caso de una CPU 
con un solo núcleo, es posible ejecutar varias aplicaciones al mismo tiempo 
mediante segmentación temporal (time slicing). Cuando el sistema operativo 
emplea este mecanismo, cambia automáticamente entre los procesos en 
ejecución después de cierto tiempo.

#### 2. Hilos:
- Los hilos pueden considerarse procesos de menor peso. Además, representan 
la mínima unidad de ejecución que un sistema operativo puede gestionar. 
A diferencia de los procesos, los hilos no poseen memoria propia; 
en cambio, comparten la memoria del procesos que los creó. Los hilos
siempre están asociados al proceso que los generó. Un proceso, 
siempre tendrá un hilo asociado (hilo principal). Un proceso también puede
crear hilos adicionales llamados hilos de trabajo. Al igual que los 
procesos, los hilos pueden ejecutarse en paralelo en CPUs multinúcleo. 

## ***2. Procesos y subprocesos en una aplicación sencilla de Python***

```python
import os
import threading

print(f'Proceso de Python en ejecución con id de proceso: {os.getpid()}')

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Python está ejecutando actualmente {total_threads} hilo(s).')
print(f'El hilo actual es {thread_name}.') 
```

```plaintext
SALIDA:
Proceso de Python en ejecución con id de proceso: 13524
Python está ejecutando actualmente 1 hilo(s).
El hilo actual es MainThread.
```

Este código simplemente muestra el ID del proceso en el que se ejecuta
Python y la cantidad de hilos activos en ese momento. Esto permite 
conocer cómo Python maneja los hilos. 

## ***3. Creación de una aplicación Python multihilo***

```python
import threading

def hello_from_thread():
    print(f'Hola desde el hilo {threading.current_thread()}!')
    
    
hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Python está ejecutando actualmente {total_threads} hilo(s).')
print(f'El hilo actual es {thread_name}.')
 
hello_thread.join()
```

```plaintext
SALIDA:
Hola desde el hilo <Thread(Thread-1 (hello_from_thread), started 27672)>!
Python está ejecutando actualmente 2 hilo(s).
El hilo actual es MainThread.
```

En este código definimos una función que imprime un mensaje desde un hilo.
Se crea e inicia un hilo secundario, se obtiene el número total de hilos 
y después el nombre del hilo actual. 

## ***4. Creando múltiples procesos***

```python

```


Es