def conexo(v: int, grafo: dict, nao_direcionado: bool):
    if not nao_direcionado:
        for i in range(0, len(grafo)):
            for aresta in grafo[i]:
                grafo[aresta[1]].append((aresta[0], i, grafo[2]))

    visitado = [False] * len(list(grafo.keys()))

    pilha = [v]

    while pilha:
        vertice = pilha.pop()

        if not visitado[vertice]:
            visitado[vertice] = True

            for vizinho in grafo[vertice]:
                if not visitado[vizinho[1]]:
                    pilha.append(vizinho[1])

    if all(visitado):
        return 1
    return

def dfs_fortemente_conexo(grafo: dict, v, visitado, pilha=None):
    visitado[v] = True
    for aresta in grafo[v]:
        vertice = aresta[1]
        if not visitado[vertice]:
            dfs_fortemente_conexo(grafo, vertice, visitado, pilha)
    if pilha is not None:
        pilha.append(v)


def transpor_grafo(grafo: dict):
    grafo_transposto = {v: [] for v in grafo}  # Inicializa todos os vértices com listas vazias

    for i in grafo:
        for aresta in grafo[i]:
            # Certifica que o vértice destino existe no grafo transposto
            if aresta[1] not in grafo_transposto:
                grafo_transposto[aresta[1]] = []
            # Adiciona a aresta transposta
            grafo_transposto[aresta[1]].append((aresta[0], i, aresta[2]))

    print(grafo_transposto)
    return grafo_transposto


def fortemente_conexos(grafo: dict, nao_direcionado):
    if nao_direcionado:
        return -1

    pilha = []
    visitado = [False] * len(grafo)

    for i in range(0, len(grafo)):
        if not visitado[i]:
            dfs_fortemente_conexo(grafo, i, visitado, pilha)

    grafo_transposto = transpor_grafo(grafo)

    visitado = [False] * len(grafo)
    componente_forte_conexos = []

    while pilha:
        v = pilha.pop()
        if not visitado[v]:
            componente = []
            dfs_fortemente_conexo(grafo_transposto, v, visitado, componente)
            componente_forte_conexos.append(componente)

    return componente_forte_conexos


if __name__ == '__main__':
    grafo = {0: [(0, 1, 1)], 1: [(0, 0, 1), (1, 2, 1), (2, 3, 1)], 2: [(1, 1, 1), (3, 3, 1)], 3: [(2, 1, 1), (3, 2, 1)]}

    print(conexo(0, grafo, True))
