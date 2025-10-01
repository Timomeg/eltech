import matplotlib.pyplot as plt
import numpy as np

# Параметры стенда для phi в R-С и С-R
R1 = 220    # Ом
Lk = 0.1    # Гн
Rk = 190    # Ом
C = 4.4e-6  # Ф

# Диапазон логарифма частоты (lg ω)
lg_omega = np.linspace(2, 5, 500)  # lg ω от 2 до 5 (ω от 100 до 100000 рад/с)
omega = 10**lg_omega 

# Формулы для цепей R-C и C-R
omega_R1C = omega * R1 * C
phi_R_C = -np.pi/2 + np.arctan(omega_R1C)
phi_C_R =  np.arctan(1 / omega_R1C)
phi_deg_R_C = np.degrees(phi_R_C)
phi_deg_C_R = np.degrees(phi_C_R)

# График
plt.figure(figsize=(10, 6))

plt.plot(lg_omega, phi_deg_C_R, "black", linewidth=2, markersize=6, label="1 четверть")

plt.plot(lg_omega, phi_deg_R_C, "black", linewidth=2, markersize=6, label="4 четверть")

# Миллиметровая сетка
plt.grid(True, which="both", alpha=0.3)
plt.minorticks_on()

# Настройка осей
plt.xlim(1.9, 4.2)
plt.ylim(-90, 100)

# Деления по оси X
x_ticks = np.arange(2.1, 4.3, 0.3)
plt.xticks(x_ticks)

# Линия y=0
plt.axhline(y=0, color="black", linewidth=1)

# Подписи
plt.xlabel("lgω", fontsize=12)
plt.ylabel("$\\varphi$, град", fontsize=12)

# Сетка по X и Y
plt.xticks(np.arange(1.9, 4.2, 0.02), minor=True)
plt.yticks(np.arange(-85, 91, 5))
plt.gca().set_yticks(np.arange(-91, 101, 1), minor=True)

# Отключение tight_layout
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
# plt.show()
plt.savefig("R_C_phi.jpg")