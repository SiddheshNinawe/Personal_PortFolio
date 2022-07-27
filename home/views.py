from django.shortcuts import render
from home.models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        saveData=Contact(name=name, phone=phone, email=email, subject=subject, message=message)
        saveData.save()

        
    return render(request, 'contact.html')