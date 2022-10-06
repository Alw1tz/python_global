#if simplificado
# x = False
#
# print(f'el valor de x es: {x}') if x else print(f'el valor de x es: {x}')

#ejercicio
edad = int(input('Dame tu edad: '))
if (edad >=0 and edad<=10):
    print('La infancia es increible')
elif(edad > 10 and edad <=20):
    print('Muchos cambios y mucho trabajo')
else:
    print('No aplica')