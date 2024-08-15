def ler_grafo():
    nao_direcionado = True
    v, a = map(int, input())
    direcao = input()
    if direcao != "nao_direcionado":
        nao_direcionado = False

    arestas = {}
    for i in range(0, v, 1):
        arestas[i] = []

    for i in range(0, a, 1):
        id, v1, v2, p = map(int, input())
        arestas[v1].append((id, v2, p))
        if nao_direcionado:
            arestas[v2].append((id, v1, p))
    return list(arestas.keys()), arestas, nao_direcionado


def main():

    opcoes = input()
    opcoes = opcoes.split(" ")
    vertices, arestas, nao_direcionado = ler_grafo()

    for func in opcoes:
        if func == 0:

        elif func == 1:

        elif func == 2:

        elif func == 3:

        elif func == 4:

        elif func == 5:

        elif func == 6:

        elif func == 7:

        elif func == 8:

        elif func == 9:

        elif func == 10:

        elif func == 11:

        elif func == 12:

        elif func == 13:

        elif func == 14: