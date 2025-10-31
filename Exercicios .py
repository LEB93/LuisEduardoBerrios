# Escreva um programa que leia a idade e se a pessoa possui carteira de motorista (S ou N).
# Exiba:

# “Pode dirigir” se tiver 18 anos ou mais e carteira.
# “Pode tirar carteira” se tiver 18 anos ou mais e não tiver carteira.
# “Não pode dirigir” caso contrário.

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você não pode dirigir, pois é menor de idade.")
else:
    carteira = input("Possui CNH? S ou N: ").upper()

    if carteira == "S":
        print("Você pode dirigir.")
    elif carteira == "N":
        print("Precisa obter sua CNH.")

# Crie uma função chamada par_ou_impar(numero) que retorne "Par" se o número for par e "Ímpar" caso contrário.
# Depois, peça ao usuário um número e mostre o resultado da função.

par_ou_impar = int(input("Digite um número: "))

if par_ou_impar % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")

def par_ou_impar1(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

print(par_ou_impar1(20))   # -> Ímpar
print(par_ou_impar1(101))  # -> Par

# Crie uma função chamada classificar_nota(nota) que receba uma nota de 0 a 10 e retorne:

# "Aprovado" se a nota for maior ou igual a 7
# "Recuperação" se estiver entre 5 e 6.9
# "Reprovado" se for menor que 5

# Use operadores lógicos e if/elif/else corretamente.

def classificar_nota(nota):
    if nota >=7:
        return "Aprovado"
    elif 5 <= nota < 7:
        return "Recuperação"
    else:
        return "Reprovado"

nota = float(input("Digite uma nota do aluno entre 0 e 10: "))
resultado = classificar_nota(nota)
print("Situação do aluno: ", resultado)

# Peça ao usuário:
# Seu nome
# Sua idade
# Depois, exiba a frase:
# Olá, [nome]! Você tem [idade] anos.
# Use concatenação e também uma f-string para praticar as duas formas.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá, {nome}! Você tem {idade} anos.")

# O código abaixo tem erro de indentação. Corrija-o:

def verificar(numero):
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")

n = int(input("Digite um número: "))
verificar(n)

# Você recebeu o seguinte código repetitivo. Refatore para usar uma função que receba uma lista de números e retorne a média.
# A entrada de dados deve ser feita com um laço.

# n1 = int(input("Digite o 1º número: "))
# n2 = int(input("Digite o 2º número: "))
# n3 = int(input("Digite o 3º número: "))

# media = (n1 + n2 + n3) / 3
# print("A média é:", media)


def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

# Lista para armazenar os números
numeros = []

# Quantos números o usuário quer digitar
qtd = int(input("Quantos números você quer digitar? "))

for i in range(qtd):
    n = float(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

# Calcula e mostra a média
media = calcular_media(numeros)
print("A média é:", media)
