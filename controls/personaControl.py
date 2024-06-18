from models.persona import Persona
from controls.tda.linked.linkedList import Linked_List
import json

class PersonaControl:
    def __init__(self):
        self.__persona = None
        self.__id_counter = 0
        self.__lista = Linked_List()
        

    @property
    def _persona(self):
        if self.__persona == None:
            self.__persona = Persona()
        return self.__persona

    @_persona.setter
    def _persona(self, value):
        self.__persona = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value
        
    
    def save(self):
        self._persona._id = self.__id_counter
        self._lista.add(self._persona, self._lista._lenght)

    def obtener_id(self):
        persona_info = f"ID: {self._persona._id}, Apellidos: {self._persona._apellidos}, Nombres: {self._persona._nombres}"
        self.__id_counter += 1 
        self._persona = Persona()
        return persona_info
    
    def saveJson(self):
        try:
            personas = []

            if self._persona._apellidos or self._persona._nombres or self._persona._dni or self._persona._direccion or self._persona._telefono:
                personas.append(self._persona.to_dict())

            node = self._lista._head
            while node is not None:
                if node._data._apellidos or node._data._nombres or node._data._dni or node._data._direccion or node._data._telefono:
                    personas.append(node._data.to_dict())
                node = node._next
            with open('c:/Estructuradedatos/Files/persona.json', 'w') as file:
                json.dump(personas, file, indent=4)
        except Exception as error:
            print("Error al guardar en JSON:", error)
