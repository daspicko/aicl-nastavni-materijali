import cv2
import matplotlib.pyplot as plt

slika_mono = cv2.imread("primjer_2.jpg", cv2.IMREAD_GRAYSCALE)

histogram_mono = cv2.calcHist([slika_mono], [0], None, [256], [0, 256])
slika_ujednacena = cv2.equalizeHist(slika_mono)

ujednacen_histogram = cv2.calcHist([slika_ujednacena], [0], None, [256], [0, 256])

plt.plot(histogram_mono, color="red")
plt.plot(ujednacen_histogram, color="blue")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.title("Originalan i ujednačen histogram")
plt.show()

cv2.imshow("Original", slika_mono)
cv2.imshow("Ujednačen histogram", slika_ujednacena)
cv2.waitKey(0)
cv2.destroyAllWindows()
