from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from tkinter import *
from tkinter import ttk
from dotenv import load_dotenv
import os
# import time

# PROXY = f'http://{os.getenv('usuario')}:{os.getenv('senha')}@{os.getenv('firewall')}'
# webdriver.DesiredCapabilities.CHROME['proxy'] = {
# "httpProxy": PROXY,
# "ftpProxy": PROXY,
# "sslProxy": PROXY,
# "proxyType": "manual",

# }

# Tela de login

def tela_login():
    janela = Tk()
    janela.geometry('400x250')

    # logo seduc
    # diretorio_atual = os.getcwd()
    # janela.iconbitmap(fr'{diretorio_atual}\logo_seduc.ico')

    janela.title('Assinaturas SEI')
    janela.resizable(width=False, height=False)
    # Titulo da tela
    container_titulo = Frame(janela, padx=140, pady=10) 
    container_titulo.grid()
    titulo = Label(container_titulo, text='Login SEI')
    titulo.grid()
    # Usuario
    container_usuario = Frame(janela, padx=140, pady=10)
    container_usuario.grid()
    label_usuario = Label(container_usuario, text='Usuário').grid()
    entry_usuario = Entry(container_usuario).grid()
    # Senha
    container_senha = Frame(janela, padx=140, pady=10)
    container_senha.grid()
    label_senha = Label(container_senha, text='Senha').grid()
    entry_senha = Entry(container_senha, show='*').grid()

    # Botão confirmação
    container_botao = Frame(janela, padx=140, pady=10)
    container_botao.grid()
    botao = Button(container_botao, text='Login', command=janela.destroy, width='10').grid()
    janela.mainloop()



docs_selecionados = [] 


# Selecionar os documentos

janela_docs = Tk()
janela_docs.geometry('450x250')
janela_docs.title('Documentos para assinatura')
container_documentos = Frame(janela_docs, padx=100, pady=30)
# scroll_list = Scrollbar(container_documentos)
container_documentos.grid()
documentos = ['Todos', 'doc 1', 'doc 2', 'doc 3', 'doc 4', 'doc 5', 'doc 6', 'doc 7', 'doc 8', 'doc 9', 'doc 10']
sel_docs = Label(container_documentos, text='Selecione os documentos').grid()
# combobox = ttk.Combobox(janela, state="readonly", values=documentos, height=5)
# combobox = ttk.Combobox(container_documentos, state="disabled")
# combobox.current(0)
listbox = Listbox(container_documentos, selectmode="multiple", exportselection=0, height=5, width=40)
for doc in documentos:
   listbox.insert(END, doc)



# define a function to update the combobox when the user selects or deselects a value
# def update_combobox():
#    # Get selected values from the Listbox widget
#    selected_values = [listbox.get(idx) for idx in listbox.curselection()]
    
#    # Update the combobox with the selected values
#    combobox.configure(width=40, height=5)
#    combobox.set(", ".join(selected_values))
    
# bind the update_combobox function to the Listbox widget
# listbox.bind("<<ListboxSelect>>", lambda _: update_combobox())
# combobox.grid()
listbox.grid()

def seleciona_docs():
    global janela_docs
    global listbox
    for i in listbox.curselection():
        docs_selecionados.append(listbox.get(i))
    janela_docs.destroy()
    tela_login()

container_botao = Frame(janela_docs, padx=100, pady=5)
container_botao.grid()
confirmacao = Button(container_botao, text='Selecionar', command=seleciona_docs)
confirmacao.grid()
# confirmacao.bind('<Return>', seleciona_docs(janela_docs))
janela_docs.mainloop()
print(docs_selecionados)

# tela_login()

# with webdriver.Chrome() as driver:
#     driver.get("https://selenium.dev")
# driver = webdriver.Chrome()