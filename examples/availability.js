// Uproszczony przykład: przedziały [start, end), końce mogą się stykać.
export function overlaps(first, second) {
  for (const slot of [first, second]) {
    if (!Number.isFinite(slot.start) || !Number.isFinite(slot.end) || slot.start >= slot.end) {
      throw new RangeError("Nieprawidłowy przedział czasu");
    }
  }
  return first.start < second.end && second.start < first.end;
}
