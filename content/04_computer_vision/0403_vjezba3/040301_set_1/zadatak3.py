import cv2
import matplotlib.pyplot as plt

slika_bgr = cv2.imread("primjer_3.png")
slika_mono = cv2.cvtColor(slika_bgr, cv2.COLOR_BGR2GRAY)

slika_ujednacena = cv2.equalizeHist(slika_mono)

histogram_ujednacena = cv2.calcHist([slika_ujednacena], [0], None, [256], [0, 256])

clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(7, 7))
slika_adaptivna = clahe.apply(slika_mono)

histogram_adaptivan = cv2.calcHist([slika_adaptivna], [0], None, [256], [0, 256])

plt.title("Histogram ujednacena i adaptivna")
plt.plot(histogram_ujednacena, color="red")
plt.plot(histogram_adaptivan, color="blue")
plt.show()

cv2.imshow("Slika ujednačena", slika_ujednacena)
cv2.imshow("Slika adaptivna", slika_adaptivna)
cv2.waitKey(0)
cv2.destroyAllWindows()