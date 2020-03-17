#Esse exercicio faz o usuario entrar com cada elementos de uma matriz NxN (N definido pelo usuario) e retorna a matriz transposta
print("Selecione quantos numeros deseja digitar: ")
N = input("")
num_linhas = int(N)

print("Preencha a matriz(coluna por coluna):")

A = []

for i in range(int(N)):
    A.append( [0] * int(N) )

i = 0
j = 0

for i in range(int(N)):
    for j in range(int(N)):
        A[i][j] = input("")
    print("\n")

i = 0

for i in range(int(N)):
    print(A[i])
