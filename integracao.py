import csv

with open("tabela.csv") as f:
    matriz = [[int(item) for item in row] for row in csv.reader(f)]

dias = matriz[0]
I = matriz[1]
n = len(dias) - 1

def trapezio(dias, I, n):
    h = (dias[n] - dias[0]) / n
    soma = sum(I[1:n])
    T = (h/2) * (I[0] + I[n] + (2*soma))
    print("\nTrapézios:")
    print(f"Intervalo: [{dias[0]}, {dias[n]}] | n = {n} | h = {h}")
    print(f"Extremos: I_0 = {I[0]}, I_n = {I[n]}")
    print(f"Soma dos pontos internos = {soma}")
    print(f"Resultado: ({h}/2) * [{I[0]} + 2*{soma} + {I[n]}] = {T}")
    return T

def simpson(dias, I, n):
    h = (dias[n] - dias[0]) / n
    soma_impar = sum(I[1:n:2])
    soma_par = sum(I[2:n:2])
    S = (h/3) * (I[0] + I[n] + (2*soma_par) + (4*soma_impar))
    print("\nSimpson 1/3")
    print(f"Intervalo: [{dias[0]}, {dias[n]}] | n = {n} ({"par" if n % 2 == 0 else "ímpar"}) | h = {h}")
    print(f"Extremos: I_0 = {I[0]}, I_n = {I[n]}")
    print(f"Soma dos ímpares = {soma_impar}")
    print(f"Soma dos pares = {soma_par}")
    print(f"Resultado: ({h}/3) * [{I[0]} + 4*{soma_impar} + 2*{soma_par} + {I[n]}] = {S}")
    return S

print(trapezio(dias, I, n))
print(simpson(dias[1:], I[1:], n-1))