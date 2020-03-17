#Esse programa pede N números inteiros(N escolhido pelo usuario), e mostra a quantidade de números pares e a quantidade de números impares

print("Selecione quantos numeros deseja digitar: ")
N = input("")


print("\nEscreva " + N + " numeros:")

x = 0
pares = 0
impares = 0

while(x < int(N)):
    num = input("")
    x += 1



    div1 = int(num)/2
    div2 = int(div1)
    y = div1 - div2

    if (y == 0):
    #    print("par\n")
        pares += 1
    else:
    #    print("impar\n")
        impares += 1

print(str(pares) + " numeros pares\n")
print(str(impares) + " numeros impares\n")
