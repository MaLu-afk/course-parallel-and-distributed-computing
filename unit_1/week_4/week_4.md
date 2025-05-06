# Métricas de desempeño: Speedup, eficiencia, escalabilidad

- **Speedup**, revela cuánto se acelera el procesamiento frente a una ejecución secuencial.
- **Eficiencia**, mide la eficacia en el uso de los recursos disponibles.
- **Escalabilidad**, que determina la capacidad del sistema para crecer sin perder el rendimiento.

## Introducción a las métricas de desempeño

Una métrica de desempeño es una medida cuantitativa que nos ayuda a evaluar la eficacia y eficiencia al ejecutar un algoritmo o una aplicación en un entorno que utiliza múltiples procesadores o núcleos de forma simultánea.

## Tipos de métricas y cuándo se aplican
1. Tiempo de ejecución:
    - ***Qué mide:*** El tiempo total que tarda la aplicación en finalizar la tarea asignada.
    - ***Cuándo se aplica:*** Es la métrica básica y siempre se mide para poder comparar, por ejemplo, una versión secuencial con la paralela del mismo algoritmo para ver la ganancia en velocidad.

2. Speedup:
    - ***Qué mide:*** La realación entre el tiempo de ejecución secuencial y el tiempo de ejecución paralela.
    - ***Fórmula:*** $Speedup = \frac {Tiempo\_secuencial}{Tiempo\_paralelo}$
 
3. Eficiencia:
    - ***Qué mide:*** El aprovechamiento de los recursos paralelos.
    - ***Fórmula común:*** $Eficiencia = \frac{Speedup}{número -de-procesadores}$
    - ***Cuándo se aplica:*** Para identificar si el aumento en el número de procesadores se traduce en un desempeño proporcional.

4. Escalabilidad:
    - ***Qué mide:*** La capacidad del sistema o algoritmo de mantener el rendimiento al incrementar el número de procesadores.
    - ***Tipos:***
        + Escalabilidad fuerte: ocurre cuando se mantiene constante el tamaño del problema y se aumenta el número de procesadores. Se espera que disminuya en el tiempo.
        + Escalabilidad débil:ocurre cuando el tamaño del problema es proporcional al número de procesadores, buscando mantener el tiempo de ejecución.

5. Overhead de comunicación y sincronización:
    - ***Qué mide:*** El tiempo extra requerido para la coordinación entre procesos.
    - ***Cuándo se aplica:*** Al desarrollar algoritmos paralelos, para saber si la comunicación entre nodos o hilos no consume un porcentaje demasiado alto del tiempo total.

### ¿Por qué medir el desempeño en sistemas paralelos?
- Evaluar la eficiencia de la paralelización.
- Identificar cuellos de botella. 
- Escalabilidad del sistema.
- Análisis costo-beneficio.
- Optimización y validación de algoritmos.

Agregar más procesadores en principio puede garantizar mayor velocidad, pero la realidad es más compleja:
- División de tareas y Speedup.
- Comunicacinón y sincronización.
- Eficiencia y rendimientos decrecientes.
- Escalabilidad: Fuerte y débil.

---
---

# Métricas de desempeño: Speedup (Aceleración)

## 1. Definición de Speedup

Mide la ganancia en rendimiento obtenida al ejecutar una tarea específica en N procesadores (sistema paralelo) en lugar de uno solo (sistema secuencial). En esencia, cuantifica cuántas veces más rápido se completa una tarea cuando se usan N procesadores (cores, nodos) en lugar de uno.

Un Speedup ideal (llamado Speedup lineal) sería igual al número de procesadores. Sin embargo, en la práctica, esto raramente se alcanza debido a varios factores como la porción secuencial inherente (Ley de Ambahl), el costo de coordinación (comunicación y sincronización) entre procesos, desequilibrio de carga, etc.


## 2. Fórmula del Speedup

$$
S(N) = \frac{T\_serial}{T\_parallel(N)}
$$

    * S(N): Es el Speedup encontrado con N unidades de procesamiento.
    
    * T_serial: Es el tiempo de ejecución del mejor algoritmo secuencial para resolver el problema en una sola unidad de procesamiento. Es importante considerar que dicho algoritmo sea el mejor, porque al comparar con un algoritmo paralelo en caso el algoritmo secuencial no sea el mejor, inflaría artificialmente el Speedup.

    * T_parallel(N): Es el tiempo de ejecución del algoritmo paralelo para el mismo problema utilizando N unidades de procesamiento.

### Interpretación de los valores S(N):

+ S(N) = 1: No hay ganancia de rendimiento. El programa paralelo tarda lo mismo que el programa secuencial.
+ S(N) < 1: ¡Hay una realentización! El programa paralelo es más lento que el programa secuencial. Esto puede ocurrir si los costes de comunicación, sincronización o gestión del paralelismo superan los beneficios de la ejecución concurrente (especialmente en problemas pequeños o con N muy grande y poca carga por procesar).
+ S(N) > 1: Se muestra una aceleración. El programa paralelo es más rápido que el programa secuencial.
+ S(N) = N: Speedup lineal (ideal). El programa es N veces más rápido con N procesadores.
+ S(N) > N: Seedup superlineal. Es poco usual pero posible, generalmente cuando se debe a efectos de jerarquía de memoria (ejemplo, al dividir los problemas en porciones pequeñas, caben mejor en las cachés de los procesadores individuales, reduciendo drásticamente los accesos a la memoria principal comparado con el caso secuencial que podría sufrir muchos fallos de caché).


# Ley de Ambahl: Teoría, Fórmula

## 1. Teoría de la Ley de Ambahl

La Ley de Ambahl, formulada por Gene Ambahl en 1967, es un principio fundamental en la computación paralela que describe el límite teórico máximo del Speedup.

La idea central es que todo programa o algoritmo tiene una porción que es inherentemente secuencial y otra porción sí puede ser dividida y ejecutada en paralelo. La porción secuencial incluye tareas como:

+ Inicialización del programa.
+ Lectura de datos de entrada o escritura de resultados finales. 
+ Partes del algoritmo que dependen estrictamente del resultado del paso anterior. 
+ Comunicación y sincronización. 

La Ley de Ambahl establece que la fracción secuencial del programa actúa como un cuello de botella. 

## 2. Fórmula de la Ley de Ambahl

La fórmula para calcular el Speedup máximo teórico S(N) según la Ley de Ambahl es:

$$
S(N) = \frac{1}{f + \frac{(1-f)}{N}}
$$

Donde:  

    * S(N): Es el Speedup teórico máximo que se puede alcanzar utilizando N unidades de procesamiento. 
    * f: Es la fracción de tiempo de ejecución del programa original (secuencial) que es inherentemente secuencial (no paralelizable). Se expresa como un valor entre 0 y 1 (0.1 para 10%).
    * 1-f: Es la fracción del tiempo de ejecución del programa original (secuencial) que es paralizable. 
    * N: Es el número de unidades de procesamiento (cores, procesadores, nodos) utilizadas en la ejecución paralela. 

### Límite Máximo de Speepup:

$$
S\_max = \lim_{N \to \infty} S(N) = \lim_{N \to \infty} \frac{1}{f + \frac{(1-f)}{N}} = \frac{1}{f+0} = \frac{1}{f}
$$

Esto quiere decir si un programa tiene un 10% de código secuencial ($f=0.1$), el Speedup máximo que jamás podrá alcanzar, incluso con un número infinito de procesadores, es $1/0.1 = 10x$.
 

# Ley de Gustafson (o Ley de Gustafson-Barsis): Teoría, Comparación

## 1. Teoría de la Ley de Gustafson

La Ley de Gustafson surgió debido a la limitaciones percibidas de la Ley de Amdhal, en el contexo de comoputación masiva paralela. 

Mientras Amdhal se centra en mantener el tamaño fijo del problema y evaluar cuánta velocidad se gana al incrementar el número de procesadores, Gustafson observó que en la práctica cuando se dispone de más potencia de cómputo (más procesadores), los usuarios tienden a aumentar el tamaño del problema (mayor resolución, más detalle) para obtener resultados más precisos o complejos manteniedo el tiempo de ejecución en aproximadamente constante. La perspectiva es: "Dado un tiempo de ejecución fijo, ¿cuánto más trabajo puedo realizar utilizando N procesadores en comparación con uno solo?".

## 2. Comparación: Ley de Amdhal vs. Ley de Gustafson

|*Características*|Ley de Amdhal|Ley de Gustafson|
|-|-|-|
|**Supuesto clave**|*Tamaño* del problema fijo|*Tiempo* de ejecución fijo|
|**Objetivo**|Minimizar el tiempo para un problema|Maximizar el trabajo en un tiempo|
|**Perspectiva**|¿Cuánto más rápido?|¿Cuánto más trabajo?|
|**Variable clave**|f: Fracción secuencial del tiempo de ejecución original|s: Fracción secuencial del tiempo de ejecución paralelo|
|**Limitación**|Speedup limitada por 1/f|Speedup puede crecer linealmente (si `s` es pequeño y el problema escala)|
|**Optimismo**|Más pesimita para N grande|Más optimista para N grande (si aplica)|
|**Aplicabilidad**|Problemas con tamaño fijo|Problemas cuyo tamaño se escala con lo recursos (simulaciones, gráficos, big data)|

### ¡Importante distinción entre fracción secuencial!
- **Amdhal (f):** Porcentaje del tiempo original (en 1 procesador) que no se puede paralelizar.
- **Gustafson (s):** Porcentaje del tiempo total en la ejecución paralela (con N procesadores) se dedica a tareas secuenciales.

## 3. Fórmula de la Ley de Gustafson

Scaled Speedup (Speedup Escalado) S_scaled(N) es:

$$
S\_scaled(N) = s + p*N
$$

Donde:
    
    * S_scaled: Es el Speedup escalado con N procesadores. Representa cuánto más trabajo se hizo en el mismo tiempo.
    * s: Es la fracción del tiempo de ejecución paralela total que se dedica a la parte secuencial.
    * p: Es la fracción del tiempo de ejecución paralela total que se dedica a la parte paralela (p = 1 - s).

La fórmula también se puede reescribir como:

$
S\_scaled(N) = s + N*(1-s) = N - s*(N - 1)
$




