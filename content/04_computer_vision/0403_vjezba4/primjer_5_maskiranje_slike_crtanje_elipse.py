import cv2
import numpy as np

HEIGHT = 500
WIDTH = 700

mask = np.zeros((HEIGHT, WIDTH))

cv2.ellipse(img=mask,
            center=(WIDTH // 2, HEIGHT // 2),
            axes=(WIDTH // 2, HEIGHT // 2),
            angle=0,
            startAngle=180,
            endAngle=360,
            color=255,
            thickness=2)  # ako postavimo vrijednost na -1, elipsa bude popunjena

cv2.imshow("Mask", mask)
cv2.waitKey()
cv2.destroyAllWindows()
