# =====================================================================
# DECLARAÇÃO DE USO DE INTELIGÊNCIA ARTIFICIAL
# Este arquivo foi gerado 100% com auxílio de inteligência artificial
# (Claude, da Anthropic), a partir de instruções e do código-base
# fornecidos pelos autores. Ele é responsável apenas pela formatação
# do README (Markdown) e não contém a lógica numérica, que está em
# questao3.py. Os autores revisaram e validaram a saída gerada.
# =====================================================================
from questao3 import carregar_dados, trapezio, simpson_com_ajuste

ARQUIVO_SAIDA = "README.md"


def md_dados(dias, I):
    return (
        "| Dia | " + " | ".join(str(d) for d in dias) + " |\n"
        "|---|" + "---|" * len(dias) + "\n"
        "| I | " + " | ".join(str(v) for v in I) + " |"
    )


def md_trapezio(r):
    return f"""### Regra dos Trapézios Repetida

- **Intervalo:** [{r['a']}, {r['b']}]
- **Subintervalos:** n = {r['n']}
- **Passo:** h = {r['h']:g}
- **Extremos:** I₀ = {r['I0']}, Iₙ = {r['In']}
- **Soma dos pontos internos:** {r['soma']}

$$\\frac{{{r['h']:g}}}{{2}} \\left[{r['I0']} + 2 \\cdot {r['soma']} + {r['In']}\\right] = {r['valor']:g}$$

**Resultado:** {r['valor']:g} indivíduos-dia
"""


def md_simpson(r, titulo="Regra de Simpson 1/3 Repetida"):
    return f"""### {titulo}

- **Intervalo:** [{r['a']}, {r['b']}]
- **Subintervalos:** n = {r['n']} (par)
- **Passo:** h = {r['h']:g}
- **Extremos:** I₀ = {r['I0']}, Iₙ = {r['In']}
- **Soma dos ímpares:** {r['soma_impar']}
- **Soma dos pares:** {r['soma_par']}

$$\\frac{{{r['h']:g}}}{{3}} \\left[{r['I0']} + 4 \\cdot {r['soma_impar']} + 2 \\cdot {r['soma_par']} + {r['In']}\\right] = {r['valor']:g}$$

**Resultado:** {r['valor']:g} indivíduos-dia
"""


def md_trapezio_simples(r):
    return f"""### Trapézio simples no trecho restante [{r['a']}, {r['b']}]

$$\\frac{{{r['h']:g}}}{{2}} \\left[{r['I0']} + {r['I1']}\\right] = {r['valor']:g}$$

**Resultado:** {r['valor']:g} indivíduos-dia
"""


def md_simpson_com_ajuste(r):
    S, T = r["simpson"], r["trapezio"]
    if not r["ajustado"]:
        return md_simpson(S)

    return f"""**Observação:** o número de subintervalos da amostra é ímpar, então o Simpson não se aplica a todo o intervalo.
Aplicamos Simpson em [{S['a']}, {S['b']}] e Trapézio simples em [{T['a']}, {T['b']}].

{md_simpson(S, titulo=f"Simpson 1/3 Repetida no trecho [{S['a']}, {S['b']}]")}
{md_trapezio_simples(T)}
**Total (Simpson + Trapézio):** {S['valor']:g} + {T['valor']:g} = **{r['total']:g} indivíduos-dia**
"""


def nome_variante(r):
    if not r["ajustado"]:
        return "Simpson 1/3 repetida"
    S, T = r["simpson"], r["trapezio"]
    return (f"Simpson 1/3 em [{S['a']}, {S['b']}] "
            f"+ Trapézio em [{T['a']}, {T['b']}]")


def md_comparacao(res_trap, variantes):
    ref = res_trap["valor"]
    linhas = [f"| Trapézios repetida | {ref:g} | — | — |"]
    for r in variantes:
        diff = abs(r["total"] - ref)
        rel = 100 * diff / ref
        linhas.append(f"| {nome_variante(r)} | {r['total']:g} | {diff:g} | {rel:.2f}% |")

    texto = (
        "| Método | ∫ I dt (indivíduos-dia) | Diferença absoluta | Diferença relativa |\n"
        "|---|---|---|---|\n" + "\n".join(linhas) + "\n"
    )

    if len(variantes) == 2:
        v1, v2 = variantes[0]["total"], variantes[1]["total"]
        texto += (
            f"\n**Sensibilidade à escolha do extremo:** as duas adaptações do Simpson "
            f"diferem em {abs(v1 - v2):g} indivíduo-dia "
            f"({100 * abs(v1 - v2) / ref:.2f}% em relação aos Trapézios).\n"
        )
    return texto


def montar_relatorio(dias, I, res_trap, variantes):
    if len(variantes) == 1:
        secoes = f"## Simpson 1/3\n\n{md_simpson_com_ajuste(variantes[0])}\n"
    else:
        secoes = (
            f"## Simpson 1/3: ajuste no início (trapézio em [{dias[0]}, {dias[1]}])\n\n"
            f"{md_simpson_com_ajuste(variantes[0])}\n"
            f"## Simpson 1/3: ajuste no fim (trapézio em [{dias[-2]}, {dias[-1]}])\n\n"
            f"{md_simpson_com_ajuste(variantes[1])}\n"
        )

    return f"""# Carga total da doença: integração numérica

## Dados

{md_dados(dias, I)}

## Trapézios

{md_trapezio(res_trap)}
{secoes}
## Comparação

{md_comparacao(res_trap, variantes)}"""


def main():
    dias, I = carregar_dados("tabela.csv")
    n = len(dias) - 1

    res_trap = trapezio(dias, I, n)
    res_simp = simpson_com_ajuste(dias, I, n)

    # Se n é par, não há ajuste e só existe uma variante.
    variantes = [res_simp, res_simp["fim"]] if res_simp["ajustado"] else [res_simp]

    with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
        f.write(montar_relatorio(dias, I, res_trap, variantes))

    print(f"Arquivo {ARQUIVO_SAIDA} gerado.")


if __name__ == "__main__":
    main()