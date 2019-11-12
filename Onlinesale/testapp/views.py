from django.shortcuts import render
from . import forms

# Create your views here.
def saleinfo(request):
    form=forms.online()
    if request.method=='POST':
        form=forms.online(request.POST)
        if form.is_valid():
            print('WELCOME TO ONLINE SALE')
            return render(request,'testapp/thank.html')

    return render(request,'testapp/index.html',{'form':form})
