from tkinter import *
from tkinter import messagebox
from Codigo.gerador_pdf import gerar_pdf ## remover o 'Codigo' quando testar apenas a tela 

def gerador_janela():
    janela = Tk()
    janela.title('Orçamento PDF')
    texto_titulo = Label(janela, text='Coloque as informações abaixo para criar o orçamento', font='Arial 20')
    texto_titulo.grid(column=0,row=4)
    Campo_de_cliente = Label(janela, text='Cliente', font='Arial 15')
    Campo_de_cliente.grid(column=1,row=7)
    texto_cliente = Entry(janela, width= 8, font='Arial 10')
    texto_cliente.grid(column=2, row= 9)

    Campo_de_Servico = Label(janela, text='Serviço', font='Arial 15')
    Campo_de_Servico.grid(column=1,row=10)
    texto_Servico = Entry(janela, width= 8, font='Arial 10')
    texto_Servico.grid(column=2, row= 11)

    Campo_de_Preco = Label(janela, text='Preço', font='Arial 15')
    Campo_de_Preco.grid(column=1,row=12)
    texto_Preco = Entry(janela, width= 8, font='Arial 10')
    texto_Preco.grid(column=2, row= 13)

    Campo_de_Descricao = Label(janela, text='Descrição', font='Arial 15')
    Campo_de_Descricao.grid(column=1,row=14)
    texto_Descricao = Entry(janela, width= 8, font='Arial 10')
    texto_Descricao.grid(column=2, row= 15)

    def spam():
        messagebox.showinfo('PDF Gerado','PDF Gerado com sucesso')
        texto_cliente.delete(0, END)
        texto_Descricao.delete(0, END)
        texto_Preco.delete(0, END)
        texto_Servico.delete(0, END)
        

    botao = Button(janela, text='Gerar PDF', command= lambda: (gerar_pdf(texto_cliente.get(), texto_Servico.get(), 
                                                                        texto_Preco.get(), texto_Descricao.get()), spam()))
    botao.grid(column=1, row=17)
    janela.mainloop()