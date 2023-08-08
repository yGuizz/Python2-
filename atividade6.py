import random

def dado():
    dado = random.randint(1,6)
    return dado

dado1 = dado()
dado2 = dado()

print ("Seu resultado do dado 1 é:" ,dado1)
print ("Seu resultado do dado 2 é:" ,dado2)

soma= dado1+dado2
print ("Seu resutaldo é ",soma)
    
