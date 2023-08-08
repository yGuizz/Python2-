def eh_palindromo(palavra):
    palavra = palavra.lower()  # Convertendo a palavra para minúsculas
    palavra = palavra.replace(" ", "")  # Removendo espaços em branco
    return palavra == palavra[::-1]

def main():
    palavra = input("Digite uma palavra: ")
    if eh_palindromo(palavra):
        print("A palavra é um palíndromo.")
    else:
        print("A palavra não é um palíndromo.")

if __name__ == "__main__":
    main()
