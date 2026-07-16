import urllib.request, os

dst = r"C:\Users\Lenovo\Documents\caballos-cotizacion"

# Imágenes del sitio oficial de Salón Los Caballos
assets = [
    ("https://salonloscaballos.com.mx/banners/aTW97iBz.jpg",    "caballos_hero1.jpg"),
    ("https://salonloscaballos.com.mx/banners/88MnTVXo.jpg",    "caballos_hero2.jpg"),
    ("https://salonloscaballos.com.mx/banners/S332R86X.jpg",    "caballos_hero3.jpg"),
    ("https://salonloscaballos.com.mx/banners/u30E5R0I.jpg",    "caballos_hero4.jpg"),
    ("https://salonloscaballos.com.mx/images/B2Rus5at.jpg",     "caballos_banos.jpg"),
    ("https://salonloscaballos.com.mx/images/dQ0sR6ab.jpg",     "caballos_lounge.jpg"),
    ("https://salonloscaballos.com.mx/images/12Sm3z37.jpg",     "caballos_jardin1.jpg"),
    ("https://salonloscaballos.com.mx/images/C1Uxa0X7.jpg",     "caballos_jardin2.jpg"),
    ("https://salonloscaballos.com.mx/img/topLogo2.png",        "logo_caballos.png"),
]

for url, name in assets:
    dest = os.path.join(dst, name)
    if os.path.exists(dest):
        print(f"  [SKIP] {name}")
        continue
    try:
        print(f"  Descargando {name}...", end=" ")
        urllib.request.urlretrieve(url, dest)
        print(f"OK ({os.path.getsize(dest):,} bytes)")
    except Exception as e:
        print(f"ERROR: {e}")

print("\nListo.")
