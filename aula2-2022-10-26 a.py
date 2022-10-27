# comando input(): quero permitir que
# o usuario digite algo...
nome = input("Digite seu nome: ")
#pede a idade para o usuario "Qual a sua idade?"
idade = int(input("Digite sua idade: "))

# comando de saída..exibir na tela
print(f"Boa noite, seu nome é {nome}")
#exiba "Sua idade é ..."
print(f"Sua idade é {idade}")

#e se eu quisesse mostrar o DOBRO da idade informada?
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Voê é maior de idade, ótimo! Já pode beber ou dirigir"
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber e dirigir")
else:
  print("Você é xóvem ainda, xóvem ainda...")

#E se eu quisesse perguntar o gênero (M = Masculino e F = Feminino)
#Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)

genero = input("Informe seu gênero M=Masculino, F=Feminino: ")
if idade >= 18 and genero == "M":
  print("Você também precisa se alistar no serviço militar")

