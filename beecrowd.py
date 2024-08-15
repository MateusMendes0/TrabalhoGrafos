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
    vertices, arestas, nao_direcionado = ler_grafo()