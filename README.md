# MS211 — Modelo SIR: Métodos Numéricos em Epidemiologia

 Repositório com as implementações numéricas em Python e o código-fonte em LaTeX desenvolvidos para o **Trabalho Avaliativo 2** da disciplina **MS211 (Cálculo Numérico - UNICAMP)**.

O estudo analisa a propagação de um surto infeccioso em uma população fechada ($N = 763$) combinando resolução de EDOs, diferenciação numérica e integração definida.

## 🛠️ Estrutura do Repositório

├── a.py               # Questão 1a: Método de Euler Explícito (h = 0.1)
├── b.py               # Questão 1b: Método de Runge-Kutta de 4ª Ordem - RK4 (h = 0.1)
├── c.py               # Questão 1c: Script comparativo entre Euler e RK4 (gera gráficos)
├── q2_diferenciacao.py # Questão 2: Diferenças Finitas Centradas e busca do pico
├── q3_integracao.py   # Questão 3: Integração da carga da doença (Trapézios e Simpson)
├── main.tex           # Código-fonte do relatório final em LaTeX (Overleaf)
├── references.bib     # Arquivo de referências BibTeX
└── figures/           # Imagens e gráficos gerados pelos scripts (.png)

## Declaração do uso de IA
### 1. Ferramentas Utilizadas
No desenvolvimento deste trabalho, foram consultadas assistentes de Inteligência Artificial (modelos de linguagem natural e geração de código).

### 2. Escopo de Atuação da IA
As ferramentas foram aplicadas para:
1. Apoio no suporte à programação em Python como uso de bibliotecas Matplotlib, Pandas e Numpy.
2. Estruturação e Revisão de clareza e ortogragia na escrita da documentação do repositório e do relatório final.
3. Formatação e estruturação estética de tabelas e marcações Markdown.

### 3. Validação Humana e Autoria
Todos os cálculos numéricos, equações teóricas, análises de convergência, escolha dos passos de integração $h$ e interpretações epidemiológicas foram revisados, testados e validados integralmente pelos autores humanos. Nenhuma etapa analítica ou lógica numérica foi aceita sem a devida verificação dos alunos responsáveis.

# Explicação da Questão 02
## Carga total da doença: integração numérica

### Dados

| Dia | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I | 3 | 7 | 22 | 78 | 233 | 300 | 256 | 233 | 189 | 128 | 72 | 33 | 11 | 6 |

### Trapézios

#### Regra dos Trapézios Repetida

- **Intervalo:** [1, 14]
- **Subintervalos:** n = 13
- **Passo:** h = 1
- **Extremos:** I₀ = 3, Iₙ = 6
- **Soma dos pontos internos:** 1562

$$\frac{1}{2} \left[3 + 2 \cdot 1562 + 6\right] = 1566.5$$

**Resultado:** 1566.5 indivíduos-dia

### Simpson 1/3: ajuste no início (trapézio em [1, 2])

**Observação:** o número de subintervalos da amostra é ímpar, então o Simpson não se aplica a todo o intervalo.
Aplicamos Simpson em [2, 14] e Trapézio simples em [1, 2].

#### Simpson 1/3 Repetida no trecho [2, 14]

- **Intervalo:** [2, 14]
- **Subintervalos:** n = 12 (par)
- **Passo:** h = 1
- **Extremos:** I₀ = 7, Iₙ = 6
- **Soma dos ímpares:** 783
- **Soma dos pares:** 772

$$\frac{1}{3} \left[7 + 4 \cdot 783 + 2 \cdot 772 + 6\right] = 1563$$

**Resultado:** 1563 indivíduos-dia

#### Trapézio simples no trecho restante [1, 2]

$$\frac{1}{2} \left[3 + 7\right] = 5$$

**Resultado:** 5 indivíduos-dia

**Total (Simpson + Trapézio):** 1563 + 5 = **1568 indivíduos-dia**

### Simpson 1/3: ajuste no fim (trapézio em [13, 14])

**Observação:** o número de subintervalos da amostra é ímpar, então o Simpson não se aplica a todo o intervalo.
Aplicamos Simpson em [1, 13] e Trapézio simples em [13, 14].

#### Simpson 1/3 Repetida no trecho [1, 13]

- **Intervalo:** [1, 13]
- **Subintervalos:** n = 12 (par)
- **Passo:** h = 1
- **Extremos:** I₀ = 3, Iₙ = 11
- **Soma dos ímpares:** 779
- **Soma dos pares:** 772

$$\frac{1}{3} \left[3 + 4 \cdot 779 + 2 \cdot 772 + 11\right] = 1558$$

**Resultado:** 1558 indivíduos-dia

#### Trapézio simples no trecho restante [13, 14]

$$\frac{1}{2} \left[11 + 6\right] = 8.5$$

**Resultado:** 8.5 indivíduos-dia

**Total (Simpson + Trapézio):** 1558 + 8.5 = **1566.5 indivíduos-dia**


### Comparação

| Método | ∫ I dt (indivíduos-dia) | Diferença absoluta | Diferença relativa |
|---|---|---|---|
| Trapézios repetida | 1566.5 | — | — |
| Simpson 1/3 em [2, 14] + Trapézio em [1, 2] | 1568 | 1.5 | 0.10% |
| Simpson 1/3 em [1, 13] + Trapézio em [13, 14] | 1566.5 | 0 | 0.00% |

**Sensibilidade à escolha do extremo:** as duas adaptações do Simpson diferem em 1.5 indivíduo-dia (0.10% em relação aos Trapézios).
