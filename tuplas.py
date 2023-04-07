#TUPLAS 

numbers = (1, 2, 3, 4, 5)

strings = ('andres', 'angie', 'licet', 'andres')

print(numbers)
print('0 => ', numbers[0])
print('0 => ', numbers[-1])
print(type(numbers))

print(strings)
print('0 => ', strings[0])
print('0 => ', strings[-1])
print(type(strings))

'''
- Acá vamos a ver un par de metodos que tiene la Tupla 
- Uno de ellos es buscar un elemento dentro de la tupla y ver cuales son los elementos  o en que posicion 
  está ese elemento


'''
print(strings)
print(strings.index('angie'))
print(strings.count('andres'))


#Convertimos una Tupla a una lista
my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[0] = 'Fabian'
print(my_list)
print(type(my_list))

#Ahora transformamos de una lista a una Tupla
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))