import cv2

slika_bgr = cv2.imread('kamera3.jpg')

slika_bgr_flipped = cv2.flip(slika_bgr, -1)

cv2.imwrite('zaokrenuta_slika.jpg', slika_bgr_flipped)
