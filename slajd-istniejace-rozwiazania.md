# Slajd „Istniejące rozwiązania” — treść sprawdzona w pełnych tekstach

To jest treść slajdów 5 i 6 gotowej prezentacji (link i plan w `plan-wystapienia.md`), tu w wersji tekstowej
do kopiowania. Wszystkie liczby sprawdzone w pełnych tekstach prac 2026-10-10.

## Slajd 5: Istniejące rozwiązania

| Praca | Podejście | Wynik | Ograniczenie |
|---|---|---|---|
| Fang i in. (2018), *Autom. Constr.* 85 | Faster R-CNN na nagraniach z kamer monitoringu 25 budów | precision 95,7%, recall 94,9% | tylko kask; ok. 0,2 s na klatkę |
| Nath i in. (2020), *Autom. Constr.* 112 | YOLOv3, kask + kamizelka, od razu klasa pracownika | 72,3% mAP, 11 klatek/s na laptopie | uczony na zdjęciach z internetu i crowdsourcingu |
| Wang i in. (2021), *Sensors* 21(10) | 8 wariantów YOLOv3–v5, otwarty zbiór CHV | 86,55% mAP (v5x); 52 klatki/s (v5s, GPU) | ocena modelu na 1330 zdjęciach, bez systemu |
| Gallo i in. (2022), *IEEE Access* 10 | system brzegowy: Raspberry Pi + Intel NCS2 przy kamerze | YOLOv4-Tiny najszybszy, o 10,4 pkt mAP słabszy od YOLOv4 | słaby sprzęt przy każdej kamerze |
| Al-Azani i in. (2024), *IEEE Access* 12 | kilka kamer CCTV, YOLOv7 na GPU, 30 klatek/s, dashboard | 92,4% mAP, ale 66,7% na innej kamerze | spadek trafności w nowym środowisku |

Pod tabelą: wyniki według autorów, na różnych zbiorach danych, więc liczby nie są wprost porównywalne.

Skąd liczby: Fang — rozdz. 6 (wnioski) i tab. 3; Nath — abstrakt i tab. 3 (wariant 2; wariant 1: 63,1% przy
13 klatkach/s); Wang — wnioski; Gallo — rozdz. VI–VII; Al-Azani — abstrakt, rozdz. I i VI (zbiór testowy II
„z innej kamery w innym środowisku pracy, poza rozkładem danych uczących”).

## Slajd 6: Luka, którą wypełnia praca

Kompletny system na placu budowy, od kamer do powiadomienia, uczony i sprawdzany na nagraniach z tego placu.

| W literaturze | W tej pracy |
|---|---|
| model i zbiór danych oceniany na zdjęciach (Nath 2020, Wang 2021) | działający system: 4 kamery RTSP, aplikacja i GUI |
| osobne urządzenie brzegowe przy każdej kamerze (Gallo 2022) | jeden komputer obsługuje kolejkę 4 strumieni |
| model z innego miejsca traci ok. 25 pkt mAP (Al-Azani 2024) | uczenie i walidacja na nagraniach z docelowego placu |
