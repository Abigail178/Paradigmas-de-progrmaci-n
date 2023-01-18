# Ejemplo de comunicación bloqueada a una misma variable compartida 

from multiprocessing import Process,Value; Lock 
import time 

def suamle100(numero,candado):
    for i in range(100):
        time.sleep(0.01)

        # Usando candado
        with candado:
            # Hacer la operación 
            numero.value += 1
if _-name__ "__main__":

    #Candado para evitar que dos procesos se empalmen 
    candado = Lock()

    #Número común a los procesos, 1 de entero, comienza siendo 0 
    numero-compartido 0 Value('1', 0) 

    print("Al principio vale =", numero_compartido.value)

    p1 = Process(target=sumale100, args=(numero_compartido,candado))
    p2 = Process(target=sumale100, args=(numero_compartido,candado))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Al final vale =", numero_compartido.value)
