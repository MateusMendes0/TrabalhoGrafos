import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from leitura import ler_grafo

vertices = []
arestas = []
nao_direcionado = True

# Functions
def Grafo(arestas: dict) -> nx.DiGraph:
    aresta_nx = []
    for key in arestas:
        for aresta in arestas[key]:
            aresta_nx.append((key, aresta[1],aresta[2]))

    G = nx.DiGraph()
    for aresta in aresta_nx:
        G.add_edge(aresta[0],aresta[1], weight=aresta[2])
    drawGraph(G)

    return G

def salvar_arquivo(vertices: list, arestas: list, filepath):
    file = open(filepath, 'w')
    final = 'V = {'
    for n in range(len(vertices)):
        if n != len(vertices)-1:
            final += str(vertices[n])+","
        else:
            final += str(vertices[n])+'}; A = {'

    for n in range(len(arestas)):
        if n != len(arestas)-1:
            final += '('
            final += str(arestas[n][0])+","
            final += str(arestas[n][1])+"),"
        else:
            final+= '('
            final += str(arestas[n][0])+","
            final += str(arestas[n][1])+")};"

    file.write(final)
    print(final)




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
        [sg.Text(size=(60, 10), key='texto')],
        [sg.Image(key='image')]
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
            print('matriz')
            #representacoesWindow['image'].update(filename=None)
            #matriz = nx.adjacency_matrix(G).todense()
            #representacoesWindow['texto'].update(value=matriz)
        elif event == 'grafica':
            print('grafica')
            G = Grafo(arestas)
            representacoesWindow['texto'].update(value='')
            representacoesWindow['image'].update(filename="grafo.png")
        elif event == 'lista':
            print('lista')
            representacoesWindow['image'].update(filename=None)
            listaDeAdjacencia = ""
            for vertice in vertices:
                try:
                    listaDeAdjacencia += f"{vertice} -> {arestas[vertice]} \n"
                except:
                    listaDeAdjacencia += f"O vértice {vertice} não possui conexao com outro vertice"
            representacoesWindow['texto'].update(value=listaDeAdjacencia)


def janelaOperacoes():

    operacoesVertice = [
        [
            sg.Button('Inserir vertice', key='inserirV'),
            sg.Input(key='add-v', expand_x=False),
            sg.Button('Remover vertice', key='removerV'),
            sg.Input(key='remove-v', expand_x=False),
        ]
    ]

    operacoesAresta = [
        [
            sg.Button('Inserir aresta', key='inserirA'),
            sg.Input(key='add-a', expand_x=False),
            sg.Button('Remover aresta', key='removerA'),
            sg.Input(key='remove-a', expand_x=False),
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
            valor = values['add-v']

            if valor not in vertices:
                G.add_node(valor)
                vertices.append(valor)
                salvar_arquivo(vertices, arestas, './ler.txt')
        elif event == 'removerV':
            print('removerV')
        elif event == 'inserirA':
            print('inserirA')
            valor_a = values['add-a']
            vertices_new = (valor_a.split(','))
            vertices_new[0] = int(vertices_new[0])
            vertices_new[1] = int(vertices_new[1])
            arestas.append(tuple(vertices_new))

            if nao_direcionado:
                tupla_naoDirecionado = (vertices_new[1],vertices_new[0])
                arestas.append(tupla_naoDirecionado)

            salvar_arquivo(vertices,arestas, './ler.txt')

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
    [sg.Radio('Não direcionado', group_id=1, default=True, key='nao_direcionado', enable_events=True), sg.Radio('Direcionado', group_id=1, default=False, enable_events=True)]
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
        janelaRepresentacoes()
        if(G):
            janelaRepresentacoes()
        else:
            sg.popup("Leia um grafo para ver as representações!")

    elif event == 'operacoes':
        janelaOperacoes()

    elif event == 'verificacoes':
        janelaVerificacoes()

    elif event == 'nao_direcionado':
        nao_direcionado = values['nao_direcionado']

    elif event == 'read':
        if values['-IN-'] == '':
            text = 'Nenhum grafo foi selecionado'
            window['texto'].update(value=text)
        else:
            print(f'Arquivo Escolhido: {values["-IN-"]}')
            try:
                vertices, arestas, nao_direcionado = ler_grafo(values['-IN-'], values['nao_direcionado'])
                nao_direcionado = values['nao_direcionado']
                sg.popup("Grafo lido com sucesso!")
            except Exception as e:
                print(e)
                sg.popup("Erro ao ler grafo")
            # window['image'].update(filename="grafo.png")
           
            window['texto'].update(value=arestas)