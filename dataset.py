import os
import numpy as np
from PIL import Image, ImageFile
import torch
import pandas as pd
from torch.utils.data import Dataset, DataLoader
"""from utils import(
    iou_width_height as iou,
    non_max_suppresion as nms,
)
"""


class WAIDDataset(Dataset):
    def __init__(
        self,
        csv_file,
        img_dir,
        label_dir,
        image_size = 640,
        S=20,
        C=6,
        transform=None,
    ):
        self.annotations = pd.read_csv(csv_file)
        self.img_dir = img_dir
        self.label_dir = label_dir
        self.transform = transform
        self.S = S
        self.C = C
        self.ignore_iou_thresh = 0.5

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, index):
        label_path = os.path.join(self.label_dir, self.annotatins.iloc[index, 1])
        bboxes = np.roll(np.loadtxt(fname=label_path, delimiter=' ', ndmin=2), 4, axis=1).tolist()
        img_path = os.path.join(self.img_dir, self.annotations.iloc[index, 0])
        image = np.array(Image.open(img_path).convert("RGB"))

        """if self.transform:
            #TODO: augmentaion"""

        output_channels = 5 + self.C
        target = torch.zeros((self.S, self.S, output_channels))

        for box in bboxes:
            x, y, w, h, class_label = box

            grid_x = int(x * self.S)
            grid_y = int(y * self.S)

            x_center = x * self.S - grid_x
            y_center = y * self.S - grid_y

            objectness_score = 1

            target[grid_y, grid_x, :] = torch.tensor([x_center, y_center, w, h, objectness_score] + [0] * self.C)
            target[grid_y, grid_x, 5 + class_label] = 1

        return image, target




