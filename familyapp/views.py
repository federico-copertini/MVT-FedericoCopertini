from django.shortcuts import render
from .models import Familiar
# Create your views here.

def index(request):
    familiares = Familiar.objects.all()
    contexto = {"familiares":familiares}
    return render(request, "familyapp/index.html", contexto)

