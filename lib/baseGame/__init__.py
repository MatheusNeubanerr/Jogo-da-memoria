from random import randint, shuffle

# Gera uma lista com todos os elemntos e seus resultados dentro da tabuada de 1 à 10
def tabuada():
    tabuada = list()
    auxiliar = list()
    elemento: str
    valor: int
    contTabuada: int = 1
    while contTabuada != 11:
        for num in range(1, 11):
            elemento = str(contTabuada) + " x " + str(num) 
            valor = num * contTabuada
            auxiliar.append(elemento)
            auxiliar.append(valor)
            tabuada.append(auxiliar[:])
            auxiliar.clear()
        contTabuada += 1
    return tabuada


# Sorteia aleatoriamente numeros para gerar a matriz do jogo
def sortearNumerosJogo():
    t = tabuada()
    numeros = list()
    numsSorteados = list()
    num: int
    cont: int = 0
    while cont < 8:
        indice = randint(0, 99)
        num = t[indice][1]
        while num in numsSorteados:
            indice = randint(0, 99)
            num = t[indice][1]
        numsSorteados.append(num)
        numeros.append(t[indice])
        cont += 1
    return numeros
 

# Com base nos números sorteados, gera uma matriz 4x4 com os números e suas multiplicações, embaralhando aleatoriamente na matriz os pares 
def gerarMatrizDoJogo(numerosSorteados: list):
    matriz = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    elementos = list()
    resultados = list()
    for elemento in numerosSorteados:
        elementos.append(elemento[0])
        resultados.append(elemento[1])
    elementosCombinados = elementos + resultados
    shuffle(elementosCombinados)
    for linha in range(0, 4):
        for coluna in range(0, 4):
            if elementosCombinados:
                matriz[linha][coluna] = elementosCombinados.pop(0)
    return matriz


# Combina as funções anteriores para montar o jogo definitivamente, de forma totalmente aleatoria 
def criarJogo():
    numeros = sortearNumerosJogo()
    jogo = gerarMatrizDoJogo(numeros)
    return jogo
