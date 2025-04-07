# I. Concurrencia vs. Paralelismo
## 1. Concurrencia:

La concurrencia ocurre cuando múltiples tareas se ejecutan alternadamente, esto no necesariamente al mismo tiempo.

### Ejemplo: Descargar archivos (concurrencia con hilos I/O-bound).

Supongamos que tenemos un programa que necesita descargar cinco archivos grandes desde un servidor.

#### Pasos:

1. Crear hilos
    + El programa crea cinco hilos (uno para cada uno).
    + Cada hilo inicia la solicitud de descarga al servidor.
2. Intercalado de procesos
    + Mientras un hilo está a la espera de datos del servidor, el SO pasa la ejecución a otro hilo.
    + Esto permite aprovechar el tiempo de espera para procesar otras descargas.
3. Finalización
    + Cuando el hilo recibe datos del servidor, procesa esa información y luego vuelve a esperar. Este ciclo se repite hasta que se termine de descargar. 

#### Beneficios:
+ Se maximiza la eficiencia del sistema y se minimiza el tiempo total de ejecución, ya que los hilos aprovechan tiempos de inactividad. Sin concurrencia se esperaría que un archivo termine de descargarse para pasar a la siguiente descarga.

## 2. Paralelismo:

El paralelismo ocurre cuando múltiples tareas se ejecutan al mismo tiempo en diferentes núcleos de CPU. 

### Ejemplo: Procesar número primos (paralelismo con procesos CPU-bound).

Supongamos que tenemos un programa que calcula los números primos entre 1 y 10 millones, y queremos acelerar el proceso utilizando cuatro núcleos de CPU.

#### Pasos:

1. Dividir el trabajo
    + El rango de números (1 a 10 millones) se dividen en cuatro partes iguales:
        - Núcleo 1: 1 a 2.5 millones.
        - Núcleo 2: 2.5 a 5 millones.
        - Núcleo 3: 5 a 7.5 millones.
        - Núcleo 4: 7.5 a 10 millones.

2. Crear procesos   
    + Cada núcleo de la CPU ejecuta un proceso independiente que calcula los números primos en su rango asignado.
3. Ejecución simultánea
    + Cada núcleo trabaja simultáneamente, sin interferir entre ellos, realizando cálculos en paralelo.
4. Recolección de resultados
    + Terminado la ejecución de los procesos, sus resultados (los números primos de cada rango) se combinan para producir la lista final.

#### Beneficio: 
+ El trabajo se divide entre núcleos, reduciones significativamente el tiempo de cálculo en comparación con un solo núcleo.

## Diferencias:
+ **Concurrencia:** Las tareas son ejecutadas intercaladas. Ideal para I/O-bound, donde hay tiempo de espera significativo.
+ **Paralelo:** Las tareas son ejecutadas en múltiples núcleos. Ideal para CPU-bound, donde los cálculos demandan recursos intensivos.

# II. Problemas clave
## 1. Race conditions: 

Un race condition ocurre cuando múltiples hilos o procesos acceden y modifican un recurso compartido de forma no sincronizada. Esto puede generar errores impredecibles.

### Ejemplo práctico: 

Supongamos que tenemos un contador global llamado `contador` que debe incrementar dos hilos simultáneamente.

```python
import threading
import time

contador = 0

def incrementar():
    global contador
    temporal = contador
    print(f"Hilo {threading.current_thread().name} leyó: {temporal}")
    time.sleep(0.1)
    temporal += 1
    contador = temporal
    print(f"Hilo {threading.current_thread().name} escribió: {temporal}")

# Crear 2 hilos
hilo1 = threading.Thread(target=incrementar, name="Hilo-1")
hilo2 = threading.Thread(target=incrementar, name="Hilo-2")

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(f"\nValor final del contador: {contador} (debería ser 2)")
```

```plaintext
SALIDA:
Hilo Hilo-1 leyó: 0
Hilo Hilo-2 leyó: 0
Hilo Hilo-2 escribió: 1
Hilo Hilo-1 escribió: 1

Valor final del contador: 1 (debería ser 2)
```

Este código, nos ayuda a entender que en escenarios reales, los retardos son comunes en sistemas distribuidos o con alta concurrencia. De esa manera, se puede notar el problema de condición de carrera.

#### Pasos: 
1. Inicio de los hilos
    + El hilo A y el hilo B ejecutan la función incrementar() al mismo tiempo.
2. Acceso al recurso compartido
    + El hilo A lee contador = 0 y guarda en la variable temporal.
    + Antes de que el hilo A pueda escribir el nuevo valor (1) en el contador, hilo B también lee contador = 0.
3. Resultado incorrecto
    + Ambos hilos escriben contador = 1, ignorando el trabajo del otro hilo. El valor correcto debería haber sido contador = 2.

#### Solución: Utilizar técnica de sincronización, como un lock:

```python
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
```

```plaintext
SALIDA:
Hilo Hilo-1 leyó: 0
Hilo Hilo-1 escribió: 1
Hilo Hilo-2 leyó: 1
Hilo Hilo-2 escribió: 2

Valor final del contador: 2 (debería ser 2)
```

Gracias al uso de Lock, podemos garantizar que no haya condiciones de carrera al acceder a un recurso compartido, ya que bloquea el acceso cuando un hilo está usando la variable compartida, impidiendo que otros hilos o tareas se ejecuten en ese mismo fragmento de código.

#### Ejercicio 1: Race Conditions con Threads

**Objetivo:** Mostrar cómo el acceso no controlado a recursos compartidos causa incosistencias.

```python
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

print(f"\nValor final del contador: {contador} (debería ser {len(hilos)})")
```

```plaintext
SALIDA:
Hilo 1 leyó: 0
Hilo 1 escribió: 100000
Hilo 2 leyó: 100000
Hilo 3 leyó: 100000
Hilo 2 escribió: 200000
Hilo 4 leyó: 200000
Hilo 4 escribió: 300000
Hilo 3 escribió: 200000

Valor final del contador: 200000 (debería ser 400000)
```

**Discusión:** 
+ ¿Por qué el resultado no es 400,000?

+ Demostrar que contador += 1 no es una operación atómica.

---
---

# Ejemplos

## Mecanismos de sincronización y comunicación:

A continuación se muestra los mecanismo más comunes:
+ Uso de los locks (cerrojos) para proteger las regiones críticas.
+ Semáforos para gestionar acceso a recursos compartidos.
+ Variables de condición y eventos para la señalización entre hilos.

### Ejemplo 1: Condición de carrera y uso de lock

En este ejemplo se muestra la situación donde dos hilos intenan modificar una variable compartida llamada contador, causando la condición de carrera. Luego otra usando Lock.

```python
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
```

```plaintext
SALIDA:
DEMOSTRACIÓN DE CONDICIÓN DE CARRERA
====================================
SIN LOCK
Valor esperado: 160000
Valor obtenido: 158354
CON LOCK
Valor esperado: 160000
Valor obtenido: 160000
```

Este código muestra cómo una condición de carrera (es decir, la cantidad de iteraciones que cada hilo puede realizar) puede modificar un recurso compartido y provocar datos corruptos. En la función sin lock, se puede notar que durante la iteración se agrega [x for x in range(50)] para simular el procesamiento de una operación que, a su vez, puede variar, como por ejemplo el pago de un cliente, momento en el cual otro hilo puede intervenir y modificar el recurso. En la segunda función, se añade el lock, lo que permite manejar operaciones de forma atómica; es decir, si una sección del código se está ejecutando (utilizando el recurso), ningún otro hilo puede intervenir hasta que finalice. 

### Ejemplo 2: Uso de semáforos para limitar acceso a recursos

En este caso se simula un recurso limitado (por ejemplo, a una conexión a base de datos) y se utiliza un semáforo para limitar el número de hilos que pueden acceder simultáneamente.

```python
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
```

```plaintext
SALIDA:
Tarea 0 esperando para acceder al recurso ...
Tarea 1 esperando para acceder al recurso ...
Tarea 0 accediendo al recurso.
Tarea 1 accediendo al recurso.
Tarea 2 esperando para acceder al recurso ...
Tarea 2 accediendo al recurso.
Tarea 3 esperando para acceder al recurso ...
Tarea 4 esperando para acceder al recurso ...
Tarea 5 esperando para acceder al recurso ...
Tarea 0 liberando recurso.
Tarea 1 liberando recurso.
Tarea 2 liberando recurso.
Tarea 3 accediendo al recurso.
Tarea 4 accediendo al recurso.
Tarea 5 accediendo al recurso.
Tarea 3 liberando recurso.
Tarea 4 liberando recurso.
Tarea 5 liberando recurso.
```

Este código muestra un acceso flexible para un número de hilos. Aunque hemos solicitado la creación de 6 hilos, solo 3 serán ejecutados y podrán compartir la sección crítica, lo que simula el control de recursos limitados.

## Problemas de concurrencia en ejercicios prácticos

### Ejercicio 1: Multiplicación concurrente de matrices

Dividir la tarea de multiplicar dos matrices en subtareas concurrentes.

```python
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
```

```plaintext
SALIDA:
Tamaño matriz: 80x80
Número de hilos a: 1
Número de hilos b: 8
--------------------------------
Prueba en a:
Hilo 0 ha terminado. Tiempo: 0.20140886306762695 segundos

Tiempo total de ejecución: 0.2024085521697998 segundos
Tiempo del Hilo 0: 0.20140886306762695 segundos
--------------------------------
Prueba en b:
Hilo 0 ha terminado. Tiempo: 0.024003982543945312 segundos
Hilo 1 ha terminado. Tiempo: 0.044991254806518555 segundos
Hilo 2 ha terminado. Tiempo: 0.028888463973999023 segundos
Hilo 3 ha terminado. Tiempo: 0.029082059860229492 segundos
Hilo 4 ha terminado. Tiempo: 0.029007673263549805 segundos
Hilo 5 ha terminado. Tiempo: 0.04805159568786621 segundos
Hilo 6 ha terminado. Tiempo: 0.03897571563720703 segundos
Hilo 7 ha terminado. Tiempo: 0.026987075805664062 segundos

Tiempo total de ejecución: 0.22466135025024414 segundos
Tiempo del Hilo 0: 0.024003982543945312 segundos
Tiempo del Hilo 1: 0.044991254806518555 segundos
Tiempo del Hilo 2: 0.028888463973999023 segundos
Tiempo del Hilo 3: 0.029082059860229492 segundos
Tiempo del Hilo 4: 0.029007673263549805 segundos
Tiempo del Hilo 5: 0.04805159568786621 segundos
Tiempo del Hilo 6: 0.03897571563720703 segundos
Tiempo del Hilo 7: 0.026987075805664062 segundos
```

Se presenta una comparativa entre el uso de varios hilos y el uso de un solo hilo para una operación de multiplicación matricial. De esta manera, también se puede observar el tiempo total de ejecución con un solo hilo, así como los tiempos individuales de cada hilo cuando se utilizan múltiples hilos.

### Ejercicio 2: Productor-Consumidor con cola y condición

Implementar un modelo clásico de productor/consumidor para manejar la sincronización y comunicación.

```python
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
```

```plaintext
SALIDA:
Productor produjo: item-0
Consumidor consumió: item-0
Productor produjo: item-1
Consumidor consumió: item-1
Productor produjo: item-2
Consumidor consumió: item-2
Productor produjo: item-3
Consumidor consumió: item-3
Productor produjo: item-4
Consumidor consumió: item-4
Productor produjo: item-5
Consumidor consumió: item-5
Productor produjo: item-6
Consumidor consumió: item-6
Productor produjo: item-7
Consumidor consumió: item-7
Productor produjo: item-8
Consumidor consumió: item-8
Productor produjo: item-9
Consumidor consumió: item-9
```

En este código el productor genera ítems y los agrega a una cola compartida, notificando al consumidor cada vez que se agrega un nuevo ítem. El consumidor, por su parte, espera hasta que haya algo en la cola para consumir. Cuando la cola está vacía, el consumidor espera de manera controlada, y una vez que el productor notifica, el consumidor consume el ítem. 

## Conclusión:

Los mecanismos de sincronización en Python son fundamentales para coordinar hilos y evitar condiciones de carrera. Los locks (cerrojos) son el mecanismo más básico, permitiendo que solo un hilo acceda a una sección crítica a la vez. Se implementan con threading.Lock() y es recomendable usarlos con el contexto 'with' para garantizar su liberación. Los semáforos (threading.Semaphore) son una extensión que permite limitar el acceso a un recurso a N hilos simultáneos, ideal para gestionar recursos limitados como conexiones a bases de datos. Las variables de condición (threading.Condition) añaden capacidad de notificación entre hilos, siendo esenciales para patrones como productor-consumidor, donde unos hilos generan datos y otros los procesan de manera coordinada.

El modelo de ejecución de Python se basa en bytecode y ticks. El bytecode es la representación intermedia del código Python, donde cada línea se compila en múltiples instrucciones. Los ticks son unidades de trabajo del intérprete (no de tiempo) que determinan cuándo se verifican cambios de contexto. Cada aproximadamente 100 ticks, el intérprete libera el GIL (Global Interpreter Lock), que es el mecanismo que permite solo un hilo ejecutando bytecode Python a la vez. Esta arquitectura explica por qué Python tiene limitaciones para paralelismo CPU-bound pero funciona bien para I/O-bound. Los ticks y el bytecode son invisibles al programador pero cruciales para entender el comportamiento concurrente.

Para problemas de concurrencia prácticos, el patrón productor-consumidor es un ejemplo práctico. Se implementa típicamente con una cola compartida (deque) y variables de condición. Los productores añaden elementos a la cola y notifican a los consumidores, que esperan cuando la cola está vacía. Este modelo es útil para pipelines de procesamiento de datos, donde la producción y consumo pueden tener velocidades diferentes. La sincronización mediante Condition garantiza que los consumidores no consuman CPU mientras esperan, haciendo el patrón eficiente. La elección entre locks, semáforos o condiciones depende de la naturaleza del problema de concurrencia a resolver.

---
---