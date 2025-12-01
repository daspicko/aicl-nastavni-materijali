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

open_1_iteracija = cv2.morphologyEx(slika_mono, cv2.MORPH_OPEN, kernels[3], iterations = 1)
open_2_iteracija = cv2.morphologyEx(slika_mono, cv2.MORPH_OPEN, kernels[3], iterations = 2)

close_1_iteracija = cv2.morphologyEx(slika_mono, cv2.MORPH_CLOSE, kernels[3], iterations = 1)
close_2_iteracija = cv2.morphologyEx(slika_mono, cv2.MORPH_CLOSE, kernels[3], iterations = 2)

kombinirana_slika_open = np.concatenate((slika_mono, open_1_iteracija, open_2_iteracija), axis = 0)
kombinirana_slika_close = np.concatenate((slika_mono, close_1_iteracija, close_2_iteracija), axis = 0)
cv2.imshow("1 i 2 iteracija - Open", kombinirana_slika_open)
cv2.imshow("1 i 2 iteracija - Close", kombinirana_slika_close)
cv2.waitKey(0)
cv2.destroyAllWindows()

open_3 = cv2.morphologyEx(slika_mono, cv2.MORPH_OPEN, kernels[3], iterations = 1)
open_5 = cv2.morphologyEx(slika_mono, cv2.MORPH_OPEN, kernels[5], iterations = 1)
open_7 = cv2.morphologyEx(slika_mono, cv2.MORPH_OPEN, kernels[7], iterations = 1)
open__9 = cv2.morphologyEx(slika_mono, cv2.MORPH_OPEN, kernels[9], iterations = 1)
open_3x5 = cv2.morphologyEx(slika_mono, cv2.MORPH_OPEN, kernels["3x5"], iterations = 1)

close_3 = cv2.morphologyEx(slika_mono, cv2.MORPH_CLOSE, kernels[3], iterations = 1)
close_5 = cv2.morphologyEx(slika_mono, cv2.MORPH_CLOSE, kernels[5], iterations = 1)
close_7 = cv2.morphologyEx(slika_mono, cv2.MORPH_CLOSE, kernels[7], iterations = 1)
close_9 = cv2.morphologyEx(slika_mono, cv2.MORPH_CLOSE, kernels[9], iterations = 1)
close_3x5 = cv2.morphologyEx(slika_mono, cv2.MORPH_CLOSE, kernels["3x5"], iterations = 1)

kombinirana_slika_open = np.concatenate((slika_mono, open_3, open_5, open_7, open__9, open_3x5), axis = 0)
kombinirana_slika_close = np.concatenate((slika_mono, close_3, close_5, close_7, close_9, close_3x5), axis = 0)
cv2.imshow("Slika open", kombinirana_slika_open)
cv2.imshow("Slika close", kombinirana_slika_close)
cv2.waitKey(0)
cv2.destroyAllWindows()
