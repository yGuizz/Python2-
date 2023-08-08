
n=int(input("Digite um número natural: "))
if n < 0:
  print("Só podemos calcular o fatorial de números inteiros e positivos")
elif n >= 0:
  i=0
  fatoracao=1
  while i != n:
    if n-i != 0 :
        print("Número",i+1," = ",n-i)
    fatoracao = fatoracao*(n-i)
    i = i + 1
  print("O fatorial de",n,",ou seja,",n,"!, vale: ",fatoracao)