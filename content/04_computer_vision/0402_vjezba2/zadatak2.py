import cv2

slika_mono = cv2.imread('kamera3.jpg', cv2.IMREAD_GRAYSCALE) # Ne zanimaju nas boje, može monokromatska
visina, sirina = slika_mono.shape
print('Visina:', visina)
print('Širina:', sirina)

uvecana_slika_mono = cv2.resize(slika_mono, dsize=(1000, 650))
visina_uvecane, sirina_uvecana = uvecana_slika_mono.shape
print('Visina uvećane slike', visina_uvecane)
print('Širina uvećane slike', sirina_uvecana)

cv2.imshow('Kamera 3 - Nijanse sive', uvecana_slika_mono)
cv2.waitKey(0)
cv2.destroyAllWindows()