from django.shortcuts import render
from .forms import common_form
# Create your views here.
def home(request):
    
    form=common_form()
    return render(request, 'home.html', {"form":form})