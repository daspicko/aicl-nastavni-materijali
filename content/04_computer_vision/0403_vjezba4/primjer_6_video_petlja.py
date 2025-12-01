import cv2

#capture = cv2.VideoCapture(0) -> video s web kamere
capture = cv2.VideoCapture('autocesta_video.mp4')

if not capture.isOpened():
    print('Unable to open video')
    exit(1)

while True:
    ret, frame = capture.read()

    if frame is None:
        break

    cv2.imshow('Frame', frame)

    if cv2.waitKey(100) == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()


