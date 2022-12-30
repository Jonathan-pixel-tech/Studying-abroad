from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import CreateView, DeleteView
from .models import Universidade, CollegeList, ListaNews, CollegeList, Pais
from conteudo.forms import criaCollegeList, criaUniversidade
from django.core.validators import validate_email
from django.contrib import messages
from django.urls import reverse_lazy



def index(request):
    if request.method!='POST':
        return render(request, 'index.html')
    email = request.POST.get('email_news')
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')    
        return render(request, 'index.html')
    
    if ListaNews.objects.filter(email_news=email).exists():
        messages.error(request, 'O email informado já foi cadastrado')
        return render(request, 'index.html')
         
    assinante = ListaNews(email_news=email)
    assinante.save()
    messages.success(request, 'O email foi cadastrado com sucesso')
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def detalha(request, pk):
    universidade = Universidade.objetos.get(id=pk)
    return render(request, 'detalha.html', {'universidade':universidade})

def mostra_pais(request, pk):
    pais = Pais.objetos.get(id=pk)
    return render(request, 'mostra_pais.html', {'pais': pais})

def dashboard(request):

    if request.user.is_authenticated:

        if request.user.is_superuser:
            if request.method != 'POST':   
                form = criaUniversidade()
                return render(request, 'dashboard.html', {'form': form})

            form = criaUniversidade(request.POST)
            if not form.is_valid():
                messages.error(request, "ERRO AO ENVIAR FORMULÁRIO")
                form = criaUniversidade(request.POST)
                return render(request, 'dashboard.html', {'form': form})

            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('dashboard')
        else:
            return redirect('dashboard_usuario')
    else:
        return render(request, 'login.html')




   

class listaCollege(ListView):
    model = CollegeList
    template_name = 'collegeList.html'
    context_object_name = 'colleges'
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id')
        return qs

    def get_queryset(self):
        self.colleges = CollegeList.objects.filter(usuario=self.request.user)
        return self.colleges


class listaUniversidades(ListView):
    model = Universidade
    template_name = 'universidades.html'
    context_object_name = 'universidades'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id')
        return qs

class cadastraCollege(CreateView):
    template_name= 'dashboard_usuario.html'
    model = CollegeList
    form_class = criaCollegeList
    success_url = 'collegeList' 
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class DeletaUniversidade(DeleteView):
    template_name='exclui_universidade_collegelist.html'
    model= CollegeList
    context_object_name='universidade'
    success_url= reverse_lazy('collegeList')
    