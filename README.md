# Hand-Gesture-Based-LED-Control-Using-Machine-Learning
🎯 A Python + OpenCV based project that detects hand gestures using cvzone and controls 5 LEDs via Arduino using pyFirmata. Each finger pattern triggers a unique LED combination in real time — a fun intro to computer vision and hardware integration!

 🖐 How it Works
- Webcam detects fingers using hand landmarks
- Finger pattern (like `[0, 1, 1, 0, 0]`) is passed to Arduino
- LEDs light up based on the number or combination of fingers
