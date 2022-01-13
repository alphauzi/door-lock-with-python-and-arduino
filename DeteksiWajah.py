import cv2

cam = cv2.VideoCapture(2)
cam.set(3, 640)                                                            #kode 3 untuk lebar
cam.set(4, 480)                                                            #kode 4 untuk tinggi

faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    retV, frame = cam.read()
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(abuAbu, 1.3, 5)                   #frame, scale factor, minNeighbours
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow('test webcam',frame)
    # cv2.imshow('test webcam2', abuAbu)
    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()