import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt("co2_mm_mlo.txt", comments="#")
tiempo = datos[:,2]
CO2 = datos[:,3]
incert = datos[:,7]

plt.plot(tiempo, CO2, label="CO2")
plt.xlabel("Tiempo")
plt.ylabel("CO2 (ppm)")
plt.title("Evolución del CO2 atmosférico")
plt.grid(ls=":")
plt.legend()

plt.show()