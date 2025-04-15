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
 
