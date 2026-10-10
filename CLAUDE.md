# Pomoc koledze: literatura do Prezentacji I (seminarium dyplomowe)

Ten folder jest osobny od mojej pracy (`~/Projects/prywatne/inzynierka`). Pomagamy **koledze**, który
zamienił się ze mną terminem Prezentacji I. To **jego temat pracy**, nie mój. Zakres: **tylko literatura
do jego Prezentacji I**, ewentualnie szkic slajdu o istniejących rozwiązaniach. Nie piszemy za niego
pracy ani prezentacji.

## Termin i wymagania

- **Poniedziałek 2026-10-12, 13:15**, seminarium prof. Świątka (INS I st.), kolega występuje jako 2. na liście.
  Zostały ok. 2 dni, więc liczy się szybki, sensowny wybór, a nie kompletny przegląd.
- Format: **15 min prezentacji + 5 min dyskusji.**
- Prezentacja I ma zawierać:
  1. sformułowanie tematu: cel i zakres pracy, motywacja;
  2. **ulokowanie na tle istniejących rozwiązań i literatury** ← tu pomagamy;
  3. zadania do wykonania (projektowe, badawcze).
- Wyniki ani kod **nie są wymagane** (to Prezentacja II).
- Po wystąpieniu prezentację wysyła się na jerzy.swiatek@pwr.edu.pl, nazwa pliku
  `imię_nazwisko_prezentacja_1`. Tylko jedna prezentacja w semestrze daje maksymalnie ocenę dostateczną.

## Temat kolegi (z APD)

**„System automatycznego wykrywania naruszeń BHP w czasie rzeczywistym”**

- Cel: rozproszony system zbierania i analizy danych — 4 kamery cyfrowe (RTSP) + komputer z aplikacją
  do kolejkowania i przetwarzania strumieni; aplikacja wykrywa osoby bez kasku ochronnego lub kamizelki
  odblaskowej na placu robót.
- Zakres: konfiguracja i komunikacja urządzeń; aplikacja z modułami: akwizycja strumieni wideo, GUI,
  inteligentna analiza obrazu (detekcja osób, klasyfikacja naruszeń); uczenie maszynowe na rzeczywistych
  danych wideo; weryfikacja i walidacja w środowisku rzeczywistym.
- Aspekty: inżynierski (system o zastosowaniu praktycznym) i systemowy (widzenie komputerowe, modelowanie
  matematyczne, uczenie maszynowe, projektowanie interfejsów — pełny proces inżynierii danych).
- Wątki literatury: (1) akwizycja i przetwarzanie strumieni wideo w czasie rzeczywistym (RTSP, systemy
  rozproszone, analityka wideo), (2) detekcja obiektów (YOLO i inne) i detekcja środków ochrony (kaski,
  kamizelki, zbiory danych), (3) computer vision w bezpieczeństwie budowy, (4) inżynieria danych i aplikacje
  integrujące moduły AI z GUI.

## Najpierw zapytaj o to (jeśli jeszcze nie wiadomo)

1. Temat pracy z APD (dokładny tytuł) i 2–3 zdania opisu.
2. Promotor i kierunek/specjalność (wpływa na to, czego recenzent oczekuje).
3. Słowa kluczowe po polsku i angielsku; czy ma już jakieś źródła.
4. Czy temat jest bardziej projektowy (system, aplikacja) czy badawczy (porównanie metod).

## Co ma powstać

- `literatura.md`: **8–12 pozycji** z podziałem na grupy tematyczne; przy każdej: pełny opis
  bibliograficzny, liczba cytowań, gdzie pobrać, jedno zdanie „po co / co z niej wynika”.
- Mieszanka: 2–3 **klasyki** z dużą liczbą cytowań (pokazują, że znamy podstawy), 4–6 prac
  **najbliższych tematowi** z ostatnich ~5 lat (pokazują stan wiedzy), 1–2 **przeglądy** (survey).
  Przewaga czasopism i książek nad blogami i preprintami.
- Szkic treści 1–2 slajdów „Istniejące rozwiązania”: krótka tabela *praca / podejście / wynik /
  czego brakuje*, a pod nią zdanie, czym praca kolegi się różni (luka, którą wypełnia).
- Opcjonalnie `bibliografia.bib` z DOI.
- Forma jak w mojej pracy: **jedna lista do klikania** — przy każdej pozycji link „gdzie pobrać” (otwarty /
  przez PWr / Scholar), a po pobraniu PDF-ów oznaczenie ✓ (adaptacja `scripts/literatura.py`, patrz niżej).
  **Nie dawać list fraz wyszukiwania** do samodzielnego szukania — dostarczamy gotową, zweryfikowaną listę.
- **Stan 2026-10-10:** gotowe `literatura.md` (22 pozycje, 12 ★, generuje `literatura.py`), `bibliografia.bib`,
  `slajd-istniejace-rozwiazania.md`. `kandydaci-wstepni.md` jest już tylko historyczny.
- **Repo:** prywatne `github.com/CHMALU/prezentacja-1-literatura-bhp` (kolegę zaprasza się jako collaboratora).
  PDF-y są w `.gitignore`, bo z płatnych baz nie wolno ich udostępniać.

## Jak szukać (sprawdzone 2026-10-07/08 przy mojej pracy)

1. **Kandydaci z OpenAlex** (darmowe API, bez klucza; pokrywa to co Scopus/WoS):
   `https://api.openalex.org/works?filter=title_and_abstract.search:<fraza>,publication_year:>2015&sort=cited_by_count:desc&per_page=10`
   Szukać w tytule i abstrakcie; zwykłe `search=` sortowane po cytowaniach daje śmieci z innych dziedzin.
   Kilka fraz po angielsku, osobno dla każdego wątku tematu.
2. **Weryfikacja każdej pozycji**, także tych „z pamięci”: wyszukanie po tytule
   (`filter=title.search:<tytuł>`; dwukropki i przecinki z tytułu usunąć, bo psują filtr).
   **Nie zmyślać pozycji ani liczb** — wszystko musi mieć potwierdzenie w źródle.
3. **Metadane z DOI**: `curl -LH "Accept: application/vnd.citationstyles.csl+json" https://doi.org/<DOI>`
   (rok wydania, tom, strony; OpenAlex podaje czasem rok publikacji online). BibTeX: ten sam adres
   z `Accept: application/x-bibtex`. DOI z `<`, `>`, `#` trzeba zakodować w linku (quote).
4. **Cytowania** z OpenAlex (`cited_by_count`), z dopiskiem daty. OpenAlex bywa rozbity na dwa rekordy
   (wersja wstępna i czasopismo); wtedy podać obie liczby. Google Scholar pokazuje zwykle więcej, Scopus mniej.
5. **Treść**: przed wpisaniem „co z niej wynika” przeczytać abstrakt i wnioski (z PDF przez `pdftotext`),
   a nie streszczać z pamięci. Zbyt piękne wyniki (np. 80%+ trafności na rynkach) oznaczyć jako do ostrożnego
   traktowania.

## Dostęp do pełnych tekstów (PWr)

- Pobiera **kolega na swoim koncie PWr**. Nie udostępniać mu mojego loginu (zasady e-źródeł PWr zabraniają
  udostępniania danych logowania).
- Na kampusie bazy działają od razu; z domu przez VPN PWr (GlobalProtect, portal `vpn.student.pwr.edu.pl`,
  login AD z USOS) albo portal webowy tego VPN-a. Moja konfiguracja Ubuntu z haczykami (serwer nie podaje DNS):
  `~/baza-wiedzy/prywatne/inzynierka/vpn-pwr-ubuntu.md`.
- **Działa przez PWr (sprawdzone):** Elsevier/ScienceDirect, Springer, Wiley, IEEE Xplore, ACM Digital Library,
  ProQuest Ebook Central (`ebookcentral.proquest.com/lib/pwr`), katalog książek Primo:
  `https://omnis-pwr.primo.exlibrisgroup.com/discovery/search?vid=48OMNIS_TUR:48TUR`.
  **Nie działa:** MIT Press. Pełna lista e-zasobów: biblioteka.pwr.edu.pl/en/e-resources/e-books.
- **Haczyki:**
  - IEEE: PDF zapisywać ikoną pobierania w podglądzie. **Nie „Drukuj”** — daje tylko 1. stronę (sprawdzone
    2026-10-10, skrypt teraz takie pliki pomija). Bez ikony: Ctrl+S „strona kompletna”, PDF ląduje w `*_files`
    i skrypt go wyjmuje.
  - Ebook Central: plik `.acsm` to wypożyczenie z DRM (na Linuksie nie otworzy się); pobierać **pojedyncze
    rozdziały** jako PDF; limit **40% stron książki na 24h**.
  - Gdy brak dostępu: wersja otwarta przez Google Scholar (link [PDF] po prawej), arXiv, SSRN, strona autora.
- **Nie pobierać masowo skryptem** z płatnych baz (łamie licencję i może zablokować dostęp całej uczelni);
  automatycznie wolno tylko z otwartych źródeł (arXiv itp.).

## Narzędzie, które można zaadaptować

`~/Projects/prywatne/inzynierka/scripts/literatura.py` — moja wersja: lista pozycji na górze pliku
(`ENTRIES`, `BOOKS`, `GROUPS`), `fetch` pobiera metadane z DOI i cytowania z OpenAlex, a uruchomienie bez
argumentów rozpoznaje PDF-y (po DOI/tytule) i generuje listę z zestawieniem „masz / brakuje”. Do skopiowania
tutaj i podmiany danych na temat kolegi — ścieżki i nazwy plików w nagłówku skryptu trzeba zmienić.
Przy 8–12 pozycjach wystarczy też ręczna lista w Markdown.

## Zasady

- Ten folder i jego pliki nie trafiają do repo `inzynierka` ani do bazy wiedzy (poza krótką notatką o zamianie terminów
  w `prywatne/inzynierka/inzynierka.md`); mają własne prywatne repo (wyżej).
- Język: polski; terminy techniczne po angielsku.
- Na koniec: krótko podsumować koledze, które 3–4 pozycje są najważniejsze i dlaczego, bo na 15 minut
  więcej i tak się nie zmieści.
