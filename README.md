🎮 Jogo da Forca — LP

Este é um Jogo da Forca desenvolvido em Python como projeto da disciplina de LP (Linguagem de Programação).
O objetivo do jogo é permitir que o jogador tente adivinhar uma palavra secreta através de tentativas de letras ou do chute da palavra inteira, utilizando lógica de repetição, condicionais e manipulação de strings.

📝 Sobre o Jogo

O programa seleciona uma palavra aleatória de uma lista pré-definida.
O jogador pode:

Digitar uma letra por vez, ou

Tentar adivinhar a palavra inteira.

A cada erro, uma tentativa é perdida. O jogo termina quando:

✔️ O jogador descobre todas as letras
❌ Ou quando suas tentativas chegam a zero

O jogo fornece feedback constante ao jogador sobre:

Letras já usadas

Estado atual da palavra

Número de tentativas restantes

✨ Funcionalidades Implementadas

- Sorteio automático da palavra secreta

- Tentativas limitadas (6 erros)

- Aceita letras ou palavra inteira como chute

- Bloqueia letras repetidas

- Verifica se o chute é válido

- Atualiza as letras descobertas dinamicamente

- Mensagens amigáveis com emojis de feedback

🛠 Tecnologias Utilizadas

- Python 3

- Biblioteca padrão random

🧠 Lógica do Código (Resumo)

- Uma lista de palavras é definida

- Uma delas é sorteada com random.choice()

- O jogador interage pelo terminal

- Letras corretas substituem “_” na palavra

- Chutes inválidos reduzem tentativas

- Vitória ou derrota é informada ao final

💻 Trecho do Código Principal
palavras = ["python", "computador", "programacao", "terminal", "jogo",
            "algoritmo", "linguagem", "banco de dados", "laboratorio"]

palavra = random.choice(palavras)
letras_descobertas = ["_"] * len(palavra)
tentativas = 6
letras_usadas = []

👨‍🏫 Disciplina

- LP — Linguagem de Programação

- Projeto desenvolvido para fins acadêmicos.

👤 Autor(a)

- Bianca Milani
