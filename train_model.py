import numpy as np
import cv2
from utils.preprocess import preprocess_image
from utils.database import collection
from utils.cnn_model import build_model



x=[]
y=[]

persons = collection.find()

for person in persons:
    label = person['label']

    for img_binary in person['images']:
        img = preprocess_image(img_binary)
        x.append(img)
        y.append(label)

x = np.array(x)
y = np.array(y)

num_classes = len(np.unique(y))
model = build_model(num_classes)

model.fit(x, y, epochs=10, batch_size=32)

model.save("model/face_model.h5")
print("Model trained successfully.")