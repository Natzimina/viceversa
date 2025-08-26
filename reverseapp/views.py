from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .utils import reverse_string  # импортируем логику из utils.py (см. шаг 8)

def home(request):
    text = "Vice Versa"
    reversed_text = reverse_string(text)
    return HttpResponse(reversed_text)
