from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'bgnm/register.html', {'form': form})


def home(request):
    return render(request, 'bgnm/home.html', {})


def festival(request):
    return render(request, 'bgnm/festival.html', {})


def picnic(request):
    return render(request, 'bgnm/picnic.html', {})


def rajgad(request):
    return render(request, 'bgnm/rajgad.html', {})


def shivneri(request):
    return render(request, 'bgnm/shivneri.html', {})

def raigad(request):
    return render(request, 'bgnm/raigad.html', {})

def malvan(request):
    return render(request, 'bgnm/malvan.html', {})

def harihareshwar(request):
    return render(request, 'bgnm/harihareshwar.html', {})

def khopoli(request):
    return render(request, 'bgnm/khopoli.html', {})

def malvali(request):
    return render(request, 'bgnm/malavali.html', {})

def vijaydurga(request):
    return render(request, 'bgnm/vijaydurga.html', {})

def dahihandi(request):
    return render(request, 'bgnm/dahihandi.html', {})

def republic(request):
    return render(request, 'bgnm/republic.html', {})

def shivjayanti(request):
    return render(request, 'bgnm/shivjayanti.html', {})

def ganpati(request):
    return render(request, 'bgnm/ganpati.html', {})

def devi(request):
    return render(request, 'bgnm/devi.html', {})

def independence(request):
    return render(request, 'bgnm/independence.html', {})

def holi(request):
    return render(request, 'bgnm/holi.html', {})

def members(request):
    return render(request, 'bgnm/members.html', {})