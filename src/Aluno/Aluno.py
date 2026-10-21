from datetime import date
from src.Plano.Plano import Plano

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