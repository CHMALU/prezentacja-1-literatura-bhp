# Prezentacja I: system wykrywania naruszeń BHP w czasie rzeczywistym

Temat: „System automatycznego wykrywania naruszeń BHP w czasie rzeczywistym” (seminarium dyplomowe
prof. Świątka, Prezentacja I, 2026-10-12).

- **Prezentacja (12 slajdów, 15 min), PowerPoint w `prezentacja/`:**
  - `prezentacja_1_wykrywanie_naruszen_BHP.pptx`: z docelowymi czcionkami (Space Grotesk + IBM Plex Sans).
    Zainstaluj je najpierw (darmowe: [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk),
    [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans)), inaczej PowerPoint podstawi inne.
  - `prezentacja_1_wykrywanie_naruszen_BHP_Arial.pptx`: ta sama prezentacja na Arialu, wygląda tak samo na każdym komputerze.
  - Wersja online: https://claude.ai/artifact/7fezmZZugbnat7s5USqZS8; źródło slajdów (HTML + notatki prelegenta)
    w `prezentacja/slides/`. Notatki prelegenta są też w plikach .pptx.
  - Po wystąpieniu plik wysyła się na jerzy.swiatek@pwr.edu.pl jako `imię_nazwisko_prezentacja_1`.
- **[plan-wystapienia.md](plan-wystapienia.md)**: co uzupełnić przed wystąpieniem, przebieg z czasem na każdy slajd
  i ściąga na pytania z dyskusji (z odpowiedziami opartymi na źródłach).
- **[literatura.md](literatura.md)**: lista do klikania, przy każdej pozycji link „gdzie pobrać” i „co z niej
  wynika”. Na górze stan pobrania i 4 najważniejsze pozycje.
- **[slajd-istniejace-rozwiazania.md](slajd-istniejace-rozwiazania.md)**: tabela ze slajdu 5 i luka ze slajdu 6
  w wersji tekstowej, ze wskazaniem, skąd każda liczba.
- **[bibliografia.bib](bibliografia.bib)**: BibTeX wszystkich pozycji.
- `literatura.py`: generuje `literatura.md` (`python3 literatura.py fetch` odświeża metadane i cytowania;
  `python3 literatura.py` przenosi pasujące PDF-y z Pobranych do `pdf/`, nadaje im nazwy z tytułów i oznacza ✓).
  PDF-y nie trafiają do repo.
- `kandydaci-wstepni.md`: surowe wyniki pierwszego wyszukiwania (historyczne).
