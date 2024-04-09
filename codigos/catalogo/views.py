from django.shortcuts import render, redirect
from catalogo.models import BiCard
from catalogo.forms import BiCardsForms
from django.contrib import messages


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
    if not request.user.is_authenticated:
        messages.error(request, 'Efetue Login')
        return redirect('login')

    form = BiCardsForms

    if request.method == 'POST':
        form = BiCardsForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'BI adicionado com sucesso')
            return redirect('add_bi')
        
    return render(request, 'catalogo/add_new_bi.html', {'form': form})


def edit_bi(request, card_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Efetue Login')
        return redirect('login')
    
    bicard = BiCard.objects.get(id=card_id)
    form = BiCardsForms(instance=bicard)

    if request.method == 'POST':
        form = BiCardsForms(request.POST, request.FILES, instance=bicard)
        if form.is_valid():
            form.save()
            messages.success(request, 'Card atualizado com sucesso')
            return redirect('index')
        
    return render(request, 'catalogo/edit_bi.html', {'form': form, 'card_id': card_id})


def delete_bi(request, card_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Efetue Login')
        return redirect('login')

    bicard = BiCard.objects.get(id=card_id)
    bicard.delete()
    messages.error(request, 'BI deletado com sucesso')
    return redirect('index')