# Literatura do Prezentacji I: system wykrywania naruszeń BHP w czasie rzeczywistym

Temat: „System automatycznego wykrywania naruszeń BHP w czasie rzeczywistym” (seminarium dyplomowe
prof. Świątka, Prezentacja I, 2026-10-12).

- **[literatura.md](literatura.md)**: lista do klikania, 22 pozycje (12 ★ = rdzeń na slajd, reszta zapas),
  przy każdej link „gdzie pobrać” i jedno zdanie „co z niej wynika”. Na górze: 4 najważniejsze pozycje.
- **[slajd-istniejace-rozwiazania.md](slajd-istniejace-rozwiazania.md)**: szkic slajdu „Istniejące
  rozwiązania” (tabela praca / podejście / wynik / czego brakuje + luka) i odpowiedzi na pytania z dyskusji.
- **[bibliografia.bib](bibliografia.bib)**: BibTeX wszystkich pozycji.
- `literatura.py`: generuje `literatura.md` (`python3 literatura.py fetch` odświeża metadane i cytowania;
  `python3 literatura.py` oznacza ✓ pobrane PDF-y, które przenosi z Pobranych do `pdf/`). PDF-y nie trafiają
  do repo.
- `kandydaci-wstepni.md`: surowe wyniki pierwszego wyszukiwania (historyczne, zastąpione przez `literatura.md`).
