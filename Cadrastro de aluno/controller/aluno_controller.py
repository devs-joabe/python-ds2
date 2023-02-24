#  Camada de controle é responsável por intermediar as requisições enviadas pelo View com as respostas fornecidas pelo Model, 
# processando os dados que o usuário informou e repassando para outras camadas. 
# Numa analogia bem simplista, o controller  operaria como o ‘’maestro de uma orquestra’’  
# que permite a comunicação entre o detentor dos dados e a pessoa com vários questionamentos no MVC

from aluno_view import *
from aluno import *

root = Tk()

view = AlunoView(root)

root.mainloop()
