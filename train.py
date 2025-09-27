from ultralytics import YOLO

# Carica un modello pre-addestrato
model = YOLO('yolov8n-pose.pt')  # load a pretrained model (recommended for training)
model.to('cuda')

if __name__ == '__main__':
    model.train(data='config.yaml', epochs=500, imgsz=1024, batch=8, device=0, workers=1)
