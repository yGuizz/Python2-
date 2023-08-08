primeiro = int (input('Primeiro numero'))
segundo = int (input('Segundo numero'))
terceiro = int (input('Terceiro numero'))

maior = primeiro

if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro

print('Maior:',maior)

menor = primeiro

if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro

print ('Menor' ,menor)