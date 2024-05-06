import os
import numpy as np
from sklearn.cluster import KMeans
from tqdm import tqdm

"""
File uses k-means clustering to generate anchor boxes
Anchor boxes are used as references for algorithm to build off in some versions of yolo
YOLOv8 no longer uses anchor boxes
"""

# given path to dataset, get_boxes will compile all bounding box coordinates into an array
def get_boxes(label_file_path):
    bounding_box_list = []

    files = [f for f in os.listdir(label_file_path) if os.path.isfile(os.path.join(label_file_path, f))]

    progress = tqdm(total=len(files), desc="Parsing")

    for file_name in files:
        file_path = os.path.join(label_file_path, file_name)

        with open(file_path, 'r') as file:

            lines = file.readlines()

            for line in lines:
                values = line.strip().split()
                width = float(values[3])
                height = float(values[4])
                bounding_box_list.append([width, height])
        progress.update(1)
    bounding_box_array = np.array(bounding_box_list)
    return bounding_box_array

# path to dataset
label_path = '../../../desktop/WAID/WAID-main/WAID-main/WAID/labels/train'
bounding_boxes = get_boxes(label_file_path=label_path)

# perform k-means on total coordinate array
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(bounding_boxes)

anchor_boxes = kmeans.cluster_centers_
scale_1_boxes = anchor_boxes / 20
scale_2_boxes = anchor_boxes / 40
scale_3_boxes = anchor_boxes / 80
print(f'Anchor Boxes: {anchor_boxes} Scale_20: {scale_1_boxes} Scale 40: {scale_2_boxes} Scale 80: {scale_3_boxes}')
