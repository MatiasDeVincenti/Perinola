class Jugador:
    def __init__(self, nombre, fichas=5):
        self.nombre = nombre
        self.fichas = fichas

    def darFicha(self, cuantas=1):
        self.fichas = self.fichas + cuantas

        def tomarFicha(self, cuantas=1):
            if cuantas > self.fichas:
                raise ValueError(f"No alcanza para sacar {cuantas} fichas.  Hay solo {self.fichas}")
        self.fichas = self.fichas - cuantas