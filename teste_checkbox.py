from tkinter import *
from tkinter import ttk




janela = Tk()
janela.geometry('450x250')
container_select = Frame(janela, padx=150)
container_select.grid()
lista_docs = Text(container_select, pady=30, padx=30)
lista_docs.grid()
scrollbar = Scrollbar(lista_docs)
scrollbar.grid()
documentos = ['doc 1', 'doc 2', 'doc 3']

vars = []
for i in range(len(documentos)):
    var = IntVar()
    vars.append(var)
    checkbutton = Checkbutton(lista_docs, text=documentos[i], variable=var, onvalue=1, offvalue=0)
    lista_docs.window_create("end", window=checkbutton)
    lista_docs.insert("end", "\n")
    # print(var.get())
    # print(checkbutton.cget('text'))

    # checkbutton.getvar

# lista_docs.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=lista_docs.yview)

# disable the widget so users can't insert text into it
lista_docs.configure(state="disabled")

# for doc in documentos:
#     checkbox = Checkbutton(lista_docs)
#     checkbox.config(text=doc)
#     checkbox.grid()



def select_docs():
    # print(lista_docs.ge)
    # print(lista_docs.window)
    print(lista_docs.window_cget('.!text.!checkbutton3', 'window'))
    window = lista_docs.window_cget('.!text.!checkbutton3', 'create')
    print(window.window_create())
    print(window.cget('text'))
    # for doc in lista_docs.get(1.0, END).split('\n'):
    #     # print(str(lista_docs.get(1.0, END)))
    #     # doc = intVar()
    #     print(type(doc))
    #     print(doc.cget())
        # if doc.cget('text'):
        #     print(doc)

container_botao = Frame(janela, pady=9)
container_botao.grid()
botao_sel = Button(container_botao, text='selecionar', command=select_docs)
botao_sel.grid()
janela.mainloop()



# root = tk.Tk()

# scrollbar = tk.Scrollbar(root)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# checklist = tk.Text(root, width=20)
# checklist.pack()

# vars = []
# for i in range(50):
#     var = tk.IntVar()
#     vars.append(var)
#     checkbutton = tk.Checkbutton(checklist, text=i, variable=var)
#     checklist.window_create("end", window=checkbutton)
#     checklist.insert("end", "\n")

# checklist.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=checklist.yview)

# # disable the widget so users can't insert text into it
# checklist.configure(state="disabled")

# root.mainloop()