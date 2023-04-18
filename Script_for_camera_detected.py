from imageai.Detection import ObjectDetection
import os
import cv2
import time
from datetime import datetime
import asyncio

base_path = r'Z:\IT_files\PycharmProjects\Web_camera'

study_path = os.path.join(base_path, 'File_for_study')
object_path = os.path.join(base_path, 'Object_detected')

camera = cv2.VideoCapture(0)

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(study_path, "yolov3.pt"))
custom = detector.CustomObjects(person=True)
detector.loadModel()


async def camera_on_detected():
    finish = 0
    while True:
        name_file = datetime.now().strftime('%H-%M-%S_%m.%d.%Y')
        _, frame = camera.read()
        start = time.time()
        if start - finish > 1:
            detections = detector.detectObjectsFromImage(
                custom_objects=custom,
                input_image=frame,
                output_image_path=os.path.join(object_path, f"{name_file}.jpg"),
                extract_detected_objects=True,
                minimum_percentage_probability=85)
            finish = time.time()
            print(detections)
            await asyncio.sleep(1)

    cv2.destroyAllWindows()
