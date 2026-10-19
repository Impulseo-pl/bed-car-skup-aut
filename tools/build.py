"""Generator dema BED-CAR. Uruchomienie z katalogu repo: python3 tools/build.py

Wspólny nagłówek, stopka i meta (w tym noindex dema) są tylko tutaj — nie edytować .html ręcznie.
Treść: wyłącznie fakty z FB klienta (Skup aut, złomowanie samochodów, sprzedaż samochodów Bed-car handel)
i notatki z CRM. Python 3.9: bez f-stringów z backslashami, szablony podmieniane przez .replace().
"""
import hashlib
import json

BAZA = 'https://impulseo-pl.github.io/bed-car-skup-aut/'
TEL = '661 982 860'
TEL_HREF = 'tel:+48661982860'
MAIL = 'bedcar@o2.pl'
ADRES = 'Wiejska 24, 42-421 Rzędkowice'
MIASTA = ['Zawiercie', 'Katowice', 'Kraków', 'Częstochowa', 'Dąbrowa Górnicza', 'Myszków',
          'Olkusz', 'Chrzanów', 'Rybnik', 'Lubliniec']


def ver(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()[:8]


I = {
    'tel': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
    'check': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
    'clock': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9.5"/><path d="M12 6.5V12l3.5 2"/></svg>',
    'truck': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M1.5 16.5V8a1 1 0 0 1 1-1H13v9.5"/><path d="M13 10h4.2a1 1 0 0 1 .8.4l3.3 4.3a1 1 0 0 1 .2.6v1.2h-2"/><path d="M1.5 16.5h2M9 16.5h6.5"/><circle cx="6.2" cy="17" r="2.2"/><circle cx="17.7" cy="17" r="2.2"/></svg>',
    'cash': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.6"/><path d="M6 9.5v5M18 9.5v5"/></svg>',
    'doc': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></svg>',
    'shield': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
    'car': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 17H3.5a1 1 0 0 1-1-1v-3.2a2 2 0 0 1 .6-1.4L5 9.5l1.7-3.3A2 2 0 0 1 8.5 5h7a2 2 0 0 1 1.8 1.2L19 9.5l1.9 1.9a2 2 0 0 1 .6 1.4V16a1 1 0 0 1-1 1H19"/><path d="M5 9.5h14M9 17h6"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/></svg>',
    'crash': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 17H3.5a1 1 0 0 1-1-1v-3.2a2 2 0 0 1 .6-1.4L5 9.5l1.7-3.3A2 2 0 0 1 8.5 5h4"/><path d="M5 9.5h7M9 17h3"/><circle cx="7" cy="17" r="2"/><path d="m15 4 1.5 3 2.5-2-.5 3.2 3 .8-2.6 1.6 1.6 2.6-3-.6"/></svg>',
    'recycle': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 19H4.8a1.8 1.8 0 0 1-1.5-2.7L5.5 12.5"/><path d="m11 19 6.2 0a1.8 1.8 0 0 0 1.5-2.7l-1.2-2"/><path d="M8.5 7.5 10.5 4a1.8 1.8 0 0 1 3 0l2.6 4.5"/><path d="m14 16-3 3 3 3M4 9.5l1.5 3 3.4-.6M19.5 7.8l-3.4 1.2-.9-3.3"/></svg>',
    'nooc': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="m9.5 12.5 5 5M14.5 12.5l-5 5"/></svg>',
    'lorry': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="1.5" y="4.5" width="13" height="11" rx="1"/><path d="M14.5 8.5h4l3 3.5v3.5h-7"/><circle cx="6" cy="17.5" r="2"/><circle cx="17.5" cy="17.5" r="2"/></svg>',
    'wrench': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/></svg>',
    'refund': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/><path d="M12 7.5v9M14.5 9.5h-3.3a1.7 1.7 0 0 0 0 3.4h1.6a1.7 1.7 0 0 1 0 3.4H9.5"/></svg>',
    'pin': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>',
    'chat': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2-5.4A8.4 8.4 0 1 1 21 11.5z"/></svg>',
    'key': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="7.5" cy="15.5" r="4.5"/><path d="m10.7 12.3 9.8-9.8M17 6l3 3M14.5 8.5l2 2"/></svg>',
}

NAV = [('index.html', 'Strona główna'), ('skup-aut.html', 'Skup aut'), ('zlomowanie-aut.html', 'Złomowanie'),
       ('index.html#obszar', 'Obszar'), ('kontakt.html', 'Kontakt')]

HEAD = """<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}}</title>
<meta name="description" content="{{DESC}}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{{URL}}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pl_PL">
<meta property="og:title" content="{{TITLE}}">
<meta property="og:description" content="{{DESC}}">
<meta property="og:url" content="{{URL}}">
<meta property="og:image" content="{{BAZA}}assets/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1b1e24">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,600..900;1,62..125,700..900&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="assets/styles.css?v={{CSSV}}">
{{PRELOAD}}<script type="application/ld+json">{{LD}}</script>
</head>
<body>
<a class="skip" href="#tresc">Przejdź do treści</a>
<div class="topbar"><div class="wrap">
  <div class="tb-l"><span><i class="dot"></i> Czynne całą dobę</span><span class="tb-hide">Województwo śląskie i małopolskie</span></div>
  <a href="{{TEL_HREF}}">{{TEL}}</a>
</div></div>
<header class="hdr" id="hdr"><div class="wrap">
  <a class="logo" href="index.html" aria-label="BED-CAR — strona główna"><img src="assets/img/logo-ciemne.png" alt="BED-CAR" width="640" height="{{LOGOH}}"></a>
  <nav class="nav" id="nav" aria-label="Menu główne">{{NAV}}</nav>
  <a class="btn btn-amber hdr-cta" href="{{TEL_HREF}}">{{I_TEL}} {{TEL}}</a>
  <button class="burger" id="burger" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span></button>
</div></header>
<main id="tresc">
"""

FOOT = """</main>
<section class="cta"><div class="wrap">
  <div>
    <h2>Masz auto do sprzedania albo do kasacji?</h2>
    <p>Zadzwoń o dowolnej porze. Wycenimy samochód przez telefon i ustalimy termin odbioru lawetą.</p>
  </div>
  <a class="phone-big" href="{{TEL_HREF}}">{{I_TEL}} {{TEL}}</a>
</div></section>
<footer class="ftr">
  <div class="wrap">
    <div>
      <img src="assets/img/logo-jasne.png" alt="BED-CAR" width="640" height="{{LOGOH}}" loading="lazy">
      <p>Skup, złomowanie i sprzedaż samochodów. Odkupujemy auta całe, uszkodzone, powypadkowe i przeznaczone do kasacji na terenie województwa śląskiego i małopolskiego.</p>
    </div>
    <div>
      <h4>Usługi</h4>
      <ul><li><a href="skup-aut.html">Skup aut</a></li><li><a href="zlomowanie-aut.html">Złomowanie aut</a></li><li><a href="index.html#sprzedaz">Sprzedaż samochodów</a></li><li><a href="index.html#sprzedaz">Pomoc drogowa</a></li></ul>
    </div>
    <div>
      <h4>Obszar</h4>
      <ul><li>Zawiercie</li><li>Katowice</li><li>Kraków</li><li>Częstochowa</li><li><a href="index.html#obszar">Pełna lista miast</a></li></ul>
    </div>
    <div>
      <h4>Kontakt</h4>
      <ul><li><a href="{{TEL_HREF}}">{{TEL}}</a></li><li><a href="mailto:{{MAIL}}">{{MAIL}}</a></li><li>{{ADRES}}</li><li>Czynne całą dobę</li></ul>
    </div>
  </div>
  <div class="ftr-bottom"><div class="wrap"><span>© 2026 BED-CAR · Skup i złomowanie aut</span><a href="kontakt.html">Kontakt</a></div></div>
</footer>
<div class="mbar">
  <a class="btn btn-amber" href="{{TEL_HREF}}">{{I_TEL}} Zadzwoń</a>
  <a class="btn btn-dark" href="{{WYCENA}}">Wyceń auto</a>
</div>
<script src="assets/main.js?v={{JSV}}" defer></script>
</body>
</html>
"""

QUOTE_FORM = """<form class="js-form" novalidate>
  <div class="form-body">
    <div class="f-row">
      <div class="field"><label for="{{P}}marka">Marka i model</label><input id="{{P}}marka" name="auto" placeholder="np. Opel Astra" required></div>
      <div class="field"><label for="{{P}}rok">Rok produkcji</label><input id="{{P}}rok" name="rok" inputmode="numeric" placeholder="np. 2008"></div>
    </div>
    <div class="field"><label for="{{P}}stan">Stan auta</label>
      <select id="{{P}}stan" name="stan"><option>Sprawne, na chodzie</option><option>Uszkodzone</option><option>Powypadkowe</option><option>Niesprawne, do kasacji</option><option>Bez ważnego OC lub przeglądu</option></select></div>
    <div class="field"><label for="{{P}}tel">Telefon</label><input id="{{P}}tel" name="telefon" type="tel" inputmode="tel" placeholder="Numer do kontaktu" required></div>
    {{EXTRA}}
    <button class="btn btn-amber" type="submit">Wyślij do wyceny</button>
    <p class="form-note">Oddzwonimy z propozycją ceny. Wolisz od razu? <a href="{{TEL_HREF}}">{{TEL}}</a></p>
  </div>
  <div class="form-ok" role="status">{{I_CHECK}}<h3>Dziękujemy, zgłoszenie przyjęte</h3><p>W wersji demonstracyjnej formularz niczego nie wysyła. Na docelowej stronie zgłoszenie trafi od razu na skrzynkę i telefon firmy.</p></div>
</form>"""

FAQ_HOME = [
    ('Czy kupujecie auta bez ważnego OC i przeglądu?', 'Tak. Brak opłaconego OC i aktualnego badania technicznego nie przeszkadza w sprzedaży. Auto odbieramy lawetą, więc nie musi poruszać się po drodze o własnych siłach.'),
    ('Ile kosztuje odbiór samochodu lawetą?', 'Odbiór lawetą jest bezpłatny. Przyjeżdżamy pod wskazany adres na terenie województwa śląskiego i małopolskiego.'),
    ('Jakie auta skupujecie?', 'Skupujemy wszystkie auta osobowe i ciężarowe: całe i sprawne, uszkodzone, powypadkowe oraz przeznaczone do kasacji.'),
    ('Co z ubezpieczeniem OC po sprzedaży lub kasacji?', 'Po sprzedaży lub złomowaniu auta można odzyskać niewykorzystaną część składki OC. Pomagamy w formalnościach związanych ze zwrotem składki.'),
    ('W jakich godzinach można się z wami kontaktować?', 'Jesteśmy dostępni całą dobę, siedem dni w tygodniu. Najszybciej jest zadzwonić pod numer ' + TEL + '.'),
]


def faq_html(items):
    return '<div class="faq">' + ''.join(
        '<details class="rv"><summary>%s</summary><p>%s</p></details>' % (q, a) for q, a in items) + '</div>'


def faq_ld(items):
    return {'@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in items]}


def biznes_ld():
    return {
        '@type': 'AutomotiveBusiness', '@id': BAZA + '#firma', 'name': 'BED-CAR Skup i złomowanie aut',
        'url': BAZA, 'telephone': '+48661982860', 'email': MAIL, 'image': BAZA + 'assets/img/og.jpg',
        'address': {'@type': 'PostalAddress', 'streetAddress': 'Wiejska 24', 'postalCode': '42-421',
                    'addressLocality': 'Rzędkowice', 'addressCountry': 'PL'},
        'openingHoursSpecification': {'@type': 'OpeningHoursSpecification', 'dayOfWeek': [
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'opens': '00:00', 'closes': '23:59'},
        'areaServed': [{'@type': 'AdministrativeArea', 'name': 'województwo śląskie'},
                       {'@type': 'AdministrativeArea', 'name': 'województwo małopolskie'}],
        'sameAs': ['https://www.facebook.com/profile.php?id=100083579265653'],
    }


def quote(prefix, extra=''):
    return (QUOTE_FORM.replace('{{P}}', prefix).replace('{{EXTRA}}', extra))


def ph(crumb, eyebrow, h1, lead, img, alt):
    return """<section class="ph"><div class="wrap">
  <div>
    <div class="crumbs"><a href="index.html">Strona główna</a> / {{CRUMB}}</div>
    <h1>{{H1}}</h1>
    <p class="lead">{{LEAD}}</p>
    <div class="hero-ctas"><a class="btn btn-amber btn-lg" href="{{TEL_HREF}}">{{I_TEL}} {{TEL}}</a><a class="btn btn-ghost btn-lg" href="#wycena">Formularz wyceny</a></div>
  </div>
  <div class="ph-img"><img src="assets/img/{{IMG}}" alt="{{ALT}}" width="1200" height="800" fetchpriority="high"></div>
</div></section>""".replace('{{CRUMB}}', crumb).replace('{{H1}}', h1).replace('{{LEAD}}', lead).replace('{{IMG}}', img).replace('{{ALT}}', alt)


INDEX = """
<section class="hero">
  <div class="wrap">
    <div>
      <span class="pill"><i class="dot"></i> Zawiercie · cały Śląsk i Małopolska</span>
      <h1>Skup i <em class="acc">złomowanie</em> aut za gotówkę</h1>
      <p class="lead">Odkupujemy samochody całe, uszkodzone, powypadkowe i przeznaczone do kasacji. Odbieramy je lawetą bez żadnych opłat, także bez ważnego OC i przeglądu technicznego.</p>
      <div class="hero-ctas">
        <a class="btn btn-amber btn-lg" href="{{TEL_HREF}}">{{I_TEL}} Zadzwoń: {{TEL}}</a>
        <a class="btn btn-ghost btn-lg" href="#wycena">Wyceń auto online</a>
      </div>
      <ul class="checks">
        <li>{{I_CHECK}} Każdy stan auta</li>
        <li>{{I_CHECK}} Laweta gratis</li>
        <li>{{I_CHECK}} Zwrot składki OC</li>
      </ul>
    </div>
    <div class="hero-media">
      <div class="hero-photo"><picture><source media="(max-width:620px)" srcset="assets/img/hero-laweta-m.webp"><img src="assets/img/hero-laweta.webp" alt="Samochód wciągany na lawetę" width="1800" height="1100" fetchpriority="high"></picture></div>
      <div class="hero-badge">{{I_CLOCK_AMBER}}<div><b>24/7</b><small>czynne<br>całą dobę</small></div></div>
      <div class="quote" id="wycena">
        <h3>Szybka wycena auta</h3>
        <p class="sub">Podaj kilka informacji, oddzwonimy z ceną.</p>
        {{QUOTE}}
      </div>
    </div>
  </div>
</section>

<section class="strip" aria-label="Najważniejsze informacje"><div class="wrap">
  <div class="strip-it">{{I_CAR}}<div><b>Każdy stan techniczny</b><span>całe, uszkodzone, rozbite</span></div></div>
  <div class="strip-it">{{I_NOOC}}<div><b>Bez OC i przeglądu</b><span>formalności po naszej stronie</span></div></div>
  <div class="strip-it">{{I_TRUCK}}<div><b>Odbiór lawetą gratis</b><span>spod domu lub warsztatu</span></div></div>
  <div class="strip-it">{{I_REFUND}}<div><b>Zwrot składki OC</b><span>pomagamy odzyskać pieniądze</span></div></div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head rv"><span class="eyebrow">Co skupujemy</span><h2>Kupujemy wszystkie auta, niezależnie od stanu</h2><p>Nie ma znaczenia, czy samochód jeździ, stoi od miesięcy pod domem, czy po kolizji nadaje się już tylko do kasacji. Każde auto wyceniamy indywidualnie.</p></div>
  <div class="cards">
    <article class="card feat rv"><span class="tag">Specjalizacja</span><div class="ico">{{I_RECYCLE}}</div><h3>Auta do kasacji</h3><p>Złomowanie samochodów to główna część naszej pracy. Odbieramy auta niesprawne, niekompletne i wyeksploatowane.</p></article>
    <article class="card rv"><div class="ico">{{I_CRASH}}</div><h3>Powypadkowe i uszkodzone</h3><p>Auta po kolizji, z uszkodzonym silnikiem lub skrzynią biegów, z korozją albo po zalaniu.</p></article>
    <article class="card rv"><div class="ico">{{I_CAR}}</div><h3>Całe i sprawne</h3><p>Samochody na chodzie, które chcesz sprzedać szybko, bez wystawiania ogłoszeń i spotkań z kupującymi.</p></article>
    <article class="card rv"><div class="ico">{{I_NOOC}}</div><h3>Bez OC i przeglądu</h3><p>Brak ważnego ubezpieczenia lub badania technicznego nie jest przeszkodą. Auto zabieramy lawetą.</p></article>
    <article class="card rv"><div class="ico">{{I_LORRY}}</div><h3>Osobowe i ciężarowe</h3><p>Skupujemy samochody osobowe oraz ciężarowe, zarówno całe, jak i uszkodzone.</p></article>
    <article class="card rv"><div class="ico">{{I_KEY}}</div><h3>Do renowacji</h3><p>Część odkupionych aut przywracamy do sprawności i wystawiamy na sprzedaż.</p></article>
  </div>
</div></section>

<section class="sec sec-grey" id="proces"><div class="wrap">
  <div class="sec-head center rv"><span class="eyebrow">Jak to działa</span><h2>Sprzedaż auta w trzech krokach</h2><p>Cała procedura zajmuje zwykle jedną rozmowę telefoniczną i jeden przyjazd lawety.</p></div>
  <div class="steps">
    <div class="step rv"><div class="n">{{I_TEL}}</div><h3>Zadzwoń lub wyślij zgłoszenie</h3><p>Opisz auto: markę, model, rocznik i stan techniczny. Zdjęcia pomagają w dokładniejszej wycenie.</p></div>
    <div class="step rv"><div class="n">{{I_CHAT}}</div><h3>Ustalamy cenę i termin</h3><p>Przedstawiamy propozycję ceny i umawiamy odbiór w dogodnym dla Ciebie miejscu i czasie.</p></div>
    <div class="step rv"><div class="n">{{I_CASH}}</div><h3>Odbiór i płatność</h3><p>Przyjeżdżamy lawetą, podpisujemy umowę, wypłacamy pieniądze i zabieramy samochód.</p></div>
  </div>
  <div class="docs rv"><b>Przygotuj na odbiór:</b><span>{{I_CHECK}} dowód rejestracyjny</span><span>{{I_CHECK}} kartę pojazdu, jeśli była wydana</span><span>{{I_CHECK}} dowód osobisty właściciela</span><span>{{I_CHECK}} kluczyki</span></div>
</div></section>

<section class="sec"><div class="wrap split">
  <div class="split-media rv"><img src="assets/img/zlomowanie.webp" alt="Auta przygotowane do kasacji" width="1200" height="800" loading="lazy"><div class="float">{{I_TRUCK_AMBER}} Odbiór auta do kasacji bez opłat</div></div>
  <div class="rv">
    <span class="eyebrow">Złomowanie aut</span>
    <h2>Kasacja pojazdu bez wychodzenia z domu</h2>
    <p>Większość samochodów, które do nas trafiają, to auta do złomowania. Zajmujemy się całym procesem: od odbioru lawetą po dokumenty potrzebne do wyrejestrowania pojazdu.</p>
    <ul class="list">
      <li>{{I_CHECK}}<div><b>Odbieramy auta w każdym stanie</b><span>niesprawne, niekompletne, bez kół, po pożarze lub zalaniu</span></div></li>
      <li>{{I_CHECK}}<div><b>Płacimy za auto do kasacji</b><span>wycena zależy od masy, kompletności i stanu pojazdu</span></div></li>
      <li>{{I_CHECK}}<div><b>Pomagamy przy zwrocie składki OC</b><span>niewykorzystana część ubezpieczenia wraca do właściciela</span></div></li>
    </ul>
    <a class="btn btn-dark" href="zlomowanie-aut.html">Więcej o złomowaniu</a>
  </div>
</div></section>

<section class="sec sec-grey" id="sprzedaz"><div class="wrap split rev">
  <div class="split-media rv"><img src="assets/img/renowacja.webp" alt="Samochód w warsztacie podczas renowacji" width="1200" height="800" loading="lazy"><div class="float">{{I_WRENCH_AMBER}} Renowacja i sprzedaż samochodów</div></div>
  <div class="rv">
    <span class="eyebrow">Sprzedaż i pomoc</span>
    <h2>Auta po renowacji, pomoc przy zakupie i pomoc drogowa</h2>
    <p>Część skupionych samochodów przywracamy do sprawności i sprzedajemy. Jeżeli szukasz auta, zadzwoń i zapytaj o samochody dostępne w tej chwili.</p>
    <div class="mini">
      <div><b>Sprzedaż aut</b><span>samochody po renowacji</span></div>
      <div><b>Pomoc przy zakupie</b><span>doradzimy przy wyborze auta</span></div>
      <div><b>Pomoc drogowa</b><span>transport lawetą</span></div>
    </div>
    <p style="margin-top:28px"><a class="btn btn-amber" href="{{TEL_HREF}}">{{I_TEL}} Zapytaj o dostępne auta</a></p>
  </div>
</div></section>

<section class="sec" id="obszar"><div class="wrap area">
  <div class="rv">
    <span class="eyebrow">Obszar działania</span>
    <h2>Dojeżdżamy na terenie całego Śląska i Małopolski</h2>
    <p>Nasza baza znajduje się w Rzędkowicach koło Zawiercia. Po samochody przyjeżdżamy na terenie województwa śląskiego i małopolskiego, do miast i mniejszych miejscowości.</p>
    <div class="chips">{{CHIPS}}<span>i okolice</span></div>
    <div class="addr">{{I_PIN}}<div><b>BED-CAR</b><br><span>{{ADRES}}<br>gmina Włodowice, powiat zawierciański</span></div></div>
  </div>
  <div class="map-box rv">{{MAPA}}</div>
</div></section>

<section class="sec sec-grey"><div class="wrap">
  <div class="sec-head center rv"><span class="eyebrow">Pytania</span><h2>Najczęściej zadawane pytania</h2></div>
  {{FAQ}}
</div></section>
"""

SKUP = """
{{PH}}
<section class="sec"><div class="wrap cols2">
  <div class="prose">
    <h2 style="margin-top:0">Szybka sprzedaż auta bez ogłoszeń</h2>
    <p>Sprzedaż samochodu przez ogłoszenie wymaga zdjęć, odpowiadania na telefony, umawiania oględzin i negocjacji. W przypadku auta uszkodzonego, bez przeglądu albo bez ubezpieczenia znalezienie kupca bywa bardzo trudne. Skup aut rozwiązuje ten problem: jedna rozmowa, jedna wizyta i samochód zostaje sprzedany.</p>
    <p>BED-CAR skupuje samochody osobowe i ciężarowe na terenie województwa śląskiego i małopolskiego. Odbieramy auta całe, uszkodzone, powypadkowe oraz przeznaczone do kasacji. Transport lawetą jest bezpłatny.</p>
    <h2>Jakie auta kupujemy</h2>
    <ul class="list">
      <li>{{I_CHECK}}<div><b>Auta sprawne</b><span>na chodzie, z ważnymi lub nieważnymi dokumentami</span></div></li>
      <li>{{I_CHECK}}<div><b>Auta uszkodzone</b><span>z awarią silnika, skrzyni biegów, elektroniki lub z korozją</span></div></li>
      <li>{{I_CHECK}}<div><b>Auta powypadkowe</b><span>po kolizji, także z rozbitą karoserią i wystrzelonymi poduszkami</span></div></li>
      <li>{{I_CHECK}}<div><b>Auta bez OC i przeglądu</b><span>odbieramy lawetą, więc auto nie musi wyjeżdżać na drogę</span></div></li>
      <li>{{I_CHECK}}<div><b>Auta do kasacji</b><span>niekompletne i wyeksploatowane, przeznaczone do złomowania</span></div></li>
    </ul>
    <h2>Od czego zależy cena</h2>
    <p>Cenę ustalamy indywidualnie. Bierzemy pod uwagę markę, model i rocznik, stan techniczny, kompletność auta, przebieg oraz to, czy samochód nadaje się do dalszej jazdy lub naprawy. Dokładniejszą wycenę przygotujemy na podstawie zdjęć.</p>
    <h2>Przebieg sprzedaży</h2>
    <div class="steps" style="grid-template-columns:1fr;gap:12px">
      <div class="step"><h3>Kontakt</h3><p>Dzwonisz lub wysyłasz formularz z opisem auta.</p></div>
      <div class="step"><h3>Wycena i termin</h3><p>Przedstawiamy propozycję ceny i umawiamy odbiór.</p></div>
      <div class="step"><h3>Odbiór</h3><p>Przyjeżdżamy lawetą, podpisujemy umowę i wypłacamy pieniądze.</p></div>
    </div>
  </div>
  <aside class="aside-card" id="wycena">
    <h3>Wycena auta</h3>
    <p>Opisz samochód, a oddzwonimy z propozycją ceny.</p>
    {{QUOTE}}
  </aside>
</div></section>
<section class="sec sec-grey"><div class="wrap">
  <div class="sec-head center rv"><span class="eyebrow">Pytania</span><h2>Skup aut: pytania i odpowiedzi</h2></div>
  {{FAQ}}
</div></section>
"""

ZLOM = """
{{PH}}
<section class="sec"><div class="wrap cols2">
  <div class="prose">
    <h2 style="margin-top:0">Złomowanie samochodu krok po kroku</h2>
    <p>Kasacja to najprostszy sposób na pozbycie się auta, które nie nadaje się już do jazdy ani do opłacalnej naprawy. Złomowanie samochodów stanowi główną część naszej działalności, dlatego cały proces przeprowadzamy sprawnie i bez dodatkowych kosztów po stronie właściciela.</p>
    <ul class="list">
      <li>{{I_CHECK}}<div><b>Zgłoszenie</b><span>dzwonisz lub wysyłasz formularz, podając markę, model i stan auta</span></div></li>
      <li>{{I_CHECK}}<div><b>Wycena</b><span>przedstawiamy kwotę, którą płacimy za auto przeznaczone do kasacji</span></div></li>
      <li>{{I_CHECK}}<div><b>Odbiór lawetą</b><span>przyjeżdżamy pod wskazany adres, transport jest bezpłatny</span></div></li>
      <li>{{I_CHECK}}<div><b>Dokumenty</b><span>po demontażu właściciel otrzymuje zaświadczenie potrzebne do wyrejestrowania pojazdu</span></div></li>
    </ul>
    <h2>Zwrot składki OC po kasacji</h2>
    <p>Po zezłomowaniu samochodu umowa ubezpieczenia OC wygasa, a właścicielowi przysługuje zwrot składki za niewykorzystany okres ochrony. Podpowiemy, jakie dokumenty przesłać do ubezpieczyciela, aby odzyskać pieniądze.</p>
    <h2>Wyrejestrowanie pojazdu</h2>
    <p>Z zaświadczeniem o demontażu właściciel wyrejestrowuje samochód w wydziale komunikacji właściwym dla miejsca zamieszkania. Od tej chwili auto nie podlega obowiązkowemu ubezpieczeniu ani opłatom.</p>
    <h2>Jakie auta odbieramy do kasacji</h2>
    <p>Odbieramy samochody osobowe i ciężarowe w każdym stanie: niesprawne, niekompletne, po wypadku, po pożarze, po zalaniu, długo stojące oraz bez ważnego OC i przeglądu technicznego.</p>
  </div>
  <aside class="aside-card" id="wycena">
    <h3>Zgłoś auto do kasacji</h3>
    <p>Podaj podstawowe informacje, a oddzwonimy z wyceną i terminem odbioru.</p>
    {{QUOTE}}
  </aside>
</div></section>
<section class="sec sec-grey"><div class="wrap">
  <div class="sec-head center rv"><span class="eyebrow">Pytania</span><h2>Złomowanie aut: pytania i odpowiedzi</h2></div>
  {{FAQ}}
</div></section>
"""

KONTAKT = """
<section class="ph"><div class="wrap" style="grid-template-columns:1fr">
  <div>
    <div class="crumbs"><a href="index.html">Strona główna</a> / Kontakt</div>
    <h1>Kontakt</h1>
    <p class="lead" style="max-width:40em">Jesteśmy dostępni całą dobę. Najszybciej wycenimy auto przez telefon, możesz też wysłać zgłoszenie przez formularz.</p>
  </div>
</div></section>
<section class="sec"><div class="wrap contact">
  <div class="c-list">
    <a class="c-item rv" href="{{TEL_HREF}}"><span class="ico">{{I_TEL}}</span><div><small>Telefon, całą dobę</small><b>{{TEL}}</b></div></a>
    <a class="c-item rv" href="mailto:{{MAIL}}"><span class="ico">{{I_MAIL}}</span><div><small>E-mail</small><b>{{MAIL}}</b></div></a>
    <div class="c-item rv"><span class="ico">{{I_PIN}}</span><div><small>Adres</small><b>{{ADRES}}</b></div></div>
    <div class="c-item rv"><span class="ico">{{I_CLOCK}}</span><div><small>Godziny</small><b>Czynne całą dobę, 7 dni w tygodniu</b></div></div>
    <div class="map-box rv" style="margin-top:8px">{{MAPA}}</div>
  </div>
  <div class="form-card rv" id="wycena">
    <h2 style="font-size:1.8rem">Formularz wyceny</h2>
    <p style="color:var(--ink-2)">Opisz samochód. Oddzwonimy z propozycją ceny i terminem odbioru.</p>
    {{QUOTE}}
  </div>
</div></section>
"""

FAQ_SKUP = [
    ('Czy kupujecie auta bez ważnego OC i przeglądu?', FAQ_HOME[0][1]),
    ('Czy odbiór auta jest płatny?', 'Nie. Samochód odbieramy lawetą bezpłatnie z terenu województwa śląskiego i małopolskiego.'),
    ('Jakie dokumenty są potrzebne do sprzedaży auta?', 'Dowód rejestracyjny, karta pojazdu, jeśli była wydana, oraz dowód osobisty właściciela. Jeżeli auto ma kilku współwłaścicieli, każdy z nich musi podpisać umowę.'),
    ('Czy kupujecie auta ciężarowe?', 'Tak. Skupujemy samochody osobowe i ciężarowe, zarówno sprawne, jak i uszkodzone.'),
    ('Jak szybko możecie odebrać auto?', 'Termin odbioru ustalamy podczas rozmowy telefonicznej, dopasowując go do Twoich możliwości.'),
]
FAQ_ZLOM = [
    ('Czy za auto do kasacji dostanę pieniądze?', 'Tak. Za samochód przeznaczony do złomowania płacimy. Kwota zależy od masy, kompletności i stanu pojazdu.'),
    ('Czy auto musi być kompletne?', 'Nie. Odbieramy także samochody niekompletne, bez kół, bez silnika lub po pożarze. Przy zgłoszeniu warto opisać, czego brakuje.'),
    ('Jak odzyskać składkę OC po złomowaniu?', FAQ_HOME[3][1]),
    ('Ile kosztuje odbiór auta do kasacji?', 'Odbiór lawetą jest bezpłatny na terenie województwa śląskiego i małopolskiego.'),
    ('Czy trzeba wyrejestrować auto przed złomowaniem?', 'Nie. Auto wyrejestrowuje się dopiero po kasacji, na podstawie zaświadczenia o demontażu pojazdu.'),
]

STRONY = [
    dict(plik='index.html', nav='index.html', title='Skup i złomowanie aut Zawiercie, Śląsk i Małopolska | BED-CAR',
         desc='Skup aut całych, uszkodzonych i powypadkowych oraz złomowanie. Laweta gratis, auta bez OC i przeglądu, czynne 24/7. Tel. ' + TEL + '.',
         body=INDEX, faq=FAQ_HOME, preload='assets/img/hero-laweta.webp', wycena='#wycena'),
    dict(plik='skup-aut.html', nav='skup-aut.html', title='Skup aut za gotówkę: całe, uszkodzone, powypadkowe | BED-CAR',
         desc='Skup samochodów osobowych i ciężarowych w każdym stanie na Śląsku i w Małopolsce. Bezpłatny odbiór lawetą. Tel. ' + TEL + '.',
         body=SKUP, faq=FAQ_SKUP, wycena='#wycena',
         ph=ph('Skup aut', '', 'Skup aut <em class="acc">w każdym</em> stanie',
               'Kupujemy samochody osobowe i ciężarowe: sprawne, uszkodzone, powypadkowe, bez OC i przeglądu. Odbieramy je lawetą bez opłat.',
               'kasacja.webp', 'Uszkodzone samochody')),
    dict(plik='zlomowanie-aut.html', nav='zlomowanie-aut.html', title='Złomowanie aut, kasacja pojazdów, zwrot OC | BED-CAR',
         desc='Złomowanie samochodów na Śląsku i w Małopolsce. Płacimy za auto do kasacji, odbiór lawetą gratis, pomoc przy zwrocie składki OC. Tel. ' + TEL + '.',
         body=ZLOM, faq=FAQ_ZLOM, wycena='#wycena',
         ph=ph('Złomowanie aut', '', 'Złomowanie aut <em class="acc">z odbiorem</em> lawetą',
               'Odbieramy auta do kasacji w każdym stanie, płacimy za nie i pomagamy w formalnościach, w tym przy zwrocie składki OC.',
               'zlomowanie.webp', 'Samochody przeznaczone do kasacji')),
    dict(plik='kontakt.html', nav='kontakt.html', title='Kontakt: skup i złomowanie aut | BED-CAR',
         desc='BED-CAR, ' + ADRES + '. Telefon ' + TEL + ', czynne całą dobę. Skup i złomowanie aut na Śląsku i w Małopolsce.',
         body=KONTAKT, faq=None, wycena='#wycena'),
]


def main():
    from PIL import Image
    logo_h = Image.open('assets/img/logo-ciemne.png').size[1]
    mapa = open('assets/mapa-obszar.svg').read()
    cssv, jsv = ver('assets/styles.css'), ver('assets/main.js')
    amber = lambda s: s.replace('<svg ', '<svg style="color:var(--amber-2)" ', 1)
    for s in STRONY:
        url = BAZA + ('' if s['plik'] == 'index.html' else s['plik'])
        nav = ''.join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == s['nav'] else '', t) for h, t in NAV)
        graf = [biznes_ld(), {'@type': 'WebPage', 'url': url, 'name': s['title'], 'about': {'@id': BAZA + '#firma'}}]
        if s['faq']:
            graf.append(faq_ld(s['faq']))
        ld = json.dumps({'@context': 'https://schema.org', '@graph': graf}, ensure_ascii=False)
        pre = '<link rel="preload" as="image" href="%s" media="(min-width:621px)">\n' % s['preload'] if s.get('preload') else ''
        chips = '<span class="base">Zawiercie (baza)</span>' + ''.join('<span>%s</span>' % m for m in MIASTA[1:])
        html = HEAD + s['body'] + FOOT
        rep = {
            '{{PH}}': s.get('ph', ''), '{{QUOTE}}': quote(s['plik'][:4] + '-'), '{{FAQ}}': faq_html(s['faq']) if s['faq'] else '',
            '{{MAPA}}': mapa, '{{CHIPS}}': chips, '{{NAV}}': nav, '{{LD}}': ld, '{{PRELOAD}}': pre,
            '{{TITLE}}': s['title'], '{{DESC}}': s['desc'], '{{URL}}': url, '{{BAZA}}': BAZA, '{{CSSV}}': cssv, '{{JSV}}': jsv,
            '{{LOGOH}}': str(logo_h), '{{WYCENA}}': s['wycena'],
            '{{I_CLOCK_AMBER}}': amber(I['clock']).replace('<svg ', '<svg width="30" height="30" ', 1),
            '{{I_TRUCK_AMBER}}': I['truck'], '{{I_WRENCH_AMBER}}': I['wrench'],
        }
        for k, v in rep.items():
            html = html.replace(k, v)
        for k, v in I.items():
            html = html.replace('{{I_%s}}' % k.upper(), v)
        for k, v in {'{{TEL_HREF}}': TEL_HREF, '{{TEL}}': TEL, '{{MAIL}}': MAIL, '{{ADRES}}': ADRES}.items():
            html = html.replace(k, v)
        assert '{{' not in html, (s['plik'], html[html.index('{{'):html.index('{{') + 40])
        open(s['plik'], 'w').write(html)
        print('ok', s['plik'], len(html) // 1024, 'kB')


if __name__ == '__main__':
    main()
