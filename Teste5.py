'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

reverter = 'Escreva um programa que inverta os caracteres de um string'
resultado = ''

for i in range(len(reverter)-1, -1, -1):
    resultado += reverter[i]

print(resultado)