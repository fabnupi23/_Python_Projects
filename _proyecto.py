'''
crearemos un programa que ejecute la logica del juego piedra papel o tijera y asi jugar contra
la computadora, poco a poco se ira incrementando el nivel de este proyecto 
'''
import random #importamos esta liberia, este módulo implementa generadores de números pseudoaleatorios para varias distribuciones.

#Vamos a crear una tupla para estas opciones
options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0

rounds = 1

while True:

    print('*' * 10)
    print('Round', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)

    #Primero creamos dos variables 

    user_option = input('piedra, papel o tijera => ')   #Leemos la opción del usuario
    user_option = user_option.lower() #Pasamos todo a minuscula

    rounds += 1

    if not user_option in options:
        print('Esa opción no es valida')
        continue


    computer_option = random.choice(options)  #La computadora tiene la opción piedra para siempre, con la implementación de Random se generara una opción aleatoria 

    print('User Options => ', user_option)
    print('Computer Options => ', computer_option)

    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('User gano¡')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('Computer gano¡')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('User gano¡')
            user_wins += 1
        else:
            print('Tijera gana a papel')
            print('Computador gano¡')
            computer_wins += 1
    elif user_option == 'tijeras':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('User gano¡')
            user_wins += 1
        else: 
            print('Piedra gana a tijera')
            print('Computer gano¡')
            computer_wins += 1

    if computer_wins == 2:
        print('El rotundo ganador es la computadora')
        break
    if user_wins == 2:
        print('El rotundo ganador es la computadora')
        break
        
    
