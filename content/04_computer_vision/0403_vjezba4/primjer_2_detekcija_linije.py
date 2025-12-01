import cv2
import numpy as np

image_bgr = cv2.imread("lanes.jpeg", cv2.IMREAD_COLOR)
# 1. Ucitavanje slike u nijansama sive boje
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

# 2. Primjena Canny detektora rubova
image_canny = cv2.Canny(image_gray, 100, 200)

# 3 Primjena Houghove transformacije za detekciju linija
lines = cv2.HoughLinesP(image_canny, rho=1, theta=np.pi / 180, threshold=150, minLineLength=100, maxLineGap=100)

# 4. Crtanje detektiranih linija
if lines is not None:
	for line in lines:
		x1, y1, x2, y2 = line[0]
		cv2.line(image_bgr, (x1, y1), (x2, y2), (0, 255, 0), 2)
else:
	print("No lines were found by HoughLinesP.")

cv2.imshow("Highway lanes (detected)", image_bgr)
cv2.waitKey()
cv2.destroyAllWindows()


