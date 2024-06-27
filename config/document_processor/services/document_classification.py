import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('path/to/your/classification_model.h5')

def classify_document(image):
    img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (224, 224))
    img = img.reshape(1, 224, 224, 1)
    prediction = model.predict(img)
    document_types = ['2A', '2B', '3']
    return document_types[np.argmax(prediction)]