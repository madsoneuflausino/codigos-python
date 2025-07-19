frase = str(input('Digite uma frase: ')).strip()
print(f'A letra "a" aparece {frase.lower().count("a")} vezes.')
print(f'A letra "a" aparece primeiro na posição {frase.lower().find("a") + 1}')
print(f'A letra "a" aparece por último na posição {frase.lower().rfind("a") + 1}')