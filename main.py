import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from leitura import ler_grafo


# Functions
def Grafo(arestas: list[tuple]) -> nx.DiGraph:
    G = nx.DiGraph(arestas)
    drawGraph(G)

    return G

def drawGraph(graph: nx.DiGraph):
    nx.draw_networkx(graph, with_labels=True)
    plt.savefig("grafo.png")
    plt.clf()

def janelaRepresentacoes():

    opcoesRepresentacoes = [
        [
            sg.Button('Matriz de adjacência', key='matriz'),
            sg.Button('Lista de adjacência', key='lista'),
            sg.Button('Representação gráfica', key='grafica'),
        ]
    ]

    outputRepresentacao = [
        [sg.Image(key='image')],
        [sg.Text(size=(60, 10), key='texto')]
    ]
    
    representacoesLayout = [
        [sg.Frame('', opcoesRepresentacoes)],
        [sg.Frame('Saída', outputRepresentacao)],
        [sg.Cancel(button_text="Sair", key='Cancel')]
    ]

    representacoesWindow = sg.Window('Representacoes', representacoesLayout, element_justification='center', modal=False)

    while True:
        event, values = representacoesWindow.read()
        if event in (None, 'Quit'):
            break
        if event == 'Cancel' or event is None:
            representacoesWindow.close()
            break
        elif event == 'matriz':
            representacoesWindow['image'].update(filename=None)
            matriz = nx.adjacency_matrix(G).todense()
            representacoesWindow['texto'].update(value=matriz)
        elif event == 'grafica':
            representacoesWindow['texto'].update(value='')
            representacoesWindow['image'].update(filename="grafo.png")
        elif event == 'lista':
            representacoesWindow['image'].update(filename=None)
            listaDeAdjacencia = ""
            for vertice in vertices:
                try:
                    listaDeAdjacencia += f"{vertice} -> {list(G[vertice].keys())} \n"
                except:
                    listaDeAdjacencia += f"O vértice {vertice} não possui conexao com outro vertice"
            representacoesWindow['texto'].update(value=listaDeAdjacencia)

            
def janelaOperacoes():

    operacoesVertice = [
        [
            sg.Button('Inserir vertice', key='inserirV'),
            sg.Input(key='-IN-', expand_x=False),
            sg.Button('Remover vertice', key='removerV'),
            sg.Input(key='-IN-', expand_x=False),
        ]
    ]

    operacoesAresta = [
        [
            sg.Button('Inserir aresta', key='inserirA'),
            sg.Input(key='-IN-', expand_x=False),
            sg.Button('Remover aresta', key='removerA'),
            sg.Input(key='-IN-', expand_x=False),
        ]
    ]

    outputOperacao = [
        [sg.Text(size=(60, 10), key='texto')]
    ]


    operacoesLayout = [
        [sg.Frame('operacoesVertice', operacoesVertice)],
        [sg.Frame('operacoesAresta', operacoesAresta)],
        [sg.Frame('Saída', outputOperacao)],
        [sg.Cancel(button_text="Sair", key='Cancel')]
    ]

    operacoesWindow = sg.Window('Operacoes', operacoesLayout, modal=True, element_justification='center')

    while True:
        event, values = operacoesWindow.read()
        if event in (None, 'Quit'):
            break
        if event == 'Cancel' or event is None:
            break
        elif event == 'inserirV':
            print('inserirV')
        elif event == 'removerV':
            print('removerV')
        elif event == 'inserirA':
            print('inserirA')
        elif event == 'removerA':
            print('removerA')

def janelaVerificacoes():

    outputVerificacao = [
        [sg.Text(size=(60, 10), key='texto')]
    ]
    
    verificacoesLayout = [
        [sg.Frame('Saída', outputVerificacao)],
        [sg.Cancel(button_text="Sair", key='Cancel')]
    ]

    verificacoesWindow = sg.Window('Verificacoes', verificacoesLayout, modal=True, element_justification='center')

    # if values['-IN-'] == '':
    #     text = 'Nenhum grafo foi selecionado'
    #     window['texto'].update(value=text)
    # else:
    #     print(f'Arquivo Escolhido: {values["-IN-"]}')
    #     vertices, arestas = ler_grafo(values['-IN-'], values['nao_direcionado'])
    #     G = Grafo(arestas)
    
    # textoVerificacoes = f"\
    #         Quantidade de vértices: {len(vertices)} \n\
    #         Quantidade de arestas {len(arestas)} \n\
    #         O grafo é conexo?  \n\
    #        {'' if values['nao_direcionado'] else 'O grafo é fortemente conexo? (somente se for direcionado) \n'}{arestas} \
    #         O grafo possui ciclos?  {arestas} \n\
    #         O grafo é Euleriano? {arestas}"

    while True:
        # verificacoesWindow['texto'].update(value=textoVerificacoes)
        event, values = verificacoesWindow.read()
        if event in (None, 'Quit'):
            break
        if event == 'Cancel' or event is None:
            break


# Variables
G = None

# Definção da Janela
sg.theme('DarkBlack')

grafoIMG = [
    [sg.Image(key='image')]
]

algoritmos = [
    [
        sg.Button('Busca DFS',key='dfs'),
        sg.Button('Busca BFS',key='bfs'),
        sg.Button('Kruskall',key='kruskall'),
        sg.Button('Prim',key='prim'),
        sg.Button('Ordenar topologicamente (Kahn)',key='kahn'),
        sg.Button('Ordenar topologicamente (DFS)',key='ordemDfs'),
        sg.Button('Componentes fortes',key='Kosaraju')
    ]
]

representacoesOperacoesVerificacoes = [
    [
        sg.Button('Representações',key='representacoes'),
        sg.Button('Operações',key='operacoes'),
        sg.Button('Verificações',key='verificacoes'),
    ]
]

outputwin = [
    [sg.Text(size=(60,10) , key='texto')]
]

tipoGrafo = [
    [sg.Radio('Não direcionado', group_id=1, default=True, key='nao_direcionado'), sg.Radio('Direcionado', group_id=1, default=False)]
]

# Layout da janela
layout = [
    [sg.Frame('Tipo do Grafo', tipoGrafo)],
    [sg.Input(key='-IN-'), sg.FileBrowse(), sg.Button("Ler", key='read')],
    [sg.Frame('Grafo Inicial', grafoIMG)],
    [sg.Frame('', representacoesOperacoesVerificacoes)],
    [sg.Frame('Algoritmos', algoritmos)],
    [sg.Frame('Saída', outputwin)],
    [sg.Cancel(button_text="Sair", key='Cancel')]
]

window = sg.Window('Grafos', layout, font=('Bahnschrift SemiBold Condensed',15), resizable=True, element_justification='center', grab_anywhere=True).Finalize()
window.Maximize()

counter = 0

# Loop usado para manter a janela ativa e registrar eventos
while True:
    event, values = window.read()
    if event == 'Cancel' or event is None:
        break
    elif event == 'dfs':
        print(event)
        counter += 1
        text = ''
        for num in range(0,counter):
            text += 'DFS '

        window['texto'].update(value=text)

    elif event == 'bfs':
        print(event)
    
    elif event == 'representacoes':
        if(G):
            janelaRepresentacoes()
        else:
            sg.popup("Leia um grafo para ver as representações!")

    elif event == 'operacoes':
        janelaOperacoes()

    elif event == 'verificacoes':
        janelaVerificacoes()

    elif event == 'read':
        if values['-IN-'] == '':
            text = 'Nenhum grafo foi selecionado'
            window['texto'].update(value=text)
        else:
            print(f'Arquivo Escolhido: {values["-IN-"]}')
            try:
                vertices, arestas = ler_grafo(values['-IN-'], values['nao_direcionado'])
                G = Grafo(arestas)
                sg.popup("Grafo lido com sucesso!")
            except:
                sg.popup("Erro ao ler grafo")
            # window['image'].update(filename="grafo.png")
            window['texto'].update(value=arestas)