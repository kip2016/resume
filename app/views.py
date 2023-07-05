from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import FileResponse
from django.conf import settings
import os
# Create your views here.
def index(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    
    context = {
        "form": form
        }
    return render(request, "app/index.html", context)

def download(request):
    file = os.path.join(settings.BASE_DIR, 'download/CV.pdf')
    fileOpened = open(file, 'rb')

    return FileResponse(fileOpened)