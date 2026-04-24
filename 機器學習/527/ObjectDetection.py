import numpy as np
import mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions
import cv2 as cv

model_path = 'models/efficientdet_lite2.tflite' # 模型檔案位置
image_path = 'data/street.jpg' # 要辨識的影像位置


base_options = BaseOptions(model_asset_path=model_path)
options = vision.ObjectDetectorOptions(base_options=base_options,
                                       score_threshold=0.5)
detector = vision.ObjectDetector.create_from_options(options)


image = mp.Image.create_from_file(image_path)


detection_result = detector.detect(image)
print(detection_result)



image_copy = np.copy(image.numpy_view())

def visualize(img, detection_results):
    for result in detection_results.detections:
        category = result.categories[0].category_name
        cx = result.bounding_box.origin_x
        cy = result.bounding_box.origin_y
        w = result.bounding_box.width
        h = result.bounding_box.height
        p1 = (int(cx), int(cy))
        p2 = (int(cx+w), int(cy+h))
        cv.rectangle(img, p1, p2, (255,0,0), 2, cv.LINE_4)
        cv.putText(img, category, (cx+5, cy+15), 0, 0.5, (255,0,0), 1, cv.LINE_4)
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    cv.imshow('result',img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
visualize(image_copy, detection_result)
        
