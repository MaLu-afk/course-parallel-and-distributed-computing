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