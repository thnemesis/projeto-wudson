#Primeiro
"""nome = input("Digite seu nome: ")
nome_curso = input("Digite seu nome curso: ")
periodo_atual = input("Digite seu periodo atual: ")

print(f"nome é {nome} e voçê faz o curso {nome_curso} e esta no periodo {periodo_atual}")

#Segundo
soma = 0
for i in range(3):
    valor = int(input(f"Digiite o {i+1}º número: "))
    soma += valor

print("A soma dos números é:", soma)

#Terceiro
valor_decimal = float(input("Digite um valor decimal: "))
print(valor_decimal / 3)

#Quarto
kmPercorrido = float(input("Digite um valor de km percorrido: "))
litroGasolina = float(input("Digite um valor de litro gasolina: "))
print(kmPercorrido / litroGasolina)

#Quinto
valorSalario = float(input("Digite o valor do salario"))
porcetagem = (valorSalario * 0.15) + valorSalario
print(porcetagem)

#Sexto
anos_em_meses = int(input("Digite sua iddade: "))
print("vc tem aproximadamente ", anos_em_meses * 12, "meses")

#Setimo
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
area = (base * altura) / 2

print("A área do triângulo é:", area)

#Oitavo
preco = float(input("Digite o valor do produto: "))
desconto = float(input("Digite a porcentagem de desconto: "))

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto

print(f"O preço final com desconto é: {preco_final}" )

#Nono (pesquisei a formula, não lembrava.)
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")"""

#Decimo 
nome = input("Digite o nome do aluno: ")

soma = 0

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma += nota

media = soma / 3

print(f"O aluno {nome} tem média {media:.2f}")