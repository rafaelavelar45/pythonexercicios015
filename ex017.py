from math import hypot
oposto = float(input('Digite o valor do cateto oposto :'))
adj = float(input('Digite o valor do cateto adjacente :'))
hip = hypot(oposto, adj)
print('O valor da sua hipotenusa sera: {:.2f}'.format(hip))


