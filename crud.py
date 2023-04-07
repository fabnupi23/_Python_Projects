#CRUD Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])

numbers[-1] = 10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0, 'Hola')
print(numbers)

numbers.insert(3, 'Change')
print(numbers)

tasks = ['Todo 1', 'Todo 2', 'Todo 3']
new_list = numbers + tasks
print(new_list)

print(new_list.index('Todo 2'))

new_list.remove('Todo 1')
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

numbers_a = [1, 7, 8, 5, 6, 9, 2, 3, 4]
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)