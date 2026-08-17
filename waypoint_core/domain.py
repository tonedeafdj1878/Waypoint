class Distance:
    def __init__(self, magnitude, unit="km"):
        if magnitude < 0:
            raise ValueError("Distance magnitude cannot be negative.")
        if unit not in ("km", "mi"):
            raise ValueError("Unit must be 'km' or 'mi'.")
        self._magnitude = magnitude
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
        
        if self._unit == "mi" and target_unit == "km":
            return Distance(self._magnitude * 1.60934, "km")
        elif self._unit == "km" and target_unit == "mi":
            return Distance(self._magnitude / 1.60934, "mi")
        else:
            raise ValueError("Invalid target unit.")


class Trail:
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


class Itinerary:
    def __init__(self):
        self._trails = []

    def add_trail(self, trail):
        self._trails.append(trail)

    def total_distance(self):
        total_mag = sum(t.distance.magnitude for t in self._trails)
        unit = self._trails[0].distance.unit if self._trails else "km"
        return Distance(total_mag, unit)