person = {
    'name' : 'Fabian',
    'apellido'  : 'Nunez',
    'age' : 31,
    'langs' : ['python', 'JavaScript']
}

print(person)

#Actualización de atributos
person['name'] = 'Andres'
person['age'] -= 20
person['langs'].append('Rust')
print(person)

#Para eliminar un atributo
del person['apellido']
person.pop('age')
print(person)

#Obtener items de un diccionario
print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())