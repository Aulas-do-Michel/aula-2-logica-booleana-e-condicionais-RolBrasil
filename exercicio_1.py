"""
#### Exercício 1

Receba um número inteiro de um usuário. Se ele for par, imprima "Par". Se não, imprima "Ímpar".

Exemplo:

Digite um número:
10

Par
--------
Digite um número:
1

Ímpar

Dica: Lembre do comando de resto da divisão inteira!
"""
numero_digitado = input('Digite um número:')
numero = int(numero_digitado)
divisao = numero%2

if (divisao == 1):
 print('Ímpar')
else:
 print('Par')    
 
