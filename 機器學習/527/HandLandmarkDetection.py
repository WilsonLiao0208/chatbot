import mediapipe as mp
import cv2 as cv
from mediapipe.tasks.python import vision, BaseOptions

model_path = 'models/hand_landmarker.task'
    
def draw_landmarks(img, result):
    h, w = img.shape[:2]
    print(len(result.hand_landmarks))
    if result.hand_landmarks:
        for hand in result.hand_landmarks:
            def draw_connected_points(point_list):
                for i in range(len(point_list)-1):
                    a = hand[point_list[i]]
                    b = hand[point_list[i+1]]
                    cv.line(img, (int(a.x*w), int(a.y*h)), (int(b.x*w), int(b.y*h)), (0,255,0), 2, 4)
                
            draw_connected_points([0,1,2,3,4])
            draw_connected_points([5,6,7,8])
            draw_connected_points([9,10,11,12])
            draw_connected_points([13,14,15,16])
            draw_connected_points([17,18,19,20])
            draw_connected_points([0,5,9,13,17,0])
            for landmark in hand:
                x = int(landmark.x*w)
                y = int(landmark.y*h)
                cv.circle(img, (x, y), 3, (0, 0, 255), -1, cv.LINE_4)
    return img

base_options =  BaseOptions(model_asset_path=model_path)   
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.IMAGE,
    num_hands=2,
    min_hand_detection_confidence=0.2 
    )

landmarker = vision.HandLandmarker.create_from_options(options)

cap = cv.VideoCapture(0) # 打開連接電腦的攝影機

while 1:
    flag, frame = cap.read() # 從攝影機抓取畫面
    if flag:
        img_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB) #將影像從 BGR 轉換成 RGB
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb) #將影像轉換成 mediapipe 格式
        result = landmarker.detect(mp_image) #偵測手部特徵點
        frame = draw_landmarks(frame, result) #將偵測結果畫在影像上
        cv.imshow('camera', frame) #秀出偵測結果
        key = cv.waitKey(100)
        if key == ord('q'):
            # 按 'q' 結束程式
            break

cv.destroyAllWindows()
cap.release()

    