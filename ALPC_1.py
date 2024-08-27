# 1.  Faça um Programa que mostre a mensagem "Alo mundo" na tela.

  #print("Hello World")
  #print('Hello World')

# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

  #numero = input("Informe um número: ")
  #print("O número informado foi", numero)

# 3. Faça um Programa que peça dois números e imprima a soma.

  #num1 = float(input("Informe o primeiro número: ")) #tem que ter o float ou int para o python entender que a soma não é concatenar texto, e sim somar números
  #num2 = float(input("Informe o segundo número " ))
  #soma = num1 + num2
  #print("A soma dos números escolhidos é", soma)

# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

  #nota1 = float(input("Informe a nota do 1º bimestre: "))
  #nota2 = float(input("Informe a nota do 2º bimestre: "))
  #nota3 = float(input("Informe a nota do 3º bimestre: "))
  #nota4 = float(input("Informe a nota do 4º bimestre: "))

#media = (nota1 + nota2 + nota3 + nota4)/4
#print("Sua média bimestral foi de", media)

# 5. Faça um Programa que converta metros para centímetros.

#metros = float(input("Informe a medida em metros: "))
#conversao_em_centimetros = metros*100
#print(metros, "metro(s) é equivalente a ",conversao_em_centimetros, "centímetros.")
  

# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

#import math #importar biblioteca para ter o número exato de pi
#raio = float(input("Informe o raio de determinado círculo: "))
#area = math.pi * raio ** 2
#print("A área do círculo é ", area)

# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

#lado = float(input("Informe a medida em centímetros de um lado do quadrado em questão: "))
#area = lado ** 2
#dobro_area = area * 2
#print ("O dobro da área do quadrado com os lados equivalentes a ", lado, "é igual a ", dobro_area, "cm²")


# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

#ganho_hora = float(input("Informe o valor que você ganha por hora trabalhada: "))
#horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))
#salario = ganho_hora * horas_trabalhadas
#print ("Seu salário neste mês será de ", salario)


# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

#F = float(input("Informe a temperatura em graus Fahrenheit: "))
#C = 5 * ((F-32) / 9)
#print("A conversão da temperatura informada resulta em ", C, "°C")


# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

# C = float(input("Informe a temperatura em graus Celsius: "))
# F = (C * 1.8) + 32
# print("A conversão da temperatura informada resulta em ", F, "°F")


# 11. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

# altura = float(input("Informe a sua altura: "))
# peso_ideal = (72.7*altura) - 58
# print("O peso ideal para a sua altura é de", peso_ideal, "kg")


# 12. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#a.)Para homens: (72.7*h) - 58
#b.) Para mulheres: (62.1*h) - 44.7

##meu jeito##

# altura = float(input("Informe a sua altura para descobrir seu peso ideal: "))
# homem = (72.7 * altura) - 58
# mulher = (62.1 * altura) - 44.7
# print("Peso ideal para homem:", homem, "kg")
# print("Peso ideal para mulher:", mulher, "kg")

##ou final pode ser com quebra de linha \n##

# print("Peso ideal para homem:", homem, "kg", "\n",
# "Peso ideal para mulher:", mulher, "kg")

# 13. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

##meu jeito##

# peso_peixes = float(input("João, informe quantos quilos de peixe você pegou hoje: "))
# peso_excedente = peso_peixes - 50
# multa = peso_excedente * 4
# if peso_peixes < 51:
#   print("Que ótimo! Você está dentro do limite previsto por lei e está isento de multa!")
# else:
#   print("João, infelizmente será necessário pagar uma multa de R$", multa, "pois você excedeu", peso_excedente, "kg do regulamento de rendimento diário de pesca do estado de São Paulo.")

##resolução da professora##

# peso = float(input("Infome o peso de peixe: "))
# if peso > 50:
#   excesso = peso - 50
#   multa = excesso * 4
#   print("Peso excedente: ", excesso)
#   print("Multa: ", multa)

# 14. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

##ceil arredonda pra cima (precisa importar math)
##round arredonda para o mais próximo (NÃO precisa importar math)

# import math
# area = float(input("Informe a área: "))
# litros = area / 3
# latas = math.ceil(litros / 18)
# preco = latas * 80
# print("Litros: ", litros)
# print("Quantidade de latas: ", latas)
# print("Valor da tinta: ", preco)


# 15. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# a) comprar apenas latas de 18 litros;
# b) comprar apenas galões de 3,6 litros;
# c) misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10%

# import math
# area = float(input('informe a área'))
# litros = area/6*1.10
# #calculando latas
# latas = math.ceil(litros/18)
# precolata = latas*80
# print('latas ', latas)
# print('preço latas ', precolata)

# #calculando galões
# galao = math.ceil(litros/3.6)
# precogalao = galao*25
# print('galão ', galao)
# print('preço galão ', precogalao)

# #melhor combinação
# galaom = int(litros/18)
# precogalaom = galaom*25
# print('galão ', galaom)
# print('preço galão ', precogalaom)
# latam = math.ceil((litros%18/3.6))
# precolatam = latam*25
# print('lata ', latam)
# print('preço lata ', precolatam)
      #print não precisa estar no final




#estrutura de decisão - exemplos

# if <condição>

# else

                            # operadores lógicos
    # e - (V+V=V) precisa ser tudo V para ser V
    # ou - (V+F=V) apenas um V já é V
    # não (V+V=F) oposto

                          # operadores ralacionais:
    # >=
    # >
    # <=
    # <
    # ==
    # !=

#operadores relacionais retorna V ou F, exemplo:
# a = 7
# b = 8
# print(a < b)
# #V
# print(a > b and a == 7) 
# #F and V = F
# print(a > b or a == 7)
# #F or V = V
# print(a > b or (a == 7 and b == 8))
# #F or V and V
# #V and V
# # =V
# print(a < b or a == 7 and b > 8)
# # resolve o and primeiro
# print((a < b or a == 7) and b > 8)
# # resolve o parênteses primeiro


#estrutura de decisão/condicional
#observações gerais: não esquecer dos dois pontos e comando tem que estar na mesma margem para entrar na estrutura.
#if: NÃO tem condição, e sim situação, e não precisa ter else
#else: condição vai aqui, precisa obrigatoriamente ter if

# a = 7
# b = 8

# if a == 7: #verdadeiro
#   print("Teste if")
#   print("Fim if")

# if b == 8: #verdadeiro
#   print("Teste 2 if")

# if b < a: #falso
#   print("Teste 3 if")
# else:
#   print("Teste else")
#   print("Fim else")

# EXERCÍCIOS:

# 1) “Ler dois valores numéricos, efetuar a adição e apresentar o seu resultado caso o valor somado seja maior que 10”.
# num1 = float(input("Insira o primeiro número: "))
# num2 = float(input("Insira o segundo número: "))
# soma = num1 + num2
# if soma > 10:
#   print("A soma dos valores é: ", soma)
# else:
#   print("A soma dos números não é maior que 10, logo, o resultado não será mostrado.")


# 2) Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
# a = float(input("Insira o primeiro número: "))
# b = float(input("Insira o segundo número: "))
# c = float(input("Insira o terceiro número: "))
# soma_a_b = a + b
# if soma_a_b < c:
#   print("A soma do primeiro e segundo número é: ", soma_a_b)
# else:
#   print("A soma do primeiro e segundo número não é menor que o terceiro número, logo, o resultado não será mostrado.")

# 3) Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).


nome = input("Informe o seu nome: ")
sexo = input("Informe o seu sexo (F ou H): ")
estado_civil = input("Informe seu estado civil: ")
 
 
if sexo in ["F" , "f"] and estado_civil in ["casada" , "Casada" , "CASADA"]:
   
    tempo_casada = int(input("Quanto tempo de casada (anos)? "))
    print("Nome: ", nome)
    print("Sexo: ", sexo)
    print("Estado civil: ", estado_civil)
    print("Tempo casada: ", tempo_casada)
 
else:
    print("Nome: ", nome)
    print("Sexo: ", sexo)
    print("Estado civil: ", estado_civil)
 
nome = input("Informe o seu nome: ")
sexo = input("Informe o seu sexo (F ou H): ")
estado_civil = input("Informe seu estado civil: ")
 
 
if sexo == ("F" or "f") and estado_civil == ("casada" or "Casada" or "CASADA"):
   
    tempo_casada = int(input("Quanto tempo de casada (anos)? "))
    print("Nome: ", nome)
    print("Sexo: ", sexo)
    print("Estado civil: ", estado_civil)
    print("Tempo casada: ", tempo_casada)
 
else:
    print("Nome: ", nome)
    print("Sexo: ", sexo)
    print("Estado civil: ", estado_civil)
 
















  
# ctrl + / comenta um código inteiro selecionado

#int = numero inteiro
#float = numero quebrado
      
# regras nome de variáveis: começa com letra; pode ter número; underline (melhor sem acentuação)

# python não precisa tipificar a variável, como número inteiro, string, etc, assim como outras linguagens, como Java e C#

      
