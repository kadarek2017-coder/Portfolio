# AI Planista Szkoły

> **Case study:** lokalna aplikacja wspierająca plan lekcji i zastępstwa  
> **Stan:** lokalna aplikacja 1.3  
> **Technologie:** Python • Streamlit • SQLite • OR-Tools • XLSX/CSV • macOS

## Problem

Zastępstwo za nieobecnego nauczyciela nie sprowadza się do znalezienia wolnej osoby. Trzeba uwzględnić plan lekcji, obecność nauczycieli, kwalifikacje, łączenie klas oraz sposób rozliczania zastępstwa.

## Moje rozwiązanie

Zbudowałem lokalną aplikację, w której reguły organizacyjne szkoły są zapisane jako logika systemu. Projekt rozwijałem wersjami, dodając m.in.:

- import danych XLSX/CSV,
- kartotekę i dostępność nauczycieli,
- sale i ograniczenia planu,
- wyszukiwanie wariantów zastępstw,
- reguły łączenia wybranych klas,
- rozróżnienie zastępstw płatnych i niepłatnych,
- rejestr wykonanych zastępstw,
- zapis danych w SQLite,
- eksport wyników.

Do problemów optymalizacyjnych wykorzystuję OR-Tools.

## Przykład reguły biznesowej

Jeżeli nauczyciel jest nieobecny, system powinien najpierw szukać osoby obecnej w szkole i możliwej do wykorzystania w danym czasie. Psycholog, pedagog specjalny lub logopeda mogą w określonym scenariuszu wykonać zastępstwo bez dodatkowego rozliczenia, natomiast zastępstwo nauczyciela może wymagać oznaczenia jako płatne. System musi też rozpoznawać dozwolone łączenia klas.

To właśnie takie reguły są sednem projektu.

## Moja rola

Sam rozpisuję reguły i kolejne przypadki użycia, testuję wyniki i rozwijam aplikację wersjami. AI pomaga mi w implementacji, ale model procesu i decyzje dotyczące działania programu wynikają z analizy rzeczywistych potrzeb szkoły.

## Co ten projekt pokazuje

- Python w praktycznym narzędziu,
- modelowanie złożonych reguł,
- pracę z danymi XLSX/CSV i SQLite,
- wykorzystanie optymalizacji zamiast prostego zestawu warunków,
- rozwijanie aplikacji krok po kroku na podstawie scenariuszy użytkownika.

Pełne źródła pozostają prywatne. Publiczny opis nie zawiera danych szkoły ani nauczycieli.

[← Wróć do portfolio](../../README.md)
