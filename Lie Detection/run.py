import cv2 

eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture('eyeBlinkVid.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Video doesn't work")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 5)



    cv2.imshow('frame', gray)

    if cv2.waitKey(1) == ord('q'):
       break

cap.release()
cv2.destroyAllWindows()