from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from tkinter import *
from tkinter import ttk
from dotenv import load_dotenv
import os
# import time

PROXY = f'http://{os.getenv('usuario')}:{os.getenv('senha')}@{os.getenv('firewall')}'
webdriver.DesiredCapabilities.CHROME['proxy'] = {
"httpProxy": PROXY,
"ftpProxy": PROXY,
"sslProxy": PROXY,
"proxyType": "manual",

}

janela = Tk()
janela.geometry('400x350')
janela.title('Assinaturas SEI')
janela.resizable(width=False, height=False)
# titulo = Label(janela, text='Login SEI', pady=10).grid(row=1, columnspan=2, column=10)
titulo = Label(janela, text='Login SEI', pady=10).grid(row=1)
# Usuario
label_usuario = Label(janela, text='Usuário', pady=10).grid(row=2, column=0)
entry_usuario = Entry(janela).grid(row=2, column=1)
# Senha
label_senha = Label(janela, text='Senha', pady=10).grid(row=5, column=0)
entry_senha = Entry(janela, show='*').grid(row=5, column=1)

# botao.pack()

# select
documentos = ['Todos', 'doc 1', 'doc 2', 'doc 3', 'doc 4', 'doc 5', 'doc 6', 'doc 7', 'doc 8', 'doc 9', 'doc 10']
sel_docs = Label(janela, text='Documentos').grid(row=9, column=0)
# combobox = ttk.Combobox(janela, state="readonly", values=documentos, height=5)
combobox = ttk.Combobox(janela, state="disabled")
# combobox.current(0)
listbox = Listbox(janela, selectmode="multiple", exportselection=0, height=5, width=40)
for doc in documentos:
   listbox.insert(END, doc)

# combobox['values'] = ('Todos', 'doc 1', 'doc 2', 'doc 3', 'doc 4', 'doc 5', 'doc 6', 'doc 7', 'doc 8', 'doc 9', 'doc 10')


# print(listbox.size())
# elements = print(listbox.get(FIRST, last=None))
# for idx in elements:
#    print(idx)

# combobox.current(0)

# define a function to update the combobox when the user selects or deselects a value
def update_combobox():
   # Get selected values from the Listbox widget
   selected_values = [listbox.get(idx) for idx in listbox.curselection()]
    
   # Update the combobox with the selected values
   combobox.configure(width=40, height=5)
   combobox.set(", ".join(selected_values))
    
# bind the update_combobox function to the Listbox widget
listbox.bind("<<ListboxSelect>>", lambda _: update_combobox())
combobox.grid(row=9, column=1)
listbox.grid(row=10, column=1)

# Botão confirmação
botao = Button(janela, text='Login', command=janela.destroy, width='10').grid(row=12, columnspan=4)
janela.mainloop()

# with webdriver.Chrome() as driver:
#     driver.get("https://selenium.dev")
# driver = webdriver.Chrome()