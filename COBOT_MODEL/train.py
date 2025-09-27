# This file is part of Markerless-3D-Human-Cobot-Pose-Estimation
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Portions derived from Ultralytics YOLO, Copyright © Ultralytics Inc., AGPL-3.0.

from ultralytics import YOLO

# Carica un modello pre-addestrato
model = YOLO('yolov8n-pose.pt')  # load a pretrained model (recommended for training)
model.to('cuda')

if __name__ == '__main__':
    model.train(data='config.yaml', epochs=500, imgsz=1024, batch=8, device=0, workers=1)
