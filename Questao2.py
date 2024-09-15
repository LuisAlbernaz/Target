def verificar_letra_a(texto):
    texto_lower = texto.lower()
    quantidade = texto_lower.count('a')
    
    if quantidade > 0:
        print(f"A letra 'a' aparece {quantidade} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

string_usuario = input("Digite uma string: ")
verificar_letra_a(string_usuario)

