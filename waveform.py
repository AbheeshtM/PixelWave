import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

# Load audio file
audio, sr = sf.read("qr_sonified.wav")

# Plot waveform
plt.figure(figsize=(12, 4))
plt.plot(np.linspace(0, len(audio)/sr, len(audio)), audio, color='cyan')
plt.title("Waveform of Sonified QR Code")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
