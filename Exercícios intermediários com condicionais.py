# Peça três lados de um triângulo e diga se ele é equilátero, isósceles ou escaleno.

print("\nVamos descobrir o tipo de triangulo?")
l1 = int(input("Digite o primero lado do triangulo: "))
l2 = int(input("Digite o segundo lado do triangulo: "))
l3 = int(input("Digite o terceiro lado do triangulo: "))

if l1 == l2 == l3:
    print("O triângulo é equilátero.")
elif l1 == l2 or l2 == l3 or l3 == l1:
    print("O triangulo é um isoceles")
else:
    print("O triângulo é escaleno.")

# Peça o peso e a altura do usuário e calcule o IMC = peso / (altura²). Mostre a classificação: 
# Abaixo de 18.5 → “Abaixo do peso”, 18.5 a 24.9 → “Peso normal”, 25 a 29.9 → “Sobrepeso”, 30 ou mais → “Obesidade”

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura**2)
print(f"\nO seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 24.9:
    print("Seu peso está normal.")
elif imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")

# Peça um ano e diga: Se é bissexto; E também a qual século pertence (ex: 1999 → século 20, 2024 → século 21).
# Dica: um ano é bissexto se for divisível por 4, mas não por 100, exceto se também for divisível por 400.)

ano = int(input("Digite um ano: "))
seculo = (ano - 1) // 100 + 1

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f"O {ano} é bissexto e pertence ao século {seculo}.")
else:
    print(f"{ano} não é um ano bissexto. Pertence ao {seculo}.")

# Pedra, Papel ou Tesoura - Peça a escolha do jogador 1 e do jogador 2, e diga quem venceu ou se deu empate.

jogador_1 = input("\nJogador 1, faça sua escolha: Pedra, Papel ou Tesoura: ").lower()
jogador_2 = input("Jogador 2, faça sua escolha: Pedra, Papel ou Tesoura: ").lower()

print(f"\nO jogador1 escolheu {jogador_1} e o jogador2 escolheu {jogador_2}")

if jogador_1 == jogador_2:
    print("Jogo empatado.")
elif jogador_1 == "pedra" and jogador_2 == "tesoura":
    print("O jogador 1 ganhou")
elif jogador_1 == "tesoura" and jogador_2 == "papel":
    print("O jogador 1 ganhou")
elif jogador_1 == "papel" and jogador_2 == "pedra":
    print("O jogador 1 ganhou")
else: 
    print("O jogador 2 ganhou")

# Peça uma nota de 0 a 10 e converta em conceito: 9–10 → A, 8–8.9 → B, 7–7.9 → C, 6–6.9 → D, abaixo de 6 → E

nota = float(input("Digite a nota: "))
if nota >= 9 and nota <= 10:
    print("Nota A")
elif nota >= 8:
    print("Nota B")
elif nota >= 7:
    print("Nota C")
elif nota >= 6:
    print("Nota D")
else: 
    print("Nota E")

# Peça o consumo de energia (em kWh) e o tipo de instalação:

# R para Residencial: até 500 → R$ 0.40, acima → R$ 0.65
# C para Comercial: até 1000 → R$ 0.55, acima → R$ 0.60
# I para Industrial: até 5000 → R$ 0.55, acima → R$ 0.60
# Calcule e mostre o valor total.

print("\nTipos de Instalação: Residencial (R), Comercial (C) e Industrial (I).")
instalação = input("\nQual é o tipo de instalação: R / C /I ==> ").upper()
consumo = float(input("Qual foi o consumo de energia (KWH): "))

if instalação == "R":
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65

elif instalação == "C":
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
    
elif instalação == "I":
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60

else:
    print("Escolha um tipo de instalação válido (R, C ou I).")
    preco = None

print(f"O valor total a pagar é R$ {consumo*preco:.2f}")

# Solução 2

if instalação == "R" and consumo <= 500:
    print(f"O valor total a pagar é de R$ {consumo*0.40}")
elif instalação == "R" and consumo > 500:
    print(f"O valor total a pagar é de R$ {consumo*0.65}")

if instalação == "C" and consumo <= 1000:
    print(f"O valor total a pagar é de R$ {consumo*0.55}")
elif instalação == "C" and consumo > 1000:
    print(f"O valor total a pagar é de R$ {consumo*0.60}")

if instalação == "I" and consumo <= 5000:
    print(f"O valor total a pagar é de R$ {consumo*0.55}")
elif instalação == "I" and consumo > 5000:
    print(f"O valor total a pagar é de R$ {consumo*0.60}")

else:
    print("Escolha o tipo de instalação listado!")

# Peça a média do aluno e a frequência (em %).
# Se média ≥ 7 e frequência ≥ 75 → “Aprovado”
# Se média < 7 ou frequência < 75 → “Reprovado"

media = float(input("Digite a média do aluno: "))
frequencia = float(input("Qual a frequência (%) do aluno: "))

if media >= 7 and frequencia >= 75:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")

# Peça a velocidade de um carro.
# Se for maior que 80 km/h, calcule uma multa de R$ 5 por km acima do limite.
# Mostre o valor da multa, ou diga “Dentro do limite”.

velocidade = float(input("Digite a velocidade registrada (KM/h): "))
velocidade_excedida = velocidade - 80

if velocidade > 80:
    print(f"Você excedeu a velocidade da pista em {velocidade_excedida} km/h")
    print(f"O valor da multa é R$ {velocidade_excedida*5}")
else:
    print("Velocidade dentro do limite.")

# Peça o sexo (M/F) e a idade. Homens podem se aposentar com 65 anos ou mais e Mulheres com 60 anos ou mais
# Mostre se já pode se aposentar ou quanto tempo falta.

sexo = input("Sexo - M para masculino e F para feminino: ").upper()
idade = int(input("Digite sua idade: "))

if sexo == "M":
    if idade >=65:
        print("Você pode se aposentar.")
    elif idade < 65:
        falta = 65 - idade
        print(f"Ainda falta mais {falta} anos para se aposentar.")

elif sexo == "F": 
    if idade >=60:
        print("Você pode se aposentar.")
    elif idade < 60:
        falta = 60 - idade
        print(f"Ainda falta mais {falta} anos para se aposentar.")

else:
    print("Digitou dados inválidos!")

# Peça o salário e calcule o imposto com base nas faixas:
# Até 2000 → isento
# 2000.01 até 3000 → 8%
# 3000.01 até 4500 → 18%
# Acima de 4500 → 28%
# Mostre o valor do imposto e o salário líquido.

salario = float(input("Digite o valor do seu salário: "))

if salario <= 2000:
    imposto = 0
elif salario <= 3000:
    imposto = (salario - 2000) * 0.08
elif salario <= 4500:
    imposto = (1000 * 0.08) + (salario - 3000) * 0.18
else:
    imposto = (1000 * 0.08) + (1500 * 0.18) + (salario - 4500) * 0.28

if imposto == 0:
    print("Isento de Imposto.")
else:
    print(f"Imposto retido: R$ {imposto:.2f}")
    print(f"Salário líquido: R$ {salario - imposto:.2f}")
