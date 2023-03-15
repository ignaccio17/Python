#-----------------------------------------------------------------------------------------------------------#
#Básico: imprime todos los números enteros del 0 al 150.
'''
for i in range(151):
    print(i)
'''

#-----------------------------------------------------------------------------------------------------------#
#Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
'''
for x in range(0,1005,5):
    print(x)
'''

#-----------------------------------------------------------------------------------------------------------#
#Contar, a la manera del Dojo: imprime números enteros del 1 al 100. 
# Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".

'''
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
'''

#-----------------------------------------------------------------------------------------------------------#
#Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.

'''
sum= 0
for i in range(1, 500000):
    if i % 2 == 1:
        print(i)
    sum += i
print(sum)
'''

#-----------------------------------------------------------------------------------------------------------#
#Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.

'''
y = 2018
while y > 0:
    print(y)
    y = y - 4
    if y == 0:
'''

#-----------------------------------------------------------------------------------------------------------#
#Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, 
# imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. 
# El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 

'''
lowNum=2
highNum=500
mult=10

for i in range(lowNum, highNum + 1 ):
 if i % mult == 0:
    print(i)
'''

#-----------------------------------------------------------------------------------------------------------#