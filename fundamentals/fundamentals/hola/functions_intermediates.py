#--------------------------------------------------------------
#1. Actualizar valores en diccionarios y listas

#Cambia el valor 10 en x a 15. Una vez que hayas terminado, 
#x ahora debería ser [ [5,2,3], [15,8,9] ].

x = [ [5,2,3], [10,8,9] ] 

x [0][0] = 15
print(x)

#--------------------------------------------------------------
#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.

estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

estudiantes [0] ['last_name']= 'Bryant'
print(estudiantes)

#--------------------------------------------------------------
#En el directorio_deportes, cambia "Messi" por "Andrés".

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'futbol' : ['Messi', 'Ronaldo', 'Rooney']
}

directorio_deportes ['futbol'] [0] = 'Andrés'
print(directorio_deportes)

#--------------------------------------------------------------
#Cambia el valor 20 en z a 30.

z = [ {'x': 10, 'y': 20} ]

z [0] ['y'] = 30
print(z)

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
    for i in range(0, len(estudiantes)):
        output = ""
        for key, val in estudiantes[i].items():
            output += f" {key} - {val},"
        print(output)

iterateDictionary(estudiantes)
        
#--------------------------------------------------------------
#3. Obtener valores de una lista de diccionarios

#Crea una función iterateDictionary2(key_name, some_list)que, 
#dada una lista de diccionarios y un nombre de clave, la función 
#imprima el valor almacenado en esa clave para cada diccionario. 
#Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:

def iterate_Dictionary2(key_name,list):
    for i in range(0, len(list)):

        for key,val in list[i].items():
            if key == key_name:
                print(val)
iterate_Dictionary2('first_name', estudiantes)
iterate_Dictionary2('last_name', estudiantes)
#--------------------------------------------------------------
#4. Iterar a través de un diccionarios con valores de lista

#Crea una función printInfo(some_dict)que, dado un diccionario 
#cuyos valores son todos listas, imprima el nombre de cada clave
#junto con el tamaño de su lista, y luego imprima los valores 
#asociados dentro de la lista de cada clave. Por ejemplo:

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info(dict):
    for key,val in dict.items():
        print(f"-------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

print_info(dojo)