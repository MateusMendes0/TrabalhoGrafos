import leitura

def dfs(grafo: dict, v: int):
    arvore_dfs = []
    pilha = [v]
    visitado = set()

    while pilha:
        vertice = pilha.pop()

        if vertice not in visitado:
            visitado.add(vertice)

            ultimo_id = -1
            for (id_aresta, vizinho, peso) in sorted(grafo[vertice], key=lambda x: x[1], reverse=True):
                if vizinho not in visitado:
                    pilha.append(vizinho)
                    ultimo_id = id_aresta
            if ultimo_id != -1:
                arvore_dfs.append(ultimo_id)
    return arvore_dfs


def conexo(v: int, grafo: dict, nao_direcionado: bool):
    if not nao_direcionado:
        for i in range(0, len(grafo)):
            for aresta in grafo[i]:
                grafo[aresta[1]].append((aresta[0], i, aresta[2]))

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

def componentes_conexas(grafo:dict) -> list:
    contador = 0
    visitado = [False] * len(list(grafo.keys()))

    pilha = []
    comp_conexos = []
    for i in range(len(visitado)):
        if not visitado[i]:
            comp_conexos1 = []
            contador += 1
            pilha.append(i)
            while pilha:
                vertice = pilha.pop()
                if not visitado[vertice]:
                    comp_conexos1.append(vertice)
                    visitado[vertice] = True

                    for vizinho in grafo[vertice]:
                        if not visitado[vizinho[1]]:
                            pilha.append(vizinho[1])
            comp_conexos.append(sorted(comp_conexos1))
    return comp_conexos


if __name__ == '__main__':
    grafo = {0: [(0, 1, 1)], 1: [(0, 0, 1), (1, 2, 1), (2, 3, 1)], 2: [(1, 1, 1), (3, 3, 1)], 3: [(2, 1, 1), (3, 2, 1)]}
    grafo2 = {0: [(0, 4, 1)], 1: [(0, 3, 1), (1, 2, 1), (2, 3, 1)], 2: [(1, 1, 1), (3, 3, 1)], 3: [(2, 1, 1), (3, 2, 1)], 4: [(4, 2, 1)], 5:[]}
    grafo3 = {
        0: [(0, 2, 5)],
        1: [(0, 0, 3), (1, 2, 2)],
        2: [(0, 0, 5), (1, 1, 2), (2, 3, 4)],
        3: [(2, 2, 4), (3, 4, 3)],
        4: [(3, 3, 3), (4, 1, 6)],
        5: [(5, 4, 1), (6, 2, 3)]
    }
    grafo4 = {
        0: [(0, 1, 1), (1, 2, 1)],
        1: [(0, 0, 1), (1, 2, 2)],
        2: [(1, 1, 2), (2, 3, 1)],
        3: [(2, 2, 1), (3, 4, 2)],
        4: [(3, 3, 2), (4, 5, 1)],
        5: [(4, 4, 1), (5, 6, 3)],
        6: [(5, 5, 3), (6, 7, 2)],
        7: [(6, 6, 2), (7, 8, 1)],
        8: [(7, 7, 1), (8, 9, 2)],
        9: [(8, 8, 2)]
    }

    grafo5 = {
        0: [(0, 1, 2)],
        1: [(0, 0, 2), (1, 2, 1)],
        2: [(1, 1, 1), (2, 3, 3)],
        3: [(2, 2, 3), (3, 4, 4)],
        4: [(3, 3, 4), (4, 5, 5)],
        5: [(4, 4, 5), (5, 6, 2)],
        6: [(5, 5, 2), (6, 7, 1)],
        7: [(6, 6, 1), (7, 8, 3)],
        8: [(7, 7, 3), (8, 9, 2)],
        9: [(8, 8, 2)]
    }

    grafo6 = {
        0: [(0, 1, 1)],
        1: [(0, 0, 1)],
        2: [(1, 3, 2)],
        3: [(1, 2, 2)],
        4: [(2, 5, 3)],
        5: [(2, 4, 3)],
        6: [(3, 7, 2)],
        7: [(3, 6, 2)]
    }

    vertices, arestas, nao_direcionado = leitura.ler_grafo()

    print(arestas)

    print(dfs(arestas, 0))

    print(conexo(0, arestas, True))

    comp = componentes_conexas(arestas)
    print(" ".join(map(str, comp[0])))
