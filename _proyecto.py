'''
crearemos un programa que ejecute la logica del juego piedra papel o tijera y asi jugar contra
la computadora, poco a poco se ira incrementando el nivel de este proyecto 
'''
import random #importamos esta liberia, este módulo implementa generadores de números pseudoaleatorios para varias distribuciones.

#Vamos a crear una tupla para estas opciones
options = ('piedra', 'papel', 'tijera')


#Primero creamos dos variables 

user_option = input('piedra, papel o tijera => ')   #Leemos la opción del usuario
user_option = user_option.lower() #Pasamos todo a minuscula

if not user_option in options:
    print('Esa opción no es valida')


computer_option = random.choice(options)  #La computadora tiene la opción piedra para siempre, con la implementación de Random se generara una opción aleatoria 

print('User Options => ', user_option)
print('Computer Options => ', computer_option)

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
