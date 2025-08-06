import numpy as np
import soundfile as sf
from PIL import Image

# Read 3-channel WAV
rgb_audio, _ = sf.read("color_encoded.wav")  # shape: (n_samples, 3)

def denormalize_channel(audio):
    return ((audio + 1.0) * 127.5).astype(np.uint8)

r = denormalize_channel(rgb_audio[:, 0])
g = denormalize_channel(rgb_audio[:, 1])
b = denormalize_channel(rgb_audio[:, 2])

# Reconstruct and save image
w, h = 128, 128
recon_img = Image.merge("RGB", (
    Image.fromarray(r.reshape((h, w))),
    Image.fromarray(g.reshape((h, w))),
    Image.fromarray(b.reshape((h, w)))
))
recon_img.save("reconstructed.png")
