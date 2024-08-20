import heapq
from collections import deque, defaultdict

def ler_grafo_terminal(nao_direcionado: bool = True):
    # Lê o número de vértices e arestas
    v, a = map(int, input().split())

    # Lê a direção do grafo
    direcao = input().strip()

    if direcao != "nao_direcionado":
        nao_direcionado = False

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

def ordenacao_topologica(grafo, nao_direcionado):
    if nao_direcionado:
        return -1
    
    if possui_ciclo(grafo.keys(), grafo, nao_direcionado):
        return -1
    
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

    fecho.remove(0)
    
    return fecho

def arvore_minima(vertices, arestas, nao_direcionado):

    if (not nao_direcionado):
        return -1
    
    if (possui_ciclo(vertices, arestas, nao_direcionado)):
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

def encontrarPontes(grafo, nao_direcionado):
    if not nao_direcionado:
        return -1 

    n = len(grafo)
    descoberta = [-1] * n
    menorTempo = [-1] * n
    pai = [-1] * n
    pontes = []

    def dfs(u, tempo):
        descoberta[u] = menorTempo[u] = tempo
        tempo += 1
        
        for (idAresta, v, peso) in grafo[u]:
            if descoberta[v] == -1:  # Se v não foi visitado
                pai[v] = u
                tempo = dfs(v, tempo)
                
                menorTempo[u] = min(menorTempo[u], menorTempo[v])
                
                # Se a menor altura alcançável de v é maior que descoberta de u, (u, v) é uma ponte
                if menorTempo[v] > descoberta[u]:
                    pontes.append(idAresta)
            
            elif v != pai[u]:  # Atualiza menorTempo[u] para back edge
                menorTempo[u] = min(menorTempo[u], descoberta[v])

        return tempo

    # Chama DFS para cada vértice não visitado
    for i in range(n):
        if descoberta[i] == -1:
            dfs(i, 0)
    
    return sorted(pontes)

def arvore_largura(arestas: dict, vertice_inicial: int) -> int:
    visitados = set()
    fila = deque([vertice_inicial])
    
    arvore = []

    while fila:
        # Remove o vértice da frente da fila e o marca como visitado
        vertice_atual = fila.popleft()
        visitados.add(vertice_atual)

        for id_aresta, destino, peso in sorted(arestas.get(vertice_atual, []), key=lambda x: x[1]):
            # Se o destino da aresta ainda não foi visitado
            if destino not in visitados:
                fila.append(destino)
                visitados.add(destino)
                arvore.append(id_aresta)  

    return arvore

def valor_do_caminho_minimo_entre_2_vertices(grafo: dict, nao_orientado):
    if (nao_orientado):
        return -1

    vertices = list(grafo.keys())
    
    origem = min(vertices)
    destino = max(vertices)

    # Verificar se o grafo contém pesos diferentes
    pesos = set()
    for vertice, arestas in grafo.items():
        for aresta in arestas:
            peso = aresta[2]
            pesos.add(peso)
            
    if len(pesos) <= 1:
        return -1
    
    # Initialize-single-source  
    distancias = {vertice: float('inf') for vertice in grafo} # Definir todos os vertices com distancia infinita
    distancias[origem] = 0

    # Fila de prioridades 
    fila = [(0, origem)]  # (distância, vértice)
    

    while fila:
        dist_atual, vertice_atual = heapq.heappop(fila)

        # Se o vértice atual é o destino, retorna a distância mínima encontrada
        if vertice_atual == destino:
            return dist_atual

        # Verifica se a distância atual é maior que a registrada
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

    # Não chegou ao destino
    return -1

def encontra_vertice_articulacao(grafo, nao_direcionado):

    if not nao_direcionado:
        return -1

    # Estruturas para a busca em profundidade
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

def conexoAux(v: int, grafo: dict, nao_direcionado: bool) -> int:
    grafo_temp = {k: v[:] for k, v in grafo.items()}  # Cria uma cópia do grafo
    
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
    
    # Verificar se é conexo
    if (not conexoAux(list(arestas.keys())[0], arestas, nao_direcionado)):
        return 0
    
    for vertice in arestas:
        # Para cada vértice, ver quantas arestas ele possui. 
        if (len(arestas[vertice]) % 2 == 1):
            return 0
    return 1

def dfs(grafo: dict, v: int) -> list:
    arvore_dfs = []
    pilha = [(grafo[v][0][0],v)]
    visitado = set()

    while pilha:
        vertice = pilha.pop()

        # Se o vértice ainda não foi visitado
        if vertice[1] not in visitado:
            visitado.add(vertice[1])
            arvore_dfs.append(vertice[0])

            # Explorar os vizinhos do vértice atual em ordem decrescente de identificação
            ultimo_id = -1
            for (id_aresta, vizinho, peso) in sorted(grafo[vertice[1]], key=lambda x: x[1], reverse=True):
                if vizinho not in visitado:
                    pilha.append((id_aresta,vizinho))

    # Remove o identificador 0 da árvore
    arvore_dfs.remove(0)
    return arvore_dfs

def conexo(v: int, grafo: dict, nao_direcionado: bool): 
    grafo_temp = {k: v[:] for k, v in grafo.items()} # copiar grafo
    
    # Se o grafo for direcionado, transformar em não-direcionado
    if not nao_direcionado:
        for i in range(0, len(grafo)):
            for aresta in grafo[i]:
                grafo_temp[aresta[1]].append((aresta[0], i, aresta[2]))

    visitado = [False] * len(list(grafo_temp.keys()))

    pilha = [v]

    while pilha:
        vertice = pilha.pop()

        # Se o vértice ainda não foi visitado
        if not visitado[vertice]:
            visitado[vertice] = True

            # Adicionar vizinhos não visitados à pilha
            for vizinho in grafo_temp[vertice]:
                if not visitado[vizinho[1]]:
                    pilha.append(vizinho[1])

    # Verifica se todos os vértices foram visitados
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
        if not visitado[i]: # Se o vértice ainda não foi visitado
            comp_conexos1 = []
            contador += 1
            pilha.append(i)
            while pilha:
                vertice = pilha.pop()
                if not visitado[vertice]:
                    comp_conexos1.append(vertice)
                    visitado[vertice] = True

                    # Adicionar vizinhos não visitados à pilha
                    for vizinho in grafo[vertice]:
                        if not visitado[vizinho[1]]:
                            pilha.append(vizinho[1])

            # Adicionar o componente conexo encontrado à lista principal
            comp_conexos.append(sorted(comp_conexos1))

    return len(comp_conexos)

def bfs_bipartido(grafo, origem, cor):
    fila = deque([origem])
    cor[origem] = 0

    while fila:
        no_atual = fila.popleft()
        cor_atual = cor[no_atual]

        for id, vizinho, peso in grafo.get(no_atual, []):
            if vizinho not in cor:  # Se o vizinho ainda não foi colorido

                # Atribui a cor oposta ao vizinho
                cor[vizinho] = 1 - cor_atual
                fila.append(vizinho)
            elif cor[vizinho] == cor_atual: # Se o vizinho tem a mesma cor, o grafo não é bipartido
                return False
    return True

def bipartido(grafo, nao_direcionado):
    if not nao_direcionado:
        return 0
    
    cor = {} # Dicionário para armazenar as cores dos vértices

    # Verificar se cada componente do grafo é bipartida
    for origem in grafo:
        if origem not in cor: # Se o vértice ainda não foi visitado
            if not bfs_bipartido(grafo, origem, cor):
                return 0

    return 1

def componentes_fortemente_conexos(V, grafo, nao_direcionado):
    if nao_direcionado:
        return -1

    def dfs(v, visitado, pilha):
        visitado.add(v) # Marca o vértice como visitado
        for _, vizinho, _ in grafo.get(v, []): # Explora todos os vizinhos do vértice atual
            if vizinho not in visitado:
                dfs(vizinho, visitado, pilha)
        pilha.append(v) # Adiciona o vértice na pilha após explorar todos os vizinhos

    def transpor_grafo(grafo):
        transposto = {}
        for origem in grafo:
            for id_aresta, destino, peso in grafo[origem]:
                if destino not in transposto:
                    transposto[destino] = []
                transposto[destino].append((id_aresta, origem, peso))
        return transposto

    def dfs_transposto(v, visitado, componente, grafo_transposto):
        visitado.add(v) # Marca o vértice como visitado
        componente.append(v)
        for _, vizinho, _ in grafo_transposto.get(v, []):  # Explora todos os vizinhos no grafo transposto
            if vizinho not in visitado:
                dfs_transposto(vizinho, visitado, componente, grafo_transposto)

    pilha = []
    visitado = set()

    # Passo 1: Preenchendo a pilha com a ordem de finalização dos vértices
    for vertice in grafo:
        if vertice not in visitado:
            dfs(vertice, visitado, pilha)

    # Passo 2: Transpor o grafo
    grafo_transposto = transpor_grafo(grafo)

    # Passo 3: Processar os vértices na ordem inversa da finalização
    visitado = set()
    componentes = []
    while pilha:
        v = pilha.pop()
        if v not in visitado:
            componente = []
            dfs_transposto(v, visitado, componente, grafo_transposto)
            componentes.append(componente)
    
    return len(componentes)

def bfsFluxoMaximo(grafo_residual, origem, destino, pai):
    visitado = set()
    fila = deque([origem])
    visitado.add(origem)
    
    while fila:
        u = fila.popleft()
        
        for v, capacidade in grafo_residual[u].items():
            if v not in visitado and capacidade > 0:  # Aresta com capacidade residual
                fila.append(v)
                visitado.add(v)
                pai[v] = u
                
                if v == destino:  # Encontrou o destino
                    return True
    return False

def fluxo_maximo(grafo, origem, destino, nao_direcionado):
    if nao_direcionado:
        return -1

    grafo_residual = defaultdict(dict)
    
    # Construir o grafo residual
    for u in grafo:
        for _, v, capacidade in grafo[u]:
            grafo_residual[u][v] = grafo_residual[u].get(v, 0) + capacidade
            grafo_residual[v][u] = grafo_residual[v].get(u, 0)  # aresta reversa
    
    pai = {}
    fluxo_maximo = 0
    
    while bfsFluxoMaximo(grafo_residual, origem, destino, pai):
        fluxo_do_caminho = float('Inf')
        s = destino
        
        # Encontrar a capacidade mínima no caminho encontrado
        while s != origem:
            fluxo_do_caminho = min(fluxo_do_caminho, grafo_residual[pai[s]][s])
            s = pai[s]
        
        # Atualizar as capacidades residuais do grafo
        v = destino
        while v != origem:
            u = pai[v]
            grafo_residual[u][v] -= fluxo_do_caminho
            grafo_residual[v][u] += fluxo_do_caminho
            v = pai[v]
        
        # Somar ao fluxo total
        fluxo_maximo += fluxo_do_caminho
    
    return fluxo_maximo

def main():
    opcoes = input()
    opcoes = opcoes.split(" ")
    vertices, arestas, nao_direcionado = ler_grafo_terminal()
    for func in opcoes:
        if func == '0':
            print(conexo(0, arestas, nao_direcionado))
        elif func == '1':
            print(bipartido(arestas, nao_direcionado))
        elif func == '2':
            print(euleriano(arestas, nao_direcionado))
        elif func == '3':
            print(possui_ciclo(vertices, arestas, nao_direcionado))
        elif func == '4':
            print(componentes_conexas(arestas, nao_direcionado))
        elif func == '5':
            print(componentes_fortemente_conexos(vertices, arestas, nao_direcionado))
        elif func == '6':
            vertices_art = encontra_vertice_articulacao(arestas, nao_direcionado)
            if type (vertices_art) == list:
                if (len(vertices_art) == 0):
                    print(0)
                else:
                    print(vertices_art)
            else:
                print(vertices_art)
        elif func == '7':
            pontes = encontrarPontes(arestas, nao_direcionado)
            if (type (pontes) == list):
                if (len(pontes) == 0):
                    print(-1)
                else:
                    print(pontes)
            else:
                print(pontes)
        elif func == '8':
            print(dfs(arestas, 0))
        elif func == '9':
            print(arvore_largura(arestas, vertice_inicial=0))
        elif func == '10':
            print(arvore_minima(vertices, arestas, nao_direcionado))
        elif func == '11':
            print(ordenacao_topologica(arestas, nao_direcionado))
        elif func == '12':
            print(valor_do_caminho_minimo_entre_2_vertices(arestas, nao_direcionado))
        elif func == '13':
            print(fluxo_maximo(arestas, 0, vertices[-1], nao_direcionado))
        elif func == '14':
            print(fecho_transitivo(arestas, 0, nao_direcionado))

main() 
