from ultralytics import YOLO
import os

save_dir = os.getcwd()
video_file = 'camels.mp4'

model = YOLO('animalDetector.pt')

results = model.track(source=video_file, show=False, tracker="bytetrack.yaml", save=True, project=os.getcwd())
