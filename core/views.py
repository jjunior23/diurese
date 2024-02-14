from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest
import json
from django.http import JsonResponse
from django.http import HttpResponse, request
from django.core.paginator import Paginator
from .models import Diurese
from .forms import DiureseForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

'''def api_parametro(request):
    exames = Exame.objects.all().order_by('nome')
    # exames = Exame.objects.filter(id=2)
    data_exame = [item.to_dict2() for item in exames]

    parametros = Parametro.objects.all().order_by('nome')
    # parametros = Parametro.objects.filter(exame_id=5)
    data = [item.to_dict() for item in parametros]

    response = {
        'data': data,
        'data_exame': data_exame

    }
    return JsonResponse(response)'''



def api_diurese(request):
    diureses = Diurese.objects.all().order_by('volume')

    data = [item.to_dict() for item in diureses]

    response = {
        'data': data
    }

    return JsonResponse(response)





def lista_diurese(request):
    form = DiureseForm
    diurese_list = Diurese.objects.all().order_by('volume')
    paginator = Paginator(diurese_list, 2)
    page = request.GET.get('page')
    diurese = paginator.get_page(page)
    data = {}
    data['diurese'] = diurese
    data['form'] = form
    return render(request, 'core/lista_diurese.html', data)

def diurese_novo(request):
    if request.method == "POST":
        volume = request.POST.get('volume')
        count = Diurese.objects.filter(volume=volume).count()
        if count > 0:
            messages.error(request, 'Registro jรก cadastrado com este Nome !')
            return redirect('diurese_novo')
        else:
            form = DiureseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_diurese')
    else:
        form = DiureseForm
        return render(request, 'core/diurese_novo.html', {'form': form})

def diurese_update(request, id):
    diurese = Diurese.objects.get(id=id)
    form = DiureseForm(request.POST or None, instance=diurese)
    data = {}
    data['diurese'] = diurese
    data['form'] = form
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('lista_diurese')
    else:
        form = DiureseForm
        return render(request, 'core/diurese_update.html', data)
