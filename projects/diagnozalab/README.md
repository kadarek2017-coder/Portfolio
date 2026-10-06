# DiagnozaLab / Formularze Pro Center

> **Case study:** automatyzacja obsługi formularzy diagnostycznych w WordPressie  
> **Stan:** rozwijany projekt — wersja 1.33.38  
> **Obszary:** WordPress • PHP • formularze • raporty • e-mail • API AI

## Problem

Wyniki kwestionariuszy trzeba było zbierać, przeliczać i przygotowywać do dalszej pracy specjalisty. Przy większej liczbie formularzy oznacza to dużo powtarzalnych czynności i zwiększa ryzyko pomyłki.

## Moje rozwiązanie

Zaprojektowałem własną wtyczkę WordPress, która łączy cały proces w jednym narzędziu:

- zbiera odpowiedzi z formularzy,
- automatycznie oblicza wyniki zgodnie z regułami danego testu,
- przygotowuje czytelny raport,
- przekazuje wynik w dalszym procesie,
- może pomocniczo korzystać z API AI przy tworzeniu opisu.

Punktacja testu nie jest pozostawiona modelowi AI. Reguły obliczeń są częścią logiki aplikacji, a opis AI ma charakter pomocniczy i podlega ocenie specjalisty.

## Moja rola

To projekt rozwijany przeze mnie od strony problemu i procesu. Określam wymagania, sposób działania formularzy, strukturę raportów i kolejne funkcje. AI wykorzystuję jako wsparcie przy programowaniu, analizie błędów i poprawianiu kolejnych wersji.

W trakcie rozwoju wielokrotnie zmieniałem szczegóły formularzy i raportów na podstawie testów praktycznych — m.in. sposób prezentacji wyników, układ dokumentów i przepływ informacji.

## Co ten projekt pokazuje

- przełożenie rzeczywistego procesu na logikę aplikacji,
- rozwijanie własnej wtyczki WordPress,
- pracę z formularzami i walidacją danych,
- automatyzację obliczeń i raportowania,
- świadome oddzielenie deterministycznych obliczeń od generatywnego AI,
- iteracyjne testowanie i poprawianie produktu.

## Bezpieczeństwo portfolio

Pełne źródła, konfiguracja wdrożenia, algorytmy poszczególnych kwestionariuszy oraz dane użytkowników nie są publikowane. Publiczne portfolio pokazuje architekturę problemu i zakres mojej pracy bez ujawniania wrażliwych elementów.

[← Wróć do portfolio](../../README.md)
