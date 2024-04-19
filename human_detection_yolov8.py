# -*- coding: utf-8 -*-
#human_detection yolov8.ipynb


#install ultralytics for yolo v8
pip install ultralytics

#import pretrained model and tran it with custom dataset
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.train(data = "Path/data.yaml", epochs = 50)
