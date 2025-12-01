import cv2
import numpy as np

slika_bgr = cv2.imread("primjer_1.png")
slika_mono = cv2.cvtColor(slika_bgr, cv2.COLOR_BGR2GRAY)

kernels = {
    3: cv2.getStructuringElement(cv2.MORPH_RECT, (3,3)),
    5: cv2.getStructuringElement(cv2.MORPH_RECT, (5,5)),
    7: cv2.getStructuringElement(cv2.MORPH_RECT, (7,7)),
    9: cv2.getStructuringElement(cv2.MORPH_RECT, (9,9)),
    "3x5": cv2.getStructuringElement(cv2.MORPH_RECT, (3,5)),
}

erode_1_iteracija = cv2.erode(slika_mono, kernels[3], iterations = 1)
erode_2_iteracija = cv2.erode(slika_mono, kernels[3], iterations = 2)

cv2.imshow("Slika original", slika_mono)
cv2.imshow("Slika erode 1 iteracija", erode_1_iteracija)
cv2.imshow("Slika erode 2 iteracija", erode_2_iteracija)
cv2.waitKey(0)
cv2.destroyAllWindows()

erode_3 = cv2.erode(slika_mono, kernels[3], iterations = 1)
erode_5 = cv2.erode(slika_mono, kernels[5], iterations = 1)
erode_7 = cv2.erode(slika_mono, kernels[7], iterations = 1)
erode_9 = cv2.erode(slika_mono, kernels[9], iterations = 1)
erode_3x5 = cv2.erode(slika_mono, kernels["3x5"], iterations = 1)

kombinirana_slika_okomito = np.concatenate((slika_mono, erode_1_iteracija, erode_2_iteracija, erode_3, erode_5, erode_7,erode_9, erode_3x5), axis = 0)

#cv2.imshow("Slika erode kernel 3", erode_3)
#cv2.imshow("Slika erode kernel 5", erode_5)
#cv2.imshow("Slika erode kernel 7", erode_7)
#cv2.imshow("Slika erode kernel 9", erode_9)
cv2.imshow("Slika", kombinirana_slika_okomito)
cv2.waitKey(0)
cv2.destroyAllWindows()