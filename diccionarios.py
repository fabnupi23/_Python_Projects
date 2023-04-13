my_dict = {}
print(type(my_dict))

my_dict = {
    'name' : "Fabian",
    'apellido' : "Nunez",
    'age' : 30
}
print(my_dict)
print(len(my_dict))

#Para saber en que posición  se encuentra cada dato
print(my_dict['age'])
print(my_dict['apellido']) #En caso de no existir el dato presenta error, se recomienda utilizar el get para mitigar errores
print(my_dict.get('SinValor')) 

#Verificamos si el tipo de dato esta o no en el diccionario
print('name' in my_dict)
print('Otro que no' in my_dict)