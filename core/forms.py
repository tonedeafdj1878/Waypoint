from django import forms

class TrailReportForm(forms.Form):
    trail_name = forms.CharField(max_length=100, label="Trail Name")
    distance_km = forms.FloatField(min_value=0.1, label="Distance (km)")
    elevation_gain_m = forms.IntegerField(min_value=0, label="Elevation Gain (m)")
    difficulty = forms.ChoiceField(
        choices=[
            ("Easy", "Easy"),
            ("Moderate", "Moderate"),
            ("Hard", "Hard"),
            ("Expert", "Expert"),
        ],
        label="Difficulty"
    )
    notes = forms.CharField(widget=forms.Textarea, required=False, label="Trail Notes")