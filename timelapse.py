#ffmpeg -pattern_type glob -i "*.jpg" -c:v libx264 -pix_fmt yuv410p out.mp4

import cv2 
import time;
from datetime import datetime 

cap = cv2.VideoCapture(0);
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720);

if not cap.isOpened():
	print("Error: Could not open webcam");
	exit();


for pic in range(0, 2*60): 
	ret, frame = cap.read();
	if ret: 
		timestring = datetime.now().strftime("%y%m%d_%H%M%S")
		cv2.imwrite(f"{timestring}.jpg", frame);
		print(f"Image captured at {timestring}");
	else: 
		print("Error: Could not read from webcam.");
	time.sleep(10);

cap.release();
