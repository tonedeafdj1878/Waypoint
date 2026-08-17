from django.db import models

class Trail(models.Model):
    name = models.CharField(max_length=100, unique=True)
    distance_km = models.FloatField()
    elevation_gain_m = models.IntegerField()
    difficulty = models.CharField(max_length=20, choices=[
        ("Easy", "Easy"),
        ("Moderate", "Moderate"),
        ("Hard", "Hard"),
        ("Expert", "Expert"),
    ])
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.difficulty})"