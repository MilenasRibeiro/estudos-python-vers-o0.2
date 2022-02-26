notas = [0] * 15
soma = 0


for i in range(0,15):
  notas[i]  = float(input('Digite as 15 notas:'))
  soma += notas[i]
media = soma / len(notas)

print( "A média é ", media)