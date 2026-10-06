# Kalendarz rejestracyjny WordPress

> **Case study:** system rezerwacji wizyt dla gabinetu  
> **Stan:** rozwijany projekt — wersja 1.25.5  
> **Obszary:** WordPress • PHP • JavaScript • rezerwacje • role użytkowników • powiadomienia

## Problem

Prosty kalendarz nie wystarcza, gdy trzeba jednocześnie uwzględnić dostępność terapeuty, długość usług, zajęte terminy, różne rodzaje wizyt oraz późniejszą obsługę rezerwacji.

## Moje rozwiązanie

Rozwijam własną wtyczkę WordPress, która łączy najważniejsze elementy procesu:

- prezentację dostępnych terminów,
- rezerwację wizyty przez pacjenta,
- panel terapeuty,
- obsługę statusów wizyty,
- powiadomienia,
- zarządzanie i zmianę rezerwacji.

Panel terapeuty jest częścią tego samego systemu, a nie osobnym projektem.

## Moja rola

Definiuję logikę procesu i zachowanie systemu z punktu widzenia pacjenta oraz terapeuty. Kolejne wersje powstają na podstawie realnych scenariuszy: rezerwacja, przełożenie, odwołanie, zamknięcie wizyty czy zachowanie interfejsu na telefonie.

AI wspiera mnie przy implementacji i debugowaniu, natomiast wymagania, reguły procesu i decyzje dotyczące działania systemu wynikają z mojej analizy problemu i testów.

## Najciekawsze wyzwania

- zapobieganie konfliktom terminów,
- czytelny interfejs tygodniowego kalendarza,
- różne akcje zależne od statusu rezerwacji,
- responsywność na telefonach i komputerach,
- utrzymanie spójności między widokiem pacjenta i terapeuty.

## Co ten projekt pokazuje

Projekt pokazuje nie tylko tworzenie funkcji WordPress, ale przede wszystkim pracę nad **procesem biznesowym, stanami systemu i przypadkami brzegowymi**.

Pełne źródła oraz konfiguracja wdrożenia pozostają prywatne.

[← Wróć do portfolio](../../README.md)
