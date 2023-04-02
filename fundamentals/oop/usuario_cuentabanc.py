class Bancocuenta:
    cuentas = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        Bancocuenta.cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Monto insuficiente: 5.00")
            self.balance -= 5.00
        return self
    
    def cuenta_info(self):
        return f"{self.balance}"
    
    def interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def all_accounts(cls):
        for account in cls.cuentas:
            account.cuenta_info()

class Usuario:
    def __init__(self, name)
        self.name = name
        self.account = {
            "checking" : Bancocuenta(.02,1000),
            "Savings" : Bancocuenta(.05,3000)
        }

    def mostrar_saldo(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].cuenta_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].cuenta_info()}")
        return self
    
    def transferir_dinero(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.mostrar_saldo()
        user.mostrar_saldo()
        return self
    
Ignacio = user("Ignacio")

Ignacio.account['checking'].deposito(100)
Ignacio.mostrar_saldo()