import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from leitura import ler_grafo

def Grafo(arestas):
    G = nx.DiGraph(arestas)
    drawGraph(G)

    return G

def drawGraph(graph):
    nx.draw_networkx(graph, with_labels=True)
    plt.savefig("grafo.png")
    plt.clf()



#Variables

G = None


sg.theme('DarkBlack')

grafoIMG = [
    [sg.Image(key='image')]
]

opcoesGraph = [
    [sg.Button('Busca DFS',key='dfs'),sg.Button('Busca BFS',key='bfs')]
]

outputwin = [
    [sg.Text(size=(60,10) , key='texto')]
]

tipoGrafo = [
    [sg.Radio('Não direcionado', group_id=1, default=True, key='nao_direcionado'), sg.Radio('Direcionado', group_id=1, default=False)]
]

layout = [
    [sg.Frame('Tipo do Grafo', tipoGrafo)],
    [sg.Input(key='-IN-'), sg.FileBrowse(), sg.Button("Ler", key='read')],
    [sg.Frame('Grafo Inicial', grafoIMG)],
    [sg.Frame('Opções', opcoesGraph)],
    [sg.Frame('Saída', outputwin)],
    [sg.Cancel(button_text="Sair", key='Cancel')]
]

window = sg.Window('Grafos', layout, font=('Bahnschrift SemiBold Condensed',15), resizable=True, element_justification='center')
counter = 0
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

    elif event == 'read':
        if(values['-IN-'] == ''):
            text = 'Nenhum grafo foi selecionado'
            window['texto'].update(value=text)
        else:
            print(f'Arquivo Escolhido: {values["-IN-"]}')
            vertices, arestas = ler_grafo(values['-IN-'], values['nao_direcionado'])
            G = Grafo(arestas)
            window['image'].update(filename="grafo.png")
            window['texto'].update(value=arestas)