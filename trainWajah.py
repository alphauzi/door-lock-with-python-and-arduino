import cv2, os, numpy as np
from PIL import Image

names = []
paths = []

for users in os.listdir("dataWajah"):
    names.append(users)

for name in names:
    for image in os.listdir("dataWajah/{}/".format(name)):
        path_string = os.path.join("dataWajah/{}/".format(name),image)
        paths.append(path_string)

faces = []
ids = []

for img_path in paths:
    image = Image.open(img_path).convert('L')
    imgNp = np.array(image, "uint8")
    faces.append(imgNp)
    id = int(img_path.split("/")[2].split(".")[0])
    ids.append(id)

ids = np.array(ids)
trainer = cv2.face.LBPHFaceRecognizer_create()
trainer.train(faces, ids)
trainer.write("trainWajah"+'/training.xml')