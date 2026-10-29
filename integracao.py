import csv

with open('tabela.csv') as f:
    matriz = [[int(item) for item in row] for row in csv.reader(f)]

dias = matriz[0]
I = matriz[1]
n = len(dias) - 1

def trapezio(dias, I, n):
    h = (dias[n]- dias[0]) / n
    soma = sum(I[1:n])
    T = (h/2) * (I[0] + I[n] + (2*soma))
    return T

def simpson(dias, I, n):
    h = (dias[n] - dias[0]) / n
    soma_impar = sum(I[1:n:2])
    soma_par = sum(I[2:n:2])
    S = (h/3) * (I[0] + I[n] + (2*soma_par) + (4*soma_impar))
    return S

print("Integral aproximada pela Regra dos Trapézios Repetida:", trapezio(dias, I, n))
print("Integral aproximada pela Regra de Simpson 1/3 Repetida:", simpson(dias[1:], I[1:], n-1))