from typing import Any
import json
from controls.tda.linked.node import Node
from controls.exception.arrayPositionException import ArrayPositionException
from controls.exception.linkedEmpty import LinkedEmpty
from controls.tda.linked.sort.insercion import Insercion
from numbers import Number
from controls.tda.linked.sort.burbuja import Burbuja
from controls.tda.linked.sort.mergeSort import MergeSort
from controls.tda.linked.sort.quickSort import QuickSort
from controls.tda.linked.sort.shellSort import ShellSort
from controls.tda.linked.search.binary import Binary
from controls.tda.linked.search.secuencial import Secuencial
from controls.tda.linked.search.binarySecuencial import BinarySecuencial

class Linked_List(object):
    def __init__(self):
        self.__head = None  
        self.__last = None
        self.__lenght = 0

    @property
    def _lenght(self):
        return self.__lenght

    @_lenght.setter
    def _lenght(self, value):
        self.__lenght = value

    @property
    def isEmpty(self):
        return self.__head == None or self.__lenght == 0  

    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node  
            self.__last = node
            self.__lenght += 1
        else:
            headOld = self.__head  
            node = Node(data, headOld)
            self.__head = node  
            self.__lenght += 1

    def __addLast__(self, data):
        if self.isEmpty:
           self.__addFirst__(data)
        else:
            node = Node(data)
            self.__last._next = node
            self.__last = node
            self.__lenght += 1

    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__lenght = 0

    #insetar en una posicion           
    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__lenght:
            self.__addLast__(data)
        else:
            node_preview = self.getNode(pos - 1)
            node_last = node_preview._next #self.getNode(pos)
            node = Node(data, node_last)
            node_preview._next = node
            self.__lenght += 1
    
    #Modificar
    def edit(self, data, pos = 0):
        if pos == 0:
            self.__head._data = data 
        elif pos == self.__lenght:
            self.__last._data = data
        else:
            node = self.getNode(pos)  
            node._data = data
    # Remove the duplicate definition of the toArray method

   
        #TODO:
    def delete(self, pos = 0):
        if pos == 0:
            self.__head = self.__head._next  
        elif pos == self.__lenght - 1:
            node = self.__head  
            while node._next != self.__last:
                node = node._next
            node._next = None
            self.__last = node
        else:
            cont = 1
            node = self.__head  
            
            while node._next != None and cont < pos:
                node = node._next
                cont += 1
        self.__lenght -= 1
    
    """Obtiene el objeto nodo"""
    def getNode(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._lenght:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head
        elif pos == (self.__lenght - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
        
    """Obtiene el objeto nodo"""
    def get(self, pos):
        
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._lenght:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head._data
        elif pos == (self.__lenght - 1):
            return self.__last._data
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node._data
    
    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            return "List is Empty"
        else:
            node = self.__head  # Cambio aquí
            while node != None:
                out += str(node._data) + "\t"
                node = node._next          
        return out
    
    @property
    def print(self):
        node = self.__head
        data = ""    
        while node != None:
            data += str(node._data)+"    "            
            node = node._next
        print("Lista de datos")
        print(data)
        
    @property
    def toArray(self):
        array = []
        if not self.isEmpty:
            node = self.__head
            cont = 0
            while cont < self.__lenght:
                array.append(node._data)
                cont += 1
                node = node._next
        return array
    
    def toList(self, array):
        self.clear
        for i in range(0, len(array)):
            self.__addLast__(array[i])      
    # a < b
             
    def sort(self, type,metodo = 1):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            # Datos primitivos
            if isinstance(array[0], Number) or isinstance (array[0], str):
                if metodo == 1:
                    order = QuickSort()
                elif metodo == 2:
                    order = MergeSort()
                else:
                    order = ShellSort()
            
                if type == 1:
                    #array = order.sort_burbuja_number_ascendent(array)
                    array = order.sort_primitive_ascendent(array)
                else:
                    array = order.sort_primitive_descendent(array)
                    #array = order.sort_burbuja_number_descendent(array)
            
            self.toList(array)
    
    def sort_models(self,attribute, type = 1, metodo= 1):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if isinstance(array[0], object):
                if metodo == 1:
                    order = QuickSort()
                elif metodo == 2:
                    order = MergeSort()
                else:
                    order = ShellSort()
            
                if type == 1:
                    #array = order.sort_burbuja_attribute_ascendent(array, attribute)
                    array = order.sort_models_ascendent(array, attribute)
                else:
                    #array = order.sort_burbuja_attribute_descendent(array, attribute)
                    array = order.sort_models_descendent(array, attribute)
                #cls = getattr(array[0], attribute)
                #print(cls)
            self.toList(array)
        return self
    
    def search_equals(self, data):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray    
            for i in range(0, len(array)):
                if array[i] == data: #array[i].lower().startswith(data.lower()): #:
                    list.add(array[i], list._length)
        return list
    
    def busqueda_binaria(self, data):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            binary = Binary()
            return binary.search_binary(array, data)
        
    def busqueda_binaria_models(self, data, attribute):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            binary = Binary()
            array= binary.search_binary_models(array, data, attribute)
            self.toList(array)