import numpy as np
import matplotlib.pyplot as plt

# Gegeven waarden
x = np.array([0.3, 0.5, 0.7, 1.3, 1.5, 1.6, 1.7, 2.6, 2.7, 2.8])
y = np.array([0.2955, 0.4794, 0.6442, 0.9636, 0.9975,
             0.9996, 0.9917, 0.5155, 0.4274, 0.335])

# Voer kwadratische regressie uit
coeff = np.polyfit(x, y, 2)

# Formule van de parabool
print(f"y = {coeff[0]:.5f}x^2 + {coeff[1]:.5f}x + {coeff[2]:.5f}")

# Plot de parabool
x_plot = np.linspace(min(x), max(x), 100)
y_plot = coeff[0] * x_plot**2 + coeff[1] * x_plot + coeff[2]

plt.scatter(x, y, label="Gegeven punten")
plt.plot(x_plot, y_plot, 'r-', label="Kwadratische regressie")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parabool Regressie')
plt.show()
