dias = int(input('Quantos dias alugados? '))
km = float(input('Km rodado? '))
dias1 = (dias * 60)
km1 = (km * 0.15)
t = (dias1 + km1)
print('='*12)
print('Preço a pagar R${:.2f}'.format(t))
print('='*12)



