from jugador import Jugador

def test_constructor():
    j = Jugador("Matias")
    assert(j.nombre == "Matias")
    assert(j.fichas == 5)

def test_dar_ficha():
    j = Jugador("Matias", 10)
    j.darFicha(5)
    assert(j.fichas == 15)

def test_dar_ficha_sin_argumento():
    j = Jugador("Matias", 10)
    j.darFicha()
    assert(j.fichas == 11)

def testSacarFicha(self,cuantas):
    j = Jugador("Matias", 15)
    j.sacarFicha(7)
    assert(j.fichas == 8)