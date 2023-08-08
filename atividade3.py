def imprimir_numeros_naturais(n):
    for i in range(n + 1):
        print(i)

def main():
    numero = int(input("Digite um número inteiro positivo: "))
    if numero < 0:
        print("Por favor, digite um número positivo.")
    else:
        imprimir_numeros_naturais(numero)

if __name__ == "__main__":
    main()





