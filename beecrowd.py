import heapq
from collections import deque, defaultdict

def ler_grafo_terminal(nao_direcionado: bool = True):
    # Lê o número de vértices e arestas
    v, a = map(int, input("Digite o número de vértices e arestas (separados por espaço): ").split())
    # print(v, a)

    # Lê a direção do grafo
    direcao = input().strip()
    # print(direcao)
    if direcao != "nao_direcionado":
        nao_direcionado = False
    # print(nao_direcionado)

    # Inicializa o dicionário para armazenar as arestas
    arestas = {}
    for i in range(v):
        arestas[i] = []

    # Lê as arestas
    for i in range(a):
        id, v1, v2, p = map(int, input().split())
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
                    return 1
            elif vizinho != anterior:
                # Encontrou um ciclo
                return 1
        return 0

    # Verificar todos os componentes do grafo
    for vertice in vertices:
        if vertice not in visitado:
            if busca_profundidade(vertice, -1):
                return 1
    return 0

# ORDENAÇÃO TOPOLÓGICA (PAI MANJA)
def ordenacao_topologica(grafo, nao_direcionado):
    if nao_direcionado:
        return -1
    
    if possui_ciclo(grafo.keys(), grafo, nao_direcionado):
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

# FECHO TRANSITIVO:
def fecho_transitivo(grafo, vertice_inicial=0, nao_direcionado=False):
    #grafo_9.txt é bom p testar

    if (nao_direcionado):
        return -1
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
    return fecho

# árvore geradora mínima
def economia(arestas, nao_direcionado):

    if (not nao_direcionado):
        return -1

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

# arestas ponte
def encontrarPontes(grafo, nao_direcionado):

    if not nao_direcionado:
        return -1 

    n = len(grafo)
    descoberta = [-1] * n
    menorTempo = [-1] * n
    pai = [-1] * n
    tempo = 0
    pontes = []

    def dfs(u):
        nonlocal tempo
        descoberta[u] = menorTempo[u] = tempo
        tempo += 1
        
        for (idAresta, v, peso) in grafo[u]:
            if descoberta[v] == -1:  # Se v não foi visitado
                pai[v] = u
                dfs(v)
                
                menorTempo[u] = min(menorTempo[u], menorTempo[v])
                
                # Se a menor altura alcançável de v é maior que descoberta de u, (u, v) é uma ponte
                if menorTempo[v] > descoberta[u]:
                    pontes.append(idAresta)
            
            elif v != pai[u]:  # Atualiza menorTempo[u] para back edge
                menorTempo[u] = min(menorTempo[u], descoberta[v])

    # Chama DFS para cada vértice não visitado
    for i in range(n):
        if descoberta[i] == -1:
            dfs(i)
    
    return pontes





# fred
def arvore_largura(arestas: dict, vertice_inicial: int) -> int:
    visitados = set()
    fila = deque([vertice_inicial])
    
    arvore = []

    while fila:
        vertice_atual = fila.popleft()
        visitados.add(vertice_atual)

        for id_aresta, destino, peso in sorted(arestas.get(vertice_atual, []), key=lambda x: x[1]):
            if destino not in visitados:
                fila.append(destino)
                visitados.add(destino)
                arvore.append(id_aresta)  

    return arvore

def valor_do_caminho_minimo_entre_2_vertices(grafo: dict):
    vertices = list(grafo.keys())

    origem = min(vertices)
    destino = max(vertices)

    # Verificar se o grafo contém pesos diferentes
    pesos = set()
    for vertice, arestas in grafo.items():
        for aresta in arestas:
            peso = aresta[2]
            if isinstance(peso, (int, float)):  # Verifica se peso é um número
                pesos.add(peso)
            else:
                raise ValueError(f"Peso inválido encontrado: {peso}")
    if len(pesos) <= 1:
        return -1
    
    # Initialize-single-source 
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[origem] = 0

    # Fila de prioridades 
    fila = [(0, origem)]  # (distância, vértice)
    

    while fila:
        dist_atual, vertice_atual = heapq.heappop(fila)

        if vertice_atual == destino:
            return dist_atual

        if dist_atual > distancias[vertice_atual]:
            continue

        # Fazer relaxamento em cada aresta do vertice atual na lista de prioridades
        for aresta in grafo[vertice_atual]:
            _, vizinho, peso = aresta
            distancia = dist_atual + peso

            # Relaxamento
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila, (distancia, vizinho))
    return -1

def encontra_vertice_articulacao(grafo, nao_direcionado):

    if not nao_direcionado:
        return -1

    # Inicializa estruturas para a busca em profundidade
    tempo = [0]  # Relógio de tempo da DFS
    num_vertices = len(grafo)
    discover = [-1] * num_vertices  # Tempo de descoberta dos vértices na DFS
    low = [-1] * num_vertices  # Menor tempo de descoberta acessível
    parent = [-1] * num_vertices  # Vértice pai na DFS
    articulacao = [False] * num_vertices  # Marca se um vértice é de articulação
    vertices_articulacao = []  # Lista de vértices de articulação

    def dfs(v):
        # Aumenta o tempo e marca o tempo de descoberta do vértice
        discover[v] = low[v] = tempo[0]
        tempo[0] += 1
        filhos = 0  # Conta o número de filhos na DFS
        
        for (id_aresta, vizinho, peso) in grafo[v]:
            if discover[vizinho] == -1:  # Se vizinho não foi descoberto
                parent[vizinho] = v
                filhos += 1
                dfs(vizinho)

                # Atualiza o menor tempo de descoberta acessível
                low[v] = min(low[v], low[vizinho])

                # Checa condição para que v seja vértice de articulação
                if parent[v] == -1 and filhos > 1:  # Raiz da DFS com mais de 1 filho
                    articulacao[v] = True
                if parent[v] != -1 and low[vizinho] >= discover[v]:
                    articulacao[v] = True

            elif vizinho != parent[v]:  # Atualiza low[v] para back edge
                low[v] = min(low[v], discover[vizinho])

    # Chama DFS para cada vértice não visitado
    for i in sorted(grafo.keys()):  # Ordena os vértices em ordem lexicográfica
        if discover[i] == -1:
            dfs(i)

    # Coleta os vértices de articulação
    for i in range(num_vertices):
        if articulacao[i]:
            vertices_articulacao.append(i)

    return vertices_articulacao


def conexoFred(v: int, grafo: dict, nao_direcionado: bool) -> int:
    grafo_temp = {k: v[:] for k, v in grafo.items()}  # Cria uma cópia profunda do grafo
    
    # if not nao_direcionado:
    #     for i in range(0, len(grafo_temp)):
    #         for aresta in grafo_temp[i]:
    #             grafo_temp[aresta[1]].append((aresta[0], i, aresta[2]))
                
    visitado = {k: False for k in grafo_temp}
    pilha = [v]

    while pilha:
        vertice = pilha.pop()

        if not visitado[vertice]:
            visitado[vertice] = True

            for vizinho in grafo_temp.get(vertice, []):
                if not visitado[vizinho[1]]:
                    pilha.append(vizinho[1])

    if all(visitado.values()):
        return 1
    return 0

def euleriano(arestas: dict, nao_direcionado) -> int:
    # Para ver se é euleriano basta verificar se todos os vértices possuem grau par. Se sim, é euleriano (o grafo precisa ser conexo)

    if (not conexoFred(list(arestas.keys())[0], arestas, nao_direcionado)):
        return 0
    
    for vertice in arestas:
        # Para cada vértice, ver quantas arestas ele possui. 
        # Ex.: 1: [(0, 0, 1), (1, 2, 1), (2, 3, 1)]. Nesse caso o vértice 1 tem grau 3 e consequentemente resto 1
        if (len(arestas[vertice]) % 2 == 1):
            return 0
    return 1




# tg
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


def componentes_conexas(grafo:dict, nao_orientado) -> list:

    if not nao_orientado:
        return -1
    
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

# func main
def main():
    opcoes = input()
    opcoes = opcoes.split(" ")
    vertices, arestas, nao_direcionado = ler_grafo_terminal()
    for func in opcoes:
        if func == '0':
            # print(conexo(0, arestas, nao_direcionado))
            print("conexo ta cagando as outras, criar grafo temporario para manipular")
        elif func == '1':
            print("bipartido")
        elif func == '2':
            print(euleriano(arestas, nao_direcionado))
        elif func == '3':
            print(possui_ciclo(vertices, arestas, nao_direcionado))
        elif func == '4':
            print(componentes_conexas(arestas, nao_direcionado))
        elif func == '5':
            print("componentes fortemente conexas")
        elif func == '6':
            print(encontra_vertice_articulacao(arestas, nao_direcionado))
        elif func == '7':
            print(encontrarPontes(arestas, nao_direcionado))
        elif func == '8':
            print(dfs(arestas, 0))
        elif func == '9':
            print(arvore_largura(arestas, vertice_inicial=0))
        elif func == '10':
            print(economia(arestas, nao_direcionado))
        elif func == '11':
            print(ordenacao_topologica(arestas, nao_direcionado))
        elif func == '12':
            print(valor_do_caminho_minimo_entre_2_vertices(arestas))
        elif func == '13':
            print("fluxo maximo")
        elif func == '14':
            # nao precisa do 0 na saida
            print(fecho_transitivo(arestas, 0, nao_direcionado))


main()
