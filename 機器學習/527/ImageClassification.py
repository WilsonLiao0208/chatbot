
import mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions


model_path = 'models/efficientnet_lite2.tflite' # 模型檔案位置
image_path = 'data/bird.jpg' # 要辨識的影像位置

base_options = BaseOptions(model_asset_path=model_path)
options = vision.ImageClassifierOptions(
    base_options=base_options,
    max_results=5
    )

classifier = vision.ImageClassifier.create_from_options(options)

# Load the input image from an image file.
mp_image = mp.Image.create_from_file(image_path)
    
classification_result = classifier.classify(mp_image)
top_category = classification_result.classifications[0].categories[0]
print()
print(top_category.category_name)
    

    
