import numpy as np
import cv2

def nacrtaj_liniju(slika, line):
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho

    # linija koja je okomita na normalu naziva se tangenta
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(slika, (x1, y1), (x2, y2), (0, 255, 0), 2)
