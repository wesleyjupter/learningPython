#Esse programa retorna um elemento qualquer da Serie de Fibonacci e a serie ate esse indice

Fib = [1, 1]

print("Insira o indice da serie de Fibonacci que deseja saber: ")
indice = input ("")

x = 1

while (x < int(indice)):
        Fib.append(Fib[x] + Fib[x-1])
        x+=1

print("\n\nSerie ate o indice " + indice + " :")
print(Fib)

print("\n\nElemento de indice " + indice + " :")
print(Fib[int(int(indice)-1)])
