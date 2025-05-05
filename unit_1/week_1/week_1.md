# Fundamentos de programación

## Modelos de programación:

+ Secuencial.
+ Concurrente.
+ Paralela.
+ Distribuida.
+ Paralela y distribuida.

## 1. Programación secuencial

- Se refiere a que una acción sigue a otra.
- La salida de una tarea es la entrada de la siguiente. 

## 2. Programación concurrente

- Capacidad de un computador de realizar varias tareas a la vez.
- No necesariamente al mismo tiempo, es decir, en paralelo. Esto depende del número de procesadores (o cores) que tenga un computador.

### ¿Cómo sabe el sistema operativo o el intérprete cuándo cambiar de un hilo a otro?

- **En los sistemas operativos,** la planificación de procesos/hilos es responsabilidad del planificador (scheduler). Funciona con la combinación del temporizador del sistema (hardware timer) el cual genera interrupciones periódicas y el kernel del sistema operativo que responde ante esas interrupciones y decide si cambiar de contexto en caso haya hilos en espera.

- **Intérprete,** en lenguajes como Python (CPython), el cambio de hilo ocurre internamente gracias a un contador de ticks de bytecode. Los contadores se reinician al llegar a un umbral y cede el GIL (Global Interpreter Lock) si hay otros hilos esperando.

## 3. Programación paralela

- Es una forma de cómputo en la que muchas instruciones se ejecutan simultáneamente, operando sobre problemas grandes que se pueden dividir en unos más pequeños, que luego son resueltos simultáneamente (en paralelo).

## Comparación de los tres modelos

| Aspecto | Secuencial | Concurrente | Paralelo |
|-----|------|-----|-----|
| **Definción** | Las tareas se ejecutan unas a otras | Las taras parecen ejecutarse al mismo tiempo (intercaladas) | Las tareas se ejecutan realmente al mismo tiempo |
| **Consite en** | Una sola tarea en curso (un núcleo con un hilo) | Varias tareas activas, pero ejecutadas en un núcleo | Varias tareas ejecutándose simultáneamente en varios núcleos |
| **Ventajas** | Simple de entender y depurar | Mejora la eficiencia en tareas I/O-bound (E/S, red) | Aumenta velocidad en tareas pesadas |
| **Desventajas** | Ineficiente para múltiples tareas o esperas | Puede ser más lenta que la secuencial si hay mucha sincronización | Requiere cuidado en sincronización y múltiples núcleos |
| **Ejemplos** | Concinar arroz, luego freír huevo | Poner el arroz a cocer, mientras tanto cortar verduras | Dos personas: una cocina el arroz, otra fríe el huevo al mismo tiempo |


## 4. Programación distribuida

- Es un modelo para resolver problemas de computación masiva utilizando un gran número de ordenadores organizados en clústeres en una infraestructura de telecomunicaciones (internet, redes privadas, etc.) distribuida.

- **Ejemplo:** Se tiene un servidor que dividirá tres tareas y lo distribuirá por la red en tres servidores (una tarea para cada servidor).

# Programación concurrente

* Surge con la necesidad de dar soluciones con el máximo rendimiento.
* Aplicaciones computacionales que demandan gran velocidad de cálculo:
    - Visualización
    - Bases de datos distribuidas
    - Simulaciones
    - Predicciones científicas
* Afines a la concurrencia (relacionados estrechamente): 
    - Sistemas distribuidos
    - Sistemas en tiempo real

* En 1972 apareció el lenguaje Pascal concurrente, era el primer lenguaje de alto nivel para este objetivo.

* **Concurrencia:** la existencia de simultánea no implica ejecución al mismo tiempo.

* Los procesos comparten el tiempo de ejecución de un único procesador disponible.

* Conjunto de técnicas que permiten resolver problemas de comunicación y sincronización que se presentan cuando varios procesos concurrentes comparten recursos al mismo tiempo.

* Propiedad básica para este tipo de programación es el no determinismo:
    - En caso se tenga un solo procesador se desconoce si después de la ejecución de una instrucción habrá alguna interrupción para pasar de un proceso a otro.
    - En caso del sistema mulltiprocesador las velocidades de los procesadores no están sincronizadas, por lo que no se conoce a priori cuál procesador va a ser el primero en ejecutar su siguiente instrucción.
* Aprovechar el hardware: múltiples procesadores.
* Incrementar productividad de la CPU.

### Correción en sistemas concurrentes:

- Es necesario de un modelo abstracto que permita verificar y corregir los sistemas concurrentes.
- Cada problema concurrente puede aprovechar un tipo distinto de paralelismo (todo problema paralelo es concurrente pero no todo problema concurrente es paralelo). 
- Si se requier trabajar en un ambiente independiente de la arquitectura (SOs) se debe plantear un modelo para verificar que sea correcto independientemente del hardware que se ejecute.

    #### Exclusión mutua
    + Es el mecanismo por el cual se asegura que procesos concurrentes no accedan a un mismo recurso al mismo tiempo.
    + Se debe identificar regiones en donde los procesos tienen que acceder a variables (recursos) compartidas **"región crítica"**.
    + Deben determinarse mecanismos de bloqueo para garantizar que cuando se salga de un proceso en ese momento participe otro en el acceso a la región crítica.

### Sistemas concurrentes: Sincronización

Existen tres tipos de procesos:

- **Procesos independientes:** no se comunican entre sí, no requiere sincronización.
- **Procesos cooperativos:** colaboran para realizar un trabajo, por ende, deben comunicarse entre sí y sincronicen sus actividades.
- **Procesos en competencia:** Comparten un número finito de recursos del sistema por ejemplo periféricos, memoria, por tanto deben de competir para hacer uso de los recursos del sistema. También deben sincronizarse para comunicarse aunque sus labores sean independientes.
- **Sincronización:** transmisión y recepción de señal con el fin de ejecutar el procesos cooperativos o en competencia.

#### Ejemplo
- En la siguiente instrucción: `$ cat lista1.txt, lista2.txt | wc -l`

Esta instrucción crea dos procesos concurrentes: El primero ejecuta el programa cat, que concatenará el contenido de los archivos lista1 y lista2. El segundo ejecutará el programa wc (word count), que cuenta el número de lineas de la salida producida por cat.

- En la siguiente instrucción: `$ grep búsqueda | sort | lpr`

El comando grep: Global Regular Expression Print, busca líneas que contienen el texto "búsqueda" y lpr: Line Printer Request.


***"Todo paralelismo es concurrente pero no tada concurrencia es paralela"***

**Actividades ~ Procesos**

#### Aplicaciones de la concurrencia en informática
+ Sistemas Operativos
+ Sistemas de gestión de bases de datos
+ Sistemas de tiempo real
+ Sistemas distribuidos

### Concurrencia
- **Inherente:** el entorno con el que interactúa tiene actividades simultáneas.
- **Potencial:** no hay necesariamente concurrencia, pero se puede implementarse.

### Ejercicios (situaciones reales)

- 02 ejemplos de sistemas en la naturaleza que sean concurrentes
- 02 sistemas inherentemente concurrentes
- 02 sistemas potencialmente concurrentes (beneficios de la concurrencia)

### Produciendo actividades concurrentes en el ordenador
- **De forma manual:**
    + Directamente sobre el hardware
    + Usar/llamar a las librerías de software (PVM: Parallel Virtual Machine, pthreads)
    + Implementar con lenguajes de alto nivel

- **De forma automática:**
    + El SO realiza la asignación automáticamente
    + El compilador detecta concurrencia en los programas secuenciales

### Lenguajes concurrentes

- Los procesos concurrentes deben comunicarser entre sí.
- Un lenguaje concurrente debe tener mecanismos de comunicación y sincronización.

### Programación concurrente

#### Sincronización

- Señalización
    + Semáforos
    + Cerrojos y variables de condición
    + Eventos
    + Retardos temporales
- Recursos compartidos
    + Regiones críticas
    + Monitores
    + Objetos protegidos

#### Comunicación

- Memoria compartida
- Buzones
- Llamadas a procedimientos remotos (RPC)

# Programación paralela

- Programas especialmente escritos para sistemas con multiprocesadores.
- Caso particular de programación concurrente -> ejecución paralela.

### Ejercicios
Usando sentencias concurrentes:
+ Multiplicar dos matrices
+ Sumar una lista de N números
+ Ordenar un vector
+ Obtener números primos entre 2 y N

### Existenciales
+ ¿No es suficiente la programación secuencial?
    - No, la programación secuencial no siempre es suficiente. Aunque puede ser adecuada para problemas simples, se vuelve limitada cuando se trata de aplicaciones que necesiten manejar múltiples tareas al mismo tiempo, como servidores web. Esta limitación se vuelve aún más evidente en contextos donde se requiere paralelismo, ya que la programación secuencial no puede aprovechar múltiples núcleos de procesamiento. 

+ ¿Puede la programación secuencial modelar un sistema concurrente?
    - Puede intentar modelar, pero no de manera eficiente. En programación secuencial todo ocurre una instrucción después de otra, por lo tanto, simular concurrencia implica interrupciones manuales del programa, lo cula no refleja la verdadera ejecución simultánea de tareas.

+ ¿La programación secuencial puede aprovechar los múltiples procesadores de un ordenador?
    - No, la programación secuencial no puede aprovechar los múltiples procesadores o núcleos, ya que las instrucciones se ejecutan una tras otra en un solo hilo de ejecución. Para sacar provecho del hardware multinúcleo es necesario utilizar programación paralela o concurrente, dividiento la carga de trabajo en varios hilos o procesos que pueden ejecutarse simultáneamente.

---
---

## Ejemplos de la vida cotidiana

A continuación se representan paradigmas de programación.

1. **Programación concurrente -> Cajero de un banco atendiendo clientes:**

    - Un cajero atiende a múltiples clientes en un banco. Puede iniciar la atención de un cliente, pero si necesita esperar para la aprobación o documentación, puede comenzar con otro cliente en paralelo sin bloquearse.

- **Pseudocódigo: Cajero de banco**

```plaintext
proceso atenderClientes()
    mientras haya cliente esperando en la fila hacer
        cliente = siguienteCliente()
        iniciarAtencion(cliente)

        si cliente requiere autorización externa entonces
            esperarAutorizacion()
        fin si

        procesarTransaccion(cliente)
        finalizarAtencion(cliente)
    fin mientras
fin proceso
```
+ El cajero puede empezar con un cliente, pero si necesita una autorización, en lugar de esperar, puede comenzar con atender otro cliente en simultáneo.

2. **Programación paralela -> Cocinando varios platillos a la vez:**

    - Un chef prepara diferentes platos en paralelo en una cocina, asignando tareas a varios asistentes. Cada asistente se enfoca en una tarea específica al mismo tiempo (uno corta verduras, otro cocina la carne, otro lava platos).

- **Pseudocódigo: Cocina con varios asistentes**

```plaintext
proceso prepararComida()
    paralelo
        cortarVerduras()
        cocinarCarne()
        hervirAgua()
        lavarPlatos()
    fin paralelo
    servirPlato()
fin proceso
```
+ Las tareas se ejecutan al mismo tiempo (si hay suficientes recursos) para optimizar el proceso de cocinar.

3. **Programación distribuida -> Reparto de paquetes en una ciudad:**

    - Una empresa de mensajería tiene múltiples repartidores, cada uno encargado de entregar paquetes en distintas zonas. Cada respartidor opera de manera independiente, pero todos trabajan hacia el mismo objetivo.

- **Pseudocódigo: Reparto de paquetes**

```plaintext
proceso repartirPaquetes()
    listaRepartidores = asignarRepartidores()
    paralelo para cada repartidor en listaRepartidores hacer
        mientras repartidor tenga paquetes hacer
            destino = siguienteDestino(repartidor)
            entregaPaquete(destino)
        fin mientras
    fin paralelo
fin proceso
```
+ Cada repartidor trabaja de forma independiente en diferentes áreas de la ciudad. La entrega de paquetes está distribuida entre múltiples trabajadores, como ocurre en sistemas de computación distribuida.

4. **Programación concurrente -> Profesor atendiendo estudiantes y corrigiendo exámenes:**

    - Un profesor alterna entre corregir exámenes y resolver dudas de estudiantes. Si un estudiante hace una pregunta compleja que requiere investigación, el profesor puede pausar esa interacción y retornar la corrección de exámenes mientras espera.

- **Pseudocódigo: Profesor gestiona tareas**

```plaintext
proceso gestionarTareas()
    mientras haya tareas pendientes hacer
        tarea = seleccionarTarea()
        si tarea es "corregirExamen" entonces
            corregirProximoExamen()
        sino si tarea es "atenderEstudiante" entonces
            estudiante = siguienteEstudiante()
            si preguntaRequiereInvestigacion(estudiante) entonces
                programarInvestigacion(estudiante)
                continuar
            fin si
            responderPregunta(estudiante)
        fin si
    fin mientras    
fin proceso
```
+ El profesor maneja múltiples tareas de forma concurrente, cambiando entre ellas cuando requiere tiempo de espera, similar a cómo un sistema concurrente gestiona hilos.

5. **Programación paralela -> Línea de ensamblaje en una fábrica:**

    - En una fábrica de automóviles, diferentes estaciones trabajan al mismo tiempo: una ensambla el motor, otra instala las puertas y una pinta el chasis. Todas colaboran para completar el vehículo de manera eficiente.

- **Pseudocódigo: Fábrica de automóviles**

```plaintext
proceso ensamblarAuto()
    paralelo
        ensamblarMotor()
        instalarPueras()
        pintarChasis()
    fin paralelo
    ensamblarPartesVehiculo()
fin proceso
```
+ Las tareas se ejecutan en paralelo utilizando recursos independientes (estación de trabajo), optimizando el tiempo de producción.

6. **Programación distribuida -> Red de bibliotecas municipales:**

    - Cada biblioteca en una ciudad gestiona préstamos y devoluciones de libros de forma independiente, pero todas actualizan un catálogo centralizado en la nube para reflejar disponibilidad en tiempo real.

- **Pseudocódigo: Biblioteca**

```plaintext
proceso gestionarBibliotecas()
    listaBibliotecas = obtenerBibliotecas() 
    paralelo para cada biblioteca en listaBibliotecas hacer
        mientras haya actividad entonces
            si hayPrestamo() entonces
                libro = seleccionarLibro()
                registrarPrestamo(libro, biblioteca)
                actualizarCatalogoCentral(libro)
            sino si hayDevolucion() entonces
                libro = aceptarDevolucion()
                actualizarCatalogoCentral(libro)
            fin si 
        fin mientras
    fin paralelo
fin proceso
```
+ Cada nodo (biblioteca) opera de manera autónoma, pero colabora con un sistema central, similar a los nodos en una red distribuida.

7. **Programación concurrente -> Call center con múltiples agentes:**

    - En un call center, varios agentes atienden llamadas simultáneamente. Si un cliente necesita esperar para consultar información, el agente puede colocar la llamada en espera y atender a otro cliente.

- **Pseudocódigo: Atención al cliente**

```plaintext
proceso atenderClientes()
    mientras haya llamadas por atender hacer
        llamada = siguienteLlamada()
        asignarAgente(llamada)
        si llamada requiereEsperar() entonces
            ponerEnEspera(llamada)
            atenderSiguienteLlamada()
        sino
            resolverConsulta(llamada)
        fin si
    fin mientras
fin proceso
```
+ Múltiples agentes gestionan tareas (llamadas) concurrentemente, aprovechando tiempos de espera para mejorar la eficiencia.

8. **Programación concurrente -> Semáforo inteligente gestionando tráfico:**

    - Un semáforo inteligente alterna entre direcciones de tráfico. Si detecta una emergencia (e.g., ambulancia), prioriza su paso mientras pausa temporalmente el flujo de otros vehículos, retomando después el ciclo normal.

- **Pseudocódigo: Semáforos**

```plaintext
proceso gestionarTrafico()
    mientras true hacer
        cambiarALuzVerde(direccion_principal)
        si detectaEmergencia() entonces
            activarPrioridadEmergencia()
            esperarPasoEmergencia()
            reanudarCicloNormal()
        fin si
        cambiarALuzRoja(direccion_principal)
        cambiarALuzVerde(direccion_secundaria)
    fin mientras
fin proceso
```
+ El semáforo maneja múltiples eventos (flujo normal y emergencia) de forma concurrente, cambiando entre tareas según prioridades, similar a la gestión de hilos en sistemas concurrentes.

9. **Programación paralela -> Equipo de limpieza en un hotel:**

    - Un equipo de limpieza trabaja en paralelo: un grupo limpia habitaciones, otro lava la ropa de cama y un tercero abastece los carros de servicio. Todas las tareas avanzan simultáneamente para preparar el hotel rápidamente. 

- **Pseudocódigo: Limpieza de hotel**

```plaintext
proceso prepararHotel()  
    paralelo  
        limpiarHabitaciones()  
        lavarRopa()  
        reabastecerCarros()  
    fin paralelo  
    inspeccionarCalidad()  
fin proceso  
```
+ Las tareas se ejecutan en paralelo utilizando recursos independientes (empleados), reduciendo el tiempo total de preparción, análogo al uso de múltiples núcleos en computación paralela.

10. **Programación distribuida -> Red de sensores ambientales:**

    - Sensores distribuidos en una ciudad miden calidad del aire, ruido temperatura. Cada sensor envía datos a un servidor central, que procesa la información para generar reportes en tiempo real.


- **Pseudocódigo: Sensores ambientales**

```plaintext
proceso monitorearAmbiente()  
    listaSensores = obtenerSensores()  
    paralelo para cada sensor en listaSensores hacer  
        mientras true hacer  
            dato = capturarDato(sensor)  
            enviarAlServidorCentral(dato)  
            esperar(intervalo)  
        fin mientras  
    fin paralelo  
fin proceso  
```
+ Cada sensor opera de forma autónoma (nodos distribuidos), pero colaboran con sun sistema centralizado, reflejando la coordianción en sistemas distrubuidos.


---
---

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