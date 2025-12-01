import cv2
import numpy as np

slika = cv2.imread('kovanice.png')
grayscale_slika = cv2.cvtColor(slika, cv2.COLOR_BGR2GRAY)
grayscale_slika_blurred = cv2.medianBlur(grayscale_slika, 5)
circles = cv2.HoughCircles(grayscale_slika_blurred,
                           cv2.HOUGH_GRADIENT,  # jedina dostupna
                           dp=1,  # The inverse ratio of the accumulator resolution to the image resolution. For example, if dp=1, the accumulator has the same resolution as the input image. If dp=2, the accumulator has half the resolution of the input image.
                           minDist=20,  # Minimum distance between the centers of the detected circles. This parameter controls how close circles can be to each other.
                           param1=100,  #  The higher threshold for the Canny edge detector (the lower one is param1 divided by 2). This is used in the edge detection process.
                           param2=70,  #  The accumulator threshold for the circle centers at the detection stage. The smaller it is, the more false circles may be detected. Conversely, a larger value will result in fewer detections but with higher accuracy.
                           minRadius=15,
                           maxRadius=100)
circles = np.uint16(np.around(circles))

for circle in circles.squeeze():
    cv2.circle(slika, (circle[0], circle[1]), circle[2], (0, 255, 0), thickness=3)

cv2.imshow("circles", slika)
cv2.imshow("circles blurred", grayscale_slika_blurred)
cv2.waitKey()
cv2.destroyAllWindows()
