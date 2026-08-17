from django.shortcuts import render
from .forms import TrailReportForm

def home_view(request):
    return render(request, "core/home.html", {})

def report_trail_view(request):
    if request.method == "POST":
        form = TrailReportForm(request.POST)
        if form.is_valid():
            # Process the clean data (we can display a success message or summary)
            cleaned_data = form.cleaned_data
            return render(request, "core/report_success.html", {"data": cleaned_data})
    else:
        form = TrailReportForm()
    
    return render(request, "core/report.html", {"form": form})