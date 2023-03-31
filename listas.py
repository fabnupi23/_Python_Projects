#Las listas nos permiten almacenar datos de varios tipos 
numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'Play videgames', 'Go to market']
print(tasks)
print(type(tasks))

types = [1, True, 'String']
print(types)

print(numbers[0])
print(tasks[0])

#Acá realizamos una utación a una lista, en este caso a la lista Tasks
tasks[0]='Watch Platzi courses'
print(tasks)

print(numbers[:3])
print(True in types)