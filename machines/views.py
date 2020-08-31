from django.shortcuts import render, redirect, get_object_or_404
from .models import Company
from .models import AdminList
from .forms import RegForm
from .forms import HomeForm
from .encryption_util import encrypt, decrypt
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages




def home(request):
    
    companies = Company.objects.all()
    administrators = AdminList.objects.all()    
    form = HomeForm(request.POST)
        
    
    
   
    if request.method == 'POST':
        
        for adm in administrators:
            
            #pf = str(form['password'].value) #methode
            if form.is_valid():
                pf = form.cleaned_data.get("password")
                uf = form.cleaned_data.get("user")
            
                if decrypt(adm.password) == pf and adm.user == uf:
                    
                    
                    
                    company = get_object_or_404(Company, pk=adm.comp)
                    name = company.name
                    #return render(request, 'techleader_reg.html',  {'name' : name})
                    #url = reverse('techleader_reg', kwargs={ 'name' : name})
                    
                    return redirect(techleader_reg, name=name)
                else:  error_message = "Nem létező felhasználónév jelszó párossal kisérelt meg belépni. Próbálja meg újra a bejelentkezést!"

        #p = decrypt(companies.values('password')[3]['password'])
        return render(request, 'home.html',  {'companies' : companies, 'form' : form, 'error_message' : error_message})
    return render(request, 'home.html',  {'companies' : companies,  'form' : form})



def new_company(request):
    form = RegForm(request.POST)
   
       
    if request.method == 'POST':
        
        if form.is_valid():            
            topic = form.save(commit=False)
            topic.password = encrypt(topic.password)
            topic.save()
            obj = Company.objects.latest('id')
            us = obj.user
            passw = obj.password
            com = obj.id
            al = AdminList(user=us, password=passw, comp=com)
            al.save()           
            return render(request, 'new_company.html', { 'form': form })
        
    else:
        form = RegForm()

    return render(request, 'new_company.html', { 'form': form })  


def techleader_reg(request, name):
    form = RegForm(request.POST)
   
       
    if request.method == 'POST':
        
        if form.is_valid():            
            topic = form.save(commit=False)
            topic.password = encrypt(topic.password)
            topic.save()
            obj = Company.objects.latest('id')
            us = obj.user
            passw = obj.password
            com = obj.id
            al = AdminList(user=us, password=passw, comp=com)
            al.save()           
            return render(request, 'techleader_reg.html', { 'form': form })
        
        else:
            form = RegForm()
        
    return render(request, 'techleader_reg.html', { 'form': form, 'name' :name}) 
