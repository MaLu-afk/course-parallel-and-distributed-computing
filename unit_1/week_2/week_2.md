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