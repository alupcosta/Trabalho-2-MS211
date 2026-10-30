# =====================================================================
# DECLARAÇÃO DE USO DE INTELIGÊNCIA AI
# Este arquivo foi gerado 100% com auxílio de inteligência artificial
# a partir de instruções e do código-base fornecidos pelos autores.
# Ele é responsável apenas pela formatação do README (Markdown)
# e não contém a lógica numérica.
# Os autores revisaram e validaram a saída gerada.
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


def md_comparacao(T, S):
    diff = abs(S - T)
    rel = 100 * diff / S
    return f"""| Método | ∫ I dt (indivíduos-dia) |
|---|---|
| Trapézios repetida | {T:g} |
| Simpson 1/3 repetida (com ajuste) | {S:g} |
| **Diferença absoluta** | {diff:g} |
| **Diferença relativa** | {rel:.2f}% |
"""


def montar_relatorio(dias, I, res_trap, res_simp):
    return f"""# Carga total da doença: integração numérica

## Dados

{md_dados(dias, I)}

## Trapézios

{md_trapezio(res_trap)}
## Simpson 1/3

{md_simpson_com_ajuste(res_simp)}
## Comparação

{md_comparacao(res_trap['valor'], res_simp['total'])}"""


def main():
    dias, I = carregar_dados("tabela.csv")
    n = len(dias) - 1

    res_trap = trapezio(dias, I, n)
    res_simp = simpson_com_ajuste(dias, I, n)

    with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
        f.write(montar_relatorio(dias, I, res_trap, res_simp))

    print(f"Arquivo {ARQUIVO_SAIDA} gerado.")


if __name__ == "__main__":
    main()