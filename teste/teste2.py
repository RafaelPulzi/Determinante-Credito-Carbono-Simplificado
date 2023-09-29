def imprimir_texto_colorido(texto, cor_letras, cor_fundo):
    # Mapeamento de cores para códigos de cores ANSI
    cores_ansi = {
        "vermelho": 31,
        "branco": 97,
    }

    # Verifique se as cores são suportadas
    if cor_letras not in cores_ansi or cor_fundo not in cores_ansi:
        print("As cores especificadas não são suportadas.")
        return

    # Crie o texto formatado usando Unicode
    texto_formatado = f"\x1b[{cores_ansi[cor_fundo]};{cores_ansi[cor_letras]}m{texto}\x1b[0m"
    
    # Imprima o texto formatado
    print(texto_formatado)

# Exemplo de uso:
imprimir_texto_colorido("Seu texto com letras brancas e fundo vermelho", "branco", "vermelho")
