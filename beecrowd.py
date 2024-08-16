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

# POSSUI CICLO (PAI MANJA)
def possui_ciclo(vertices, arestas, nao_direcionado):
    visitado = set()
    pai = {}

    def busca_profundidade(atual, anterior):
        visitado.add(atual)
        for id_aresta, vizinho, peso in arestas[atual]:
            if vizinho not in visitado:
                pai[vizinho] = atual
                if busca_profundidade(vizinho, atual):
                    return True
            elif vizinho != anterior:
                # Encontrou um ciclo
                return True
        return False

    # Verificar todos os componentes do grafo
    for vertice in vertices:
        if vertice not in visitado:
            if busca_profundidade(vertice, -1):
                return True
    return False
# ORDENAÇÃO TOPOLÓGICA (PAI MANJA)
def ordenacao_topologica(grafo, nao_direcionado):
    if nao_direcionado:
        return -1
    
    #verificar ciclo
    
    # Inicializando estruturas auxiliares
    visitado = set()
    pilha = []
    resultado = []
    
    # Função auxiliar para DFS
    def dfs(v):
        visitado.add(v)
        for _, destino, _ in sorted(grafo.get(v, []), key=lambda x: x[1]):
            if destino not in visitado:
                dfs(destino)
        pilha.append(v)
    
    # Considerando a ordem lexicográfica dos vértices
    for vertice in sorted(grafo.keys()):
        if vertice not in visitado:
            dfs(vertice)
    
    # A ordem topológica será o reverso da pilha
    while pilha:
        resultado.append(pilha.pop())
    return resultado

topologico = ordenacao_topologica(arestas, nao_direcionado)
print(f"Ordenação topológica dos vértices: {topologico}")

# FECHO TRANSITIVO:
def fecho_transitivo(grafo, vertice_inicial=0):
    #grafo_9.txt é bom p testar

    if (nao_direcionado):
        print(-1)
    # Inicializando a estrutura auxiliar para armazenar os vértices alcançáveis
    visitado = set()
    fecho = []

    # Função auxiliar para DFS
    def dfs(v):
        visitado.add(v)
        fecho.append(v)
        # Ordenando as arestas pela ordem lexicográfica do destino
        for _, destino, _ in sorted(grafo.get(v, []), key=lambda x: x[1]):
            if destino not in visitado:
                dfs(destino)

    # Iniciar DFS a partir do vértice inicial
    dfs(vertice_inicial)

    # Imprimir o fecho transitivo ordenado pela ordem lexicográfica dos vértices
    print(f"Fecho transitivo a partir do vértice {vertice_inicial}: {fecho}")

fecho_transitivo(arestas, 0)

# árvore geradora mínima

import heapq
vertices, arestas, nao_direcionado = ler_grafo()

def economia(arestas):
    visitados = set()
    pq = []
    total_minimo = 0

    # Seleciona um vértice inicial (o primeiro vértice da lista de chaves do dicionário)
    inicial = next(iter(arestas))
    visitados.add(inicial)
    
    # Adiciona as arestas conectadas ao vértice inicial na fila de prioridades
    for id_aresta, vertice, peso in arestas[inicial]:
        heapq.heappush(pq, (peso, vertice))

    # Processa a fila de prioridades para encontrar a árvore geradora mínima
    while pq:
        peso, v = heapq.heappop(pq)
        if v not in visitados:
            visitados.add(v)
            total_minimo += peso
            for _, proximo, p in arestas[v]:
                if proximo not in visitados:
                    heapq.heappush(pq, (p, proximo))

    return total_minimo

# func main
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
