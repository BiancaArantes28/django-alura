from django.shortcuts import render
from perfis.models import Perfil

def index(request):
	return render(request, 'index.html')

def exibir(request, perfil_id):
	perfil = Perfil()

	if perfil_id == '1':
		perfil = Perfil('Bianca Aranes', 'biancaarantes28@gmail.com', '42342','NIC.br')
	return render(request, 'perfil.html', { "perfil" : perfil })
# Create your views here.
