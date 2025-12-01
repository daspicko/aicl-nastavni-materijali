import cv2
import numpy as np

slika_keksi_bgr = cv2.imread('keksi.jpg', cv2.IMREAD_COLOR)
slika_keksi_gray = cv2.cvtColor(slika_keksi_bgr, cv2.COLOR_BGR2GRAY)
slika_keksi_gray_blur = cv2.GaussianBlur(slika_keksi_gray, (5, 5), 0)
_, slika_keksi_gray_blur_thresh = cv2.threshold(slika_keksi_gray_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

'''
cv2.imshow("Blurana", slika_keksi_gray_blur_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
kernels = {
    '5x5': cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
}

slika_keksi_gray_blur_close = cv2.morphologyEx(slika_keksi_gray_blur_thresh, cv2.MORPH_OPEN, kernels['5x5'], iterations = 1)
'''
cv2.imshow("Close", slika_keksi_gray_blur_close)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
contours, hierarchy = cv2.findContours(slika_keksi_gray_blur_close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
'''
slika_sa_konturama = cv2.drawContours(slika_keksi_bgr, contours, -1, (0, 0, 255), 4)
cv2.imshow("Slika sa konturama", slika_sa_konturama)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

povrsine = [cv2.contourArea(x) for x in contours]
konture_velikih_povrsina = [c for (c, povrsina) in zip(contours, povrsine) if povrsina > 100]

slika_sa_velikim_konturama = cv2.drawContours(slika_keksi_bgr,konture_velikih_povrsina, -1, (0, 0, 255), 3)
cv2.imshow("Slika sa velikim konturama", slika_sa_velikim_konturama)
cv2.waitKey(0)
cv2.destroyAllWindows()

konture_ispravnih = [c for (c, povrsina) in zip(contours, povrsine) if povrsina > 0.03 * slika_keksi_gray_blur_close.shape[0] * slika_keksi_gray_blur_close.shape[1]]
konture_neispravnih = [c for (c, povrsina) in zip(contours, povrsine) if povrsina <= 0.03 * slika_keksi_gray_blur_close.shape[0] * slika_keksi_gray_blur_close.shape[1]]

slika_sa_ispravnim_konturama = cv2.drawContours(slika_keksi_bgr,konture_ispravnih, -1, (0, 255, 0), cv2.FILLED)
slika_sa_svim_konturama = cv2.drawContours(slika_sa_ispravnim_konturama,konture_neispravnih, -1, (0, 0, 255), cv2.FILLED)

#cv2.imshow("Slika sa svim konturama", cv2.addWeighted(slika_keksi_bgr, 0.2, slika_sa_svim_konturama, 0.8, 5))
cv2.imshow("Slika sa svim konturama", slika_sa_svim_konturama)
cv2.waitKey(0)
cv2.destroyAllWindows()
