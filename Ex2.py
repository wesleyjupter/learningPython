#Esse programa faz o usuario entrar com N numeros (N escolhido pelo usuario), e retorna eles em ordem descrescente

print("Selecione quantos numeros deseja digitar: ")
N = input("")


print("\nEscreva " + N + " numeros:")

lista = []

x = 0

while(x < int(N)):
    lista.append(input(""))
    x += 1

print ("lista em ordem descrescente: ")
lista.sort()
lista.reverse()
print(lista)
