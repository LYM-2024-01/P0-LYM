class Token:

  def __init__(self, id, valor):
    self.id = id
    self.valor = valor

p1 = Token("lp", "(")

print(p1)
print(p1.id)
print(p1.valor)
