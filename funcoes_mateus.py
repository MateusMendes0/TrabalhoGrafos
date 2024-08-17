import leitura

def dfs(grafo: dict, v: int) -> list:
    arvore_dfs = []
    pilha = [(grafo[v][0][0],v)]
    visitado = set()

    while pilha:
        vertice = pilha.pop()

        if vertice[1] not in visitado:
            visitado.add(vertice[1])
            arvore_dfs.append(vertice[0])

            ultimo_id = -1
            for (id_aresta, vizinho, peso) in sorted(grafo[vertice[1]], key=lambda x: x[1], reverse=True):
                if vizinho not in visitado:
                    pilha.append((id_aresta,vizinho))
#                    ultimo_id = id_aresta
#            if ultimo_id != -1:
#                arvore_dfs.append(ultimo_id)
    arvore_dfs.remove(0)
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

def componentes_conexas(grafo:dict) -> int:
    contador = 0
    visitado = [False] * len(list(grafo.keys()))

    pilha = []
    for i in range(len(visitado)):
        if not visitado[i]:
            contador += 1
            pilha.append(i)
            while pilha:
                vertice = pilha.pop()
                if not visitado[vertice]:
                    visitado[vertice] = True

                    for vizinho in grafo[vertice]:
                        if not visitado[vizinho[1]]:
                            pilha.append(vizinho[1])
    return contador

# FUNCOES FORTEMENTE CONEXO

def dfs_fortemente_conexo(grafo:dict, v, visitado, pilha=None):
        visitado[v] = True
        for aresta in grafo[v]:
            vertice = aresta[1]
            if not visitado[vertice]:
                dfs_fortemente_conexo(grafo,vertice, visitado, pilha)
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


def fortemente_conexos(grafo:dict, nao_direcionado):
    if nao_direcionado:
        return -1

    pilha = []
    visitado = [False] * len(grafo)

    for i in range(0,len(grafo)):
                if not visitado[i]:
                    dfs_fortemente_conexo(grafo, i, visitado, pilha)

    grafo_transposto = transpor_grafo(grafo)

    visitado = [False] * len(grafo)
    componente_forte_conexos = []

    while pilha:
        v = pilha.pop()
        if not visitado[v]:
            componente = []
            dfs_fortemente_conexo(grafo_transposto,v, visitado, componente)
            componente_forte_conexos.append(componente)

    return componente_forte_conexos


if __name__ == '__main__':
    grafo = {0: [(0, 1, 1)], 1: [(0, 0, 1), (1, 2, 1), (2, 3, 1)], 2: [(1, 1, 1), (3, 3, 1)], 3: [(2, 1, 1), (3, 2, 1)]}
    grafo2 = {0: [(0, 4, 1)], 1: [(0, 3, 1), (1, 2, 1), (2, 3, 1)], 2: [(1, 1, 1), (3, 3, 1)], 3: [(2, 1, 1), (3, 2, 1)], 4: [(4, 2, 1)], 5:[]}
    grafo3 = {
        0: [(0, 2, 5)],
        1: [(0 ,0, 3), (1, 2, 2)],
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

    conexo = conexo(0,arestas,nao_direcionado)
    print("Conexo :")
    print(conexo)

    print("DFS : ")
    print(dfs(arestas, 0))

    comp = componentes_conexas(arestas)
    print("Comp Conexos:")
    print(comp)

    print("Comp Fortemente Conexos")
    print(len(fortemente_conexos(arestas,nao_direcionado)))
