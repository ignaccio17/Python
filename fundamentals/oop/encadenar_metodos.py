class Usuario:
    def __init__(self, name, email, balance_cuenta):
        self.name = name
        self.email = email
        self.balance_cuenta = balance_cuenta
        
    def hacer_depósito(self, amount):
        self.balance_cuenta += amount
        return self

    def hacer_giro(self, amount):
        self.balance_cuenta -= amount
        return self


guido = Usuario("Guido", "Correo@correo.cl", 0)
ignacio = Usuario("Ignacio", "Correo@correo.cl", 100)

guido.hacer_depósito(150)
ignacio.hacer_depósito(150)

print("El usuario", guido.name, "Tiene en su cuenta", guido.balance_cuenta)

guido.hacer_giro(150)

print("El usuario", guido.name, "Disminuyo su saldo a", guido.balance_cuenta)
print("El usuario", ignacio.name, "tiene en su cuenta", ignacio.balance_cuenta)