class Usuario:
    def __init__(self, name, email, balance_cuenta):
        self.name = name
        self.email = email
        self.balance_cuenta = balance_cuenta

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount 

    def hacer_giro(self, amount):
        self.balance_cuenta -= amount

guido = Usuario("Guido", "email@email.com", 0)
Ignacio = Usuario("Ignacio", "email@email.com", 300)

guido.hacer_deposito(150)
Ignacio.hacer_deposito(150)

print("El usuario", guido.name, "Tiene de saldo", guido.balance_cuenta)

guido.hacer_giro(150)

print("El usuario", guido.name, "Disminuyo su saldo a", guido.balance_cuenta)
print("El usuario", Ignacio.name, "Aumento su saldo a", Ignacio.balance_cuenta)