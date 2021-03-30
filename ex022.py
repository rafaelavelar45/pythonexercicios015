nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome....')
print('Seu nome em Maiusculas é {}'.format(nome.upper()))
print('Seu nome me Minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome {} tem {} letras'.format(separa[0], len(separa[0])))








