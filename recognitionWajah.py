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

import cv2
from controller import doorAutomate

cam = cv2.VideoCapture(2)                                                       # menyalakan kamera
cam.set(3, 640)                                                                 # kode '3' untuk lebar
cam.set(4, 480)                                                                 # kode '4' untuk tinggi

faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')     # memuat file Face Haar Cascade
faceRecognition = cv2.face.LBPHFaceRecognizer_create()                          # pengenalan wajah

faceRecognition.read('trainWajah/training.xml')                                 # membaca database
font = cv2.FONT_HERSHEY_SIMPLEX                                                 # jenis font yang digunakan

id = 0
names = ['', 'yusron']

minWidth = 0.1*cam.get(3)
minHeight = 0.1*cam.get(4)

while True:
    retV, frame = cam.read()                                                    # mengambil gambar tiap frame
    frame = cv2.flip(frame, 1)                                                  # membalik sesuai sumbu y
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                            # merubah gambar frame menjadi abu-abu
    faces = faceDetector.detectMultiScale(abuAbu, 1.3, 5,)                      # mendeteksi wajah pada gambar (frame, scale factor, minNeighbours)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)           # memberi batas gambar di sekitar wajah
        id, confidence = faceRecognition.predict(abuAbu[y:y+h, x:x+w])
        if confidence <= 60:
            doorAutomate(0)
            nameID = names[id]
            confidenceTxt = "{0}%".format(round(100-confidence))
            doorAutomate(1)

        else:
            doorAutomate(1)
            nameID = names[0]
            confidenceTxt = "{0}%".format(round(100 - confidence))
        cv2.putText(frame,str(nameID), (x+5,y-5), font, 1, (255,255,255), 1)    # memberi teks nama
        cv2.putText(frame, str(confidenceTxt), (x + 5, y+h - 5), font, 1, (255, 255, 0), 1) # memberi teks tingkat akurasi

    cv2.imshow('recognition',frame)                                             # menampilkan gambar
    k = cv2.waitKey(1) & 0xff                                                   # menunggu tombol keyboard yang ditekan
    if k == ord('q'):                                                           # tombol keyboard 'q'
        break

print("EXIT")
cam.release()
cv2.destroyAllWindows()                                                         # Keluar jendela