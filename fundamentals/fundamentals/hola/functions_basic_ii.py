#-----------------------------------------------------------------------

'''1. Cuenta regresiva: crea una función que acepte un número como entrada.
Devuelve una lista nueva que cuente de uno en uno, desde el número 
(como elemento 0) hasta 0 (como último elemento).''' 
'''
def lista(num):
    lista=[]
    for x in range (num, 0, -1):
        lista.append(x)
    return lista
print(lista(5))'''

#-----------------------------------------------------------------------

'''2. Imprimir y devolver: crea una función que reciba una lista con dos 
números. Imprime el primer valor y devuelve el segundo.
Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2'''

'''
def ir_volver():
    b = 1
    print(b)
    if b < 0:
        return 5
    
    else:
            return 2
            return 7
print(ir_volver())'''

#-----------------------------------------------------------------------

'''3. Primero más longitud: crea una función que acepte una lista y 
devuelva la suma del primer valor de la lista, más la longitud de 
la lista.'''
'''
def lista(num):
    lista = []
    for x in range (num, 0, -1):
        lista.append(x)

    print(min(lista) + max(lista))
    return lista

print(lista(5))'''

#-----------------------------------------------------------------------

'''4. Valores mayores que el segundo: escribe una función que acepte una
lista y cree una nueva que contenga solo los valores de la lista
original que sean mayores que su segundo valor. Imprime cuántos valores
son y luego devuelve la lista nueva. Si la lista tiene menos de 2 
elementos, has que la función devuelva False'''
'''
def lista_val(lista):
    if len(lista) < 2:
        return False
    output = []
    for i in  range (0 , len(lista)):
        if lista [i] > lista [1]:
            output.append(lista[i])
    print(len(output))
    return output
print(lista_val([5,2,3,2,1,4]))
print(lista_val([3]))
'''

#-----------------------------------------------------------------------
'''5. Esta longitud, ese valor: escribe una función que acepte dos enteros 
como parámetros: tamaño y valor. La función debe crear y devolver 
una lista cuya longitud sea igual al tamaño dado, y cuyos valores 
sean todos el valor dado.'''

def longitud(valor,tamaño):
    output = []
    for i in range (0, tamaño):
        output.append(valor)
    return output
print(longitud(7,4))
print(longitud(2,6))