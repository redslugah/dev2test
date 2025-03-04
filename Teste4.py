'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 
'''

valores = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53
total = sum(valores)
print(f'Contribuições por estado: \nSP: {SP*100/total:.2f}%\nRJ: {RJ*100/total:.2f}%\nMG: {MG*100/total:.2f}%\nES: {ES*100/total:.2f}%\nOutros: {OUTROS*100/total:.2f}%')

