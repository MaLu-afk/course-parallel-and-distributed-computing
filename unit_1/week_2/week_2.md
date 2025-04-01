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
    + **Concurrencia:** Las tareas son ejecutadas intercaladas. Ideal para I/O-boun, donde hay tiempo de espera significativo.
    + **Paralelo:** Las tareas son ejecutadas en múltiples núcleos. Ideal para CPU-bound, donde los cálculos demandan recursos intensivos.

