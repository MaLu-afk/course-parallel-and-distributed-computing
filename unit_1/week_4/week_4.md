# Métricas de desempeño: Speedup(Aceleración)

## 1. Definición de Speedup

Mide la ganancia en rendimiento obtenida al ejecutar una tarea específica en N procesadores (sistema paralelo) en lugar de uno solo (sistema secuencial). En esencia, cuantifica cuántas veces más rápido se completa una tarea cuando se usan N procesadores (cores, nodos) en lugar de uno.

Un Speedup ideal (llamado Speedup lineal) sería igual al número de procesadores. Sin embargo, en la práctica, esto raramente se alcanza debido a varios factores como la porción secuencial inherente (Ley de Ambahl), el costo de coordinación (comunicación y sincronización) entre procesos, desequilibrio de carga, etc.

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}
$$