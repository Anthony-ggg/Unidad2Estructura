import sys
sys.path.append('../')

from controls.personaDaoControl import PersonaDaoControl
from controls.facturaDao import FacturaDao
from controls.tda.linked.linkedList import Linked_List
import time
import random
#main ing
pcd  = PersonaDaoControl()
cd = FacturaDao()
lista = Linked_List()


try:    
        

    """

    pcd._persona._apellidos = "Juan"
    pcd._persona._nombres = "Perez"
    pcd._persona._telefono = "090009990"
    pcd._persona._tipoIdentificacion = "CEDULA"
    lista = pcd._list()
    lista.print()
    #pcd.save
    #pcd._persona = None        
    #print(pcd._lista)
    pcd._persona._apellidos = "Luis"
    pcd._persona._nombres = "Perez"
    pcd._persona._telefono = "099191991"
    pcd._persona._tipoIdentificacion = "EDUCATIVO"

    pcd.save """
    


    #pcd._list().sort_models("_apellidos",1).print
    #lista = pcd._list()
   # lista.sort_models("_apellidos",1)
    #lista.print
    numeros = Linked_List()
    
    for i  in range(0, 10000):
        numeros.add(random.randint(0, 10000))
    variable1 = numeros
    variable2 = numeros
    variable3 = numeros

    tiempo = time.time()
    variable1.sort(1,1)
   
   # lista = numeros.search_binary(10) 
    #lista.print
    print("Tiempo de ejecucion: ", time.time()-tiempo)
    tiempo = time.time()
    variable2.sort(1,2)
  
    lista = numeros.search_binary(10) 
    lista.print
    print("Tiempo de ejecucion: ", time.time()-tiempo)

    tiempo = time.time()
    variable3.sort(1,3)
    
   # lista = numeros.search_binary(10) 
    #lista.print
    print("Tiempo de ejecucion: ", time.time()-tiempo)




except Exception as error:
    print("errores")
    print(error)
