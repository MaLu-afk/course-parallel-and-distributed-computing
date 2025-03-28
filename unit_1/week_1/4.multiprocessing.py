import multiprocessing
import os

def hello_from_process():
    print(f'Hola desde el proceso hijo {os.getpid()}')
    
if __name__ == '__name__':
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()
    
    print(f'Hola desde el proceso hijo {os.getpid}')
    
    hello_process.join() 