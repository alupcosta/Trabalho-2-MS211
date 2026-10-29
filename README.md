# Trabalho Avaliativo 2 – MS211 Cálculo Numérico

Modelo SIR: solução numérica de EDOs, diferenciação numérica e integração numérica.

**Universidade Estadual de Campinas (UNICAMP) – IMECC**
**Docente:** Profa. Petra M. Bartmeyer

**Integrantes:**
- Ana Luiza Paro Costa (RA 249728)
- Karen Rosas Ketelhute Sampaio (RA 174537)
- Iago Lucini da Silva (RA 281244)

## Descrição

Este repositório reúne os códigos do Trabalho Avaliativo 2, que estuda um surto de gripe em uma comunidade escolar de N = 763 alunos (dados de infectados ao longo de 14 dias) a partir do modelo SIR.

| Questão | Tema | Arquivo |
|---------|------|---------|
| 1 | Euler explícito e RK4 para o sistema SIR | `<arquivo_q1>` |
| 2 | Diferenças finitas centradas e pico da epidemia | `<arquivo_q2>` |
| 3 | Integração numérica (Trapézios e Simpson 1/3 repetidas) | `<arquivo_q3>.py` |

## Requisitos

- Python 3.8 ou superior
- Não há dependências externas no código da Questão 3 (usa apenas a biblioteca padrão, módulo `csv`)

## Como rodar

1. Clone o repositório e entre na pasta:

   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>
   ```

2. Garanta que o arquivo `tabela.csv` esteja na **mesma pasta** do script, com duas linhas separadas por vírgula: a primeira com os dias e a segunda com a contagem de infectados.

   ```csv
   1,2,3,4,5,6,7,8,9,10,11,12,13,14
   3,7,22,78,233,300,256,233,189,128,72,33,11,6
   ```

3. Execute o script:

   ```bash
   python <arquivo_q3>.py
   ```

### Questão 3 – Integração numérica

O script lê `tabela.csv` e imprime, nesta ordem, o valor da integral de I(t) no intervalo [1, 14] (indivíduos-dia):

1. **Regra dos Trapézios Repetida**, usando todos os 14 pontos (13 subintervalos).
2. **Regra de Simpson 1/3 Repetida**, que exige número par de subintervalos. Como os 14 pontos geram 13 subintervalos (ímpar), a regra é aplicada aos pontos de t = 2 a t = 14 (12 subintervalos), ou seja, `dias[1:]`, `I[1:]` e `n-1`.

### Questões 1 e 2

<!-- Preencher com as instruções de execução e dependências (ex.: numpy, matplotlib) -->

## Estrutura do repositório

```
.
├── tabela.csv        # Dados amostrais de infectados (Tabela 1)
├── <arquivo_q1>      # Questão 1
├── <arquivo_q2>      # Questão 2
├── <arquivo_q3>.py   # Questão 3
├── relatorio/        # Relatório em LaTeX
└── README.md
```