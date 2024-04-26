import os
import csv


def create_csv(image_dir, text_dir, csv_name):
    image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]

    with open(csv_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        for image_file in image_files:
            text_file = image_file.replace('.jpg', '.txt')

            if os.path.exists(os.path.join(text_dir, text_file)):
                csv_writer.writerow([image_file, text_file])


image_file_path = '../../../desktop/WAID/WAID-main/WAID-main/WAID/images/test'
label_file_path = '../../../desktop/WAID/WAID-main/WAID-main/WAID/labels/test'
output_csv = 'test.csv'

create_csv(image_dir=image_file_path, text_dir=label_file_path, csv_name=output_csv)
