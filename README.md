# 📝 Jogo de Palavras Similares

Este é um jogo simples onde o jogador deve digitar uma palavra similar, mas não idêntica, à palavra sorteada. O jogo utiliza Processamento de Linguagem Natural (NLP) com a biblioteca spaCy para calcular a similaridade entre as palavras digitadas e a palavra sorteada.

## 🎯 Como Funciona?

O jogo sorteia uma palavra aleatória de uma lista pré-definida.

O jogador digita uma palavra que ele considera similar à palavra sorteada.

O programa calcula a similaridade semântica entre as palavras utilizando o modelo en_core_web_lg do spaCy.

Se a similaridade for menor que 30%, o jogo termina.

Caso contrário, o jogador pode continuar tentando novas palavras similares.

Se o jogador digitar exatamente a palavra sorteada, ele vence!

## 🛠 Tecnologias Utilizadas

Python 3 🐍

Tkinter (Interface Gráfica)

spaCy (Processamento de Linguagem Natural)

## 🚀 Como Rodar o Jogo

### 1️⃣ Instale as Dependências

Antes de executar o jogo, instale as bibliotecas necessárias:

pip install spacy

Em seguida, baixe o modelo de NLP necessário:

python -m spacy download en_core_web_lg

### 2️⃣ Execute o Arquivo Python

Agora, basta rodar o arquivo Python:

python jogo_palavras.py

## 🎮 Exemplo de Uso

Palavra sorteada: dog

Jogador digita: cat

Similaridade: 0.85 ➡️ Continua jogando!

Jogador digita: banana

Similaridade: 0.22 ➡️ Game Over!

## 📌 Melhorias Futuras

Adicionar um placar de pontos 🏆

Permitir multiplayer 🎭

Melhorar a interface gráfica 🎨

🔹 Divirta-se jogando! 😃
