from PIL import Image
import numpy as np
import soundfile as sf

img = Image.open("a2.png").resize((128, 128)).convert("RGB")
r, g, b = img.split()

# Normalize to -1.0 to 1.0 float32
def normalize_channel(ch):
    return (np.array(ch).flatten() / 127.5) - 1.0

r_audio = normalize_channel(r)
g_audio = normalize_channel(g)
b_audio = normalize_channel(b)

# Stack into 3-channel audio (multichannel WAV)
rgb_audio = np.stack([r_audio, g_audio, b_audio], axis=1)

# Save as WAV with 3 channels
sf.write("color_encoded.wav", rgb_audio, samplerate=44100)
