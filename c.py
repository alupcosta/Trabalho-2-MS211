import matplotlib.pyplot as plt
import numpy as np


populacao = 763.0  # População total
beta = 1.68  # Taxa de transmissão
gamma = 0.44  # Taxa de recuperação
h = 0.1  # Passo temporal
t_total = 14.0  # Período de simulação

n_steps = int(t_total / h) + 1
t = np.linspace(0, t_total, n_steps)


# Equações diferenciais
def dSdt(S, I):
    return -beta * S * I / populacao


def dIdt(S, I):
    return (beta * S * I / populacao) - gamma * I


def dRdt(I):
    return gamma * I


# MÉTODO DE EULER EXPLÍCITO
S_e = np.zeros(n_steps)
I_e = np.zeros(n_steps)
R_e = np.zeros(n_steps)
S_e[0], I_e[0], R_e[0] = 762.0, 1.0, 0.0

for k in range(n_steps - 1):
    S_e[k + 1] = S_e[k] + h * dSdt(S_e[k], I_e[k])
    I_e[k + 1] = I_e[k] + h * dIdt(S_e[k], I_e[k])
    R_e[k + 1] = R_e[k] + h * dRdt(I_e[k])

# MÉTODO DE RUNGE-KUTTA DE 4ª ORDEM (RK4)
S_r = np.zeros(n_steps)
I_r = np.zeros(n_steps)
R_r = np.zeros(n_steps)
S_r[0], I_r[0], R_r[0] = 762.0, 1.0, 0.0

for k in range(n_steps - 1):
    # k1
    k1_S = dSdt(S_r[k], I_r[k])
    k1_I = dIdt(S_r[k], I_r[k])
    k1_R = dRdt(I_r[k])

    # k2
    k2_S = dSdt(S_r[k] + 0.5 * h * k1_S, I_r[k] + 0.5 * h * k1_I)
    k2_I = dIdt(S_r[k] + 0.5 * h * k1_S, I_r[k] + 0.5 * h * k1_I)
    k2_R = dRdt(I_r[k] + 0.5 * h * k1_I)

    # k3
    k3_S = dSdt(S_r[k] + 0.5 * h * k2_S, I_r[k] + 0.5 * h * k2_I)
    k3_I = dIdt(S_r[k] + 0.5 * h * k2_S, I_r[k] + 0.5 * h * k2_I)
    k3_R = dRdt(I_r[k] + 0.5 * h * k2_R)

    # k4
    k4_S = dSdt(S_r[k] + h * k3_S, I_r[k] + h * k3_I)
    k4_I = dIdt(S_r[k] + h * k3_S, I_r[k] + h * k3_I)
    k4_R = dRdt(I_r[k] + h * k3_I)

    # Atualização
    S_r[k + 1] = S_r[k] + (h / 6.0) * (k1_S + 2 * k2_S + 2 * k3_S + k4_S)
    I_r[k + 1] = I_r[k] + (h / 6.0) * (k1_I + 2 * k2_I + 2 * k3_I + k4_I)
    R_r[k + 1] = R_r[k] + (h / 6.0) * (k1_R + 2 * k2_R + 2 * k3_R + k4_R)

# CONSTRUÇÃO DO GRÁFICO COMPARATIVO
plt.figure(figsize=(10, 6))

# Curvas do Método de Euler (Tracejadas)
plt.plot(t, S_e, 'r--', linewidth=1.8, label='S(t) - Euler')
plt.plot(t, I_e, 'b--', linewidth=1.8, label='I(t) - Euler')
plt.plot(t, R_e, 'g--', linewidth=1.8, label='R(t) - Euler')

# Curvas do RK4 (Linhas Contínuas)
plt.plot(t, S_r, 'r-', linewidth=2.2, label='S(t) - RK4')
plt.plot(t, I_r, 'b-', linewidth=2.2, label='I(t) - RK4')
plt.plot(t, R_r, 'g-', linewidth=2.2, label='R(t) - RK4')

# Detalhes visuais
plt.title(
    'Comparação entre o Método de Euler Explícito e RK4 (h = 0.1 dia)',
    fontsize=12,
)
plt.xlabel('Tempo (dias)', fontsize=11)
plt.ylabel('População (indivíduos)', fontsize=11)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='center right', framealpha=0.9)
plt.tight_layout()

# Salva a imagem para usar no relatório e exibe a figura
plt.savefig('fig_sir_comparacao.png', dpi=300, bbox_inches='tight')
print("Gráfico comparativo salvo com sucesso como 'fig_sir_comparacao.png'!")
plt.show()
