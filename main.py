from src.Plano.Plano import Plano
from src.Aluno.Aluno import Aluno
from src.Academia.Academia import Academia

def menu():
  print("------SISTEMA ACADEMIA FITLIFE------")
  print("1 - Cadastrar aluno")
  print("2 - Cadastrar plano")
  print("3 - Matricular aluno em plano")
  print("4 - Desmatricular aluno do plano atual")
  print("5 - Listar planos")
  print("6 - Listar alunos")
  print("7 - Desativar aluno")
  print("8 - Ativar aluno")
  print("0 - Sair")

def cadastrarAluno(academia):
  nome = input("Insira o nome: ")
  idade = int(input("Insira a idade: "))
  cpf = input("Insira o CPF: ")

  aluno = Aluno(nome, idade, cpf)
  academia.cadastrarAluno(aluno)

  print(f"\nAluno {aluno.nome()} cadastrado com sucesso!")

def cadastrarPlano(academia):
  nome = input("Insira o nome do plano: ")
  valor = float(input("Insira o valor mensal: R$ "))

  plano = Plano(nome, valor)
  academia.cadastrarPlano(plano)

  print(f"\nPlano {plano.nome()} cadastrado com sucesso!")

def matricularAluno(academia):
  cpf = input("Insira o CPF do aluno: ")
  aluno = academia.buscarAlunoCPF(cpf)

  if aluno is None:
    print("Aluno não encontrado.")
    return

  nomePlano = input("Insira o nome do plano: ")
  plano = academia.buscarPlano(nomePlano)

  if plano is None:
    print("Plano não encontrado.")
    return

  aluno.matricularEmPlano(plano)
  print(f"\nAluno {aluno.nome()} matriculado no plano {plano.nome()}.")

def desmatricularAluno(academia):
  cpf = input("Insira o CPF do aluno: ")
  aluno = academia.buscarAlunoCPF(cpf)

  if aluno is None:
    print("Aluno não encontrado.")
    return

  aluno.cancelarPlano()
  print(f"\nAluno {aluno.nome()} foi desmatriculado do plano.")

def listarAlunos(academia):
  alunos = academia.listarAlunos()

  if not alunos:
    print("Nenhum aluno cadastrado.")
    return

  for indice, aluno in enumerate(alunos, start=1):
    print("\n" + "-" * 45)
    print(f"ALUNO {indice}")
    print(aluno.exibirDados())

def listarPlanos(academia):
  planos = academia.listarPlanos()

  if not planos:
    print("Nenhum plano cadastrado.")
    return

  for indice, plano in enumerate(planos, start=1):
    print("\n" + "-" * 45)
    print(f"PLANO {indice}")
    print(plano.exibirPlano())


def desativarAluno(academia):

  cpf = input("Insira o CPF do aluno: ")
  aluno = academia.buscarAlunoCPF(cpf)

  if aluno is None:
    print("Aluno não encontrado.")
    return

  aluno.desativar()
  print(f"Aluno {aluno.nome()} foi desativado.")

def ativarAluno(academia):

  cpf = input("Insira o CPF do aluno: ")
  aluno = academia.buscarAlunoCPF(cpf)

  if aluno is None:
    print("Aluno não encontrado.")
    return

  aluno.ativar()
  print(f"Aluno {aluno.nome()} foi ativado.")

def main():
  academia = Academia("FitLife")

  while True:
    menu()
    op = input("\nEscolha uma opção: ")

    try:
      if op == "1":
        cadastrarAluno(academia)

      elif op == "2":
        cadastrarPlano(academia)

      elif op == "3":
        matricularAluno(academia)

      elif op == "4":
        desmatricularAluno(academia)

      elif op == "5":
        listarPlanos(academia)

      elif op == "6":
        listarAlunos(academia)

      elif op == "7":
        desativarAluno(academia)

      elif op == "8":
        ativarAluno(academia)

      elif op == "0":
        print("\nEncerrando o Sistema Academia FitLife. Até logo!")
        break

      else:
        print("Opção inválida. Tente novamente.")

    except ValueError as erro:
      print(f"\nErro: {erro}")

if __name__ == "__main__":
  main()