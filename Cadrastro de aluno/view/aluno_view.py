# Essa camada é responsável por apresentar as informações de forma visual ao usuário. 
# Em seu desenvolvimento devem ser aplicados apenas recursos ligados a aparência como mensagens, 
# botões ou telas. 


from tkinter import *
from tkinter import ttk

from aluno import Aluno

class AlunoView:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.nome_label = Label(self.frame, text="Nome:")
        self.nome_label.grid(row=0, column=0)

        self.nome_entry = Entry(self.frame)
        self.nome_entry.grid(row=0, column=1)

        self.matricula_label = Label(self.frame, text="Matrícula:")
        self.matricula_label.grid(row=1, column=0)

        self.matricula_entry = Entry(self.frame)
        self.matricula_entry.grid(row=1, column=1)

        self.curso_label = Label(self.frame, text="Curso:")
        self.curso_label.grid(row=2, column=0)

        self.curso_entry = Entry(self.frame)
        self.curso_entry.grid(row=2, column=1)

        self.cadastrar_button = Button(self.frame, text="Cadastrar", command=self.cadastrar)
        self.cadastrar_button.grid(row=3, column=0)

        self.alunos_table = ttk.Treeview(self.frame, columns=("Nome", "Matrícula", "Curso"))
        self.alunos_table.heading("Nome", text="Nome")
        self.alunos_table.heading("Matrícula", text="Matrícula")
        self.alunos_table.heading("Curso", text="Curso")
        self.alunos_table.grid(row=4, columnspan=2)

    def cadastrar(self):
        nome = self.nome_entry.get()
        matricula = self.matricula_entry.get()
        curso = self.curso_entry.get()

        aluno = Aluno(nome, matricula, curso)
        self.alunos_table.insert("", "end", text=aluno.nome, values=(aluno.nome, aluno.matricula, aluno.curso))
