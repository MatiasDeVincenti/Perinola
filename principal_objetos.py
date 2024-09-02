from perinola import Perinola
from apuesta import Apuesta

# perinola = Perinola()
# perinola.tirar()
# print(perinola)

ap = Apuesta()
print(ap)
ap.ponerFicha(4)
print(ap)
ap.ponerFicha()
print(ap)

ap.tomarFicha(3)
print(ap)
ap.tomarFicha()
print(ap)
