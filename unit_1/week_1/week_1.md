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
ya que solo toma los encabezados y los concatena. El problema surgiría si 
el procesamiento de los encabezados incluyera tareas como parsers complejos, 
compresión u operaciones con matrices. Una alternativa para optimizar 
estos casos sería usar multiprocessing para aprovechar múltiples núcleos 
del procesador.

Este código ayuda a comprender cómo se presentan casos de I/O-bound en 
sitios web y cómo impactan en el rendimiento de la CPU.