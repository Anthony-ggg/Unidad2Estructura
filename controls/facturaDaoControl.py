from typing import Type
from controls.dao.daoAdapter import DaoAdapter
from models.factura import Factura

class FacturaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Factura)
        self.__factura = None

    @property
    def _factura(self):
        if self.__factura == None:
            self.__factura = Factura()   
        return self.__factura
    
    @_factura.setter
    def _factura(self, value):
        self.__factura = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__factura._id = self._lista._lenght + 1
        self._save(self.__factura)
    
    
    def merge(self, pos):
        self._merge(self.__factura,pos)

    def delete(self, pos):
        self._delete(pos)