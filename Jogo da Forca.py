import random

palavras = ["python", "computador", "programacao", "terminal", "jogo", "algoritmo", "linguagem", "banco de dados", "laboratorio"]

palavra = random.choice(palavras)
letras_descobertas = ["_"] * len(palavra)
tentativas = 6
letras_usadas = []

print("🎮Bem-vindo ao jogo da FORCA!😄")
print("Adivinhe a palavra!🤔")

while tentativas > 0 and "_" in letras_descobertas:
    print("\nPalavra:", " ".join(letras_descobertas))
    print("Letras usadas:", ", ".join(letras_usadas))
    print(f"Tentativas restantes: {tentativas}")

    chute = input("Digite uma letra ou tente adivinhar a palavra inteira: ").lower().strip()

    # Se o chute for uma palavra (mais de 1 letra)
    if len(chute) > 1:
        if chute == palavra:
            letras_descobertas = list(palavra)
            print("\n🎉 Parabéns! Você ganhou uma estrelinha🌟! A palavra era:", palavra)
            break
        else:
            print("🙅‍♀️🙅‍♂️ Palavra incorreta!")
            tentativas -= 1
            continue

    # Agora chute é uma letra só
    if not chute.isalpha() or len(chute) != 1:
        print("❌ Digite apenas uma letra válida!")
        continue

    if chute in letras_usadas:
        print("Você já tentou essa letra!‼️")
        continue

    letras_usadas.append(chute)

    if chute in palavra:
        print("😁👍 Boa! Você acertou uma letra.")
        for i, letra in enumerate(palavra):
            if letra == chute:
                letras_descobertas[i] = chute
    else:
        print("🙅‍♀️🙅‍♂️ Errou a letra.")
        tentativas -= 1

if "_" not in letras_descobertas:
    print("\n🎉 Parabéns! Você ganhou uma estrelinha🌟! A palavra era:", palavra)
else:
    print("\n💀 Game Over! A palavra correta era:", palavra)

