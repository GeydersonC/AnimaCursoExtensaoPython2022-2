#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "Você é bichão, mesmo..."
nome = input("Digite seu nome: ")
nota = float(input("Qual sua nota: "))

if (nota == 10):
  print(f"{nome}, você é o bichão mesmo, ein")
elif (nota >= 6 and nota < 10):
  print(f"{nome}, poderia ser um dez, mas ta bom")
else: # é sempre automaticamente
  print(f"{nome}, você é muito burro, não tirou dez")
