from multiprocessing import Process, Queue

def proceso_hijo(trabajo):
    print("Soy el proceso hijo")
    print(trabajo)
    

if __name__=='__main__':
    cola = Queue()
    
    lista_numeros = [1,2,3,4,5]
    
    p = Process(target=proceso_hijo,args=(lista_numeros,))
    
    p.start()
    p.join()
    
