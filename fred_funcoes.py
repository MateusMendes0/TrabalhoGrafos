from leitura import ler_grafo
from collections import deque
import heapq

vertices, arestas, nao_direcionado = ler_grafo()

def euleriano(arestas: dict) -> int:
    # Para ver se é euleriano basta verificar se todos os vértices possuem grau par. Se sim, é euleriano (o grafo precisa ser conexo)

    ############# CHAMAR FUNÇÃO DE VER SE É CONEXO (se for conexo, continuar na função, se não for, retornar 0)
    
    for vertice in arestas: 
        # Para cada vértice, ver quantas arestas ele possui. 
        # Ex.: 1: [(0, 0, 1), (1, 2, 1), (2, 3, 1)]. Nesse caso o vértice 1 tem grau 3 e consequentemente resto 1
        if (len(arestas[vertice]) % 2 == 1):
            return 0
    return 1


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





def valor_do_caminho_minimo_entre_2_vertices(grafo):
    vertices = list(grafo.keys())

    origem = min(vertices)
    destino = max(vertices)

    # Verificar se o grafo contém pesos diferentes
    pesos = set()
    for vertice, arestas in grafo.items():
        for aresta in arestas:
            pesos.add(aresta[2])
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




arvore = arvore_largura(arestas, 0)
print(f"Árvore de largura: {arvore}")

isEuleriano = euleriano(arestas)
print(f"É euleriano?: {isEuleriano}")

resultado = valor_do_caminho_minimo_entre_2_vertices(arestas)
print(f"valor_do_caminho_minimo_entre_2_vertices: {resultado}")