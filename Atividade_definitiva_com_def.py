"""
Alunos: Maria Luiza e Yan Mendes

"""


import os
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
db_f = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db_f)
session = Session()


# Criando tabela.
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionario"
    
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", String, primary_key=True)
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", Float)
    telefone = Column("telefone", String)

    def __init__(self, nome: str, idade: int, cpf: str, setor: str, funcao: str, salario: float, telefone: str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone
        
Base.metadata.create_all(bind=db_f)

def limpar_tela():
    os.system("cls || clear")

def menu():
    print("="*40)
    print(f"{'RH System':^40}")
    print("="*40)
    print("""
    1 - Adicionar um funcionário
    2 - Consultar um funcionário
    3 - Atualizar os dados de um funcionário
    4 - Excluir um funcionário 
    5 - Listar todos os funcionários
    0 - Sair do sistema.     
    """)

def adicionar_funcionario():
    inserir_nome = input("Digite seu nome: ")
    inserir_idade = int(input("Digite sua idade: "))
    inserir_cpf = input("Digite seu cpf: ")
    inserir_setor = input("Digite seu setor: ")
    inserir_funcao = input("Digite sua função: ")
    inserir_salario = float(input("Digite seu salario: "))
    inserir_telefone = input("Digite seu telefone: ")

    funcionario = Funcionario(nome=inserir_nome, idade=inserir_idade, cpf=inserir_cpf, setor=inserir_setor, funcao=inserir_funcao, salario=inserir_salario, telefone=inserir_telefone)
    session.add(funcionario)
    session.commit()
    limpar_tela()

def consultar_funcionario():
    cpf_usuario = input("Digite o CPF: ")
    funcionario = session.query(Funcionario).filter_by(cpf=cpf_usuario).first()
    if funcionario:
        print(f"{funcionario.nome} - {funcionario.idade} - {funcionario.cpf} - {funcionario.setor} - {funcionario.funcao} - {funcionario.salario} - {funcionario.telefone}")
    else:
        print("Funcionário não encontrado.")
    

def atualizar_funcionario():
    cpf_usuario = input("Digite o CPF: ")
    funcionario = session.query(Funcionario).filter_by(cpf=cpf_usuario).first()

    if funcionario:  # Verifica se o funcionário existe
        funcionario.nome = input("Digite seu nome: ")
        funcionario.idade = int(input("Digite sua idade: "))
        funcionario.setor = input("Digite seu setor: ")
        funcionario.funcao = input("Digite sua função: ")
        funcionario.salario = float(input("Digite seu salario: "))
        funcionario.telefone = input("Digite seu telefone: ")
        
        session.commit()  # Salva as alterações no banco
        print("Usuário atualizado.")
    else:
        print("Funcionário não encontrado.")

def excluir_funcionario():
    cpf_usuario = input("Digite o CPF: ")
    funcionario = session.query(Funcionario).filter_by(cpf=cpf_usuario).first()
    
    if funcionario:  # Verifica se o funcionário existe
        session.delete(funcionario)
        session.commit()
        print("Usuário deletado.")
    else:
        print("Funcionário não encontrado.")

def listar_funcionarios():
    lista_funcionario = session.query(Funcionario).all()
    for funcionario in lista_funcionario:
        print(f"{funcionario.nome} - {funcionario.idade} - {funcionario.cpf} - {funcionario.setor} - {funcionario.funcao} - {funcionario.salario} - {funcionario.telefone}\n")

# Loop principal
while True:
    menu()
    opcao = input("Resposta: ")
    match opcao:
        case "1":
            adicionar_funcionario()
        case "2":
            consultar_funcionario()
        case "3":
            atualizar_funcionario()
        case "4":
            excluir_funcionario()
        case "5":
            listar_funcionarios()
        case "0":
            break
        case _:
            print("Opção inválida.")
            continue