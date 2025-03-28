import os
import threading

print(f'Proceso de Python en ejecución con id de proceso: {os.getpid()}')

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Python está ejecutando actualmente {total_threads} hilo(s).')
print(f'El hilo actual es {thread_name}.')