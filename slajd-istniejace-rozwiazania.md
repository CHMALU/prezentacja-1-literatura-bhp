# Szkic slajdów „Istniejące rozwiązania” (Prezentacja I)

Treść na 1–2 slajdy, do przeniesienia do własnej prezentacji i przeredagowania. Liczby pochodzą z abstraktów
(przy Nath i in. 2020 z repozytorium autorów; opis zbioru testowego II u Al-Azani i in. z patentu tych samych
autorów, US 12243317 B1). Kolumna „czego brakuje” opisuje to, czego praca nie obejmuje
**według abstraktu**, więc przed wystąpieniem warto rzucić okiem na wnioski i ograniczenia w pełnym tekście
4–5 prac z tabeli. Pełne opisy i linki: `literatura.md`.

## Slajd 1: Wykrywanie kasków i kamizelek: stan wiedzy

| Praca | Podejście | Wynik | Czego brakuje względem tematu |
|---|---|---|---|
| Fang i in. (2018), *Autom. Constr.* | Faster R-CNN na nagraniach z kamer monitoringu budowy | ponad 100 tys. klatek z 25 budów | tylko kask, bez kamizelki |
| Nath i in. (2020), *Autom. Constr.* | YOLOv3, kask + kamizelka; 3 warianty klasyfikacji pracownika | mAP 72–86% | model i zbiór zdjęć (Pictor-v3), nie system wielokamerowy |
| Wang i in. (2021), *Sensors* | 8 wariantów YOLOv3–v5, otwarty zbiór CHV | mAP 86,55% (v5x), 52 FPS (v5s) | ocena modelu na 1330 zdjęciach, nie działającego systemu |
| Gallo i in. (2022), *IEEE Access* | system na brzegu: Raspberry Pi + NCS2 przy każdej kamerze | porównanie 5 CNN: trafność, opóźnienie, klatki/s | jedno słabe urządzenie na kamerę |
| Al-Azani i in. (2024), *IEEE Access* | nagrania z monitoringu (386 tys. klatek), YOLOv7 vs CenterNet vs ViT | mAP 92,4% → **66,7% w innym miejscu i pod innym kątem kamery** | model traci w nowym otoczeniu, więc potrzebne dane z docelowego placu |

**Luka, którą wypełnia praca:** jeden system, który zbiera strumienie RTSP z 4 kamer, kolejkuje je
i przetwarza na jednym komputerze, wykrywa osoby i klasyfikuje naruszenia (brak kasku, brak kamizelki),
pokazuje je w GUI, a model uczy i sprawdza na nagraniach z rzeczywistego placu robót. Prace z literatury
skupiają się zwykle na samym modelu (Nath, Wang) albo na jednej kamerze z urządzeniem brzegowym (Gallo).
Al-Azani i in. pokazują, że model przeniesiony w nowe miejsce traci ok. 25 pkt proc. mAP, co uzasadnia
uczenie na własnych danych.

## Slajd 2 (opcjonalny): Na czym opiera się praca

- **Detekcja obiektów:** YOLO, detektor jednoetapowy działający w czasie rzeczywistym (Redmon i in., 2016);
  przegląd wersji v1–v8 do wyboru modelu (Terven i in., 2023).
- **Akwizycja strumieni:** protokół RTSP, którym kamery IP udostępniają obraz (RFC 2326); analityka wideo na
  żywo wymaga architektury rozproszonej (Ananthanarayanan i in., 2017).
- **Computer vision w BHP na budowie:** przegląd zastosowań i barier wdrożenia (Fang W. i in., 2020).
- **Aspekt inżynierski:** w systemie z ML model to mały fragment całości, reszta to dane, konfiguracja
  i monitoring (Sculley i in., 2015); proces MLOps: wersjonowanie danych i modeli, wdrożenie, monitoring
  (Kreuzberger i in., 2023).

## Na pytania z dyskusji (bez slajdu)

- *„Jak klasyfikujesz naruszenie, skoro detektor widzi kask, a nie pracownika bez kasku?”* — Nath i in. (2020)
  porównują oba warianty: detekcja elementów + reguła przypisania albo od razu klasa pracownika.
  Xiong i Tang (2021) przypisują PPE do części ciała przez pose estimation.
- *„Jedna klatka bez kasku to już naruszenie?”* — Lema i in. (2023) generują alarm z kilku kolejnych klatek;
  śledzenie osób (DeepSORT, Wojke i in., 2017) pozwala liczyć naruszenie raz na osobę.
- *„Czemu nie wziąć gotowego zbioru?”* — gotowe zbiory istnieją (CHV, Pictor-v3, GDUT-HWD, SH17) i nadają się
  na start, ale Al-Azani i in. (2024) pokazują spadek trafności w nowym miejscu.
- *„Dlaczego jeden komputer, a nie przetwarzanie przy kamerze?”* — Gallo i in. (2022) opisują wariant brzegowy;
  przy 4 kamerach jeden komputer z GPU jest prostszy we wdrożeniu (to już argument kolegi, nie z literatury).
