#Librerias
import re

# while
# x = 5
# while(x >= 0):
#     print(f'{x}')
#     x-=1

# for

x = 'Holaaaa'
# for row in x:
#     print(f'{row}')

# buscar cantidad de a's que hay en la variable x
count=0
for row in x:
    if row == 'a':
        count+=1


print(f'con lógica: {count}')
print(f'sin logica: ', x.count('a'))
print(f'con expresion regular', len(re.findall("a", x)))

