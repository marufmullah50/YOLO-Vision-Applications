from ultralytics import YOLO
from PIL import Image   
import cv2

model = YOLO("G:\\Github_Projects\\YOLO_Projects\\live_tracking(translate_sign)\\best.pt")
results = model.predict(source="0", show=True)
