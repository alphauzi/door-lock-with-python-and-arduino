import cv2
from pathlib import Path

cam = cv2.VideoCapture(2)
cam.set(3, 640)                                                            #kode 3 untuk lebar
cam.set(4, 480)                                                            #kode 4 untuk tinggi

faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print("masukkan nama dan id: ")
print("masukkan nama: ")
nama = input()
print("masukkan id: ")
faceID = input()
ambilData = 1

while True:
    retV, frame = cam.read()
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(abuAbu, 1.3, 5)                   #frame, scale factor, mean neighbours
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        Path("dataWajah/{}".format(nama)).mkdir(parents=True, exist_ok=True)
        namaFile = str(faceID)+'.'+str(ambilData)+'.jpg'
        cv2.imwrite("dataWajah/{}/".format(nama)+namaFile,frame)
        ambilData +=1

    cv2.imshow('test webcam',frame)
    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        break
    elif ambilData > 100:
        break

print(f"pengambilan data wajah {faceID} selesai")
cam.release()
cv2.destroyAllWindows()