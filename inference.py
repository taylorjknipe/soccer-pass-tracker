from ultralytics import YOLO

model = YOLO('yolo11x')

results = model.predict('test-input/08fd33_4.mp4',save=True)
print(results[0])
print('=================================')
for box in results[0].boxes:
    print(box)
