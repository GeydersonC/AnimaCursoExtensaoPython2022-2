#criação de funções

preco = 1999.90

#calcular apenas 5% de imposto, guardar na variavel imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#criar uma função calcular_imposto que calcula um imposto de 5% e retorna a quem pediu...
#isso é a declaração da função(como ela chama)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto
  
#aqui é o uso... aqui é imposto a calcular... e exibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(imposto)

#explicação de variavel local x global
print(preco)
preco_produto = 100
print(preco_produto)


#agora colocarimposto e aliquota agora é 7%

valores = [1.99, 24.50, 78.27, 1515.5] 
# se eu quiser calcular o imposto destes quatro valores.... e exibir na tela assim: "O imposto de .... é...."
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")


#declarar um função calcular_imposto_aliquota que recebe dois parametros: o preço e a aliquota de imposto a ser aplicada e retorna o imposto calculando. Se a aliquota nao for informada, utilize 7% como padrão.
  def calcular_imposto_aliquota(valor, aliquota=7):
    imposto = valor * aliquota / 100
    return imposto

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor)}")

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 7)}")

#E se agora o imposto for 10%
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")