#---------------------------------------------------------------------------------------------

#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

'''
PREDECIR:

El resultado es 5
'''
#---------------------------------------------------------------------------------------------

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

'''
CORRECION:

El error es que la funcion "number_of_days_in_a_week_silicon_or_triangle_sides" pareciera que fuera una cadena
y no una funcion, ademas de que no se define ningun valor a ella.

PREDECIR:

Sin este error el codigo daria 5
'''
#---------------------------------------------------------------------------------------------

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

'''
PREDECIR:

Considerando que el primer return es el que vale el codigo daria 5
'''
#---------------------------------------------------------------------------------------------

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

'''
PREDECIR:

El resultado seria 5
'''
#---------------------------------------------------------------------------------------------

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

'''
PREDECIR:

El resultado seria 5
'''
#---------------------------------------------------------------------------------------------

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

'''
PREDECIR:

La respuestas es (3) y (5) por la suma de add(1,2) + add(2,3)
'''
#---------------------------------------------------------------------------------------------

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

'''
PREDECIR:

El resultado seria 25 por la union de 2,5
'''
#---------------------------------------------------------------------------------------------

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

'''
PREDECIR:

Se devuelve a 10 por el return 10
'''
#---------------------------------------------------------------------------------------------

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

'''
PREDECIR:

El resultado sera multiplos de 7 hasta 21
'''
#---------------------------------------------------------------------------------------------

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

'''
PREDECIR:

El resultado sera 8 por la suma de 3 + 5
'''
#---------------------------------------------------------------------------------------------

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

'''
PREDECIR:

El resultado sera 500,500 y se devolvera a 300 para dar 500
'''
#---------------------------------------------------------------------------------------------

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

'''
PREDECIR:

El resultado sera 500,500 y se devolvera a 300 para despues dar 500
'''
#---------------------------------------------------------------------------------------------

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

'''
PREDECIR:

El resultado sera 500,500 y la otra funcion 300,300
'''
#---------------------------------------------------------------------------------------------

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

'''
PREDECIR:

El resultado sera 1,3,2 por todos 3 print que hay
'''
#---------------------------------------------------------------------------------------------

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

'''
PREDECIR:

El resultado dara 1,3,5 y se devovlera a 10
'''
#---------------------------------------------------------------------------------------------