# Trabalho prático de Algoritmos em Grafos

## Entrada

```bash
3 4 5 6 9 11 12 14 # algoritmos que serão executados
6 6 # quantidade de vértices e quantidade de arestas
direcionado # ou nao_direcionado
0 0 1 1 # idAresta, origem, destino, peso
1 1 2 1
2 2 0 1
3 3 4 1
4 4 5 1
5 5 3 1
```

## Sobre os algoritmos

- Verificar se um grafo é conexo. 
    - Para o caso de grafos orientados, verificar conectividade fraca. 
- Verificar se um grafo não-orientado é bipartido. 
- Verificar se um grafo é Euleriano. 
- Verificar se um grafo possui ciclo. 
- Calcular a quantidade de componentes conexas em um grafo não-orientado. 
- Calcular a quantidade de componentes fortemente conexas em um grafo orientado. 
- Imprimir os vértices de articulação de um grafo não-orientado (priorizar a ordem lexicográfica dos vértices).  
- Calcular quantas arestas ponte possui um grafo não-orientado.  
- Imprimir a árvore em profundidade (priorizando a ordem lexicográfica dos vértices; 0 é a origem).  
    - Você deve imprimir o identificador das arestas. Caso o grafo seja desconexo, considere apenas a árvore com a raíz 0. 
- Árvore de largura (priorizando a ordem lexicográfica dos vértices; 0 é a origem).  
    - Você deve imprimir o identificador das arestas. Caso o grafo seja desconexo, considere apenas a árvore com a raíz 0.  
- Calcular o valor final de uma árvore geradora mínima (para grafos não-orientados).  
- Imprimir a ordem os vértices em uma ordenação topológica. 
    - Esta função não fica disponível em grafos não direcionado. 
    - Deve-se priorizar a ordem lexicográfica dos vértices para a escolha de quais vértices explorar. 
- Valor do caminho mínimo entre dois vértices (para grafos não-orientados com pelo menos um peso diferente nas arestas). 0 é a origem; n-1 é o destino. 
- Valor do fluxo máximo para grafos direcionados.   0 é a origem; n-1 é o destino. 
- Fecho transitivo para grafos direcionados. 
    - Deve-se priorizar a ordem lexicográfica dos vértices; 0 é o vértice escolhido.
