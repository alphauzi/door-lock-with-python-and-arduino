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

cam = cv2.VideoCapture(2)                                                       # menyalakan kamera
cam.set(3, 640)                                                                 # kode '3' untuk lebar
cam.set(4, 480)                                                                 # kode '4' untuk tinggi

faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')     # memuat file Face Haar Cascade

while True:
    retV, frame = cam.read()                                                    # mengambil gambar tiap frame
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                            # merubah gambar frame menjadi abu-abu
    faces = faceDetector.detectMultiScale(abuAbu, 1.3, 5)                       # mendeteksi wajah pada gambar (frame, scale factor, minNeighbours)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)           # memberi batas gambar di sekitar wajah

    cv2.imshow('test webcam',frame)                                             # menampilkan gambar
    # cv2.imshow('test webcam2', abuAbu)
    k = cv2.waitKey(1) & 0xff                                                   # menunggu tombol keyboard yang ditekan
    if k == ord('q'):                                                           # tombol keybard 'q'
        break

cam.release()
cv2.destroyAllWindows()                                                         # Keluar jendela