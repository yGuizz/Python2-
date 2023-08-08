from collections import Counter
import re

def contar_palavras(texto):
    # Remover pontuações e converter para minúsculas
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    
    # Dividir o texto em palavras
    palavras = texto.split()
    
    # Contar as ocorrências de cada palavra
    contagem_palavras = Counter(palavras)
    
    return contagem_palavras

# Solicitar ao usuário para inserir o texto
texto = input("Digite o texto: ")

# Contar as palavras no texto
contagem = contar_palavras(texto)

# Exibir a contagem de ocorrências de cada palavra
for palavra, contagem in contagem.items():
    print(f"{palavra}: {contagem}")
