import sqlite3
from tkinter import E

banco = sqlite3.connect('C:\\Users\\lucas\\OneDrive\\Área de Trabalho\\Projeto - Thaina Cosmetics\\ThainaCosmetics.db')

cursor = banco.cursor()

#Codigo para criação da tabela, usado somente no inicio
cursor.execute("CREATE TABLE pedidos (pedido integer, data text, cliente text, produto text, valor real, quantidade integer)")