#Indexing 
text = "Ella sabe Python"
print(text[0])

size = len(text)
print('Size => ',size)
print(text[size - 1]) #Para saber el ultimo caracter del texto

#slicing
print(text[0:5]) #Esto me ayuda a sacar cieta cantidad de caracteres sabiendo exactamente su posicion 
print(text[10:16])

'''
Así como hicimos esta notación para ir desde el principio hasta el final tambien podriamos tener una posición directa 
desde un punto en especifico y en automatico ir hasta el final 
'''
print(text[5:-1])
print(text[5:])
print(text[:])