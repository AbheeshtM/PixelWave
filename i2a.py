import cv2
import numpy as np
import soundfile as sf
import sounddevice as sd

# Load and resize QR image
img = cv2.imread("pengbrew.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (256, 256))  # standard size
flat = img.flatten().astype(np.float32)

# Normalize pixel values from [0, 255] to [-1.0, 1.0]
audio = (flat - 128) / 128.0

# Save as .wav file
sf.write("qr_sonified.wav", audio, samplerate=44100)
print("✅ Audio saved as 'qr_sonified.wav'")

# Optional: play the sound
sd.play(audio, samplerate=44100)
sd.wait()
