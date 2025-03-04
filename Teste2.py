'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não 
a sequência.
'''
fibo = [0, 1]
b_fibo = 0
number = int(input('Digite o número que deseja verificar se faz parte da sequência de Fibonacci: '))

while number not in fibo and number > b_fibo:
    fibo.append(sum(fibo[-2:]))
    b_fibo = fibo[-1]

if number in fibo:
    print('O número faz parte da sequência de Fibonacci!')
else:
    print('O número não faz parte da sequência de Fibonacci!')
