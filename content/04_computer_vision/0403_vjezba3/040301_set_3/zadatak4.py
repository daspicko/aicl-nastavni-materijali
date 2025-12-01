import cv2
import numpy as np

soba_bgr = cv2.imread("soba.png")
logo_bgr = cv2.imread("logo.png")

cv2.imshow("Soba", soba_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

def udaljenost(prva, druga):
    return np.sqrt((prva[0] - druga[0]) ** 2 + (prva[1] - druga[1]) ** 2)

P1 = (0, 271)
P2 = (239, 333)
P3 = (0, 707)
P4 = (239, 670)

w = max(int(udaljenost(P1, P2)), int(udaljenost(P3, P4)))
h = max(int(udaljenost(P1, P3)), int(udaljenost(P2, P4)))
print(w, h)
print(logo_bgr.shape)
logo_bgr_resized = cv2.resize(logo_bgr, (w, h))
print(logo_bgr_resized.shape)

L1 = (0, 0)
L2 = (logo_bgr_resized.shape[1] - 1, 0)
L3 = (0, logo_bgr_resized.shape[0] - 1)
L4 = (logo_bgr_resized.shape[1] - 1, logo_bgr_resized.shape[0] - 1)

M = cv2.getPerspectiveTransform( np.float32([L1, L2, L3, L4]), np.float32([P1, P2, P3, P4]))
logo_tra = cv2.warpPerspective(logo_bgr_resized, M, (w, h), flags=cv2.INTER_LINEAR)

cv2.imshow("logo", logo_tra)
cv2.waitKey(0)
cv2.destroyAllWindows()
