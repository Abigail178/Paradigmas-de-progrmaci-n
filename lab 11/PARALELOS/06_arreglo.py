#=============================================================================
# Ejemplo de comunicación bloqueada a un arreglo compartido 
# uso de candados (looks)
#=============================================================================
from multiprocessing import Process, Array, Lock
import time 

def sumale100(numeros,candado):
    for i in range(100):
        time.sleep(0.01)
        #usando candado 
        for i in range(len(numeros)):
            # lo que esté dentro de con candado no puede accederse 
            # desde otro procesi al mismo tiempo
            with candado:
                # HACER LA OPERACIÓN 
                numeros[i] += 1 
if __name__ == "__main__":
    #==============================================================
    # Candado para evitar que dos procesos se empalmen 
    #==============================================================

    candado = Lock() 

    # Número común a los procesos, d de dobles
    numeros_compartidps = Array('d', [0.0, 100.0, 200.0])

    # : quiere decir todos los elementos 

    print("al principio vale = ", numeros_compartidos[:])

    # Dos procesos 

    p1 = Process(target=sumale100, args=(numeros_compartidos,candado))
    p2 = Process(target=sumale100, args=(numeros_compartidos,candado))

    pi.start()
    p2.start()

    p1.join()
    p2.join()

    print("Al final vale = ", numeros_compartidos[:])
