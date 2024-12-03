from ultralytics import YOLO
import cv2 as cv
import os
import sys
import argparse
import shutil

parser = argparse.ArgumentParser(description = 'auto fill')
parser.add_argument('--YOLO_MODULE', type=str, required=True, help = 'Trained module')
args = parser.parse_args()

# This is my path
path = "original"

# to store files in a list
list = []

# dirs=directories
for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.png' in f:
            print("Processing " + f)
            image_absolute_path = "original/" + f
            image_copy_path = "png/" + f
            # Load the YOLOv8 model#
            model = YOLO(args.YOLO_MODULE)  # 4080
            image = cv.imread(image_absolute_path, 1)
            results = model.predict(image_absolute_path, imgsz=640, show=False)
            shape = image.shape
            filename = "label/" + f.replace('png', 'txt')  # 将path里的json替换成txt,生成txt里相对应的文件路径
            w = shape[1]
            h = shape[0]
            fh = open(filename, 'w', encoding='utf-8')
            all_line = ''
            results[0].plot()
            for result in results:
                for r in result.boxes.data.tolist():
                    x1, y1, x2, y2, score, class_id = r
                    x1, x2 = x1 / w, x2 / w
                    y1, y2 = y1 / h, y2 / h
                    cx = (x1 + x2) / 2
                    cy = (y1 + y2) / 2
                    wi = abs(x2 - x1)
                    hi = abs(y2 - y1)
                    line = "%d %.4f %.4f %.4f %.4f\n" % (class_id, cx, cy, wi, hi)  # 生成txt文件里每行的内容
                    all_line += line
            fh.write(all_line)
            shutil.copyfile(image_absolute_path, image_copy_path)

