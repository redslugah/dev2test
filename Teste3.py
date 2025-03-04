'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média
'''

#Não localizei a fonte dos dados na plataforma GUPY, então será utilizado uma lista de valores aleatórios
faturamento = [2480, 2294, 1085, 0, 496, 0, 2976, 0, 1085, 0, 0, 0, 3007, 2604, 0, 403, 713, 1984, 465, 2418, 0, 0, 806, 1612, 0, 837, 1209, 310, 0, 2945]
dias = 0

while 0 in faturamento:
    faturamento.remove(0)

media = sum(faturamento)/len(faturamento)
faturamento.sort()

for i in faturamento:
    if i > media:
        dias+=1

print('menor valor de faturamento em um dia: {}'.format(faturamento[0]))
print('maior valor de faturamento em um dia: {}'.format(faturamento[-1]))
print('O número de dias no mês que o valor foi maior que a média mensal é de {} dias'.format(dias))