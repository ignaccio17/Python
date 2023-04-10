import random

class Baraja:
    def __init__(self):
        # Crear baraja
        figuras = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
        valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Reina', 'Rey']
        self.baraja = []
        for figuras in figuras:
            for valor in valores:
                self.baraja.append((valor, figuras))

    def mezclar(self):
        # Mezclar la baraja
        random.shuffle(self.baraja)

    def sacar_carta(self):
        # Sacar una carta de la baraja
        return self.baraja.pop()

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def tomar_carta(self, carta):
        # Agregar carta a la mano del jugador
        self.mano.append(carta)

    def mostrar_mano(self):
        # Mostrar cartas en la mano del jugador
        print(self.nombre + "'s mano:")
        for carta in self.mano:
            print('  ' + carta[0] + ' de ' + carta[1])

    def valor_mano(self):
        # Calcular valor total de la mano del jugador
        valores = {'As': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jota': 10, 'Reina': 10, 'Rey': 10}
        total = 0
        ases = 0
        for carta in self.mano:
            valor = carta[0]
            if valor == 'As':
                ases += 1
            total += valores[valor]
        while total > 21 and ases > 0:
            total -= 10
            ases -= 1
        return total

# Crear baraja y mezclarla
baraja = Baraja()
baraja.mezclar()

# Crear dos jugadores
nacho = Jugador('nacho')
dilan = Jugador('dilan')

# Repartir dos cartas a cada jugador
nacho.tomar_carta(baraja.sacar_carta())
nacho.tomar_carta(baraja.sacar_carta())
dilan.tomar_carta(baraja.sacar_carta())
dilan.tomar_carta(baraja.sacar_carta())

# Mostrar cartas de nacho y una carta de dilan
nacho.mostrar_mano()
print(' ')
print("dilan's mano:")
print('  ' + dilan.mano[0][0] + ' de ' + dilan.mano[0][1])

# Pedir al jugador que opte por más cartas
while True:
    opcion = input("Quieres tomar otra carta? (s/n) ")
    if opcion.lower() == 's':
        nacho.tomar_carta(baraja.sacar_carta())
        nacho.mostrar_mano()
        if nacho.valor_mano() > 21:
            print('Te has pasado de 21. Perdiste.')
            quit()
    else:
        break

# Jugada de dilan
dilan.mostrar_mano()
while dilan.valor_mano() < 17:
    dilan.tomar_carta(baraja.sacar_carta())
    dilan.mostrar_mano()

# Comparar manos
nacho_total = nacho.valor_mano()
dilan_total = dilan.valor_mano()
print(' ')
print("Puntajes:")
print(nacho.nombre + ': ' + str(nacho_total))
print(dilan.nombre + ': ' + str(dilan_total))
if nacho_total > dilan_total:
    print(nacho.nombre + ' gana!')
elif dilan_total > nacho_total:
    print(dilan.nombre + ' gana!')
else:
    print('Empate!')