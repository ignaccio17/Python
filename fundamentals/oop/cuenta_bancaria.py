class CuentaBancaria:
    nombre_banco = "Bank Coding Dojo"
    todas_cuentas = []


    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance


    def deposito(self, amount):
        self.balance += amount
        return self


    def retiro(self, amount):
        self.balance -= amount
        return self


    def mostrar_info(self):
        print(f"El monto del balance es igual a {self.balance} el monto de interes es {self.tasa_interes}")
        return self


    def generar_interes(self):
        self.balance += self.balance * self.tasa_interes
        return self


Cuenta1 = CuentaBancaria(0.5, 10000)
Cuenta1.deposito(500).deposito(400).deposito(
    50).generar_interes().mostrar_info()

print((10000 + 950))
print((10000 + 950) * 0.5)
print((10000 + 950) + (10000 + 950) * 0.5)
