import numpy as np
import matplotlib.pyplot as plt

# Load the data (skip any non-numeric header lines if needed)
data = np.loadtxt("sunspots.dat")

# Extract columns
time = data[:, 0]
counts = data[:, 1]

# Plot the data
plt.figure(figsize=(12,5))
plt.plot(time, counts, lw=1)
plt.ylabel("Número manchas solares")
plt.title("Conteo diario de manchas solares")
plt.grid(ls=":")
plt.tight_layout()
plt.show()

# Compute the Fourier power spectrum
power = np.abs(np.fft.rfft(counts))**2
freqs = np.fft.rfftfreq(len(counts))

# remove DC term
power = power[1:]
freqs = freqs[1:]

# Compute the periods, in years
periods = 1/freqs/365

# Plot power spectrum
plt.figure(figsize=(8,5))
plt.loglog(periods, power)
plt.axvline(11, color="red")
plt.gca().invert_xaxis()
plt.xlabel("Period (years)")
plt.ylabel("Power")
plt.title("Espectro de potencia de Fourier de manchas solares")
plt.grid(True)
plt.tight_layout()
plt.show()
