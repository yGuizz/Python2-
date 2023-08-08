def numeros_pares(lista):
    return [numero for numero in lista if numero % 2 == 0]


entrada = input("Digite os números separados por espaços: ")
numeros = [int(numero) for numero in entrada.split()]


pares = numeros_pares(numeros)


print("Números pares:", pares)
