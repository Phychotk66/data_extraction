import cv2
import numpy as np

def detect_anchors(image):
    img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_GRAYSCALE)
    anchors = [(100, 100), (200, 200), (300, 300)]
    return anchors