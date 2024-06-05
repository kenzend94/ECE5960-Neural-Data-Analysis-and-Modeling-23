# Assuming h_opt is loaded and available
N = len(h_opt)
sampling_rate = 1  # Adjust this to your data's sampling rate if known

# Compute DFT
F_h = np.fft.fft(h_opt)

# Compute power-spectrum
power_spectrum = np.abs(F_h)**2

# Shift the zero-frequency component to the center
power_spectrum_shifted = np.fft.fftshift(power_spectrum)

# Compute frequencies for the x-axis. The zero-frequency component is at the center.
frequencies = np.fft.fftshift(np.fft.fftfreq(N, d=1.0/sampling_rate))

# Plot
plt.plot(frequencies, power_spectrum_shifted)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.title("Power-spectrum of the HRF")
plt.grid()
plt.show()