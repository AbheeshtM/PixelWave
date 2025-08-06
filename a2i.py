import soundfile as sf
import numpy as np
import cv2

# Load the audio file (make sure the file exists)
audio, sr = sf.read("dog-bark.wav")

# Normalize/scale audio into [0, 255]
pixels = (audio * 128 + 128).clip(0, 255).astype(np.uint8)

# Resize into an image
size = int(np.sqrt(len(pixels)))  # auto size
pixels = pixels[:size*size]       # crop to square
image = pixels.reshape((size, size))

# Save and display
cv2.imwrite("bark_image.png", image)
cv2.imshow("Sound Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("✅ Bark image saved and displayed.")
