import cv2
import numpy as np

from utils import nacrtaj_liniju

slika_bgr = cv2.imread("autocesta.jpeg")
slika_grey = cv2.cvtColor(slika_bgr, cv2.COLOR_BGR2GRAY)

slike_canny = [
    cv2.Canny(slika_grey, 25, 225),
    cv2.Canny(slika_grey, 50, 200),
    cv2.Canny(slika_grey, 75, 175),
    cv2.Canny(slika_grey, 100, 150),

    cv2.Canny(slika_grey, 150, 200),
    cv2.Canny(slika_grey, 175, 225),
]

lines = cv2.HoughLines(slika_canny, rho=1, theta=np.pi / 180, threshold=180)

if lines is not None:
    for line in lines:
        nacrtaj_liniju(slika_grey, line)
else:
    print("Nema detektiranih linija.")

kombinirana_slika = np.concatenate(np.array(iteracije_open), axis = 0)
cv2.imshow("Detektirane linije", slika_bgr)
cv2.waitKey()
cv2.destroyAllWindows()