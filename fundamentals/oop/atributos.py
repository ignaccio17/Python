# declarar una clase y darle el nombre Usuario
class Usuario:		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0
        self.signo = "leo"
        self.deporte = "futbol"

Usuario()
guido = Usuario()
monty = Usuario()
# Accediendo a los atributos de la instancia
print(guido.name)	# salida: Michael
print(monty.email)	# salida: Michael

# monty.email = 222                      

# print(monty.email)

print(monty.name, "y me gusta", monty.deporte, "y mi signo es ", monty.signo)

