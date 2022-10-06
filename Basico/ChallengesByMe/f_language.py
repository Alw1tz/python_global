# Idioma de la f en python
def f_language(test_str, K):
    # string of alphabet
    alphabet = 'BCDFGHJKLMNÑPQRSTVWXYZbcdfghjklmnñpqrstvwxyz'
   # iterating to check alphabet in string
    for x in alphabet:
        # replacing vowel with the specified character
        test_str = test_str.replace(x, K)
    return test_str


# Driver Code
# input string
title = 'Vamos a '
input_str = input('Escribe la frase que quieres convertir: ')

# specified character
K = 'f'


# printing output
print("Resultado:",
      f_language(input_str, K))
