from django.shortcuts import render # type: ignore

# Create your views here
def home(request):
  #returns the template file available & the request itself
  return render(request, 'sales/home.html')