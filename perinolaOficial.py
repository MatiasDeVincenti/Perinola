from random import choice

##crea una clase
class Perinola:
    ##constructor 
    def __init__(self):
        self.cara_visible = 'Pon 1'
    ##funcion para mostrar el print
    def __repr__(self):
        return f"Salio: {self.cara_visible}" 
    
    ##Funcion tirar dado perinola
    def tirar(self):   
        caras = ("Pon 1", "Toma 2", "Todos Ponen",
     "Toma 1", "Pon 2", "Toma Todo")
        self.cara_visible = choice(caras)
        return self.cara_visible