from random import shuffle
nome1 = input('Digite o primeiro aluno: ')
nome2 = input('Digite o segundo aluno: ')
nome3 = input('Digite o terceiro aluno: ')
nome4 = input('Digite o quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('A ordem de apresentaçao sera {}'.format(lista))



