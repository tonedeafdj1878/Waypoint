import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'waypoint.settings')
django.setup()

from core.models import Trail

# Implement a custom Distance class to satisfy the test operators and sorting
class Distance:
    def __init__(self, value, unit="km"):
        self.value = value
        self.unit = unit

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.value + other.value, self.unit)
        return Distance(self.value + other, self.unit)

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return f"{self.value} {self.unit}"

print("--- 1. Distance Operators & Sorting ---")
d1 = Distance(3, "km")
d2 = Distance(2, "km")
print(f"d1 + d2 = {d1 + d2}")

distances = [Distance(10, "km"), Distance(2, "km"), Distance(5, "km")]
print(f"Sorted distances: {sorted(distances)}")

print("\n--- 2. Method Resolution Order (__mro__) ---")
print(Trail.__mro__)