import cv2
import numpy as np

slika = cv2.imread("primjer_2.png")
slika_mono = cv2.cvtColor(slika, cv2.COLOR_BGR2GRAY)

kernels = {}

for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        kernels["%sx%s" % (i, j)] = cv2.getStructuringElement(cv2.MORPH_RECT, (i, j))

iteracije_open = [
    slika_mono,
]

iteracije_close = [
    slika_mono,
]

for key in kernels:
    iteracije_open.append(cv2.morphologyEx(slika_mono, cv2.MORPH_OPEN, kernels[key], iterations = 1))

for key in kernels:
    iteracije_close.append(cv2.morphologyEx(slika_mono, cv2.MORPH_CLOSE, kernels[key], iterations = 1))

kombinirana_slika_open = np.concatenate(np.array(iteracije_open), axis = 0)
kombinirana_close = np.concatenate(np.array(iteracije_close), axis = 0)
cv2.imshow("Iteracija - Open", kombinirana_slika_open)
cv2.imshow("Iteracija - Close", kombinirana_close)
cv2.waitKey(0)
cv2.destroyAllWindows()

iteracije_open = [
    slika_mono,
]

iteracije_open.append(cv2.morphologyEx(slika_mono, cv2.MORPH_OPEN, kernels["1x9"], iterations = 1))
iteracije_open.append(cv2.morphologyEx(slika_mono, cv2.MORPH_OPEN, kernels["1x9"], iterations = 2))
kombinirana_slika_open = np.concatenate(np.array(iteracije_open), axis = 0)
cv2.imshow("Iteracija - Open", kombinirana_slika_open)
cv2.waitKey(0)
cv2.destroyAllWindows()
