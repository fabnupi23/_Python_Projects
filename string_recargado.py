text = 'Angie sabe programar en Python'
print('JavaScript' in text)
print('Python' in text)

'''
if 'JS' in  text:
    print('Elegiste bien!!')
else:
    print('Tambien elegiste bien!!')

'''


#cosas que podemos hacer con el string y es evaluar el tamaño de un string 

size = len('') #el metodo len examina el tamaño en el numero de caracteres y también cuenta los espacios 
print(size)

print(text)
print(text.upper()) #Esta metodo upper pasaria todo a mayuscula
print(text.lower()) #Esta metodo upper pasaria todo a minuscula
print(text.count('a'))#con esta metodo contamos el numero de apariciones que tiene una letra en especifico 
#print(text.startswith('Angie')) #Este metodo nos indica con que palabra inicia el texto, esa palabra la indicamos nosotros, la respuesta sera booleana
#print(text.swapcase())#este metodo lo que nos va a ahcer es transformar cualqhier caracter que este en mayuscula lo pasa a minuscula y viceversa 
#print(text.endswith()) #Este metodo nos indica con que palabra finaliza el texto, esa palabra la indicamos nosotros, la respuesta sera booleana
print(text.replace('Python', 'React')) #Este metodo nos ayuda a reemplazar una cosa po otra.


text_2 = 'este es mi titulo'
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())