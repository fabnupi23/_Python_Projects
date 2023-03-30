'''
crearemos un programa que ejecute la logica del juego piedra papel o tijera y asi jugar contra
la computadora, poco a poco se ira incrementando el nivel de este proyecto 
'''

#Primero creamos dos variables 

user_option = input('piedra, papel o tijera => ')
computer_option = 'piedra' 

if user_option == computer_option:
    print('Empate!')