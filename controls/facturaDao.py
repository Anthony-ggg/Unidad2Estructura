from typing import Type
from controls.dao.daoAdapter import DaoAdapter
from models.factura import Factura

class FacturaDao(DaoAdapter):
    def __init__(self):
        super().__init__(Factura)
        self.__factura = None

    @property
    def _factura(self):
        return self.__factura

    @_factura.setter
    def _factura(self, value):
        self.__factura = value
    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        #print("ccc")
        #print(self.__persona)
        self.__factura = self._lista._lenght + 1
        self._save (self.__factura)
   