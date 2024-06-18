import enum
class EnumTipoIdentificacion(enum.Enum):
    EDUCATIVO = 'EDUCATIVO'
    PROFESIONAL= 'PROFESIONAL'
    @property
    def strToEnum(self):
        if self.value == 'EDUCATIVO':
            return EnumTipoIdentificacion.EDUCATIVO
        elif self.value == 'PROFESIONAL':
            return EnumTipoIdentificacion.PROFESIONAL
        else:
            return None
    