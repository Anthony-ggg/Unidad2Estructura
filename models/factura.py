from models.persona import Persona

class Factura:
    def __init__(self):
        self.__id = 0
        self.__fecha = ""
        self.__persona = ""
        self.__subtotal = 0.0
        self.__precio = 0.0
        self.__ruc = ""
        self.__tipo=""
        self.__retencion=0.0

    @property
    def _retencion(self):
        return self.__retencion

    @_retencion.setter
    def _retencion(self, value):
        self.__retencion = value

    @property
    def _tipo(self):
        return self.__tipo

    @_tipo.setter
    def _tipo(self, value):
        self.__tipo = value


    @property
    def _ruc(self):
        return self.__ruc

    @_ruc.setter
    def _ruc(self, value):
        self.__ruc = value


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _persona(self):
        return self.__persona

    @_persona.setter
    def _persona(self, value):
        self.__persona = value

    @property
    def _subtotal(self):
        return self.__subtotal

    @_subtotal.setter
    def _subtotal(self, value):
        self.__subtotal = value

    @property
    def _precio(self):
        return self.__precio

    @_precio.setter
    def _precio(self, value):
        self.__precio = value

    
    
    @property
    def serializable(self):
        return {
            "id": self._id,
            "fecha": self._fecha,
            "persona": self._persona,
            "subtotal": self._subtotal,
            "precio": self._precio, 
            "ruc": self._ruc,
            "tipo": self._tipo,
            "retencion": self._retencion
        }
#conocer contexto de deserializar-----``
    def deserializar(data):
        factura = Factura()
        factura._id = data["id"]
        factura._fecha = data["fecha"]
        factura._persona = data["persona"]
        factura._subtotal= data["subtotal"] 
        factura._precio= data["precio"]
        factura._ruc = data["ruc"]
        factura._tipo = data["tipo"]
        factura._retencion = data["retencion"]
        
        return factura