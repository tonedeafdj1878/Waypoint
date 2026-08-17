from django.shortcuts import render, redirect
from .forms import TrailReportForm
from .models import Trail

def home_view(request):
    trails = Trail.objects.all()
    return render(request, "core/home.html", {"trails": trails})

def report_trail_view(request):
    if request.method == "POST":
        form = TrailReportForm(request.POST)
        if form.is_valid():
            # Save the reported trail to the database
            trail = Trail.objects.create(
                name=form.cleaned_data['trail_name'],
                distance_km=form.cleaned_data['distance_km'],
                elevation_gain_m=form.cleaned_data['elevation_gain_m'],
                difficulty=form.cleaned_data['difficulty'],
                notes=form.cleaned_data['notes']
            )
            return render(request, "core/report_success.html", {"data": trail})
    else:
        form = TrailReportForm()
    
    return render(request, "core/report.html", {"form": form})