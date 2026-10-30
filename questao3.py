import csv

def carregar_dados(caminho="tabela.csv"):
    with open(caminho) as f:
        matriz = [[int(item) for item in row] for row in csv.reader(f)]
    return matriz[0], matriz[1]


def trapezio(dias, I, n):
    h = (dias[n] - dias[0]) / n
    soma = sum(I[1:n])
    valor = (h / 2) * (I[0] + I[n] + 2 * soma)
    return {
        "a": dias[0], "b": dias[n], "n": n, "h": h,
        "I0": I[0], "In": I[n], "soma": soma, "valor": valor,
    }


def simpson(dias, I, n):
    h = (dias[n] - dias[0]) / n
    soma_impar = sum(I[1:n:2])
    soma_par = sum(I[2:n:2])
    valor = (h / 3) * (I[0] + I[n] + 2 * soma_par + 4 * soma_impar)
    return {
        "a": dias[0], "b": dias[n], "n": n, "h": h,
        "I0": I[0], "In": I[n],
        "soma_impar": soma_impar, "soma_par": soma_par, "valor": valor,
    }


def simpson_com_ajuste(dias, I, n):
    if n % 2 == 0:
        S = simpson(dias, I, n)
        return {"ajustado": False, "simpson": S, "trapezio": None, "total": S["valor"]}

    S = simpson(dias[1:], I[1:], n - 1)
    h = dias[1] - dias[0]
    T = {
        "a": dias[0], "b": dias[1], "h": h,
        "I0": I[0], "I1": I[1],
        "valor": (h / 2) * (I[0] + I[1]),
    }
    return {
        "ajustado": True,
        "simpson": S,
        "trapezio": T,
        "total": S["valor"] + T["valor"],
    }