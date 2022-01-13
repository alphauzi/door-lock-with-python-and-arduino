import cv2
from controller import doorAutomate

cam = cv2.VideoCapture(2)
cam.set(3, 640)                                                            #kode 3 untuk lebar
cam.set(4, 480)                                                            #kode 4 untuk tinggi
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceRecognition = cv2.face.LBPHFaceRecognizer_create()

faceRecognition.read('trainWajah/training.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0
names = ['Tidak diketahui', 'yusron']

minWidth = 0.1*cam.get(3)
minHeight = 0.1*cam.get(4)

while True:
    retV, frame = cam.read()
    frame = cv2.flip(frame, 1)
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(abuAbu, 1.3, 5,)                   #frame, scale factor, mean neighbours
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
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
        cv2.putText(frame,str(nameID), (x+5,y-5), font, 1, (255,255,255), 1)
        cv2.putText(frame, str(confidenceTxt), (x + 5, y+h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('recognition',frame)
    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        break

print("EXIT")
cam.release()
cv2.destroyAllWindows()