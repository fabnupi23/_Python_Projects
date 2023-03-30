'''
crearemos un programa que ejecute la logica del juego piedra papel o tijera y asi jugar contra
la computadora, poco a poco se ira incrementando el nivel de este proyecto 
'''

#Primero creamos dos variables 

user_option = input('piedra, papel o tijera => ')
computer_option = 'piedra' 

if user_option == computer_option:
    print('Empate!')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('Piedra gana a tijera')
        print('User gano¡')
    else:
        print('Papel gana a piedra')
        print('Computer gano¡')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('Papel gana a piedra')
        print('User gano¡')
    else:
        print('Tijera gana a papel')
        print('Computador gano¡')
elif user_option == 'tijeras':
    if computer_option == 'papel':
        print('Tijera gana a papel')
        print('User gano¡')
    else: 
        print('Piedra gana a tijera')
        print('Computer gano¡')
