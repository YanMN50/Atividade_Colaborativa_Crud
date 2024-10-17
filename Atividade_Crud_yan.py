import os
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
db = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=db)
session = Session()


# Criando tabela.
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionario"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", Integer)
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", Float)
    telefone = Column("telefone", Float)
    
    
    def __init__(self, nome, idade, cpf, setor, funcao, salario, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone
        
        
# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)

os.system("cls || clear")

def limpar_tela():
    os.system("cls || clear")
    

def menu():
    print("="*40)
    print(f"{"RH System":^40}")
    print("="*40)
    print("""
    1 - Adicionar um funcionário
    2 - Consultar um funcionário
    3 - Atualizar os dados de um funcionário
    4 - Excluir um funcionário 
    5 - Listar todos os funcionários
    0 - Sair do sistema.     
          """)



while True:
    menu()
    opcao = input("Resposta: ")
    match opcao:
        case "1": 
            limpar_tela()
            inserir_nome = input("Digite seu nome: ")
            inserir_idade = int(input("Digite sua idade: "))
            inserir_cpf = int(input("Digite seu cpf: "))
            inserir_setor = input("Digite seu setor: ")
            inserir_funcao = input("Digite sua função: ")
            inserir_salario = float(input("Digite seu salario: "))
            inserir_telefone = int(input("Digite seu telefone: "))
            
            funcionario = Funcionario(nome=inserir_nome, idade=inserir_idade, )
                        
            
            
        
    


        
    