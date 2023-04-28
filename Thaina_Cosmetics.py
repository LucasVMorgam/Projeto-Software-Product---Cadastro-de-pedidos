import sqlite3
import Back_Thaina
import PySimpleGUI as sg
import pandas as pd
from datetime import datetime

class sistema():

    def janela_inicio():
        sg.theme('LightBlue1')
        layout = [  [sg.Text('Bem vindo a Thainá Cosmetics')],
                    [sg.Text('Selecione o que deseja fazer:')],
                    [sg.Button('Novo Pedido'), sg.Button('Consultar Pedido')],
                    [sg.Button('Sair')] ]

        janela_inicio = sg.Window('Thainá Cosmetics', layout, resizable=True, finalize=True, size=(280,125))

        event,values = janela_inicio.read()
        while True:
            if event in (sg.WIN_CLOSED, 'Sair'):
                break
            elif event == 'Novo Pedido':
                janela_inicio.close()
                sistema.adicionar_pedido()
                break
            elif event == 'Consultar Pedido':
                janela_inicio.close()
                sistema.consultar_pedido()
                break
        janela_inicio.close()

    def adicionar_pedido():
        info_pedido = []
        heading = ['Produto', 'Valor', 'Quantidade','Total']
        layout = [  [sg.Text('Bem vindo a Thainá Cosmetics')],
                    [sg.Text('Cliente:'),sg.InputText(k=('-CLIENTE-'), do_not_clear=True)],
                    [sg.Text('Produto:'), sg.Input(size=(25,0),k=('-PRODUTO-'), do_not_clear=False ),
                    sg.Text('Valor:'), sg.InputText(size=(10,1),k=('-VALOR-'), do_not_clear=False),
                    sg.Text('Quantidade:'), sg.InputText(size=(5,1),k=('-QTD-'), do_not_clear=False)],
                    [sg.Button('Adicionar Produto')],
                    [sg.Table(values=info_pedido, headings=heading,
                    key='-TABELA-',
                    auto_size_columns=True,
                    display_row_numbers=False,
                    alternating_row_color='white',
                    justification='center')],
                    #[sg.Button('Quantidade de Produtos:'), sg.Text('Total do Pedido:')],
                    [sg.Button('Registrar Pedido'),sg.Button('Sair')] ]

        janela_novo_pedido = sg.Window('Novo Pedido', layout, resizable=True)
        while True:
            event,values = janela_novo_pedido.read()
            if event in (sg.WIN_CLOSED, 'Sair'):
                break
            elif event == 'Adicionar Produto':
                total_produto = Back_Thaina.totalizando_produto((values['-VALOR-']), values['-QTD-'])
                info = [values['-PRODUTO-'], values['-VALOR-'], values['-QTD-'], total_produto]
                info_pedido.append(info)
                janela_novo_pedido['-TABELA-'].update(values=info_pedido)
            elif event == 'Registrar Pedido':
                Back_Thaina.tratar_dados(Back_Thaina.numero_pedido(),values['-CLIENTE-'], info_pedido)
                break
        janela_novo_pedido.close()
        sistema.janela_inicio()
    
    def consultar_pedido():
        info_consulta = Back_Thaina.consultar_tudo()
        heading = ['Pedido','Data','Cliente','Produto', 'Valor', 'Quantidade']

        layout = [[sg.Text('Consultar Pedido')],
                  [sg.Text('Digite o nome do cliente:'), sg.InputText(size=(25,0),k='-CLIENTE-')],
                  [sg.Text('Digite o número do pedido:'), sg.InputText(size=(25,0),k='-PEDIDO-')],
                  [sg.Button('Consultar', k='-CONSULTAR-')],
                  [sg.Table(values=info_consulta, headings=heading,
                    key='-TABELA-',
                    auto_size_columns=True,
                    display_row_numbers=False,
                    alternating_row_color='white',
                    justification='center')],
                  [sg.Button('Sair')]]

        janela_consultar_pedido = sg.Window('Consultar Pedido', layout, resizable=True)

        while True:
            event,values = janela_consultar_pedido.read()
            if event in (sg.WIN_CLOSED, 'Sair'):
                break
            elif '-CONSULTAR-' in event:
                if values['-CLIENTE-'] != '':
                    cliente = Back_Thaina.consultar_cliente(values['-CLIENTE-'])
                    if len(cliente) == 0 :
                        sg.popup('Cliente não encontrado!')
                    else:
                        janela_consultar_pedido['-TABELA-'].update(values=cliente)
                elif values['-PEDIDO-'] != '':
                    pedido = Back_Thaina.consultar_pedido(values['-PEDIDO-'])
                    if len(pedido) == 0 :
                        sg.popup('Pedido não encontrado!')
                    else:
                        janela_consultar_pedido['-TABELA-'].update(values=pedido)
                else:
                    sg.popup('Digite nome do cliente ou número do pedido!')
                    janela_consultar_pedido['-TABELA-'].update(values=info_consulta)
            elif event == 'Ok':
                sg.popup('Ok')
                break
        janela_consultar_pedido.close()
        sistema.janela_inicio()
        
sistema.janela_inicio()