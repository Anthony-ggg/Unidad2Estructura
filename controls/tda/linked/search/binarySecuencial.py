from controls.tda.linked.search.binary import Binary
from controls.tda.linked.search.secuencial import Secuencial
from controls.tda.linked.sort.quickSort import QuickSort

class BinarySecuencial:

    def search_BinarySecuencial(self, array, element):
        quickSort = QuickSort()
        binary = Binary()
        secuencial = Secuencial()

        sorted_array = quickSort.sort_primitive_ascendent(array)
        index = binary.search_binary(sorted_array, element)
        if index == -1:
            return -1
        
        return secuencial.search_sequential(sorted_array, element, index)
    
    def search_BinarySecuencial_models(self, array, element, attribute):
        quickSort = QuickSort()
        binary = Binary()
        secuencial = Secuencial()
        
        prueba = []
        i = 0
    
        while i < len(array):
            prueba.append(array[i])
            i = i + 1
        index = binary.search_binary_models(array, element, attribute)
    
        if index == -1:
            return -1
        elif index != (len(array)):
            return secuencial.search_sequential_models(array, element, attribute, index)
        else:
            print(prueba[index])
            return secuencial.search_sequential_models(prueba, element, attribute, index)
