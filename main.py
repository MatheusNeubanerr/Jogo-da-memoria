from lib.util import *
from time import sleep

tentativas: int = 0
acertos = 0
cartasViradas = list()
valoresPossiveis = (0, 1, 2, 3)

print(101*f"{cores['amarelo']}-{cores['fechaCor']}")
print(f"{cores['amarelo']}     Bem vindo ao jogo da memória com tabuada, você tem 25 chances para finalizar, boa sorte <3{cores['fechaCor']}")
print(101*f"{cores['amarelo']}-{cores['fechaCor']}")

while True:
    # Recebe a jogada de ambas as cartas e verifica se a carta existe na matriz, ou se a carta já foi revelada
    mostraJogo()
    j1l = leiaInt("Informe a Linha[carta01]: ")
    j1c = leiaInt("Informe a coluna[carta01]: ")
    if j1l not in valoresPossiveis or j1c not in valoresPossiveis:
        print(f"{cores['vermelho']}Valor fora da matriz, tente novamente!!{cores['fechaCor']}")
        continue
    if jogo[j1l][j1c] in cartasViradas:
        print(f"{cores['vermelho']}Essa carta já foi virada, tente novamente!!{cores['fechaCor']}")
        continue
    mostraJogada(j1l, j1c)
    sleep(1)
    j2l = leiaInt("Informe a Linha[carta02]: ")
    j2c = leiaInt("Informe a coluna[carta02: ")
    if j2l not in valoresPossiveis or j2c not in valoresPossiveis:
        print(f"{cores['vermelho']}Valor fora da matriz, tente novamente!!{cores['fechaCor']}")
        continue
    if jogo[j2l][j2c] in cartasViradas:
        print(f"{cores['vermelho']}Essa carta já foi virada, tente novamente!!{cores['fechaCor']}")
        continue
    mostraJogada(j2l, j2c)
    sleep(1)

    # Verifica a jogada comparando as cartas e contabilizando as cartas já reveladas e o número de tentativas
    jogada = verificaJogada(j1l, j1c, j2l, j2c)  
    if jogada:
        acertos += 2
        cartasViradas.append(jogo[j1l][j1c]) 
        cartasViradas.append(jogo[j2l][j2c])
    tentativas += 1
    atualizaJogo(jogada, j1l, j1c, j2l, j2c)
    print(f"{cores['amarelo']}     Placar: {tentativas}/25{cores['fechaCor']}")
    sleep(1)

    # Verifica o número de tentaivas e a quantidade de acertos, para finalizar o jogo
    if tentativas == 25:
        print(f"{cores['vermelho']}Fim de jogo, você estourou o limite de tentativas!!{cores['fechaCor']}")
        break
    if acertos == 16:
        print(f"{cores['verde']}Parabéns, você acertou todos os pares!!{cores['fechaCor']}")
        break
