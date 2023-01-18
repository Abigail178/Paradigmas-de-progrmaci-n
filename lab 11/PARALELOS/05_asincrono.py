import multiprocessing as mp
import numpy as np
import time 

def my_function(i,param1, param2, param3):
    # calcula un polinomio 
    result = param1**2 + param2 + param3
    # se  hace tonta 2 segundos 
    time.sleep(2)
    return (i,result)

def get_result(result):
    # se inscriben en la lista global 
    # (mal estilo de programación)
    global results 
    results.append(result)

#======================
# Programa principal 
#======================

if __name__ == "__main__":
   
    # Matriz de 10x3 números al azar 
    params = np.random.random((10,3))*100.0
    results = []
    ts = time.time()

    # Un grupo de procekksos (Pool)
    pool = mp.Poll(mp.cpu_count())

    # loop de priemro dimensión del arreglo 
    for i in range(0, params.shape[0]):
        # Correr asincónicamente my function con argumentos args y cuando termine de correr get results 
        pool.apply_async(my_function, args = (i,params[i,0],params[i,1],params[i,2]), callback=get_result)

        # Cerrar el grupo 
        pool.close()
        # ESperarque termine el grupo 
        pool.join()
        print("TIempo en paralelo = ", time.time()-ts)
        print(results)

