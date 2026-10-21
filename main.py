from datetime import date

class Plano:
  def __init__(self, nome: str, valor: float):
    self.__nome = nome
    self.__valor = valor

  def nome(self):
    return self.__nome

  def nomePlano(self, novo_nome):
    if not novo_nome.strip():
      raise ValueError("O nome do plano não pode ser vazio.")

    self.__nome = novo_nome

  def valor(self):
    return self.__valor

  def valorPlano(self, novo_valor):
    if novo_valor <= 0:
      raise ValueError("O valor do plano deve ser maior que zero.")

    self.__valor = novo_valor

  def exibirPlano(self):
    return (
        f"Plano: {self.nome()}\n"
        f"Valor: R$ {self.valor():.2f}\n"
    )

class Aluno:
  def __init__(self, nome: str, idade: int, cpf: str):
    self.__nome = nome
    self.__idade = idade
    self.__cpf = cpf
    self.__plano = None
    self.__ativo = True
    self.__dataCadastro = date.today()

  def nome(self):
    return self.__nome

  def atualizaNome(self, novoNome):
    if len(novoNome.strip()) < 3:
      raise ValueError("O nome deve possuir pelo menos 3 caracteres.")

    self.__nome = novoNome

  def idade(self):
    return self.__idade

  def atualizarIdade(self, novaIdade):
    if novaIdade < 14:
      raise ValueError("O aluno deve ter uma idade mínima de 14.")

    self.__idade = novaIdade

  def cpf(self):
    return self.__cpf

  def plano(self):
    return self.__plano

  def matricularEmPlano(self, plano: Plano):
    self.__plano = plano

  def cancelarPlano(self):
    self.__plano = None

  def ativo(self):
    return self.__ativo

  def desativar(self):
    self.__ativo = False

  def ativar(self):
    self.__ativo = True

  def exibirDados(self):
     planoNome = self.plano().nome() if self.plano() else "Sem plano"
     status = "Ativo" if self.ativo() else "Inativo"

     return (
        f"Nome: {self.nome()}\n"
        f"Idade: {self.idade()}\n"
        f"CPF: {self.cpf()}\n"
        f"Plano: {planoNome}\n"
        f"Status: {status}\n"
        f"Cadastro: {self.__dataCadastro.strftime('%d/%m/%Y')}"
     )

class Academia:
  def __init__(self, nome: str):
    self.__nome = nome
    self.__alunos = []
    self.__planos = []

  def nome(self):
    return self.__nome

  def cadastrarPlano(self, plano: Plano):
    self.__planos.append(plano)

  def buscarAlunoCPF(self, cpf: str):
    for aluno in self.__alunos:
      if aluno.cpf() == cpf:
        return aluno

    return None

  def buscarPlano(self, nome: str):
    for plano in self.__planos:
        if plano.nome().lower() == nome.lower():
            return plano

    return None

  def cadastrarAluno(self, aluno: Aluno):
    if self.buscarAlunoCPF(aluno.cpf()):
      raise ValueError("Já existe um aluno cadastrado com este CPF.")

    self.__alunos.append(aluno)

  def listarAlunos(self):
    return self.__alunos

  def listarPlanos(self):
    return self.__planos

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