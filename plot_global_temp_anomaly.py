import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt("global_temp_monthly.csv", skiprows=1, delimiter=",")
anios = datos[:,0]
anomalias = datos[:,1:]

plt.figure(figsize=(14,4))
plt.imshow(anomalias.T, cmap="rainbow", aspect="auto", extent=[anios.min(), anios.max()+1, 1, 12+1])

meses = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dic"]
years_ticks = np.arange(anios.min(), anios.max()+1, 10)
plt.xticks(years_ticks+0.5, years_ticks)
months_ticks = np.flip(np.arange(1, 12+1))
plt.yticks(months_ticks+0.5, meses)

plt.tight_layout()
plt.show()
