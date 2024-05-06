from ultralytics import YOLO
import os

save_dir = os.getcwd()
# upload video of animals you wish to track
video_file = 'camels.mp4'

# upload model via weights in .pt file
model = YOLO('animalDetector.pt')

"""
Run YOLO tracking function:
source: your video
show: True will display live tracking in a seperate window
save: True saves tracked video in project path
"""
results = model.track(source=video_file, show=False, tracker="bytetrack.yaml", save=True, project=os.getcwd())
