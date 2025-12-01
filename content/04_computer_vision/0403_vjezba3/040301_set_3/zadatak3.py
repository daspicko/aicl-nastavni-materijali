import cv2
import numpy as np

slika_bgr = cv2.imread("primjer_2.jpg")
slika_mono = cv2.cvtColor(slika_bgr, cv2.COLOR_BGR2GRAY)
cany = cv2.Canny(slika_mono, 50, 50, apertureSize=3)

def udaljenost(prva, druga):
    return np.sqrt((prva[0] - druga[0]) ** 2 + (prva[1] - druga[1]) ** 2)

A = (288, 729)
B = (36, 395)
C = (462, 162)
D = (729, 377)

w = max(int(udaljenost(A, B)), int(udaljenost(C, D)))
h = max(int(udaljenost(A, D)), int(udaljenost(B, C)))
print(w, h)

A_ = (0, 0)
B_ = (w - 1, 0)
C_ = (w - 1, h - 1)
D_ = (0, h - 1)

M = cv2.getPerspectiveTransform(np.float32([A, B, C, D]), np.float32([A_, B_, C_, D_]))
slika_tra = cv2.warpPerspective(slika_bgr, M, (w, h), flags=cv2.INTER_LINEAR)
cv2.imshow("slika", slika_bgr)
cv2.imshow("Rubovi", slika_tra)
cv2.waitKey(0)
cv2.destroyAllWindows()