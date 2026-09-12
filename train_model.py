from utils.preprocess import preprocess_image
from utils.database import collection
from utils.cnn_model import create_cnn_model

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