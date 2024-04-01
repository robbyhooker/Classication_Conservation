from ultralytics import YOLO
import os

save_dir = os.getcwd()

model = YOLO('weights/animalDetector.pt')

results = model.track(source='camels.mp4', show=False, tracker="bytetrack.yaml", save=True, save_dir=save_dir)
