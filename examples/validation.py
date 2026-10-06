"""Uproszczona demonstracja walidacji; dane fikcyjne."""
from math import isfinite

def meal_energy(grams: float, kcal_per_100g: float) -> float:
    if not all(isfinite(value) and value >= 0 for value in (grams, kcal_per_100g)):
        raise ValueError("Ilość i wartość energetyczna muszą być skończone i nieujemne")
    result = grams * kcal_per_100g / 100
    if not isfinite(result):
        raise ValueError("Wynik przekracza obsługiwany zakres")
    return round(result, 2)
