"""Wycina logo BED-CAR z mockupu klienta (chrom na grafitowej ścianie) do płaskich PNG z przezroczystością."""
import sys
from PIL import Image
import numpy as np, cv2

SRC = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else 'assets/img'
PREV = sys.argv[3] if len(sys.argv) > 3 else None
PROG = 55

g = np.asarray(Image.open(SRC).convert('L').crop((180, 580, 2280, 1160))).astype(np.float32)
# model tła ściany: rozmyte piksele, które nie są chromem
m0 = g > 110
w = (~m0).astype(np.float32)
blur = lambda x: cv2.GaussianBlur(x, (0, 0), 45)
bg = blur(np.where(m0, 0, g)) / np.maximum(blur(w), 1e-3)
d = g - bg

def maska(prog):
    m = (d > prog).astype('uint8')
    k5 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, k5)
    return cv2.medianBlur(m * 255, 5) // 255

# wnętrze ramki wyznaczamy na łagodnym progu, potem przycinamy wszystko poza ramką
m = maska(38)
n, lab, st, _ = cv2.connectedComponentsWithStats(1 - m, connectivity=4)
H, W = m.shape
wn = max((i for i in range(1, n) if st[i][0] > 0 and st[i][1] > 0 and st[i][0] + st[i][2] < W and st[i][1] + st[i][3] < H), key=lambda i: st[i][4])
hull = cv2.convexHull(cv2.findNonZero((lab == wn).astype('uint8')))
reg = np.zeros_like(m); cv2.fillPoly(reg, [hull], 1)
reg = cv2.dilate(reg, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (71, 71)))
ostra = maska(PROG)
# ostry próg tylko w prawym górnym rogu, gdzie jasna ściana daje szum przy literze R
rog = np.zeros_like(m); rog[: int(H * 0.45), int(W * 0.8):] = 1
wynik = np.where(rog > 0, ostra, m) * reg

n2, l2, s2, _ = cv2.connectedComponentsWithStats(wynik, connectivity=8)
keep = np.zeros_like(wynik)
for i in range(1, n2):
    if s2[i][4] > 3000:
        keep |= (l2 == i).astype('uint8')
# zalep drobne dziury po ciemnych refleksach w chromie
n3, l3, s3, _ = cv2.connectedComponentsWithStats(1 - keep, connectivity=4)
for i in range(1, n3):
    if s3[i][4] < 2500:
        keep[l3 == i] = 1
k = cv2.GaussianBlur(keep * 255, (0, 0), 2.0)
k = np.where(k > 127, 255, 0).astype('uint8')
ys, xs = np.where(k > 0)
A = Image.fromarray(np.pad(k[ys.min():ys.max() + 1, xs.min():xs.max() + 1], 4))
for nazwa, kol in [('logo-ciemne', (30, 33, 39)), ('logo-jasne', (255, 255, 255))]:
    im = Image.new('RGBA', A.size, kol + (0,)); im.putalpha(A)
    im.resize((640, round(640 * A.height / A.width)), Image.LANCZOS).save(f'{OUT}/{nazwa}.png', optimize=True)
if PREV:
    p = Image.new('RGB', (700, 420), (244, 245, 247))
    a = Image.open(f'{OUT}/logo-ciemne.png'); p.paste(a, (20, 20), a)
    p.paste(Image.new('RGB', (700, 210), (24, 26, 31)), (0, 210))
    b = Image.open(f'{OUT}/logo-jasne.png'); p.paste(b, (20, 230), b)
    p.save(PREV)
