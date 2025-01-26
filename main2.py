#     # from ultralytics import YOLO
#     # import cv2

#     # model = YOLO("C:/Users/sigin/DEMO/python/HACKATHON(2024)/yolov8n.pt")
#     # results = model( "C:/Users/sigin/DEMO/python/HACKATHON(2024)/data/images/train/0tVivKVWy9s7Zp3vR7LN1syiMBfAoR375.jpg" ,show = True)
#     # cv2.waitKey(0 )
# import cv2
# from ultralytics import YOLO
# import math
# from datetime import datetime, timedelta

# def doggo(file, provided):
#     current_time = datetime.now()
#     start_time = current_time

#     def calculate_displacement(point1, point2):
#         print("IN. . . . ")
#         return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

#     def is_displaced(box1, box2, margin_threshold=10):
#         center1 = ((box1[0] + box1[2]) / 2, (box1[1] + box1[3]) / 2)
#         center2 = ((box2[0] + box2[2]) / 2, (box2[1] + box2[3]) / 2)
#         displacement = calculate_displacement(center1, center2)
#         return displacement > margin_threshold

#     cap = cv2.VideoCapture(file)
#     cap.set(3, 640)
#     cap.set(4, 488)
#     model = YOLO("yolov8n.pt")
#     class_names = [
#         "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light",
#         "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow",
#         "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee",
#         "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
#         "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
#         "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch",
#         "potted plant", "bed", "dining table", "toilet", "TV", "laptop", "mouse", "remote", "keyboard", "cell phone",
#         "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear",
#         "hair drier", "toothbrush"
#     ]

#     prev_x1, prev_y1, prev_x2, prev_y2 = 0, 0, 0, 0
#     ya = 1
#     moved = 0
#     present = 1
#     while ya != 0:
#         current_time = datetime.now()
#         success, img = cap.read()
#         result = model(img, stream=True)
#         for r in result:
#             boxes = r.boxes
#             for box in boxes:
#                 x1, y1, x2, y2 = box.xyxy[0]
#                 x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#                 cls = box.cls[0]
#                 if int(cls) == 16 and (int((current_time - start_time).total_seconds())) == provided:
#                     cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
#                     print(int((current_time - start_time).total_seconds()))
#                     if is_displaced([x1, y1, x2, y2], [prev_x1, prev_y1, prev_x2, prev_y2]):
#                         print("The bounding box is displaced by a few margins!")
#                         moved = 1
#                     ya = 0
#                     prev_x1, prev_y1, prev_x2, prev_y2 = x1, y1, x2, y2
#                 if int((current_time - start_time).total_seconds()) > provided:
#                     present = 0
#                     ya = 0

#         cv2.imshow('Image', img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             return 

#     cap.release()
#     cv2.destroyAllWindows()
#     return [present, moved]

# doggo("/home/Suchitra/Desktop/code./hack/videoplayback.mp4", 10)


import cv2
from ultralytics import YOLO
import math
from datetime import datetime, timedelta

def doggo(file, provided):
    def calculate_displacement(point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def is_displaced(box1, box2, margin_threshold=10):
        center1 = ((box1[0] + box1[2]) / 2, (box1[1] + box1[3]) / 2)
        center2 = ((box2[0] + box2[2]) / 2, (box2[1] + box2[3]) / 2)
        displacement = calculate_displacement(center1, center2)
        return displacement > margin_threshold

    # Initialize YOLO model
    model = YOLO("yolov8n.pt")
    class_names = [
        "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light",
        "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow",
        "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee",
        "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
        "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
        "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch",
        "potted plant", "bed", "dining table", "toilet", "TV", "laptop", "mouse", "remote", "keyboard", "cell phone",
        "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear",
        "hair drier", "toothbrush"
    ]

    # Open video file
    cap = cv2.VideoCapture(file)
    if not cap.isOpened():
        print(f"Error: Cannot open video file {file}")
        return [0, 0]

    cap.set(3, 640)  # Set width
    cap.set(4, 488)  # Set height

    prev_box = [0, 0, 0, 0]
    start_time = datetime.now()
    moved = 0
    present = 1

    while True:
        success, img = cap.read()
        if not success:
            print("Error: Unable to read frame from video.")
            break

        current_time = datetime.now()
        elapsed_time = (current_time - start_time).total_seconds()

        result = model(img, stream=True)
        for r in result:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cls = int(box.cls[0])

                if class_names[cls] == "dog" and int(elapsed_time) == provided:
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                    print(f"Elapsed Time: {int(elapsed_time)} seconds")
                    
                    if is_displaced([x1, y1, x2, y2], prev_box):
                        print("The bounding box is displaced by a few margins!")
                        moved = 1

                    prev_box = [x1, y1, x2, y2]

        if elapsed_time > provided:
            present = 0
            break

        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return [present, moved]


# Call the function
result = doggo("/home/Suchitra/Desktop/code./hack/videoplayback.mp4", 10)
print(f"Result: {result}")

