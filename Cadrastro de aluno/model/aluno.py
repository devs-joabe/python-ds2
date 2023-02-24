# Essa classe também é conhecida como Business Object Model (objeto modelo de negócio). 
# Sua responsabilidade é gerenciar e controlar a forma como os dados se comportam por meio das funções, 
# lógica e regras de negócios estabelecidas.

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
