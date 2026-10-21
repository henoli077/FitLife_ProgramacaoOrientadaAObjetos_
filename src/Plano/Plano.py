class Plano:
  def __init__(self, nome: str, valor: float, desc: str):
    self.__nome = nome
    self.__valor = valor
    self.__desc = desc

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

  def desc(self):
    return self.__desc

  def exibirPlano(self):
    return (
        f"Plano: {self.nome()}\n"
        f"Valor: R$ {self.valor():.2f}\n"
        f"Descrição: {self.desc()}\n"
    )