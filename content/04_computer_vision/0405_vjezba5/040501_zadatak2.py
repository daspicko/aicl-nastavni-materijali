import cv2
import numpy as np

slika_papir_bgr = cv2.imread("papir.jpg", cv2.IMREAD_COLOR)
if slika_papir_bgr is None:
    raise SystemExit("Ne mogu učitati sliku 'papir.jpg'.")

slika_papir_bgr_copy = slika_papir_bgr.copy()
cv2.imshow("1 - original", slika_papir_bgr_copy)

slika_papir_gray = cv2.cvtColor(slika_papir_bgr, cv2.COLOR_BGR2GRAY)
cv2.imshow("2 - gray", slika_papir_gray)

blur = cv2.GaussianBlur(slika_papir_gray, (5, 5), 0)
cv2.imshow("3 - blur", blur)

_, slika_papir_gray_tresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("4 - thresh (Otsu)", slika_papir_gray_tresh)

kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(slika_papir_gray_tresh, cv2.MORPH_CLOSE, kernel_close, iterations=2)
cv2.imshow("5 - morph CLOSE", closed)

contours, hierarchy = cv2.findContours(slika_papir_gray_tresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

max_povrsina = 0
for contour in contours:
    povrsina = cv2.contourArea(contour)
    if povrsina > max_povrsina:
        max_povrsina = povrsina
        papir_cnt = contour

opseg = cv2.arcLength(papir_cnt, True)
approxPravokutnik = cv2.approxPolyDP(papir_cnt, 0.02 * opseg, True)

slika_sa_konturama = cv2.drawContours(slika_papir_bgr_copy, [approxPravokutnik], -1, (0, 255, 0), 2)
cv2.imshow("slika_sa_konturama", slika_sa_konturama)
cv2.waitKey(0)
cv2.destroyAllWindows()
try:
    print("Broj vrhova aproksimirane konture:", len(approxPravokutnik))
except NameError:
    print("TODO dio s konturama NIJE dovršen - 'approx' nije definiran.")

def order_points(pts):
    # pts shape: (4, 2)
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    diff = np.diff(pts, axis=1)

    rect[0] = pts[np.argmin(s)]      # top-left
    rect[2] = pts[np.argmax(s)]      # bottom-right
    rect[1] = pts[np.argmin(diff)]   # top-right
    rect[3] = pts[np.argmax(diff)]   # bottom-left
    return rect

if len(approxPravokutnik) == 4:
    pts = approxPravokutnik.reshape(4, 2).astype("float32")
else:
    print("Upozorenje: approx nema 4 točke – koristim boundingRect kao fallback.")
    x, y, w, h = cv2.boundingRect(papir_cnt)
    pts = np.array([
        [x, y],
        [x + w, y],
        [x + w, y + h],
        [x, y + h]
    ], dtype="float32")

rect = order_points(pts)
(tl, tr, br, bl) = rect

widthA = np.linalg.norm(br - bl)
widthB = np.linalg.norm(tr - tl)
maxWidth = int(max(widthA, widthB))

heightA = np.linalg.norm(tr - br)
heightB = np.linalg.norm(tl - bl)
maxHeight = int(max(heightA, heightB))

dst = np.array([
    [0, 0],
    [maxWidth - 1, 0],
    [maxWidth - 1, maxHeight - 1],
    [0, maxHeight - 1]
], dtype="float32")

M = cv2.getPerspectiveTransform(rect, dst)
warped = cv2.warpPerspective(slika_papir_bgr_copy, M, (maxWidth, maxHeight))
cv2.imshow("7 - ispravljeni papir (color)", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()

warp_gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
warp_blur = cv2.GaussianBlur(warp_gray, (5, 5), 0)

_, scan = cv2.threshold(
    warp_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
cv2.imshow("8 - scan (Otsu)", scan)

# invert -> slova bijela, pozadina crna
scan_inv = cv2.bitwise_not(scan)

# vertikalni CLOSING (1x3) – popunjava sitne rupe u potezima
kernel_close2 = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))
scan_inv_closed = cv2.morphologyEx(scan_inv, cv2.MORPH_CLOSE, kernel_close2, iterations=1)

# vrati natrag: slova crna, pozadina bijela
scan_clean = cv2.bitwise_not(scan_inv_closed)
cv2.imshow("9 - scan (Otsu + vert closing)", scan_clean)

thresh_bgr = cv2.cvtColor(slika_papir_gray_tresh, cv2.COLOR_GRAY2BGR)
scan_bgr = cv2.cvtColor(scan_clean, cv2.COLOR_GRAY2BGR)

scale = 0.5  # smanji da stane na ekran

def resize(img):
    return cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)

row1 = cv2.hconcat([resize(slika_papir_bgr), resize(thresh_bgr), resize(slika_papir_bgr_copy)])
row2 = cv2.hconcat([resize(warped), resize(scan_bgr)])

# poravnaj širine redova ako treba
target_width = max(row1.shape[1], row2.shape[1])

def pad_to_width(img, width):
    if img.shape[1] == width:
        return img
    pad = width - img.shape[1]
    return cv2.copyMakeBorder(img, 0, 0, 0, pad, cv2.BORDER_CONSTANT, value=(0, 0, 0))

row1 = pad_to_width(row1, target_width)
row2 = pad_to_width(row2, target_width)

concat = cv2.vconcat([row1, row2])
cv2.imshow("Svi koraci (original | Otsu | kontura | warp | scan clean)", concat)

# ---------------- 6) SPREMANJE REZULTATA ----------------

cv2.imwrite("upute_warp_color.png", warped)
cv2.imwrite("upute_scan_bw.png", scan_clean)
cv2.imwrite("upute_svi_koraci.png", concat)

cv2.waitKey(0)
cv2.destroyAllWindows()
