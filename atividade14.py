def ordenar_crescente(lista):
    return sorted(lista)

entrada = input("Digite os números separados por espaços: ")
numeros = [int(numero) for numero in entrada.split()]


lista_ordenada = ordenar_crescente(numeros)


print("Lista ordenada:", lista_ordenada)
