# from flask import Flask, render_template
# from flask_cors import CORS
# import cv2
# import mediapipe as mp
# from ultralytics import YOLO
# import time
# from datetime import datetime

# # local 3312로 이동
# app = Flask(__name__)
# CORS(app)  

# # 모델 저장
# model = YOLO("C:/Users/smhrd/Desktop/final_project_data/second_try.pt")


# # 각 모델에 대한 레코딩 여부를 저장하는 변수
# record_model1 = False
# record_model2 = False
# record_model3 = False
# record_model4 = False

# # 각 모델의 레코딩 시작 시간을 저장하는 변수
# record_start_time_model1 = 0
# record_start_time_model2 = 0
# record_start_time_model3 = 0
# record_start_time_model4 = 0

# # 각 모델의 레코딩 번호
# cnt_rec_model1 = 1
# cnt_rec_model2 = 1
# cnt_rec_model3 = 1
# cnt_rec_model4 = 1

# # 영상 프레임 
# fps = 30

# # 영상 넓이
# w = 640  

# # 영상 높이
# h = 480  
# codec = cv2.VideoWriter_fourcc(*'DIVX')

# # 영상 저장 시간 몇초로 끊을지(10초)
# record_duration = 10


# def gen_model1():
#     global record_model1, record_duration, cnt_rec_model1
#     # 비디오 웹캠으로 실행시킬꺼야 
#     cap = cv2.VideoCapture(0) 

#     while True:
#         ret, frame = cap.read()

#         if not ret:
#             print("Camera error")
#             break

#         results = model.predict(frame, show=False, conf=0.5)
#         key = cv2.waitKey(33)
#         cigarette_detected = any(result.names[int(box.cls[0])] == "smoking" for result in results for box in result.boxes)

#         if cigarette_detected and record_model1:
#             print("Cigarette detected!")

#             # 프레임 단위로 이미지 저장
#             image_filename = f'C:/Users/smhrd/Desktop/deeplearning/image_save/frame_{formatted_filename}.jpg'
#             cv2.imwrite(image_filename, frame)

#             if not record_model1:
#                 record_model1 = True
#                 record_start_time_model1 = time.time()
#                 print(f"Start recording_{cnt_rec}th")
#                 out = cv2.VideoWriter(f'C:/Users/smhrd/Desktop/deeplearning/video_save/record_file_{formatted_filename}_{cnt_rec}.avi', codec, fps, (w, h))
#                 cnt_rec += 1

#         if record_model1:
#             out_model1.write(frame)

#         for result in results:
#             boxes = result.boxes.cpu().numpy()
#             for box in boxes:
#                 label = result.names[int(box.cls[0])]
#                 confidence = box.conf.tolist()
#                 (x, y, w, h) = (int(box.xyxy[0][0]), int(box.xyxy[0][1]), int(box.xyxy[0][2] - box.xyxy[0][0]), int(box.xyxy[0][3] - box.xyxy[0][1]))
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                 # 가정: label과 confidence가 리스트로 반환됨
#                 label = label[0] if isinstance(label, list) else label
#                 confidence = confidence[0] if isinstance(confidence, list) else confidence

#                 cv2.putText(frame, f'{label} {confidence:.2f}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#         ret, jpeg = cv2.imencode('.jpg', frame)
#         frame_bytes = jpeg.tobytes()       

#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')
    
# @app.route('/')
# def index():
#     return render_template('streaming.html')

# out_model1 = None

# def initialize_model1():
#     # Your initialization logic for model1 goes here
#     pass

# @app.route('/toggleModel1')
# def toggle_model1():
#     global out_model1

#     # Define 'condition' before using it
#     condition = True  # Replace this with your actual condition

#     if condition:
#         out_model1 = initialize_model1()

#     # Check if out_model1 is not None before using it
#     if out_model1 is not None:
#         out_model1.release()

#     return "Model1 toggled"


# if __name__ == '__main__':
#     app.run(debug=True, port=5000)       