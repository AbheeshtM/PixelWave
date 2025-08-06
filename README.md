# 🎨🔊 PixelWave

**PixelWave** is a unique image↔audio transformation toolkit that allows you to sonify grayscale and color images into audio signals — and reconstruct them back! It's built for artists, researchers, and curious developers to explore how visual data can be encoded into sound.

---

## 🌟 Features

- 🔄 **Image to Audio (Sonification)** — Convert grayscale or RGB images to `.wav` sound
- 🔁 **Audio to Image (Desonification)** — Reconstruct images from encoded `.wav` files
- 🎨 Supports **grayscale and full-color (RGB)**
- 🔊 Uses **multichannel audio encoding** for color images
- 🧪 Useful for **data experiments**, **art installations**, and **audio-visual hacking**

---

## 📂 Project Structure

PixelWave/
│
├── i2a.py # Grayscale image ➝ mono audio
├── a2i.py # Mono audio ➝ grayscale image
├── colouredi2a.py # RGB image ➝ 3-channel audio
├── coloureda2i.py # 3-channel audio ➝ RGB image
├── pengbrew.png # Sample grayscale image
├── a2.png # Sample RGB image
├── qr_sonified.wav # Output from i2a
├── color_encoded.wav # Output from colouredi2a
├── reconstructed.png # Output from coloureda2i
└── README.md # This file
---

## 🛠️ Technologies Used

- **Python 3**
- **NumPy** — for image/audio array manipulation
- **Pillow (PIL)** — for image loading, resizing, RGB splitting
- **SoundFile** — for reading/writing multi-channel `.wav` files
- **SoundDevice** — for optional audio playback
- **OpenCV** — for displaying and saving grayscale images

---

## 🚀 How to Use

### 1. 🔄 Convert Grayscale Image to Audio

```bash
python i2a.py
Input: pengbrew.png

Output: qr_sonified.wav

2. 🔁 Convert Audio Back to Grayscale Image

python a2i.py
Input: dog-bark.wav

Output: bark_image.png

3. 🎨 Convert RGB Image to 3-Channel Audio

python colouredi2a.py
Input: a2.png

Output: color_encoded.wav

4. 🖼️ Reconstruct Color Image from Audio

python coloureda2i.py
Input: color_encoded.wav

Output: reconstructed.png

📦 Installation
Install the required libraries:

pip install numpy pillow soundfile sounddevice opencv-python
📸 Example
Input Image	Encoded Audio	Reconstructed Image
	🎵 color_encoded.wav	

🧠 Applications
🎶 Audio-driven art

🧪 Data representation experiments

🎓 Teaching signal processing or encoding

🕵️ Hidden image transmission via sound

⚖️ License
This project is open-source and free to use under the MIT License.
