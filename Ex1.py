
#Esse programa faz o usuario entrar com N numeros (N escolhido pelo usuario), e retorna a media aritmetica dos numeros negativos que entraram

print("Selecione quantos numeros deseja digitar: ")
N = input("")


print("\nEscreva " + N + " numeros:")

lista = []
negativos = []

x = 0

while(x < int(N)):
    num = input("")
    lista.append(num)

    if float(num) < 0:
        negativos.append(num)

    x += 1

print(lista)
print(negativos)

tamanho =  len(negativos)

soma = 0
for numero_neg in negativos:
    soma +=  float(numero_neg)

media = soma/tamanho

print(media)
