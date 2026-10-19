# BED-CAR — demo strony (skup i złomowanie aut, Zawiercie)

Lead: Michał Bednarz, Bed-car (CRM: crm.impulseo.pl). Demo na GitHub Pages, `noindex`.

- Strony generuje `python3 tools/build.py` (wspólny nagłówek/stopka/meta). Nie edytuj `.html` ręcznie.
- `python3 tools/logo.py <mockup.jpg>` wycina logo z mockupu klienta do `assets/img/logo-{ciemne,jasne}.png`.
- `python3 tools/mapa.py <wojewodztwa-medium.geojson>` generuje `assets/mapa-obszar.svg` (GUGiK przez ppatrzyk/polska-geojson).
- `assets/main.js` ma na końcu licznik otwarć `demo_views` — wyciąć przed go-live.

Źródła treści: FB „Skup aut, złomowanie samochodów, sprzedaż samochodów Bed-car handel” + notatka w CRM.
Zdjęcia: Pexels (17429097 hero, 16928585, 20573982, 8310736) — zdjęcia z FB klienta mają nadrukowany tekst.

Do potwierdzenia z klientem: e-mail (FB bedcar@o2.pl vs CRM salvadorcar@o2.pl), czy wydaje zaświadczenie
o demontażu (sam czy przez stację), Kielce na liście FB (poza Śląskiem i Małopolską), zdjęcia lawety i placu.
