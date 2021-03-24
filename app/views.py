from django.shortcuts import render, redirect
from app.forms import SitesForm
from app.models import sites
# Create your views here.



def home(request):
    data = {}
    data['form'] = SitesForm()
    return render(request, 'index.html', data)

def create(request):
    form = SitesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, codigo):
    data = {}
    data['db'] = sites.objects.get(pk=codigo)
    return redirect(data['db'].url)





