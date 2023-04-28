import sqlite3
from datetime import datetime

def conectar_bd():
    global banco
    banco = sqlite3.connect(r'C:\Users\lucas\OneDrive\Área de Trabalho\Projeto - Thaina Cosmetics\ThainaCosmetics.db')
    cursor = banco.cursor()
    return cursor

def tratar_dados(pdd, cliente, dados):
    cursor = conectar_bd()
    data = datetime.now().strftime('%d/%m/%Y')
    pedido = pdd
    nome = cliente
    contador_linhas = 0
    produto = []
    valor = []
    qtd = []
    total = []
    
    for i in dados:
        produto.append(i[0])
        valor.append(i[1])
        qtd.append(i[2])
        total.append(i[3])
        contador_linhas += 1
    ic = 0
    while ic < contador_linhas:
        valores = [(pedido, data, cliente, produto[ic], valor[ic], qtd[ic])]
        cursor.executemany("INSERT INTO pedidos VALUES (?,?,?,?,?,?)",valores)
        banco.commit()
        ic += 1 

def numero_pedido():
    cursor = conectar_bd()
    try:
        cursor.execute('SELECT MAX(pedido) FROM pedidos')
        pedido = ((cursor.fetchall())[0][0])+1
    except:
        pedido = 1
    return pedido

def totalizando_produto(valor, qtd):
    valora = str(valor).replace(',','.')
    total = float(valora)*int(qtd)
    total = f'{total:.2f}'
    totaltrans = total.maketrans
    total_final = total.translate(totaltrans(',.','.,'))
    return total_final

def totalizando_pedido(valor, qtd):
    valora = str(valor).replace(',','.')
    total_valor = ''
    pass

def consultar_tudo():
    cursor = conectar_bd()
    cursor.execute('SELECT * FROM pedidos')
    consultafetch = cursor.fetchall()
    consultafinal = [list(ele) for ele in consultafetch]
    return consultafinal

def consultar_cliente(cliente):
    cursor = conectar_bd()
    cursor.execute(f"SELECT * FROM pedidos WHERE cliente = '{cliente}'")
    clientefetch = cursor.fetchall()
    retornoconsultacliente = [list(ele) for ele in clientefetch]
    return retornoconsultacliente
    
def consultar_pedido(pdd):
    cursor = conectar_bd()
    cursor.execute(f"SELECT * FROM pedidos WHERE pedido = '{pdd}'")
    pedidofetch = cursor.fetchall()
    retornoconsultapedido = [list(ele) for ele in pedidofetch]
    return retornoconsultapedido