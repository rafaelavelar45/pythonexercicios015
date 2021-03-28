largura = float(input('Digite a largura dessa parede em m:'))
altura = float(input('Digite a altura da parede em m:'))
a = largura * altura
tinta = a / 2
print('Essa parede tem a dimensão de {}X{} e sua area sera {:.2f}m2'
      ' voce precisará de {}L de tinta'.format(largura, altura, a, tinta))




