import cv2
from time import sleep

# Adjustable parameters
threshold_center=20; # Image centering sensitivity

# Camera
video_capture = cv2.VideoCapture(1) # in case of error, try (1)

# Classifier
cascPath = "lbpcascade_frontalface_default.xml" # haarcascade_frontalface_default.xml
faceCascade = cv2.CascadeClassifier(cascPath)

sleep(2)

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame

    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
