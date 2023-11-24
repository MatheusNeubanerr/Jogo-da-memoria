from lib.baseGame import criarJogo

cores = {
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'roxo': '\033[35m',
    'fechaCor':'\033[m'
}
jogo = criarJogo()
matrizJogo = [
    [f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}"],
    [f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}"],
    [f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}"],
    [f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}"],
    [f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}"],
]

# Validação de leitura de números inteiros
def leiaInt(msm: str):
    validacao = True
    while validacao:
        try:
            num = int(input(f"{cores['amarelo']}{msm}{cores['fechaCor']}"))
        except (ValueError, TypeError):
            print(f"{cores['vermelho']}ERRO, informe um número inteiro válido!!{cores['fechaCor']}")
        except KeyboardInterrupt:
            print(f"{cores['vermelho']}Entrada de dados interrompida pelo usuário!{cores['fechaCor']}")
        else:
            validacao = False
    return num


# Verifica a jogada feita pelo jogador, comparando as cartas viradas
def verificaJogada(linhaJ1:int, colunaJ1:int, linhaJ2:int, colunaJ2:int):
    cartaOne = str(jogo[linhaJ1][colunaJ1])
    cartaTwo = str(jogo[linhaJ2][colunaJ2])
    jogada: bool
    if cartaOne.isnumeric():
        cartaOne = int(cartaOne)
    else:
        cartaOne = cartaOne.split()
        cartaOne = int(cartaOne[0]) * int(cartaOne[2])
    if cartaTwo.isnumeric():
        cartaTwo = int(cartaTwo)
    else:
        cartaTwo = cartaTwo.split()
        cartaTwo = int(cartaTwo[0]) * int(cartaTwo[2])
    if cartaOne == cartaTwo:
        jogada = True
    else:
        jogada = False
    return jogada


# Atualiza a matriz que é mostrada na tela, para o jogador acompanhar visualmente as cartas ocultas e já reveladas
def atualizaJogo(ultimaJogada: bool, linhaJ1:int, colunaJ1:int, linhaJ2:int, colunaJ2:int):
    if ultimaJogada:
        matrizJogo[linhaJ1][colunaJ1] = f"{cores['verde']}✔{cores['fechaCor']}"
        matrizJogo[linhaJ2][colunaJ2] = f"{cores['verde']}✔{cores['fechaCor']}"
        print(f"{cores['verde']}Parabéns, você acertou um par!!{cores['fechaCor']}")
    else:
        print(f"{cores['vermelho']}Que pena, você errou tente novamente!!{cores['fechaCor']}")


# Revela a carta virada pelo jogador a cada tentativa
def mostraJogada(linhaJogada:int, colunaJogada:int):
    matrizJogada = [
        [f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}"],
        [f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}"],
        [f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}"],
        [f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}"],
        [f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}", f"{cores['amarelo']}-{cores['fechaCor']}"],
    ]   
    print(f"{cores['amarelo']}{'c0  c1  c2  c3':>19}{cores['fechaCor']}")
    for linha in range(0, 4):
        print(f"{cores['amarelo']}l{linha}{cores['fechaCor']}", end=f"{cores['roxo']} | {cores['fechaCor']}")
        for coluna in range(0, 4):
            if linha == linhaJogada and coluna == colunaJogada:
                matrizJogada[linha][coluna] = jogo[linha][coluna]
            print(matrizJogada[linha][coluna], end=f"{cores['roxo']} | {cores['fechaCor']}")
        print()


# Exibe na tela a matriz, com todas as cartas
def mostraJogo():
    print(f"{cores['amarelo']}{'c0  c1  c2  c3':>19}{cores['fechaCor']}")
    for linha in range(0, 4):
        print(f"{cores['amarelo']}l{linha}{cores['fechaCor']}", end=f"{cores['roxo']} | {cores['fechaCor']}")
        for coluna in range(0, 4):
            print(matrizJogo[linha][coluna], end=f"{cores['roxo']} | {cores['fechaCor']}")
        print()
