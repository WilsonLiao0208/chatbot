from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # 會自動下載模型
results = model("https://ultralytics.com/images/bus.jpg")

results[0].show()