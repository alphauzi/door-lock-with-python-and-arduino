""" ====================================================================================================
Pemrogram      : Kelompok EK-3C/10
  1. 12-Merry Nilna Na'ma      NIM:3.32.19.2.13
  2. 24-Yusron Alfauzi         NIM:3.32.19.2.25
Tgl.Presentasi  : Senin, 17 Januari 2022
=======================================================================================================
ProyekArduino
C10-Door Lock System using Face Recognition
  program untuk membuka kunci otomatis berdasarkan pengenalan wajah berbasis artificial intelligence
-----------------------------------------------------------------------------------------------------"""

import cv2, os, numpy as np
from PIL import Image

names = []
paths = []

for users in os.listdir("dataWajah"):                                       # identifikasi user pada database
    names.append(users)

for name in names:                                                          # membuat dan menggabungkan path tiap gambar
    for image in os.listdir("dataWajah/{}/".format(name)):
        path_string = os.path.join("dataWajah/{}/".format(name),image)
        paths.append(path_string)

faces = []
ids = []

for img_path in paths:
    image = Image.open(img_path).convert('L')                               # konversi gambar menjadi greyscale
    imgNp = np.array(image, "uint8")                                        # merubah gambar menjadi array
    faces.append(imgNp)
    id = int(img_path.split("/")[2].split(".")[0])                          # menghapus hal yang tidak diperlukan
    ids.append(id)

ids = np.array(ids)
trainer = cv2.face.LBPHFaceRecognizer_create()                              # melatih wajah dengan  Local Binary Pattern Histogram
trainer.train(faces, ids)
trainer.write("trainWajah"+'/training.xml')                                 # menyimpan file hasil pelatihan