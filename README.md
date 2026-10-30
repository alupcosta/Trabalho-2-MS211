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

## Simpson 1/3: ajuste no início (trapézio em [1, 2])

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

## Simpson 1/3: ajuste no fim (trapézio em [13, 14])

**Observação:** o número de subintervalos da amostra é ímpar, então o Simpson não se aplica a todo o intervalo.
Aplicamos Simpson em [1, 13] e Trapézio simples em [13, 14].

### Simpson 1/3 Repetida no trecho [1, 13]

- **Intervalo:** [1, 13]
- **Subintervalos:** n = 12 (par)
- **Passo:** h = 1
- **Extremos:** I₀ = 3, Iₙ = 11
- **Soma dos ímpares:** 779
- **Soma dos pares:** 772

$$\frac{1}{3} \left[3 + 4 \cdot 779 + 2 \cdot 772 + 11\right] = 1558$$

**Resultado:** 1558 indivíduos-dia

### Trapézio simples no trecho restante [13, 14]

$$\frac{1}{2} \left[11 + 6\right] = 8.5$$

**Resultado:** 8.5 indivíduos-dia

**Total (Simpson + Trapézio):** 1558 + 8.5 = **1566.5 indivíduos-dia**


## Comparação

| Método | ∫ I dt (indivíduos-dia) | Diferença absoluta | Diferença relativa |
|---|---|---|---|
| Trapézios repetida | 1566.5 | — | — |
| Simpson 1/3 em [2, 14] + Trapézio em [1, 2] | 1568 | 1.5 | 0.10% |
| Simpson 1/3 em [1, 13] + Trapézio em [13, 14] | 1566.5 | 0 | 0.00% |

**Sensibilidade à escolha do extremo:** as duas adaptações do Simpson diferem em 1.5 indivíduo-dia (0.10% em relação aos Trapézios).
