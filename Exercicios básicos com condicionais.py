# Peça um número ao usuário e diga se ele é positivo, negativo ou zero.

n = float(input("Digite um número: "))

if n == 0:
    print(f"{n} é Zero")
elif n > 0:
    print(f"{n} é positivo.")
else:
    print(f"{n} é negativo.")

# Peça um número inteiro e diga se ele é par ou ímpar.

n = int(input("Digite um número: "))
if n % 2 == 0:
    print(f"{n} é par.")
else:
    print(f"{n} é impar.")

# Peça a idade de uma pessoa e diga se ela é maior de idade (18 anos ou mais) ou menor de idade.

n = int(input("Digite sua idade: "))
if n >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Peça a nota de um aluno e mostre: “Aprovado” se for maior ou igual a 7, “Recuperação” se for entre 5 e 6.9 e “Reprovado” se for menor que 5.

nota = float(input("Digite a sua nota: "))

if nota >= 7:
    print("Você foi aprovaddo.")
elif nota < 5:
    print("Você foi reprovado.")
else:
    print("Você está em recuperação")

# Peça três números e mostre qual é o maior deles.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior número digitado.")
elif n2 > n1 and n2 > n3:
    print(f"{n2} é o maior número digitado.")
else:
    print(f"{n3} é o maior número digitado.")

# Peça um nome de usuário e uma senha. Se o usuário for "admin" e a senha "1234", mostre “Acesso permitido”. Caso contrário, mostre “Usuário ou senha incorretos”.

login_usuario = "admin"
senha_usuário = 1234

login_digitado = input("Digite o nome do usuário: ")
senha_digitada = int(input("Digite sua senha numérica: "))

if login_digitado == login_usuario and senha_digitada == senha_usuário:
    print("Acesso permitido.")
else:
    print("Usuário ou senha incorretos!")

# Peça a idade e diga: até 12 anos → “Criança”, de 13 a 17 → “Adolescente”, de 18 a 59 → “Adulto”, 60 ou mais → “Idoso”.

idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("Você é uma criança.")
elif idade >= 13 and idade <= 17:
    print("Você é um adolescente.")
elif idade >= 18 and idade <=59:
    print("Você é uma Adulto.")
else:
    print("Você é um idoso.")

# Solução mais simplificada

idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("Você é uma criança.")
elif idade <= 17:
    print("Você é um adolescente.")
elif idade <=59:
    print("Você é uma Adulto.")
else:
    print("Você é um idoso.")

# Peça dois números e uma operação (+, -, *, /). Mostre o resultado da operação escolhida. (Use if para decidir qual operação executar.)

n1 = int(input("Digite o primeiro número: "))
op = input("Qual operação deseja efetuar: + | - | * | / ==> ")
n2 = int(input("Digite o segundo número: "))

if op == "+":
    print(f"A soma dos valores é {n1 + n2}")
elif op == "-":
    print(f"A subtração dos valores é {n1 - n2}")
elif op == "*":
    print(f"A multiplicação dos valores é {n1 * n2}")
elif op == "/":
    try:
        print(f"A divisão dos valores é {n1 / n2}")
    except ZeroDivisionError:
        print("Não é possivel dividir por zero!")
else:
    print("Operação inválida.")

# Peça um ano e diga se ele é bissexto. Dica: um ano é bissexto se for divisível por 4, mas não por 100, exceto se também for divisível por 400.)

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")

# Peça o valor de uma compra: Se for maior ou igual a 100, dê 10% de desconto. Caso contrário, sem desconto.

total = float(input("Qual foi o valor total da compra: "))
if total >= 100:
    desconto = total - (total * 0.10)
    print(f"Você ganhou 10% de desconto, por isso, o valor da compra é de R$ {desconto:.2f}")
else:
    print(f"O valor total da compra é {total}")