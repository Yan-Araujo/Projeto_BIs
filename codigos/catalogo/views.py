from django.shortcuts import render, redirect
from catalogo.models import BiCard
from catalogo.forms import BiCardsForms


def index(request):
    bicards = BiCard.objects.filter(ativo=True)
    return render(request, 'catalogo/index.html', {'cards': bicards})


def search(request):
    bicards = BiCard.objects.filter(ativo=True)

    if 'search' in request.GET:
        requested_card = request.GET['search']
        if requested_card:
            bicards = bicards.filter(name__icontains=requested_card)

    return render(request, 'catalogo/search.html', {'cards': bicards})

def add_bi(request):
    form = BiCardsForms

    if request.method == 'POST':
        form = BiCardsForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_bi')
        
    return render(request, 'catalogo/add_new_bi.html', {'form': form})

def edit_bi(request):
    return render(request, 'catalogo/edit_bi.html')

def delete_bi(request):
    return render(request, 'catalogo/delete_bi.html')