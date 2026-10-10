# Literatura do Prezentacji I — „System automatycznego wykrywania naruszeń BHP w czasie rzeczywistym”

22 pozycji, z czego 12 oznaczonych ★ to rdzeń na slajd „Istniejące rozwiązania” (cel: 8–12
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

## Do pobrania z IEEE (4) — tak samo jak Ananthanarayanan 2017

Poprawnie pobrany plik nazywa się jak tytuł z podkreślnikami (np. `Real-Time_Video_Analytics_The_Killer_App_for_Edge_Computing.pdf`) i ma więcej niż 1 stronę. Potem `python3 literatura.py` sam go przeniesie i odhaczy.

- [ ] Amershi S., Begel A., Bird C. i in. (2019). *Software Engineering for Machine Learning: A Case Study* — [IEEE Xplore](https://doi.org/10.1109/icse-seip.2019.00042)
- [ ] Ren S., He K., Girshick R. i in. (2017). *Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks* — [IEEE Xplore](https://doi.org/10.1109/tpami.2016.2577031)
- [ ] Wojke N., Bewley A., Paulus D. (2017). *Simple online and realtime tracking with a deep association metric* — [IEEE Xplore](https://doi.org/10.1109/icip.2017.8296962)
- [ ] Xu R., Razavi S., Zheng R. (2023). *Edge Video Analytics: A Survey on Applications, Systems and Enabling Techniques* — [IEEE Xplore](https://doi.org/10.1109/comst.2023.3323091)

---
## Od czego zacząć (na 15 minut wystarczą te 4)

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

## Stan pobrania (odświeżone 2026-10-10)

**Masz 12 z 22 pozycji, z rdzenia ★ 12 z 12.**

### Brakuje z rdzenia ★ (0) — do pobrania w pierwszej kolejności


### Masz już (12)

- [x] ★ Fang Q., Li H., Luo X. i in. (2018). *Detecting non-hardhat-use by a deep learning method from far-field surveillance videos* — `Fang 2018 - Detecting non-hardhat-use by a deep learning method from far-field surveillance videos.pdf`
- [x] ★ Nath N.D., Behzadan A.H., Paal S.G. (2020). *Deep learning for site safety: Real-time detection of personal protective equipment* — `Nath 2020 - Deep learning for site safety - Real-time detection of personal protective equipment.pdf`
- [x] ★ Wang Z., Wu Y., Yang L. i in. (2021). *Fast Personal Protective Equipment Detection for Real Construction Sites Using Deep Learni* — `Wang 2021 - Fast Personal Protective Equipment Detection for Real Construction Sites Using Deep Learning Approaches.pdf`
- [x] ★ Al-Azani S., Luqman H., Alfarraj M. i in. (2024). *Real-Time Monitoring of Personal Protective Equipment Compliance in Surveillance Cameras* — `Al-Azani 2024 - Real-Time Monitoring of Personal Protective Equipment Compliance in Surveillance Cameras.pdf`
- [x] ★ Schulzrinne H., Rao A., Lanphier R. (1998). *Real Time Streaming Protocol (RTSP)* — `Schulzrinne 1998 - Real Time Streaming Protocol (RTSP).pdf`
- [x] ★ Ananthanarayanan G., Bahl P., Bodik P. i in. (2017). *Real-Time Video Analytics: The Killer App for Edge Computing* — `Ananthanarayanan 2017 - Real-Time Video Analytics - The Killer App for Edge Computing.pdf`
- [x] ★ Gallo G., Di Rienzo F., Garzelli F. i in. (2022). *A Smart System for Personal Protective Equipment Detection in Industrial Environments Base* — `Gallo 2022 - A Smart System for Personal Protective Equipment Detection in Industrial Environments Based on Deep Learning at the Edge.pdf`
- [x] ★ Redmon J., Divvala S., Girshick R. i in. (2016). *You Only Look Once: Unified, Real-Time Object Detection* — `Redmon 2016 - You Only Look Once - Unified, Real-Time Object Detection.pdf`
- [x] ★ Terven J., Córdova-Esparza D.M., Romero-González J.A. (2023). *A Comprehensive Review of YOLO Architectures in Computer Vision: From YOLOv1 to YOLOv8 and* — `Terven 2023 - A Comprehensive Review of YOLO Architectures in Computer Vision - From YOLOv1 to YOLOv8 and YOLO-NAS.pdf`
- [x] ★ Fang W., Ding L., Love P.E.D. i in. (2020). *Computer vision applications in construction safety assurance* — `Fang 2020 - Computer vision applications in construction safety assurance.pdf`
- [x] ★ Sculley D., Holt G., Golovin D. i in. (2015). *Hidden Technical Debt in Machine Learning Systems* — `Sculley 2015 - Hidden Technical Debt in Machine Learning Systems.pdf`
- [x] ★ Kreuzberger D., Kühl N., Hirschl S. (2023). *Machine Learning Operations (MLOps): Overview, Definition, and Architecture* — `Kreuzberger 2023 - Machine Learning Operations (MLOps) - Overview, Definition, and Architecture.pdf`

Pozostałe (10) to zapas — linki w tabelach niżej.

---

## Detekcja kasków i kamizelek (PPE) — najbliższe tematowi (wątek 2)

| | Pozycja | Cytowania | Gdzie pobrać | Po co / co z niej wynika |
|---|---|---|---|---|
| ★ | Fang Q., Li H., Luo X. i in. (2018). Detecting non-hardhat-use by a deep learning method from far-field surveillance videos. *Automation in Construction* 85, 1-9. | 560 | ✓ pobrane (`Fang 2018 - Detecting non-hardhat-use by a deep learning method from far-field surveillance videos.pdf`) | klasyk dziedziny: Faster R-CNN wykrywa brak kasku na nagraniach z kamer monitoringu z dużej odległości (ponad 100 tys. klatek z 25 budów) |
| ★ | Nath N.D., Behzadan A.H., Paal S.G. (2020). Deep learning for site safety: Real-time detection of personal protective equipment. *Automation in Construction* 112, 103085. | 540 | ✓ pobrane (`Nath 2020 - Deep learning for site safety - Real-time detection of personal protective equipment.pdf`) | **najbliższe tematowi:** kask + kamizelka w czasie rzeczywistym (YOLOv3), trzy warianty: detekcja elementów + klasyfikator albo od razu klasa pracownika (bez kasku i kamizelki / tylko kask / tylko kamizelka / oba); mAP 72–86% wg repozytorium autorów, zbiór Pictor-v3 i kod otwarte |
| ★ | Wang Z., Wu Y., Yang L. i in. (2021). Fast Personal Protective Equipment Detection for Real Construction Sites Using Deep Learning Approaches. *Sensors* 21(10), 3478. | 254 | ✓ pobrane (`Wang 2021 - Fast Personal Protective Equipment Detection for Real Construction Sites Using Deep Learning Approaches.pdf`) | osiem wariantów YOLO (v3–v5) na otwartym zbiorze CHV (kaski w 4 kolorach, osoba, kamizelka): YOLOv5x mAP 86,55%, YOLOv5s 52 FPS na GPU — gotowy zbiór na start i punkt odniesienia dla wyników |
| ★ | Al-Azani S., Luqman H., Alfarraj M. i in. (2024). Real-Time Monitoring of Personal Protective Equipment Compliance in Surveillance Cameras. *IEEE Access* 12, 121882-121895. | 25 | ✓ pobrane (`Al-Azani 2024 - Real-Time Monitoring of Personal Protective Equipment Compliance in Surveillance Cameras.pdf`) | system PPE na nagraniach z kamer monitoringu, od zbierania danych po wdrożenie (YOLOv7, CenterNet, ViT); mAP spada z 92,4% do 66,7% na nagraniu z innego miejsca i pod innym kątem — argument za uczeniem na własnych nagraniach z placu |
|  | Wu J., Cai N., Chen W. i in. (2019). Automatic detection of hardhats worn by construction personnel: A deep learning approach and benchmark dataset. *Automation in Construction* 106, 102894. | 298 | [Elsevier, przez PWr](https://doi.org/10.1016/j.autcon.2019.102894) · [Scholar](https://scholar.google.com/scholar?q=%22Automatic%20detection%20of%20hardhats%20worn%20by%20construction%20personnel%3A%20A%20deep%20learning%20approach%20and%20benchmark%20dataset%22) | otwarty zbiór GDUT-HWD (3174 zdjęcia, kaski z kolorami), SSD z mechanizmem uwagi, mAP 83,89% |
|  | Xiong R., Tang P. (2021). Pose guided anchoring for detecting proper use of personal protective equipment. *Automation in Construction* 130, 103828. | 87 | [Elsevier, otwarty](https://doi.org/10.1016/j.autcon.2021.103828) · [Scholar](https://scholar.google.com/scholar?q=%22Pose%20guided%20anchoring%20for%20detecting%20proper%20use%20of%20personal%20protective%20equipment%22) | pose estimation sprawdza, czy kask i kamizelka są noszone, a nie tylko widoczne w kadrze; F1 0,97 i 0,95 na zbiorze autorów (wynik na własnych danych — traktować ostrożnie) |
|  | Wang S. (2025). Automated non-PPE detection on construction sites using YOLOv10 and transformer architectures for surveillance and body worn cameras with benchmark datasets. *Scientific Reports* 15(1). | 45 | [Springer, otwarty](https://doi.org/10.1038/s41598-025-12468-8) · [Scholar](https://scholar.google.com/scholar?q=%22Automated%20non-PPE%20detection%20on%20construction%20sites%20using%20YOLOv10%20and%20transformer%20architectures%20for%20surveillance%20and%20body%20worn%20cameras%20with%20benchmark%20datasets%22) | najnowsze wyniki: YOLOv10 z backbone Swin Transformer na nagraniach z monitoringu i kamer nasobnych; AP50 brak kasku 92,4%, brak kamizelki 87,2% |
|  | Ahmad H.M., Rahimi A. (2025). SH17: A dataset for human safety and personal protective equipment detection in manufacturing industry. *Journal of Safety Science and Resilience* 6(2), 175-185. | 31 | [Elsevier, otwarty](https://doi.org/10.1016/j.jnlssr.2024.09.002) · [Scholar](https://scholar.google.com/scholar?q=%22SH17%3A%20A%20dataset%20for%20human%20safety%20and%20personal%20protective%20equipment%20detection%20in%20manufacturing%20industry%22) | zbiór SH17: 8099 zdjęć, 17 klas PPE z zakładów przemysłowych, YOLOv9-e ponad 70,9% — gdyby zakres wychodził poza kask i kamizelkę |

## Strumienie wideo z kamer i systemy czasu rzeczywistego (wątek 1)

| | Pozycja | Cytowania | Gdzie pobrać | Po co / co z niej wynika |
|---|---|---|---|---|
| ★ | Schulzrinne H., Rao A., Lanphier R. (1998). Real Time Streaming Protocol (RTSP). *RFC Editor*, RFC 2326. | 1219 | ✓ pobrane (`Schulzrinne 1998 - Real Time Streaming Protocol (RTSP).pdf`) | specyfikacja RTSP 1.0, przez który kamery IP udostępniają strumień — źródło normatywne do modułu akwizycji |
| ★ | Ananthanarayanan G., Bahl P., Bodik P. i in. (2017). Real-Time Video Analytics: The Killer App for Edge Computing. *Computer* 50(10), 58-67. | 504 | ✓ pobrane (`Ananthanarayanan 2017 - Real-Time Video Analytics - The Killer App for Edge Computing.pdf`) | analityka wideo na żywo w dużej skali wymaga architektury rozproszonej: kamery – brzeg sieci – chmura — uzasadnienie „rozproszonego systemu” z tematu |
| ★ | Gallo G., Di Rienzo F., Garzelli F. i in. (2022). A Smart System for Personal Protective Equipment Detection in Industrial Environments Based on Deep Learning at the Edge. *IEEE Access* 10, 110862-110878. | 86 | ✓ pobrane (`Gallo 2022 - A Smart System for Personal Protective Equipment Detection in Industrial Environments Based on Deep Learning at the Edge.pdf`) | system PPE (kask, kamizelka, rękawice) na strumieniu z kamery, liczony na brzegu (Raspberry Pi + Intel NCS2): porównanie 5 sieci pod kątem trafności, opóźnienia i klatek/s — kontrast dla centralnego komputera kolegi |
|  | Xu R., Razavi S., Zheng R. (2023). Edge Video Analytics: A Survey on Applications, Systems and Enabling Techniques. *IEEE Communications Surveys & Tutorials* 25(4), 2951-2982. | 99 | [IEEE, przez PWr](https://doi.org/10.1109/comst.2023.3323091) · [Scholar](https://scholar.google.com/scholar?q=%22Edge%20Video%20Analytics%3A%20A%20Survey%20on%20Applications%2C%20Systems%20and%20Enabling%20Techniques%22) | przegląd edge video analytics: architektury, frameworki, zbiory danych — gdy trzeba szerzej opisać przetwarzanie strumieni |
|  | Lema D.G., Usamentiaga R., García D.F. (2023). Low-cost system for real-time verification of personal protective equipment in industrial facilities using edge computing devices. *Journal of Real-Time Image Processing* 20(6). | 16 | [Springer, otwarty](https://doi.org/10.1007/s11554-023-01368-7) · [Scholar](https://scholar.google.com/scholar?q=%22Low-cost%20system%20for%20real-time%20verification%20of%20personal%20protective%20equipment%20in%20industrial%20facilities%20using%20edge%20computing%20devices%22) | tani system PPE na urządzeniach brzegowych z detekcją i śledzeniem; alarm z informacji czasowej (kilka klatek), nie z pojedynczej klatki — wzorzec dla klasyfikacji naruszeń |

## Detekcja obiektów: podstawy (YOLO i inne) (wątek 2)

| | Pozycja | Cytowania | Gdzie pobrać | Po co / co z niej wynika |
|---|---|---|---|---|
| ★ | Redmon J., Divvala S., Girshick R. i in. (2016). You Only Look Once: Unified, Real-Time Object Detection. *2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 779-788. | 51419 | ✓ pobrane (`Redmon 2016 - You Only Look Once - Unified, Real-Time Object Detection.pdf`) | źródło pierwotne YOLO: detekcja jako jedna regresja ramek i klas w jednym przebiegu sieci, 45 FPS — dlaczego detektor jednoetapowy nadaje się do wideo w czasie rzeczywistym |
| ★ | Terven J., Córdova-Esparza D.M., Romero-González J.A. (2023). A Comprehensive Review of YOLO Architectures in Computer Vision: From YOLOv1 to YOLOv8 and YOLO-NAS. *Machine Learning and Knowledge Extraction* 5(4), 1680-1716. | 2919 | ✓ pobrane (`Terven 2023 - A Comprehensive Review of YOLO Architectures in Computer Vision - From YOLOv1 to YOLOv8 and YOLO-NAS.pdf`) | przegląd YOLOv1–v8 i YOLO-NAS z metrykami (mAP, NMS) i zmianami architektury — do uzasadnienia wyboru konkretnej wersji YOLO |
|  | Ren S., He K., Girshick R. i in. (2017). Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks. *IEEE Transactions on Pattern Analysis and Machine Intelligence* 39(6), 1137-1149. | 55722 | [arXiv, otwarty](https://arxiv.org/abs/1506.01497) · [IEEE, przez PWr](https://doi.org/10.1109/tpami.2016.2577031) · [Scholar](https://scholar.google.com/scholar?q=%22Faster%20R-CNN%3A%20Towards%20Real-Time%20Object%20Detection%20with%20Region%20Proposal%20Networks%22) | Faster R-CNN, detektor dwuetapowy (5 FPS na GPU) — punkt odniesienia dla YOLO; użyli go Fang i in. (2018) |
|  | Wojke N., Bewley A., Paulus D. (2017). Simple online and realtime tracking with a deep association metric. *2017 IEEE International Conference on Image Processing (ICIP)*, 3645-3649. | 5020 | [arXiv, otwarty](https://arxiv.org/abs/1703.07402) · [IEEE, przez PWr](https://doi.org/10.1109/icip.2017.8296962) · [Scholar](https://scholar.google.com/scholar?q=%22Simple%20online%20and%20realtime%20tracking%20with%20a%20deep%20association%20metric%22) | DeepSORT: śledzenie osób między klatkami — żeby naruszenie liczyć raz na osobę, a nie w każdej klatce |

## Computer vision w bezpieczeństwie budowy — przegląd (wątek 3)

| | Pozycja | Cytowania | Gdzie pobrać | Po co / co z niej wynika |
|---|---|---|---|---|
| ★ | Fang W., Ding L., Love P.E.D. i in. (2020). Computer vision applications in construction safety assurance. *Automation in Construction* 110, 103013. | 290 | ✓ pobrane (`Fang 2020 - Computer vision applications in construction safety assurance.pdf`) | przegląd CV i DL w bezpieczeństwie budowy: co już wykrywa się automatycznie i co blokuje wdrożenia (dokładność, niezawodność, trudność pozyskania nagrań z monitoringu) |

## Inżynieria danych i ML w aplikacji (MLOps) (wątek 4)

| | Pozycja | Cytowania | Gdzie pobrać | Po co / co z niej wynika |
|---|---|---|---|---|
| ★ | Sculley D., Holt G., Golovin D. i in. (2015). Hidden Technical Debt in Machine Learning Systems. *Advances in Neural Information Processing Systems* 28 (NIPS 2015). | 825 (bez DOI, OpenAlex zaniża) | ✓ pobrane (`Sculley 2015 - Hidden Technical Debt in Machine Learning Systems.pdf`) | dług techniczny w systemach ML: model to mały fragment systemu, resztę stanowią dane, konfiguracja, zależności i monitoring — uzasadnienie podejścia inżynierskiego, nie tylko „wytrenuj model” |
| ★ | Kreuzberger D., Kühl N., Hirschl S. (2023). Machine Learning Operations (MLOps): Overview, Definition, and Architecture. *IEEE Access* 11, 31866-31879. | 742 | ✓ pobrane (`Kreuzberger 2023 - Machine Learning Operations (MLOps) - Overview, Definition, and Architecture.pdf`) | MLOps: definicja, zasady, komponenty i architektura (wersjonowanie danych i modeli, automatyzacja, monitoring) — rama dla „pełnego procesu inżynierii danych” z tematu |
|  | Amershi S., Begel A., Bird C. i in. (2019). Software Engineering for Machine Learning: A Case Study. *2019 IEEE/ACM 41st International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP)*, 291-300. | 1138 | [IEEE, przez PWr](https://doi.org/10.1109/icse-seip.2019.00042) · [Scholar](https://scholar.google.com/scholar?q=%22Software%20Engineering%20for%20Machine%20Learning%3A%20A%20Case%20Study%22) | jak zespoły Microsoft budują aplikacje AI (9 etapów); dane trudniej wersjonować, a modele trudniej traktować jak osobne moduły niż zwykły kod |
|  | Paleyes A., Urma R.G., Lawrence N.D. (2023). Challenges in Deploying Machine Learning: A Survey of Case Studies. *ACM Computing Surveys* 55(6), 1-29. | 630 | [ACM, otwarty](https://doi.org/10.1145/3533378) · [Scholar](https://scholar.google.com/scholar?q=%22Challenges%20in%20Deploying%20Machine%20Learning%3A%20A%20Survey%20of%20Case%20Studies%22) | przegląd problemów wdrożeniowych ML na każdym etapie: dane, uczenie, weryfikacja, wdrożenie |
