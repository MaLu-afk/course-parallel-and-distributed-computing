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