import cv2
import numpy as np
import matplotlib.pyplot as plt

slika_bgr = cv2.imread("primjer_1.png")
slika_mono = cv2.cvtColor(slika_bgr, cv2.COLOR_BGR2GRAY)

histogram_mono = cv2.calcHist([slika_mono], [0], None, [256], [0, 256])

plt.plot(histogram_mono)
#plt.hist(slika_mono.ravel(), bins=256)
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.title("Histogram Mono")
plt.show()

histogram_b = cv2.calcHist([slika_bgr], [0], None, [256], [0, 256])
histogram_g = cv2.calcHist([slika_bgr], [1], None, [256], [0, 256])
histogram_r = cv2.calcHist([slika_bgr], [2], None, [256], [0, 256])

plt.plot(histogram_b)
plt.plot(histogram_g)
plt.plot(histogram_r)
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.title("Histogram BGR sa apsolutnim vrijednostima")
plt.show()

plt.plot(histogram_b/np.sum(histogram_b) * 100)
plt.plot(histogram_g/np.sum(histogram_g) * 100)
plt.plot(histogram_r/np.sum(histogram_r) * 100)
plt.xlabel("Bins")
plt.ylabel("% of Pixels")
plt.title("Histogram BGR sa postotnim vrijednostima")
plt.show()
