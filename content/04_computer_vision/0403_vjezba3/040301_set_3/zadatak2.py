import cv2

slika_bgr = cv2.imread("primjer_1.png")

M = cv2.getRotationMatrix2D((slika_bgr.shape[1] / 2, slika_bgr.shape[0] / 2), -90, 0.5)
slika_rotirana = cv2.warpAffine(slika_bgr, M, (slika_bgr.shape[1], slika_bgr.shape[0]))

cv2.imshow("Originalna slika", slika_bgr)
cv2.imshow("Rotirana slika", slika_rotirana)
cv2.waitKey(0)
cv2.destroyAllWindows()
