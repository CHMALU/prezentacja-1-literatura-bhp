"""Literatura do Prezentacji I: metadane z DOI, cytowania z OpenAlex, stan pobranych PDF-ów.

Temat: „System automatycznego wykrywania naruszeń BHP w czasie rzeczywistym”.
Adaptacja ~/Projects/prywatne/inzynierka/scripts/literatura.py (tylko biblioteka standardowa).

    python3 literatura.py fetch   # metadane (doi.org, OpenAlex) -> literatura-meta.json + bibliografia.bib
    python3 literatura.py         # zbiera PDF-y do pdf/ i generuje literatura.md

Przy generowaniu pasujące PDF-y z ~/Pobrane, ~/Downloads i z tego katalogu (także zapisane strony HTML
z PDF-em w folderze *_files), zmienione w ostatnich `--days` dniach (domyślnie 2), są przenoszone
do pdf/. Pozycja jest rozpoznawana po DOI albo tytule w tekście pierwszych stron (pdftotext),
więc nazwa pliku nie ma znaczenia.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import shutil
import subprocess
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
META = ROOT / "literatura-meta.json"
BIB = ROOT / "bibliografia.bib"
OUT = ROOT / "literatura.md"
PDF_DIR = ROOT / "pdf"
INBOXES = [Path.home() / "Pobrane", Path.home() / "Downloads", ROOT]

# (grupa, DOI, rdzeń ★, po co / co z niej wynika — sprawdzone w abstrakcie 2026-10-10)
ENTRIES = [
    ("det", "10.1109/cvpr.2016.91", 1,
     "źródło pierwotne YOLO: detekcja jako jedna regresja ramek i klas w jednym przebiegu sieci, 45 FPS — "
     "dlaczego detektor jednoetapowy nadaje się do wideo w czasie rzeczywistym"),
    ("det", "10.3390/make5040083", 1,
     "przegląd YOLOv1–v8 i YOLO-NAS z metrykami (mAP, NMS) i zmianami architektury — do uzasadnienia "
     "wyboru konkretnej wersji YOLO"),
    ("det", "10.1109/tpami.2016.2577031", 0,
     "Faster R-CNN, detektor dwuetapowy (5 FPS na GPU) — punkt odniesienia dla YOLO; użyli go Fang i in. (2018)"),
    ("det", "10.1109/icip.2017.8296962", 0,
     "DeepSORT: śledzenie osób między klatkami — żeby naruszenie liczyć raz na osobę, a nie w każdej klatce"),
    ("ppe", "10.1016/j.autcon.2017.09.018", 1,
     "klasyk dziedziny: Faster R-CNN wykrywa brak kasku na nagraniach z kamer monitoringu z dużej odległości "
     "(ponad 100 tys. klatek z 25 budów)"),
    ("ppe", "10.1016/j.autcon.2020.103085", 1,
     "**najbliższe tematowi:** kask + kamizelka w czasie rzeczywistym (YOLOv3), trzy warianty: detekcja elementów "
     "+ klasyfikator albo od razu klasa pracownika (bez kasku i kamizelki / tylko kask / tylko kamizelka / oba); "
     "mAP 72–86% wg repozytorium autorów, zbiór Pictor-v3 i kod otwarte"),
    ("ppe", "10.3390/s21103478", 1,
     "osiem wariantów YOLO (v3–v5) na otwartym zbiorze CHV (kaski w 4 kolorach, osoba, kamizelka): YOLOv5x "
     "mAP 86,55%, YOLOv5s 52 FPS na GPU — gotowy zbiór na start i punkt odniesienia dla wyników"),
    ("ppe", "10.1109/access.2024.3451117", 1,
     "system PPE na nagraniach z kamer monitoringu, od zbierania danych po wdrożenie (YOLOv7, CenterNet, ViT); "
     "mAP spada z 92,4% do 66,7% na nagraniu z innego miejsca i pod innym kątem — argument za uczeniem "
     "na własnych nagraniach z placu"),
    ("ppe", "10.1016/j.autcon.2019.102894", 0,
     "otwarty zbiór GDUT-HWD (3174 zdjęcia, kaski z kolorami), SSD z mechanizmem uwagi, mAP 83,89%"),
    ("ppe", "10.1016/j.autcon.2021.103828", 0,
     "pose estimation sprawdza, czy kask i kamizelka są noszone, a nie tylko widoczne w kadrze; F1 0,97 i 0,95 "
     "na zbiorze autorów (wynik na własnych danych — traktować ostrożnie)"),
    ("ppe", "10.1038/s41598-025-12468-8", 0,
     "najnowsze wyniki: YOLOv10 z backbone Swin Transformer na nagraniach z monitoringu i kamer nasobnych; "
     "AP50 brak kasku 92,4%, brak kamizelki 87,2%"),
    ("ppe", "10.1016/j.jnlssr.2024.09.002", 0,
     "zbiór SH17: 8099 zdjęć, 17 klas PPE z zakładów przemysłowych, YOLOv9-e ponad 70,9% — gdyby zakres "
     "wychodził poza kask i kamizelkę"),
    ("sys", "10.1109/mc.2017.3641638", 1,
     "analityka wideo na żywo w dużej skali wymaga architektury rozproszonej: kamery – brzeg sieci – chmura — "
     "uzasadnienie „rozproszonego systemu” z tematu"),
    ("sys", "10.17487/rfc2326", 1,
     "specyfikacja RTSP 1.0, przez który kamery IP udostępniają strumień — źródło normatywne do modułu akwizycji"),
    ("sys", "10.1109/access.2022.3215148", 1,
     "system PPE (kask, kamizelka, rękawice) na strumieniu z kamery, liczony na brzegu (Raspberry Pi + Intel NCS2): "
     "porównanie 5 sieci pod kątem trafności, opóźnienia i klatek/s — kontrast dla centralnego komputera kolegi"),
    ("sys", "10.1007/s11554-023-01368-7", 0,
     "tani system PPE na urządzeniach brzegowych z detekcją i śledzeniem; alarm z informacji czasowej (kilka klatek), "
     "nie z pojedynczej klatki — wzorzec dla klasyfikacji naruszeń"),
    ("sys", "10.1109/comst.2023.3323091", 0,
     "przegląd edge video analytics: architektury, frameworki, zbiory danych — gdy trzeba szerzej opisać "
     "przetwarzanie strumieni"),
    ("bud", "10.1016/j.autcon.2019.103013", 1,
     "przegląd CV i DL w bezpieczeństwie budowy: co już wykrywa się automatycznie i co blokuje wdrożenia "
     "(dokładność, niezawodność, trudność pozyskania nagrań z monitoringu)"),
    ("ml", "10.1109/access.2023.3262138", 1,
     "MLOps: definicja, zasady, komponenty i architektura (wersjonowanie danych i modeli, automatyzacja, "
     "monitoring) — rama dla „pełnego procesu inżynierii danych” z tematu"),
    ("ml", "10.1109/icse-seip.2019.00042", 0,
     "jak zespoły Microsoft budują aplikacje AI (9 etapów); dane trudniej wersjonować, a modele trudniej "
     "traktować jak osobne moduły niż zwykły kod"),
    ("ml", "10.1145/3533378", 0,
     "przegląd problemów wdrożeniowych ML na każdym etapie: dane, uczenie, weryfikacja, wdrożenie"),
]
# legalne wersje otwarte: (etykieta, link, identyfikatory w nazwie/tekście pliku)
ALT = {
    "10.1109/cvpr.2016.91": ("arXiv, otwarty", "https://arxiv.org/abs/1506.02640", ["1506.02640"]),
    "10.1109/tpami.2016.2577031": ("arXiv, otwarty", "https://arxiv.org/abs/1506.01497", ["1506.01497"]),
    "10.1109/icip.2017.8296962": ("arXiv, otwarty", "https://arxiv.org/abs/1703.07402", ["1703.07402"]),
    "10.17487/rfc2326": ("rfc-editor.org, otwarty", "https://www.rfc-editor.org/rfc/rfc2326", ["rfc2326"]),
}
# rekordy, przy których wyszukiwanie po tytule łapie inne prace (bez korekty o osobny rekord)
NO_ALT = {"10.17487/rfc2326"}
# statusy OA w OpenAlex, przy których tekst jest za darmo u wydawcy (bronze = darmowy do czytania bez licencji)
OPEN_STATUSES = {"gold", "diamond", "hybrid", "bronze"}

# prace bez DOI: (grupa, ★, cytowania OpenAlex 2026-10-10, opis, po co, gdzie pobrać,
# klucze: "name:" = fragment nazwy pliku, pozostałe = fragment tekstu pierwszych stron)
BOOKS = [
    ("ml", 1, 825,
     "Sculley D., Holt G., Golovin D. i in. (2015). Hidden Technical Debt in Machine Learning Systems. "
     "*Advances in Neural Information Processing Systems* 28 (NIPS 2015).",
     "dług techniczny w systemach ML: model to mały fragment systemu, resztę stanowią dane, konfiguracja, "
     "zależności i monitoring — uzasadnienie podejścia inżynierskiego, nie tylko „wytrenuj model”",
     "[NeurIPS, otwarty](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)",
     ["name:86df7dcfd896fcaf2674f757a2463eba", "name:hiddentechnicaldebtinmachinelearningsystems",
      "hiddentechnicaldebtinmachinelearningsystems"]),
]
BOOK_TODO: dict[str, str] = {}
GROUPS = [
    ("ppe", "Detekcja kasków i kamizelek (PPE) — najbliższe tematowi", "wątek 2"),
    ("sys", "Strumienie wideo z kamer i systemy czasu rzeczywistego", "wątek 1"),
    ("det", "Detekcja obiektów: podstawy (YOLO i inne)", "wątek 2"),
    ("bud", "Computer vision w bezpieczeństwie budowy — przegląd", "wątek 3"),
    ("ml", "Inżynieria danych i ML w aplikacji (MLOps)", "wątek 4"),
]
# wydawcy z listy e-zasobów Biblioteki PWr (biblioteka.pwr.edu.pl/en/e-resources/e-books, sprawdzone 2026-10-08)
PWR = {"Elsevier BV": "Elsevier", "Springer Science and Business Media LLC": "Springer", "Wiley": "Wiley",
       "Institute of Electrical and Electronics Engineers (IEEE)": "IEEE", "IEEE": "IEEE",
       "ACM": "ACM", "Association for Computing Machinery (ACM)": "ACM"}
SHORT = {"MDPI AG": "MDPI", "RFC Editor": "RFC Editor"}

TOP = """## Od czego zacząć (na 15 minut wystarczą te 4)

1. **Nath i in. (2020)**: robi prawie to samo zadanie (kask + kamizelka, YOLO, czas rzeczywisty), więc to
   główny punkt odniesienia. Warianty „detekcja elementów + reguła” i „klasa pracownika od razu” to gotowy
   materiał na pytanie z dyskusji „jak klasyfikujesz naruszenie?”.
2. **Al-Azani i in. (2024)**: system na nagraniach z kamer monitoringu, od danych po wdrożenie. Spadek mAP
   z 92% do 67% na nagraniu z innego miejsca i pod innym kątem uzasadnia, czemu praca uczy model na
   nagraniach z własnego placu.
3. **Gallo i in. (2022)**: system czasu rzeczywistego na strumieniu z kamery (wariant brzegowy). Dobrze
   pokazuje, czym różni się architektura kolegi: kilka kamer RTSP, jeden komputer, kolejka strumieni i GUI.
4. **Redmon i in. (2016)** albo przegląd **Terven i in. (2023)**: podstawa metody, czyli dlaczego YOLO.

Fang i in. (2018) warto mieć na slajdzie jako klasyk dziedziny, a Sculley i in. (2015) albo Kreuzberger
i in. (2023) jako jedno zdanie o aspekcie inżynierskim. Szkic slajdu: `slajd-istniejace-rozwiazania.md`.

"""


# --- pobieranie metadanych -----------------------------------------------------------------

def get(url: str, accept: str = "application/json", tries: int = 4) -> bytes | None:
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": "prezentacja-literatura"})
            return urllib.request.urlopen(req, timeout=60).read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
        except (urllib.error.URLError, TimeoutError):
            pass
        time.sleep(3 * (attempt + 1))
    return None


def openalex(path: str, params: dict | None = None) -> dict | None:
    url = "https://api.openalex.org/" + path + ("?" + urllib.parse.urlencode(params) if params else "")
    raw = get(url)
    time.sleep(0.3)
    return json.loads(raw) if raw else None


def fetch() -> None:
    meta, bibs = {}, []
    for group, doi, _, _ in ENTRIES:
        doi_url = "https://doi.org/" + urllib.parse.quote(doi, safe="/")
        csl = json.loads(get(doi_url, "application/vnd.citationstyles.csl+json") or b"{}")
        bib = (get(doi_url, "application/x-bibtex; charset=utf-8") or b"").decode("utf-8").strip()
        if bib:
            bibs.append(clean_bib(bib))
        work = openalex("works/" + urllib.parse.quote("https://doi.org/" + doi, safe=":/"),
                        {"select": "cited_by_count,open_access"}) or {}
        oa = work.get("open_access") or {}
        rec = {"csl": csl, "cites": work.get("cited_by_count"), "oa": oa.get("is_oa"),
               "oa_status": oa.get("oa_status"), "oa_url": oa.get("oa_url")}
        title = " ".join(html.unescape(csl.get("title", "")).replace(":", " ").replace(",", " ").split())[:120]
        if doi not in NO_ALT and title:
            res = (openalex("works", {"filter": f"title.search:{title}", "per_page": 5, "select": "cited_by_count"})
                   or {}).get("results", [])
            best = max((w["cited_by_count"] for w in res), default=0)
            if best > 1.25 * (rec["cites"] or 0):
                rec["cites_alt"] = best
        meta[doi] = rec
        print(f"{group:5} {rec['cites']!s:>7} {csl.get('title', '?')[:70]}")
    bibs.append(SCULLEY_BIB)
    META.write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    BIB.write_text("\n\n".join(bibs) + "\n", encoding="utf-8")
    print(f"zapisano {META.name} ({len(meta)}) i {BIB.name} ({len(bibs)})")


def clean_bib(bib: str) -> str:
    """Poprawki pod LaTeX: encje HTML z rejestru DOI, półpauza w stronach, przedrostek nazwiska w imieniu."""
    bib = html.unescape(bib).replace("&", "\\&").replace("–", "--")
    return re.sub(r"(\w+), (\w+) (Di|De|Van|Von)\b", r"\3 \1, \2", bib)


# BibTeX ze strony NeurIPS (papers.nips.cc, plik -Bibtex.bib), strony nie są podane w rekordzie
SCULLEY_BIB = """@inproceedings{Sculley_2015,
 author = {Sculley, D. and Holt, Gary and Golovin, Daniel and Davydov, Eugene and Phillips, Todd and Ebner, Dietmar and Chaudhary, Vinay and Young, Michael and Crespo, Jean-Fran\\c{c}ois and Dennison, Dan},
 booktitle = {Advances in Neural Information Processing Systems},
 editor = {C. Cortes and N. Lawrence and D. Lee and M. Sugiyama and R. Garnett},
 publisher = {Curran Associates, Inc.},
 title = {Hidden Technical Debt in Machine Learning Systems},
 url = {https://proceedings.neurips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf},
 volume = {28},
 year = {2015}
}"""


# --- rozpoznawanie PDF-ów -------------------------------------------------------------------

def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def pdf_text(path: Path) -> str:
    try:
        out = subprocess.run(["pdftotext", "-l", "6", str(path), "-"], capture_output=True, timeout=60)
        return out.stdout.decode("utf-8", "ignore")
    except (OSError, subprocess.TimeoutExpired):
        return ""


def is_pdf(path: Path) -> bool:
    try:
        with open(path, "rb") as f:
            return f.read(5) == b"%PDF-"
    except OSError:
        return False


def safe_name(fam: str, yr, title: str) -> str:
    """Nazwa pliku z prawdziwego tytułu: „Nazwisko rok - Tytuł.pdf” (bez znaków niedozwolonych w nazwach)."""
    fam = unicodedata.normalize("NFKD", fam.title() if fam.isupper() else fam).encode("ascii", "ignore").decode()
    title = " ".join(html.unescape(re.sub(r"</?i>", "", title)).split())
    title = re.sub(r'[<>"\\|?*]', "", title.replace(": ", " - ").replace(":", " -").replace("/", "-"))
    return f"{fam} {yr} - {title}"[:180].rstrip(" .-") + ".pdf"


def file_name(rec: dict) -> str:
    c = rec["csl"]
    return safe_name((c.get("author") or [{}])[0].get("family", "X"), year(c), c.get("title", ""))


def book_file_name(ref: str) -> str:
    who, _, rest = ref.partition("). ")
    return safe_name(who.split()[0].rstrip(","), who.rsplit("(", 1)[-1], rest.split(". *")[0])


def pages(path: Path) -> int:
    try:
        out = subprocess.run(["pdfinfo", str(path)], capture_output=True, timeout=30).stdout.decode("utf-8", "ignore")
        return int(re.search(r"^Pages:\s+(\d+)", out, re.M).group(1))
    except (OSError, subprocess.TimeoutExpired, AttributeError):
        return 0


def identify(path: Path, meta: dict, strong_only: bool = False) -> str | None:
    """DOI albo opis pracy bez DOI, któremu odpowiada plik; None, gdy nie pasuje do listy.

    Kolejność: identyfikatory w nazwie pliku (DOI, PII Elseviera, arXiv), DOI w tekście, tytuł
    w tekście (przy kilku trafieniach najdłuższy — tytuł jednej pracy bywa fragmentem tytułu innej),
    na końcu klucze prac bez DOI. `strong_only` = tylko identyfikatory i DOI: tak rozpoznajemy pliki spoza
    pdf/, bo np. wykład cytujący pracę ma jej tytuł w tekście.
    """
    name = norm(path.name)
    for doi, rec in meta.items():
        c = rec["csl"]
        ids = [doi.rsplit("/", 1)[-1]] + (c.get("alternative-id") or []) + (ALT[doi][2] if doi in ALT else [])
        if doi.startswith("10.48550/arxiv."):
            ids.append(doi.split("arxiv.")[1])
        if path.name == file_name(rec) or any(len(norm(i)) >= 7 and norm(i) in name for i in ids):
            return doi
        title = norm(html.unescape(c.get("title", "")))[:40]
        if len(title) >= 25 and title in name:        # IEEE nazywa pliki pełnym tytułem artykułu
            return doi
    for book in BOOKS:
        if any(k.startswith("name:") and k[5:] in name for k in book[6]):
            return book[3]
    text = pdf_text(path)
    text_l, text_n = text.lower(), norm(text[:8000])
    for doi in meta:
        if doi.lower() in text_l or any(a.lower() in text_l for a in (ALT[doi][2] if doi in ALT else [])):
            return doi
    if strong_only:
        return None
    hits = [(len(tn), doi) for doi, rec in meta.items()
            if len(tn := norm(html.unescape(rec["csl"].get("title", "")))[:60]) >= 15 and tn in text_n]
    if hits:
        return max(hits)[1]
    for book in BOOKS:
        if any(not k.startswith("name:") and k in text_n for k in book[6]):
            return book[3]
    return None


def collect(meta: dict, days: float) -> dict[str, list[str]]:
    """Przenosi pasujące PDF-y z ostatnich `days` dni do pdf/; zwraca {DOI lub opis: pliki}."""
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    since = time.time() - days * 86400
    candidates = []
    for box in INBOXES:
        if box.exists():
            candidates += [p for p in box.glob("*.pdf")]
            candidates += [p for d in box.glob("*_files") if d.is_dir() for p in d.glob("*.pdf")]
    candidates = [p for p in candidates if p.stat().st_mtime >= since]
    for path in candidates:
        if not is_pdf(path) or identify(path, meta, strong_only=True) is None:
            continue
        if pages(path) <= 1:   # „Drukuj → Zapisz jako PDF” w podglądzie IEEE daje tylko 1. stronę artykułu
            print(f"pominięty (1 strona — wydruk podglądu, nie artykuł; pobierz ikoną pobierania): {path}")
            continue
        target = PDF_DIR / path.name
        if target.exists():
            print(f"pominięty (już jest plik o tej nazwie): {path}")
            continue
        shutil.move(str(path), target)
        print(f"przeniesiony: {path} -> {target.relative_to(ROOT)}")
    found = {}
    for path in sorted(PDF_DIR.glob("*.pdf")):
        key = identify(path, meta) if is_pdf(path) else None
        if key is None:
            print(f"nierozpoznany plik w pdf/: {path.name}")
            continue
        if pages(path) <= 1:
            print(f"za krótki (1 strona — wydruk podglądu, nie artykuł): {path.name}")
            continue
        nice = file_name(meta[key]) if key in meta else book_file_name(key)
        if path.name != nice and not (PDF_DIR / nice).exists():   # nazwa = prawdziwy tytuł pracy
            path = path.rename(PDF_DIR / nice)
            print(f"nazwa zmieniona na: {nice}")
        found.setdefault(key, []).append(path.name)
    return found


def have_text(files: list[str] | None) -> str | None:
    if not files:
        return None
    return files[0] if len(files) == 1 else f"{files[0]} + {len(files) - 1} plik(i)"


# --- generowanie listy ----------------------------------------------------------------------

PARTICLES = {"di", "de", "da", "del", "van", "von", "le", "la"}   # rejestr DOI bywa daje „Di” w imieniu


def authors(c: dict) -> str:
    def name(a):
        f, given = a.get("family", a.get("literal", "?")), a.get("given", "").split()
        if len(given) > 1 and given[-1].lower() in PARTICLES:
            f = f"{given.pop()} {f}"
        f = f.title() if f.isupper() else f
        initials = "".join(x[0] + "." for x in " ".join(given).replace("-", " ").replace(".", " ").split())
        return f"{f} {initials}".strip()
    names = [name(a) for a in c.get("author") or []]
    return ", ".join(names[:3]) + (" i in." if len(names) > 3 else "")


def year(c: dict):
    return (c.get("published-print") or c.get("published") or c.get("issued") or {}).get("date-parts", [[None]])[0][0]


def venue(c: dict) -> str:
    v = c.get("container-title") or c.get("publisher") or ""
    v = html.unescape(v[0] if isinstance(v, list) else v)
    vol, iss, pg = c.get("volume"), c.get("issue"), c.get("page")
    rfc = re.match(r"10\.17487/rfc(\d+)", c.get("DOI", ""), re.I)   # RFC: numer dokumentu z DOI
    num = rfc.group(1) if rfc else None
    return (f"*{v}*" + (f" {vol}" if vol else "") + (f"({iss})" if iss else "") + (f", {pg}" if pg else "")
            + (f", RFC {num}" if num else ""))


def where(doi: str, rec: dict, title: str, have: str | None) -> str:
    if have:
        return f"✓ pobrane (`{have}`)"
    pub, url = rec["csl"].get("publisher") or "", "https://doi.org/" + urllib.parse.quote(doi, safe="/:;()")
    name = PWR.get(pub) or SHORT.get(pub, pub)
    alt = f"[{ALT[doi][0]}]({ALT[doi][1]}) · " if doi in ALT else ""
    if rec.get("oa_status") == "bronze" and pub in PWR:   # darmowy do czytania u wydawcy, ale bez licencji OA
        link = f"[{name}, otwarty lub przez PWr]({url})"
    elif rec.get("oa_status") in OPEN_STATUSES:
        link = f"[{name}, otwarty]({url})"
    elif pub in PWR:
        link = f"[{name}, przez PWr]({url})"
    elif alt:
        link = f"[{name}]({url})"
    else:
        link = f"[{name}, poza listą PWr, spróbuj]({url})"
    scholar = "https://scholar.google.com/scholar?q=" + urllib.parse.quote(f'"{title}"')
    return f"{alt}{link} · [Scholar]({scholar})"


def render(meta: dict, found: dict[str, list[str]]) -> None:
    notes = {doi: (group, star, note) for group, doi, star, note in ENTRIES}
    lines, summary = [], []
    for key, gtitle, thread in GROUPS:
        items = []
        for doi, rec in meta.items():
            group, star, note = notes[doi]
            if group != key:
                continue
            c, cites = rec["csl"], rec.get("cites")
            cite_txt = str(cites) if cites is not None else "n/d w OpenAlex — sprawdzić w Google Scholar"
            if rec.get("cites_alt"):
                cite_txt += f" (+{rec['cites_alt']} w osobnym rekordzie wersji wstępnej)"
                cites = max(cites or 0, rec["cites_alt"])
            title = " ".join(html.unescape(c.get("title", "").replace("<i>", "").replace("</i>", "")).split())
            ref = f"{authors(c)} ({year(c)}). {title}. {venue(c)}."
            items.append((star, cites or 0, ref, cite_txt, where(doi, rec, title, have_text(found.get(doi))), note,
                          f"{authors(c)} ({year(c)}). *{title[:90]}*"))
        for group, star, cites, ref, note, link, _ in BOOKS:
            if group == key:
                got = have_text(found.get(ref))
                todo = BOOK_TODO.get(ref.split()[0].rstrip(","))
                mark = f"✓ pobrane (`{got}`)" + (f" · **{todo}**" if todo else "") if got else link
                who, _, rest = ref.partition("). ")
                brief = f"{who}). *{rest.split('. *')[0]}*"
                items.append((star, cites or 0, ref, f"{cites} (bez DOI, OpenAlex zaniża)" if cites else "—",
                              mark, note, brief))
        items.sort(key=lambda x: (-x[0], -x[1]))
        lines += [f"## {gtitle} ({thread})", "", "| | Pozycja | Cytowania | Gdzie pobrać | Po co / co z niej wynika |",
                  "|---|---|---|---|---|"]
        for star, _, ref, cite_txt, link, note, brief in items:
            lines.append(f"| {'★' if star else ''} | {ref.replace('|', '/')} | {cite_txt} | {link} | {note} |")
            summary.append((star, brief, link))
        lines.append("")

    have = [s for s in summary if s[2].startswith("✓")]
    miss_core = [s for s in summary if s[0] and not s[2].startswith("✓")]
    rest = [s for s in summary if not s[0] and not s[2].startswith("✓")]
    core_total = sum(1 for s in summary if s[0])
    status = [
        f"## Stan pobrania (odświeżone {dt.date.today().isoformat()})", "",
        f"**Masz {len(have)} z {len(summary)} pozycji, z rdzenia ★ {core_total - len(miss_core)} z {core_total}.**", "",
        f"### Brakuje z rdzenia ★ ({len(miss_core)}) — do pobrania w pierwszej kolejności", "",
        *[f"- [ ] {r} — {w}" for _, r, w in miss_core],
        "", f"### Masz już ({len(have)})", "",
        *[f"- [x] {'★ ' if st else ''}{r} — `{w.split('`')[1]}`" for st, r, w in have],
        "", f"Pozostałe ({len(rest)}) to zapas — linki w tabelach niżej.", "", "---", "",
    ]
    stars = sum(e[2] for e in ENTRIES) + sum(b[1] for b in BOOKS)
    header = f"""# Literatura do Prezentacji I — „System automatycznego wykrywania naruszeń BHP w czasie rzeczywistym”

{len(summary)} pozycji, z czego {stars} oznaczonych ★ to rdzeń na slajd „Istniejące rozwiązania” (cel: 8–12
pozycji). Reszta to zapas na pytania z dyskusji albo na później do pracy. Wszystkie pozycje sprawdzone:
metadane z rejestru DOI, treść z abstraktu (przy Nath i in. 2020 wyniki z repozytorium autorów, bo
abstrakt jest tylko u wydawcy). Plik generuje `literatura.py`, więc zmiany wprowadzać w skrypcie.

- **Wyszukiwanie (2026-10-10):** OpenAlex (tytuł + abstrakt, sortowanie po cytowaniach), osobno dla czterech
  wątków tematu, plus weryfikacja po tytule klasyków.
- **Cytowania** wg OpenAlex z 2026-10-10. Google Scholar zwykle pokazuje więcej, Scopus mniej.
- **Gdzie pobrać:** „otwarty” = za darmo, bez logowania; „przez PWr” = wydawca z listy e-zasobów PWr
  (Elsevier, Springer, Wiley, IEEE, ACM): działa w sieci uczelni albo z domu przez VPN PWr (GlobalProtect,
  portal `vpn.student.pwr.edu.pl`, login z USOS). Gdy coś nie działa, link **Scholar** (wolna kopia zwykle
  po prawej jako [PDF]). Pobierać ręcznie, nie skryptem (masowe pobieranie z płatnych baz łamie licencję).
- **IEEE Xplore:** PDF zapisywać **ikoną pobierania na pasku podglądu PDF**. **Nie „Drukuj”** — wydruk podglądu
  ma tylko 1. stronę artykułu (skrypt takie pliki pomija). Gdy ikony nie widać: Ctrl+S → „strona kompletna”;
  pełny PDF ląduje wtedy w folderze `*_files` w Pobranych, a `python3 literatura.py` sam go stamtąd wyjmuje.
- PDF-y w `pdf/` dostają nazwy z prawdziwego tytułu: „Nazwisko rok - Tytuł.pdf”.
- ✓ = plik jest w `pdf/` (lokalnie, poza gitem). `python3 literatura.py` sam przenosi tam pasujące PDF-y
  z Pobranych i odświeża tę listę.
- BibTeX wszystkich pozycji: `bibliografia.bib`.

"""
    OUT.write_text(header + TOP + "\n".join(status + lines), encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)}: masz {len(have)}/{len(summary)}, rdzeń {core_total - len(miss_core)}/{core_total}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", nargs="?", default="render", choices=["render", "fetch"])
    parser.add_argument("--days", type=float, default=2, help="z Pobranych bierz tylko pliki z ostatnich N dni")
    args = parser.parse_args()
    if args.command == "fetch":
        fetch()
        return
    meta = json.loads(META.read_text(encoding="utf-8"))
    render(meta, collect(meta, args.days))


if __name__ == "__main__":
    main()
