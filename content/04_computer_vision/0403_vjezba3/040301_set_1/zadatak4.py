import cv2

slika_bgr = cv2.imread("primjer_3.png")
slika_yuv = cv2.cvtColor(slika_bgr, cv2.COLOR_BGR2YUV)

ujednacena_yuv_slika = slika_yuv
ujednacena_yuv_slika[:,:,0] = cv2.equalizeHist(slika_yuv[:,:,0])

slika_bgr_2 = cv2.cvtColor(ujednacena_yuv_slika, cv2.COLOR_YUV2BGR)
cv2.imshow("Slika Original", slika_bgr)
cv2.imshow("Slika 2", slika_bgr_2)
cv2.waitKey(0)
cv2.destroyAllWindows()