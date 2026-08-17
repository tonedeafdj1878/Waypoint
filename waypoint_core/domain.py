from abc import ABC, abstractmethod

class Distance:
    def __init__(self, magnitude, unit="km"):
        if magnitude < 0:
            raise ValueError("Distance magnitude cannot be negative.")
        if unit not in ("km", "mi"):
            raise ValueError("Unit must be 'km' or 'mi'.")
        self._magnitude = float(magnitude)
        self._unit = unit

    @property
    def magnitude(self):
        return self._magnitude

    @property
    def unit(self):
        return self._unit

    def convert(self, target_unit):
        if target_unit == self._unit:
            return Distance(self._magnitude, self._unit)
        
        # Conversion factors: 1 mi = 1.60934 km
        if self._unit == "mi" and target_unit == "km":
            return Distance(self._magnitude * 1.60934, "km")
        elif self._unit == "km" and target_unit == "mi":
            return Distance(self._magnitude / 1.60934, "mi")
        else:
            raise ValueError("Invalid target unit.")

    def _to_base_meters(self):
        # Helper for arithmetic comparisons/operations: normalize to km
        if self._unit == "mi":
            return self._magnitude * 1.60934
        return self._magnitude

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        # Auto-convert other to match self's unit
        other_converted = other.convert(self._unit)
        return Distance(self._magnitude + other_converted.magnitude, self._unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        other_converted = other.convert(self._unit)
        new_mag = self._magnitude - other_converted.magnitude
        if new_mag < 0:
            raise ValueError("Distance magnitude cannot be negative.")
        return Distance(new_mag, self._unit)

    def __eq__(self, other):
        if not isinstance(other, Distance):
            return False
        # Compare base values to handle cross-unit equality cleanly
        return abs(self._to_base_meters() - other._to_base_meters()) < 1e-5

    def __lt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self._to_base_meters() < other._to_base_meters()

    def __gt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self._to_base_meters() > other._to_base_meters()

    def __str__(self):
        return f"{self._magnitude} {self._unit}"

    def __repr__(self):
        return f"Distance({self._magnitude}, '{self._unit}')"


# Mixins
class ElevationMixin:
    def grade_percentage(self):
        # Grade % = (elevation gain in meters / total distance in meters) * 100
        dist_m = self.distance.magnitude * (1000 if self.distance.unit == "km" else 1609.34)
        if dist_m == 0:
            return 0.0
        return (self.elevation_gain_m / dist_m) * 100


class RatingMixin:
    def __init__(self, *args, average_stars=5.0, **kwargs):
        super().__init__(*args, **kwargs)
        self.average_stars = average_stars


# Abstract Base Class
class Trail(ABC):
    DEFAULT_UNIT = "km"
    ALLOWED_DIFFICULTIES = {"Easy", "Moderate", "Hard", "Expert"}

    def __init__(self, trail_id, name, distance, elevation_gain_m, difficulty):
        self.trail_id = trail_id
        self.name = name
        self.distance = distance
        self.elevation_gain_m = elevation_gain_m
        self.set_difficulty(difficulty)

    def set_difficulty(self, difficulty):
        if difficulty not in self.ALLOWED_DIFFICULTIES:
            raise ValueError(f"Invalid difficulty. Must be one of {self.ALLOWED_DIFFICULTIES}")
        self._difficulty = difficulty

    @property
    def difficulty(self):
        return self._difficulty

    @classmethod
    def from_dict(cls, data):
        dist = Distance(data["distance_mag"], data.get("unit", cls.DEFAULT_UNIT))
        return cls(
            trail_id=data["id"],
            name=data["name"],
            distance=dist,
            elevation_gain_m=data["elevation_gain_m"],
            difficulty=data["difficulty"]
        )

    def __eq__(self, other):
        if not isinstance(other, Trail):
            return NotImplemented
        return self.trail_id == other.trail_id

    @abstractmethod
    def estimated_time(self):
        pass

    @abstractmethod
    def summary(self):
        pass


class DayHike(Trail):
    def estimated_time(self):
        # Base pacing: e.g., 4 km per hour plus time for elevation
        dist_km = self.distance.convert("km").magnitude
        hours = (dist_km / 4.0) + (self.elevation_gain_m / 600.0)
        return hours

    def summary(self):
        return f"Day Hike: {self.name} ({self.distance}), Difficulty: {self.difficulty}"


class GuidedDayHike(DayHike):
    def __init__(self, trail_id, name, distance, elevation_gain_m, difficulty, guide_name):
        super().__init__(trail_id, name, distance, elevation_gain_m, difficulty)
        self.guide_name = guide_name

    def summary(self):
        base_summary = super().summary()
        return f"{base_summary} [Guided by {self.guide_name}]"


class BackpackingRoute(Trail, ElevationMixin, RatingMixin):
    def __init__(self, trail_id, name, distance, elevation_gain_m, difficulty, average_stars=5.0, campsites=1):
        super().__init__(trail_id=trail_id, name=name, distance=distance, elevation_gain_m=elevation_gain_m, difficulty=difficulty, average_stars=average_stars)
        self.campsites = campsites

    def estimated_time(self):
        # Backpacking pacing is slower: e.g., 3 km per hour
        dist_km = self.distance.convert("km").magnitude
        hours = (dist_km / 3.0) + (self.elevation_gain_m / 500.0) + (self.campsites * 0.5)
        return hours

    def summary(self):
        return f"Backpacking Route: {self.name} ({self.campsites} campsites, {self.average_stars} stars)"


class TrailRun(Trail):
    def estimated_time(self):
        # Trail running pacing is faster: e.g., 9 km per hour
        dist_km = self.distance.convert("km").magnitude
        hours = (dist_km / 9.0) + (self.elevation_gain_m / 1000.0)
        return hours

    def summary(self):
        return f"Trail Run: {self.name} ({self.distance})"


class Itinerary:
    def __init__(self):
        self._trails = []

    def add_trail(self, trail):
        self._trails.append(trail)

    def total_distance(self):
        total_mag = sum(t.distance.convert("km").magnitude for t in self._trails)
        return Distance(total_mag, "km")


# Duck-typed class for polymorphic loop testing (inherits nothing from Trail)
class FakeTrail:
    def __init__(self, name):
        self.name = name

    def estimated_time(self):
        return 1.5

    def summary(self):
        return f"Fake Trail: {self.name}"