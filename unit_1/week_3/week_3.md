# Aceleradores de hardware

## CPUs

### Conceptos clave
- Mútiples núcleos:
    + **Definición:** Un núcleo es la unidad independiente de procesamiento. En un CPU multicore, dentro de un chip se encuentran varios núcleos, cada uno capaz de ejecutar instrucciones sin esperar que otro termine. 
    + **Beneficios:** 
        * Permite el procesamiento simultáneo de tareas.
        * Aumenta el redimiento general sin necesidad de aumentar la frecuencia de reloj de manera excesiva. 
        * Reduce el consumo energético comparando con la misma cantidad de rendimiento en un solo núcleo.
    + **Uso general:**
        * Aplicabilidad: Ideales para ejecutar múltiples procesos y tareas concurentes.
        * Ventajas para el usuario: Permite que un SO gestione varias aplicaciones al mismo tiempo, sin que se note el tiempo de retrasos o bloqueos.

## GPUs

### ¿Qué es una GPU y en qué se diferencia de una CPU?

- **CPU:** Diseñado para ejecutar pocas tareas complejas de manera eficiente (procesamiento secuencial).
- **GPU:** Diseñado para ejecutar muchas tareas simples en paralelo (procesamiento masivo).

*"PCI-Express (Peripheral Component Interconnect Express): es la autopista digital que permite a los componentes (GPU, SSD) comunicarse con la CPU a velocidades increíbles"*

### Arquitecturas Nvidia GeForce

Nvidia ofrece diferentes productos, divididos en las tres familias principales:

- **GeForce**: orientada al gran mercado de concumo multimedia (videojuegos, edición de videos, entre otros).
- **Cuadro**: orientado a soluciones profesionales que requieran modelos 3D, como los sectores de ingeniería y arquitectura.
- **Tesla**: orientada a la parte de investigación, simulación masiva, computación financiera. 

## TPUs

### ¿Qué es una TPU?
- Las TPUs (Tensor Processing Units) son chips desarrollados por Google para acelerar el procesamiento de tensores, la estructura de datos clave en redes neuronales.
- Optimizada para operaciones de matrices y vectores, esenciales para deep learning.

#### Aplicaciones:
- Google Photos: Reconocimiento de imágenes.
- Google Traslate: Traducciones automáticas eficientes.
- Google Assistant: Procesamiento de voz y comprensión de lenguaje.
- Deep Learning en la Nube: TPUs disponibles en Google Cloud para entrenar modelos de IA.

## ¿Por qué TPUs? Diferencias con CPUs y GPUs

|**Características**|CPU|GPU|TPU|
|-|-|-|-|
|Núcleos|Pocos núcleos potentes|Miles de núcleos simples|Hardware especializado para tensores|
|Uso Principal|Tareas generales|Computación paralela (gráficos, IA)|Redes neuronales e IA|
|Consumo Energético|Alto|Medio|Bajo|
|Velocidad en IA|Lenta|Rápida|Muy rápida|






---
---

# 1. CPUs Multicore - Aplicaiones en empresas y centros de investigación

Son procesadores de múltiples núcleos que permiten la ejecución simultánea de varias tareas.

## Escenarios y aplicaciones:

+ *Servidores y centros de datos (AWS, Microsoft Azure):* Gestionan múltiples solicitudes simultáneamente, optimizando el procesamiento en la nube. 

+ *Bases de datos y análisis de datos (Oracle, SAP):* Manejan grandes volúmenes de información en entornos empresariales, mejorando la eficiencia en consultas y almacenamiento.

+ *Simulaciones científicas (NASA, CERN):* Ejecutan modelos de complejos de física, biología y química, como simulaciones de partículas subatómicas o predicciones climáticas.

+ *Compilación y desarrollo de software (Google, Apple):* Mejoran la velocidad de compilación en lenguajes como c++, Java y Python, permiten la ejecución simultánea de tareas de desarrollo. 

+ *Gestión financiera y trading algorítmico (Goldman Sachs, Bloomberg):* Procesan grandes volúmenes de datos financiera en tiempo real para decisiones de inversión.

## Ventajas:

+ Versatilidad para tareas variadas.
+ Compatibilidad de múltiples software y lenguajes de programación.
+ Excelente en el procesamiento de datos estructurados.

## Desventajas:

+ Limitaciones en paralelismo masivo.
+ Ancho de banda de memoria limitada, lo que genera el problema de cuellos de botellas.

# 2. GPUs - Aplicaciones en empresas y centro de investigación

Estos aceleradores de hardware, sobresalen en el procesamiento masivo paralelo, ideal para tareas de alto rendimiento.

## Escenarios y aplicaciones:

+ *Procesamiento de imágenes y video (Pixar, Adobe):* Aceleran renderizados 3D, edición de videos y efectos especiales en cine y publicidad.

 + *Simulación científica de fluidos y física cuántica (MIT, Stanford):* Realizan simulaciones numéricas de alta complejidad, como dinámica de fluidos en ingeniría aeroespacial.

+ *Desarrollo de videojuegos (Unity, Epic Games):* Gestionan gráficos 3D en tiempo real, mejorando la calidad visual y el rendimiento.

+ *Reconocimiento facial y visión por computadora (Tesla, OpenAI):*Procesamiento de imágenes y video en aplicaciones de seguridad, conducción automática y análisis biométrico.

## Ventajas: 

+ Procesamiento masivo paralelo.
+ Ideal para tareas gráficas y simulaciones científicas.
+ Compatible con frameworks como CUDA y OpenCL para computación científica. 

## Desventajas: 

+ Costo energético.
+ Complejidad de programación.

# 3. TPUs - Aplicaciones en empresas y centros de investigación
 
 Están diseñadas especialmente para acelerar el aprendizaje profundo e inteligencia artificial.

## Escenarios y aplicaciones:

+ *Entrenamiento de modelos de IA (Google AI, DeepMind):* Optimiza redes neuronales profundas como Tensorflow y PyTorch.

+ *Procesamiento de Lenguaje Natural (NLP) (OpenAI, Google Traslate):* Mejoran la traducción automática, chatbots y sistemas de análisis de texto.

+ *Busqueda semántica de motores de Google (Google Search):* Optimiza las búsquedas mediante IA, mejorando la relevancia de las respuestas.

+ *Automatización y predicción de finanzas (JP Morgan, Nasdaq):* Analizan tendencias de meracado y automatizan decisiones de inversión mediante redes neuronales.

## Ventajas:

+ Optimización extrema para inteligencia artificial  y deep learning.
+ Menor consumo energético en comparación con GPUs para tareas de IA.
+ Altamente eficiente en matrices y cálculos de tensores.
+ Optimización para inferencias, ideales para servir modelos en producción (por ejemplo si se busca: "Qué películas de sci-fi tiene escenas grabadas en Neptuno?").

## Desventajas:

+ Vendor lock-in, solo disponible en Google Cloud (No hay TPUs físicas para comprar).
+ Limitada de flexibilidad, solo útil para cargas de trabajo de IA.

# Comparación y elección según el caso de uso

|Tecnología|Mejor aplicación|Ejemplo de uso|
|--|--|--|
|CPU Multicore|Computo general y estructura de datos|Servidores, bases de datos, simulaciones matemáticas|
|GPU|Procesamiento paralelo y gráficos|Renderizado, simulación científica, reconocimiento facial|
|TPU|Inteligencia artificial y aprendizaje profundo|Modelos de IA, búsquedas semántica, diagnóstico médico|





---
---
 # Aspectos únicos que las hacen eficientes

 ## 1. CPUs Multicore: "El cerebro versátil"

 + **Alta precisión numérica**

    + *Hardware:* Soporta operaciones de 64-bit (FP64) y hasta 128-bit (FP128) en algunos casos.
    + *Ejemplos:* En simulaciones de química cuántica, un error de redondeo en el cálculo de orbitales moleculares puede invalidar los resultados. Las CPUs garantizan precisión.
    + *¿Por qué GPUs/TPUs no?:* Las GPUs suelen usar FP32 (menos precisa) por defecto, y las TPUs están optimizadas para FP16/FP32 en IA.

+ **Baja lantencia **