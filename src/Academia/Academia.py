from src.Plano.Plano import Plano
from src.Aluno.Aluno import Aluno

class Academia:
  def __init__(self, nome: str):
    self.__nome = nome
    self.__alunos = []
    self.__planos = []

  def nome(self):
    return self.__nome

  def cadastrarPlano(self, plano: Plano):
    self.__planos.append(plano)

  def buscarAlunoemail(self, email: str):
    for aluno in self.__alunos:
      if aluno.email() == email:
        return aluno

    return None

  def buscarPlano(self, nome: str):
    for plano in self.__planos:
        if plano.nome().lower() == nome.lower():
            return plano

    return None

  def cadastrarAluno(self, aluno: Aluno):
    if self.buscarAlunoemail(aluno.email()):
      raise ValueError("Já existe um aluno cadastrado com este email.")

    self.__alunos.append(aluno)

  def listarAlunos(self):
    return self.__alunos

  def listarPlanos(self):
    return self.__planos