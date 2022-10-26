# comando input(): quero permitir que
# o usuario digite algo...
nome = input("digite seu nome: ")
#pede a idade para o usuario "Qual a sua idade?"
idade = int(input("digite sua idade: "))

# comando de saída..exibir na tela
print(f"Boa noite, seu nome é {nome}")
#exiba "Sua idade é ..."
print(f"Sua idade é {idade}")

#e se eu quisesse mostrar o DOBRO da idade informada?
dobro = idade * 2
print("o dobro da idade informada é {}".format(dobro))
