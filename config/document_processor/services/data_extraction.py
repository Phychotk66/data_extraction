import cv2
import numpy as np
import pytesseract

def extract_data(image, anchors):
    img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_GRAYSCALE)
    data = {}
    for i, anchor in enumerate(anchors):
        x, y = anchor
        roi = img[y:y+50, x:x+200]  # Adjust ROI size as needed
        text = pytesseract.image_to_string(roi)
        data[f'data_point_{i}'] = text.strip()
    return data
