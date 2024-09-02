from perinola import Perinola
from apuesta import Apuesta

# perinola = Perinola()
# perinola.tirar()
# print(perinola)

ap = Apuesta()
print(ap)
ap.ponerFicha(8)
print(ap)
ap.ponerFicha()
print(ap)

ap.tomarFicha(3)
print(ap)
ap.tomarFicha()
print(ap)

f = ap.tomarTodas()

print(f"Se sacaron {f} fichas")
print(ap)
