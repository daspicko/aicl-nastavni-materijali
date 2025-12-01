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

dilate_1_iteracija = cv2.dilate(slika_mono, kernels[3], iterations = 1)
dilate_2_iteracija = cv2.dilate(slika_mono, kernels[3], iterations = 2)

kombinirana_slika_okomito = np.concatenate((slika_mono, dilate_1_iteracija, dilate_2_iteracija), axis = 0)
cv2.imshow("Slika 1 i 2 iteracija", kombinirana_slika_okomito)
cv2.waitKey(0)
cv2.destroyAllWindows()

dilate_3 = cv2.dilate(slika_mono, kernels[3], iterations = 1)
dilate_5 = cv2.dilate(slika_mono, kernels[5], iterations = 1)
dilate_7 = cv2.dilate(slika_mono, kernels[7], iterations = 1)
dilate_9 = cv2.dilate(slika_mono, kernels[9], iterations = 1)
dilate_3x5 = cv2.dilate(slika_mono, kernels["3x5"], iterations = 1)

kombinirana_slika_okomito = np.concatenate((slika_mono, dilate_1_iteracija, dilate_2_iteracija, dilate_3, dilate_5, dilate_7,dilate_9, dilate_3x5), axis = 0)

#cv2.imshow("Slika dilate kernel 3", dilate_3)
#cv2.imshow("Slika dilate kernel 5", dilate_5)
#cv2.imshow("Slika dilate kernel 7", dilate_7)
#cv2.imshow("Slika dilate kernel 9", dilate_9)
cv2.imshow("Slika", kombinirana_slika_okomito)
cv2.waitKey(0)
cv2.destroyAllWindows()