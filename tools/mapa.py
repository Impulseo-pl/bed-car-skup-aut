"""Generuje assets/img/mapa-obszar.svg: województwo śląskie i małopolskie z miastami z wizytówki FB.

Granice: GUGiK przez github.com/ppatrzyk/polska-geojson (wojewodztwa-medium.geojson).
Uruchomienie: python3 tools/mapa.py <plik.geojson>
"""
import json
import math
import sys

SZER = 640
EPS = 0.8
OBSZAR = {'śląskie', 'małopolskie'}
SASIEDZI = {'opolskie', 'łódzkie', 'świętokrzyskie', 'podkarpackie'}

# (nazwa, lat, lon, położenie podpisu, czy baza)
MIASTA = [
    ('Zawiercie', 50.4878, 19.4170, 'right', True),
    ('Katowice', 50.2649, 19.0238, 'left', False),
    ('Kraków', 50.0647, 19.9450, 'right', False),
    ('Częstochowa', 50.8118, 19.1203, 'right', False),
    ('Dąbrowa Górnicza', 50.3217, 19.1949, 'right', False),
    ('Myszków', 50.5753, 19.3245, 'left', False),
    ('Rybnik', 50.0971, 18.5418, 'left', False),
    ('Chrzanów', 50.1355, 19.4022, 'bottom', False),
    ('Olkusz', 50.2813, 19.5650, 'right', False),
    ('Lubliniec', 50.6686, 18.6843, 'left', False),
]


def dp(pts, eps):
    if len(pts) < 3:
        return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy)
    best, idx = 0, 0
    for i in range(1, len(pts) - 1):
        px, py = pts[i]
        d = math.hypot(px - x1, py - y1) if n < 1e-9 else abs(dy * px - dx * py + x2 * y1 - y2 * x1) / n
        if d > best:
            best, idx = d, i
    if best > eps:
        return dp(pts[:idx + 1], eps)[:-1] + dp(pts[idx:], eps)
    return [pts[0], pts[-1]]


def main(src):
    dane = json.load(open(src))
    for f in dane['features']:
        if f['geometry']['type'] == 'Polygon':
            f['geometry'] = {'type': 'MultiPolygon', 'coordinates': [f['geometry']['coordinates']]}
    cel = [f for f in dane['features'] if f['properties']['nazwa'] in OBSZAR]
    lons, lats = [], []
    for f in cel:
        for poly in f['geometry']['coordinates']:
            for lon, lat in poly[0]:
                lons.append(lon)
                lats.append(lat)
    k = math.cos(math.radians((min(lats) + max(lats)) / 2))
    marg = 0.18
    x0, x1 = (min(lons) - marg) * k, (max(lons) + marg) * k
    y0, y1 = max(lats) + marg, min(lats) - marg
    skala = SZER / (x1 - x0)
    wys = round((y0 - y1) * skala)

    def pr(lon, lat):
        return ((lon * k - x0) * skala, (y0 - lat) * skala)

    def sciezka(geom):
        out = []
        for poly in geom['coordinates']:
            for ring in poly:
                p = [pr(lon, lat) for lon, lat in ring]
                xs = [a for a, _ in p]
                ys = [b for _, b in p]
                if max(xs) - min(xs) < 4 and max(ys) - min(ys) < 4:
                    continue
                p = dp(p, EPS)
                out.append('M' + 'L'.join('%g,%g' % (round(a * 2) / 2, round(b * 2) / 2) for a, b in p) + 'Z')
        return ''.join(out)

    el = []
    for f in dane['features']:
        nazwa = f['properties']['nazwa']
        if nazwa not in OBSZAR | SASIEDZI:
            continue
        klasa = 'woj woj-on' if nazwa in OBSZAR else 'woj'
        el.append('<path class="%s" d="%s"><title>%s</title></path>' % (klasa, sciezka(f['geometry']), nazwa))
    for nazwa, lat, lon, pos, baza in MIASTA:
        x, y = pr(lon, lat)
        dx, dy, anchor = {'right': (10, 4, 'start'), 'left': (-10, 4, 'end'), 'bottom': (0, 20, 'middle'), 'top': (0, -12, 'middle')}[pos]
        if baza:
            el.append('<circle class="pin-puls" cx="%.1f" cy="%.1f" r="14"/>' % (x, y))
        el.append('<circle class="pin%s" cx="%.1f" cy="%.1f" r="%d"/>' % (' pin-baza' if baza else '', x, y, 7 if baza else 4.5))
        el.append('<text class="lbl%s" x="%.1f" y="%.1f" text-anchor="%s">%s</text>' % (' lbl-baza' if baza else '', x + dx, y + dy, anchor, nazwa))
    for nazwa, lat, lon in [('ŚLĄSKIE', 49.78, 18.98), ('MAŁOPOLSKIE', 49.72, 20.35)]:
        x, y = pr(lon, lat)
        el.append('<text class="lbl-woj" x="%.1f" y="%.1f" text-anchor="middle">%s</text>' % (x, y, nazwa))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" '
           'aria-label="Obszar działania: województwo śląskie i małopolskie">%s</svg>' % (SZER, wys, ''.join(el)))
    open('assets/mapa-obszar.svg', 'w').write(svg)
    print('mapa: %d x %d, %d kB' % (SZER, wys, len(svg) // 1024))


if __name__ == '__main__':
    main(sys.argv[1])
