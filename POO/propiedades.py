class Propiedades:
    def __init__(self, dia):
        self._d = dia

    def _getDia(self):
        return self._d
    def _setDia(self, dia):
        self._d = dia

    dia = property(_getDia, _setDia)


d = Propiedades(3)
print("Dia", d.dia)