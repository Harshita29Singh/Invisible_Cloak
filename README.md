# 🪄 Invisible Cloak using OpenCV

A real-time Computer Vision project inspired by the Harry Potter invisibility cloak. This application uses OpenCV and Python to detect a specific color in a video stream and replace it with a previously captured background, creating an invisibility effect.

## 🚀 Features

- Real-time webcam processing
- Color detection using HSV color space
- Background capture and replacement
- Noise reduction using morphological operations
- Invisible cloak effect on selected colored objects

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy

## 📂 Project Structure

```
Invisible_Cloak/
│
├── invisible_cloak.py
├── camera.py
├── color_detect.py
├── README.md
└── requirements.txt
```

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Harshita29Singh/Invisible_Cloak.git
cd Invisible_Cloak
```

Install dependencies:

```bash
pip install opencv-python numpy
```

## ▶️ Run the Project

```bash
python invisible_cloak.py
```

## 🎯 How It Works

1. Capture the background frame.
2. Detect the red-colored cloak using HSV masking.
3. Create a mask for the selected color.
4. Replace the detected area with the captured background.
5. Display the final invisibility effect in real time.

## 📸 Future Improvements

- Support multiple cloak colors
- Better background segmentation
- Deep learning based object masking
- Performance optimization

## 👩‍💻 Author

**Harshita Singh**

B.Tech CSE (AI & ML)  
Galgotias University

---

⭐ If you like this project, consider giving it a star.
