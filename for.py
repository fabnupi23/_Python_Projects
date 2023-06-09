for element in range(1, 20):
    print(element)



my_list = [23, 45, 67, 89, 43]

for element in my_list:
    print(element)

my_tuple = ('Nico', 'Angie', 'Jacob')
for element in my_tuple:
    print(element)



product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}

for key in product:
    print(key, '=>', product[key])

for key, value in product.items():
    print(key, '=>', value)



people = [
    {
        'name': 'Angie',
        'age': 36
    },
    {
        
        'name': 'Nico',
        'age': 14
    },
    {
        'name': 'Jacob',
        'age': 9
    }
]

for person in people: 
    print(person)
    print('name =>', person['name'])