import numpy as np
import matplotlib.pyplot as plt

def equilibrium_positions(amplitudes, frequencies):
    g = 9.81  # ускорение свободного падения
    l = 0.2   # длина стержня
    m = 0.1   # масса грузика

    equilibriums = []

    for a in amplitudes:
        f_equilibrium = []
        for f in frequencies:
            omega = 2 * np.pi * f
            T = 2 * np.pi * np.sqrt(l / g)  # период колебаний

            # Проверка условия равновесия грузика
            if a <= l * np.sin(omega * T / 4):
                f_equilibrium.append(True)
            else:
                f_equilibrium.append(False)
        equilibriums.append(f_equilibrium)

    return np.array(equilibriums)

def plot_equilibrium_positions(amplitudes, frequencies, equilibriums):
    plt.imshow(equilibriums, extent=[frequencies[0], frequencies[-1], amplitudes[0], amplitudes[-1]], origin='lower', cmap='binary')
    plt.xlabel('f (частота)')
    plt.ylabel('a (амплитуда)')
    plt.title('Диаграмма равновесия маятника Капицы')
    plt.colorbar(label='Равновесие')

def pendulum_phase_portrait(amplitude, frequency_range):
    g = 9.81  # ускорение свободного падения
    l = 0.2   # длина стержня
    m = 0.1   # масса грузика

    omega_range = 2 * np.pi * frequency_range
    T = 2 * np.pi * np.sqrt(l / g)  # период колебаний

    t = np.linspace(0, 5 * T, 1000)
    theta = amplitude * np.sin(omega_range[:, np.newaxis] * t)

    plt.figure()
    plt.plot(theta, omega_range[:, np.newaxis], 'b-', lw=0.5)
    plt.xlabel('θ (угол)')
    plt.ylabel('ω (угловая скорость)')
    plt.title('Координатный фазовый портрет маятника Капицы')

def energy_plot(amplitude, frequency):
    g = 9.81  # ускорение свободного падения
    l = 0.2   # длина стержня
    m = 0.1   # масса грузика

    omega = 2 * np.pi * frequency
    T = 2 * np.pi * np.sqrt(l / g)  # период колебаний

    t = np.linspace(0, 3 * T, 1000)
    theta = amplitude * np.sin(omega * t)
    dtheta_dt = amplitude * omega * np.cos(omega * t)

    potential_energy = m * g * l * (1 - np.cos(theta))
    kinetic_energy = 0.5 * m * l**2 * dtheta_dt**2

    plt.figure()
    plt.plot(t, potential_energy, 'r-', label='Потенциальная энергия')
    plt.plot(t, kinetic_energy, 'b-', label='Кинетическая энергия')
    plt.xlabel('Время (сек)')
    plt.ylabel('Энергия (Дж)')
    plt.title('Зависимость энергии маятника Капицы')
    plt.legend()

# Параметры для диаграммы равновесия
amplitudes = np.linspace(0, 0.2, 100)
frequencies = np.linspace(0, 5, 100)
equilibriums = equilibrium_positions(amplitudes, frequencies)

plt.figure()
plot_equilibrium_positions(amplitudes, frequencies, equilibriums)

# Параметры для координатного фазового портрета
amplitude = 0.1
frequency_range = np.linspace(0, 4, 100)

plt.figure()
pendulum_phase_portrait(amplitude, frequency_range)

# Параметры для временной зависимости энергии
amplitude = 0.2
frequency = 3

plt.figure()
energy_plot(amplitude, frequency)

plt.show()
