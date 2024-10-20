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

    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", Integer, primary_key=True)
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
    
def adicionar_funcionario(funcionario):
    inserir_nome = input("Digite seu nome: ")
    inserir_idade = int(input("Digite sua idade: "))
    inserir_cpf = int(input("Digite seu cpf: "))
    inserir_setor = input("Digite seu setor: ")
    inserir_funcao = input("Digite sua função: ")
    inserir_salario = float(input("Digite seu salario: "))
    inserir_telefone = int(input("Digite seu telefone: "))
    
    funcionario = Funcionario(nome=inserir_nome, idade=inserir_idade, cpf=inserir_cpf, setor=inserir_setor, funcao=inserir_funcao, salario=inserir_salario, telefone=inserir_telefone)
    session.add(funcionario)
    session.commit()
    limpar_tela()
    
def pesquisar_funcionario(pesquisa):
    cpf_usuario = int(input("Digite o CPF: "))
    lista_funcionario = session.query(Funcionario).filter_by(cpf = cpf_usuario).first()

    for usuario in lista_funcionario:
        print(f"{usuario.nome} - {usuario.idade} - {usuario.cpf} - {usuario.setor} - {usuario.funcao} - {usuario.salario} - {usuario.telefone}")
    limpar_tela()

    pesquisa = pesquisar_funcionario
    return pesquisa

def atualizar_funcionario(funcionario):
    cpf_usuario = int(input("Digite o CPF: "))
    funcionario = session.query(Funcionario).filter_by(cpf = cpf_usuario).first()
    
    novos_dados = Funcionario(
    inserir_nome = input("Digite seu nome: "),
    inserir_idade = int(input("Digite sua idade: ")),
    inserir_cpf = int(input("Digite seu cpf: ")),
    inserir_setor = input("Digite seu setor: "),
    inserir_funcao = input("Digite sua função: "),
    inserir_salario = float(input("Digite seu salario: ")),
    inserir_telefone = int(input("Digite seu telefone: "))
    )

    funcionario = novos_dados
    session.add(funcionario)
    session.commit
    limpar_tela()

def excluir_funcionario(funcionario):
     cpf_usuario = int(input("Digite o CPF: "))
    funcionario = session.query(Funcionario).filter_by(cpf = cpf_usuario).first()
    session.delete(funcionario)
    session.commit()
    print("Usuário deletado.")
    limpar_tela()
            

def listar_funcionario():


while True:
    menu()
    opcao = input("Resposta: ")
    match opcao:
        case "1": 
            salvar = adicionar_funcionario(Funcionario)
            
        case "2":
            pesquisa = pesquisar_funcionario(pesquisa)
            
        case "3":
           excluir = 
            
        case "4":
            funcionario = session.query(Funcionario).filter_by(cpf = cpf_usuario).first()
            limpar_tela()
            
        case "5":
            limpar_tela()
            
        case "0":
            print("Saindo do sistema.")
            break