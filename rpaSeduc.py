from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from tkinter import *
from tkinter import ttk
from dotenv import load_dotenv
import os
# import time

docs_selecionados = [] 
usuario = None
senha = None

# PROXY = f'http://{os.getenv('usuario')}:{os.getenv('senha')}@{os.getenv('firewall')}'
# webdriver.DesiredCapabilities.CHROME['proxy'] = {
# "httpProxy": PROXY,
# "ftpProxy": PROXY,
# "sslProxy": PROXY,
# "proxyType": "manual",

# }

FONTE_PADRAO = ('Helvetica', 9)

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

   def usuario_senha():
      global usuario
      global senha
      usuario = entry_usuario.get()
      senha = entry_senha.get()
      janela.destroy()
      selec_documentos()

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
   # scroll_list = Scrollbar(container_documentos)
   container_documentos.grid()
   # C1 = Checkbutton(janela_docs, text = "Music")
   # C1.grid()
   documentos = ['Todos','doc 1', 'doc 2', 'doc 3', 'doc 4', 'doc 5', 'doc 6', 'doc 7', 'doc 8', 'doc 9', 'doc 10']
   sel_docs = Label(container_documentos, text='Selecione os documentos', font=('Helvetica', 10, 'bold')).grid()
   # combobox = ttk.Combobox(janela, state="readonly", values=documentos, height=5)
   # combobox = ttk.Combobox(container_documentos, state="disabled")
   # combobox.current(0)
   listbox = Listbox(container_documentos, selectmode="multiple", selectborderwidth=5, exportselection=0, activestyle=DOTBOX, height=5, width=40, font=FONTE_PADRAO)
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

   def seleciona_docs():
      for i in listbox.curselection():
         docs_selecionados.append(listbox.get(i))
      janela_docs.destroy()

   container_botao = Frame(janela_docs, padx=100, pady=5)
   container_botao.grid()
   confirmacao = Button(container_botao, text='Selecionar', command=seleciona_docs, font=FONTE_PADRAO)
   confirmacao.grid()
   # confirmacao.bind('<Return>', seleciona_docs(janela_docs))
   janela_docs.mainloop()

tela_login()
# print(docs_selecionados)

# tela_login()

# with webdriver.Chrome() as driver:
#     driver.get("https://selenium.dev")
# driver = webdriver.Chrome()