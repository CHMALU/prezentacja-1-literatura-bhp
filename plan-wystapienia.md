# Plan wystąpienia (Prezentacja I, 15 min + 5 min dyskusji)

Prezentacja: https://claude.ai/artifact/7fezmZZugbnat7s5USqZS8 (pobierasz jako .pptx albo PDF; źródło slajdów
w `prezentacja/`). Przy każdym slajdzie są też notatki prelegenta z tym samym tekstem co tutaj.

## Przed wystąpieniem

- [ ] Uzupełnij na slajdach 1 i 12: **[Imię Nazwisko]**, **[promotor]**, **[e-mail]**.
- [ ] Przejrzyj slajdy 3, 7, 9 i 10 (cel, koncepcja, dane, zadania) i popraw wszystko, co planujesz inaczej:
      o to będą pytać najdokładniej. Szczególnie: skąd będą nagrania i na jakim komputerze to liczysz.
- [ ] Przeczytaj abstrakty i wnioski 5 prac z tabeli (slajd 5). PDF-y są do pobrania z `literatura.md`.
- [ ] Próba na głos z zegarkiem. Jeśli wychodzi ponad 15 min, skróć slajdy 8 i 9 (mówisz po jednym zdaniu).
- [ ] Po wystąpieniu: wyślij prezentację na jerzy.swiatek@pwr.edu.pl, plik `imię_nazwisko_prezentacja_1`.

## Przebieg (razem ok. 15 min)

| # | Slajd | Czas | Co powiedzieć (sedno) |
|---|---|---|---|
| 1 | Tytuł | 0:30 | Kim jesteś i temat jednym zdaniem. |
| 2 | Motywacja | 1:30 | Budownictwo to 5% poszkodowanych, ale 24% ofiar śmiertelnych (59 z 250, GUS 2024). Kontrola kasków i kamizelek jest dziś ręczna. |
| 3 | Cel pracy | 1:30 | Rozproszony system: 4 kamery IP (RTSP), komputer z aplikacją, GUI. Dwa aspekty: inżynierski i systemowy. |
| 4 | Zakres pracy | 1:00 | Cztery części z karty tematu: urządzenia, aplikacja, uczenie maszynowe, walidacja na placu. |
| 5 | Istniejące rozwiązania | 2:30 | Pięć prac, od klasyka (Fang 2018) do najbliższego systemu (Al-Azani 2024). Liczby z różnych zbiorów, więc nie ranking. |
| 6 | Luka | 1:00 | Cały system na placu, od kamer do powiadomienia, uczony i sprawdzany na nagraniach z tego placu. |
| 7 | Koncepcja systemu | 2:00 | Droga jednej klatki: akwizycja (wątki, kolejka) → YOLO na GPU → przypisanie PPE do osoby + kilka klatek → GUI. Na dole pętla uczenia. |
| 8 | Podstawy metod | 1:00 | YOLO, RTSP, przegląd CV w BHP, MLOps; każde z jednym źródłem. |
| 9 | Dane i ocena | 1:30 | Start na otwartych zbiorach (CHV, Pictor-v3), docelowo nagrania z placu; mAP, precision/recall, klatki/s przy 4 strumieniach. |
| 10 | Zadania | 2:00 | 5 projektowych (w kolejności budowy) i 4 badawcze. Wyniki będą na Prezentacji II. |
| 11 | Bibliografia | 0:30 | Nie czytać. 13 źródeł, pełne opisy w `bibliografia.bib`. |
| 12 | Dziękuję | — | Podsumowanie jednym zdaniem i pytania. |

## Ściąga na pytania z dyskusji

Każda odpowiedź ma oparcie w źródle (sprawdzone w pełnych tekstach 2026-10-10), chyba że zaznaczono „argument własny”.

**„Skąd weźmiesz dane?”**
Na start otwarte zbiory zdjęć z budów: CHV (Wang i in. 2021, 1330 zdjęć: osoba, kask w 4 kolorach, kamizelka)
i Pictor-v3 (Nath i in. 2020, ok. 1500 zdjęć). Docelowo nagrania z rzeczywistego placu: **[uzupełnij: jaka budowa,
czyja zgoda]**.

**„A prywatność pracowników?”**
Monitoring wizyjny w pracy reguluje art. 22² Kodeksu pracy (oraz RODO): jest dopuszczalny m.in. dla bezpieczeństwa
pracowników, pracowników trzeba uprzedzić (wg komentarzy co najmniej 2 tygodnie przed uruchomieniem), teren oznaczyć,
a nagrania przechowywać najwyżej 3 miesiące. Przed powołaniem się na szczegóły sprawdź aktualny tekst na ISAP.
Technicznie: Wang i in. (2021) sprawdzili rozmywanie twarzy. Wykrywanie osoby i kamizelki się nie pogarsza,
a kasku spada o ok. 7%, gdy rozmycie zachodzi na kask.

**„Jak klasyfikujesz naruszenie, skoro detektor widzi kask, a nie brak kasku?”**
Nath i in. (2020) porównali trzy warianty: (1) wykrycie osoby, kasku i kamizelki + klasyfikator, czy są noszone
(63,1% mAP, 13 klatek/s); (2) od razu klasa pracownika: bez PPE / tylko kask / tylko kamizelka / oba (72,3% mAP,
11 klatek/s); (3) wykrycie osoby + klasyfikator na wyciętym obrazie (67,9% mAP). Porównanie tych podejść to jedno
z moich zadań badawczych. Inna droga: Xiong i Tang (2021) przypisują PPE do części ciała przez pose estimation
(F1 0,97 kask, 0,95 kamizelka, ale na ich własnym zbiorze).

**„Jedna klatka bez kasku to już naruszenie?”**
Nie. Lema i in. (2023) generują alarm na podstawie informacji czasowej (kilka klatek), a nie jednej klatki.
Śledzenie osób (DeepSORT, Wojke i in. 2017) pozwala liczyć naruszenie raz na osobę, a nie w każdej klatce.

**„Dlaczego jeden komputer, a nie obliczenia przy kamerze?”**
Gallo i in. (2022) liczą na Raspberry Pi z Intel NCS2 przy kamerze. Oszczędza to łącze i chroni prywatność, ale
słaby sprzęt wymusza szybszy model: YOLOv4-Tiny, o 10,4 pkt mAP@50 słabszy od YOLOv4, który ma ok. 90% mniejszą
przepustowość. Al-Azani i in. (2024) obsługują kilka kamer jednym serwerem z GPU przy 30 klatkach/s.
Argument własny: przy 4 kamerach w jednej sieci lokalnej centralny komputer jest prostszy we wdrożeniu i aktualizacji modelu.

**„Czym różnisz się od Al-Azani i in. (2024)?”**
To najbliższa praca: kamery CCTV, silnik na GPU dla kilku źródeł, 30 klatek/s, dashboard. Różnice: dane z placu
budowy, na którym system działa (ich model spada z 92,4% do 66,7% mAP na innej kamerze w innym środowisku),
klasyfikacja naruszeń na poziomie osoby z potwierdzeniem w kilku klatkach i walidacja w środowisku rzeczywistym.

**„Dlaczego YOLO, a nie Faster R-CNN?”**
Szybkość. Faster R-CNN działa ok. 5 klatek/s na GPU (Ren i in. 2017), u Fanga i in. (2018) to ok. 0,2 s na klatkę.
YOLO w pierwszej wersji miało 45 klatek/s (Redmon i in. 2016), a YOLOv5s u Wanga i in. (2021) 52 klatki/s.
Przy 4 strumieniach naraz przepustowość jest kluczowa.

**„Ile klatek na sekundę potrzebujesz?”**
Argument własny: naruszenie (brak kasku) trwa sekundy albo minuty, więc nie trzeba analizować każdej z 25–30 klatek
z kamery. Kilka klatek na sekundę z każdej kamery wystarczy. Dokładną wartość ustalę w testach (zadanie badawcze 2).

**„Czemu tylko kask i kamizelka?”**
Tak brzmi zakres w karcie tematu. Al-Azani i in. (2024) też ograniczyli się do kasku i kamizelki, bo mniejszych PPE
(rękawice, buty) nie dało się wiarygodnie oznaczyć na nagraniach z kamer CCTV z dużej odległości.

**„Co z typowymi błędami?”**
Wang i in. (2021): zielona koszulka brana za kamizelkę, błędny kolor kasku, małe postacie daleko od kamery.
Pomaga więcej takich przykładów w danych uczących.

**„Te wyniki z tabeli są porównywalne?”**
Nie wprost: każda praca ma inny zbiór danych i inne warunki. Tabela pokazuje rząd wielkości i podejścia.
