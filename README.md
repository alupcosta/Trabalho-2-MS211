# Carga total da doença: integração numérica

## Dados

| Dia | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I | 3 | 7 | 22 | 78 | 233 | 300 | 256 | 233 | 189 | 128 | 72 | 33 | 11 | 6 |

## Trapézios

### Regra dos Trapézios Repetida

- **Intervalo:** [1, 14]
- **Subintervalos:** n = 13
- **Passo:** h = 1
- **Extremos:** I₀ = 3, Iₙ = 6
- **Soma dos pontos internos:** 1562

$$\frac{1}{2} \left[3 + 2 \cdot 1562 + 6\right] = 1566.5$$

**Resultado:** 1566.5 indivíduos-dia

## Simpson 1/3

**Observação:** o número de subintervalos da amostra é ímpar, então o Simpson não se aplica a todo o intervalo.
Aplicamos Simpson em [2, 14] e Trapézio simples em [1, 2].

### Simpson 1/3 Repetida no trecho [2, 14]

- **Intervalo:** [2, 14]
- **Subintervalos:** n = 12 (par)
- **Passo:** h = 1
- **Extremos:** I₀ = 7, Iₙ = 6
- **Soma dos ímpares:** 783
- **Soma dos pares:** 772

$$\frac{1}{3} \left[7 + 4 \cdot 783 + 2 \cdot 772 + 6\right] = 1563$$

**Resultado:** 1563 indivíduos-dia

### Trapézio simples no trecho restante [1, 2]

$$\frac{1}{2} \left[3 + 7\right] = 5$$

**Resultado:** 5 indivíduos-dia

**Total (Simpson + Trapézio):** 1563 + 5 = **1568 indivíduos-dia**

## Comparação

| Método | ∫ I dt (indivíduos-dia) |
|---|---|
| Trapézios repetida | 1566.5 |
| Simpson 1/3 repetida (com ajuste) | 1568 |
| **Diferença absoluta** | 1.5 |
| **Diferença relativa** | 0.10% |
