from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from tkinter import *
from tkinter import ttk
import pandas as pd
from dotenv import load_dotenv
import os

# import time
FONTE_PADRAO = ('Helvetica', 9)
docs_selecionados = [] 
usuario = None
senha = None
opcao_sel = None

# PROXY = f'http://{os.getenv('usuario')}:{os.getenv('senha')}@{os.getenv('firewall')}'
# webdriver.DesiredCapabilities.CHROME['proxy'] = {
# "httpProxy": PROXY,
# "ftpProxy": PROXY,
# "sslProxy": PROXY,
# "proxyType": "manual",

# }

def busca_documentos():
   planilha = pd.read_excel(fr'{os.getcwd()}\teste_docs.xlsx')
   df = pd.DataFrame(planilha)
   return df.iloc[:, 0]

# Tela de login

def tela_login():
   janela = Tk()
   janela.geometry('400x350')

   # logo seduc
   # diretorio_atual = os.getcwd()
   # janela.iconbitmap(fr'{diretorio_atual}\logo_seduc.ico')

   janela.title('Assinaturas SEI')
   janela.resizable(width=False, height=False)
   # Titulo da tela
   container_titulo = Frame(janela, padx=90, pady=10) 
   container_titulo.grid()
   titulo = Label(container_titulo, text='Login SEI', font=('Helvetica', 10, 'bold'))
   titulo.grid()
   # Usuario
   container_usuario = Frame(janela, padx=90, pady=10)
   container_usuario.grid()
   label_usuario = Label(container_usuario, text='Usuário', font=FONTE_PADRAO).grid()
   entry_usuario = Entry(container_usuario, width=30, font=FONTE_PADRAO)
   entry_usuario.grid()
   # Senha
   container_senha = Frame(janela, padx=90, pady=10)
   container_senha.grid()
   label_senha = Label(container_senha, text='Senha', font=FONTE_PADRAO).grid()
   entry_senha = Entry(container_senha, show='*', width=30, font=FONTE_PADRAO)
   entry_senha.grid()
   # Ambiente
   container_ambiente = Frame(janela, padx=90, pady=10)
   container_ambiente.grid()
   Label(container_ambiente, text='Ambiente', font=FONTE_PADRAO).grid(columnspan=2)
   opcao = IntVar()

   def seleciona_ambiente():
      global opcao_sel
      opcao_sel = str(opcao.get())

   botao_hml = Radiobutton(container_ambiente, text='hml', variable=opcao, value=1, font=FONTE_PADRAO, command=seleciona_ambiente)
   botao_hml.grid(row=1, column=0)
   botao_producao = Radiobutton(container_ambiente, text='produção', variable=opcao, value=2, font=FONTE_PADRAO, command=seleciona_ambiente)
   botao_producao.grid(row=1, column=1)

   def usuario_senha():
      global usuario
      global senha
      global opcao_sel
      usuario = entry_usuario.get()
      senha = entry_senha.get()
      if usuario != '' and senha != '' and opcao_sel != None:
         janela.destroy()
         selec_documentos()
      else:
         if usuario == '':
            label_usuario = Label(container_usuario, text='Campo obrigatório', fg='red', font=FONTE_PADRAO)
            label_usuario.grid(row=2)
         if senha == '':
            label_senha = Label(container_senha, text='Campo obrigatório', fg='red', font=FONTE_PADRAO)
            label_senha.grid(row=2)
         if opcao_sel == None:
            label_senha = Label(container_ambiente, text='Selecione um ambiente', fg='red', font=FONTE_PADRAO)
            label_senha.grid(row=2, columnspan=2)

   # Botão confirmação
   container_botao = Frame(janela, padx=140, pady=10)
   container_botao.grid()
   botao = Button(container_botao, text='Login', command=usuario_senha, width='10', font=FONTE_PADRAO).grid()
   janela.mainloop()

# Selecionar os documentos
def selec_documentos():
   janela_docs = Tk()
   janela_docs.geometry('450x250')
   janela_docs.title('Documentos para assinatura')
   container_documentos = Frame(janela_docs, padx=80, pady=20)
   container_documentos.grid()
   dados_planilha = busca_documentos()
   documentos = [str(doc) for doc in dados_planilha]
   sel_docs = Label(container_documentos, text='Selecione os documentos', font=('Helvetica', 10, 'bold')).grid()
   listbox = Listbox(container_documentos, selectmode="multiple", selectborderwidth=5, exportselection=0, activestyle=DOTBOX, height=5, width=40, font=FONTE_PADRAO)
   listbox.insert(END, 'Todos')
   for doc in documentos:
      listbox.insert(END, doc)
   listbox.grid(row=1)

   # Colorir a lista
   for i in range(0,len(documentos),2):
      listbox.itemconfigure(i, background='#f0f0ff')
   
   if len(documentos) > 5:
      scrollbar = Scrollbar(container_documentos, orient="vertical")
      scrollbar.config(command=listbox.yview)
      scrollbar.grid(row=1, column=1, sticky=NS)
      listbox.config(yscrollcommand=scrollbar.set)

   def seleciona_docs():
      for i in listbox.curselection():
         docs_selecionados.append(listbox.get(i))
      janela_docs.destroy()

   container_botao = Frame(janela_docs, padx=100, pady=5)
   container_botao.grid()
   confirmacao = Button(container_botao, text='Selecionar', command=seleciona_docs, font=FONTE_PADRAO)
   confirmacao.grid()
   janela_docs.mainloop()

tela_login()
print(docs_selecionados)
print(usuario)
print(senha)
print(opcao_sel)

# tela_login()

# with webdriver.Chrome() as driver:
#     driver.get("https://selenium.dev")
# driver = webdriver.Chrome()