#--------------------------------------------------------------
#1. Actualizar valores en diccionarios y listas

#Cambia el valor 10 en x a 15. Una vez que hayas terminado, 
#x ahora debería ser [ [5,2,3], [15,8,9] ].
'''
x = [ [5,2,3], [10,8,9] ] 

x [1][0] = 15
print(x)
'''
#--------------------------------------------------------------
#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
'''
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

estudiantes [0] ['last_name']= 'Bryant'
print(estudiantes)
'''
#--------------------------------------------------------------
#En el directorio_deportes, cambia "Messi" por "Andrés".
'''
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'futbol' : ['Messi', 'Ronaldo', 'Rooney']
}

directorio_deportes ['futbol'] [0] = 'Andrés'
print(directorio_deportes)
'''
#--------------------------------------------------------------
#Cambia el valor 20 en z a 30.
'''
z = [ {'x': 10, 'y': 20} ]

z [0] ['y'] = 30
print(z)
'''
#--------------------------------------------------------------
#2. Iterar a través de una lista de diccionarios

#Crea una función iterateDictionary(some_list)para que, dada una 
#lista de diccionarios, la función recorra cada diccionarios de la
#lista e imprima cada llave y el valor asociado. Por ejemplo, 
#dada la siguiente lista:


estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(estudiantes):
    for i in range(len(estudiantes) - len(estudiantes), len(estudiantes)):
        for key, value in estudiantes[0].items(), estudiantes[1].items():
            print(value)
    return
print (iterateDictionary(estudiantes))