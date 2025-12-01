import cv2

slika_mono = cv2.imread('kamera3.jpg', cv2.IMREAD_GRAYSCALE)
visina, sirina = slika_mono.shape
print('Visina:', visina)
print('Širina:', sirina)

cv2.imshow('Kamera 3 - Nijanse sive', slika_mono)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('kamera3_nijanse_sive.jpg', slika_mono)