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
    return 0


if __name__ == '__main__':
    grafo = {0: [(0, 1, 1)], 1: [(0, 0, 1), (1, 2, 1), (2, 3, 1)], 2: [(1, 1, 1), (3, 3, 1)], 3: [(2, 1, 1), (3, 2, 1)]}

    print(conexo(0, grafo, True))
