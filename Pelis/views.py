from django.shortcuts import render, redirect
from .models import *
from .forms import DatosPersonaForm
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.urls import reverse_lazy

def home(request):
    return render(request, 'inicio.html')


class CreatePersona(CreateView):
    model = DatosPersona
    form_class = DatosPersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('inicio')

class ListPersona(ListView):
    model = DatosPersona
    template_name = 'listar_persona.html'


class UpdatePersona(UpdateView):
    model = DatosPersona
    form_class = DatosPersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('inicio')

class DeletePersona(DeleteView):
    model = DatosPersona
    template_name = 'eliminar_persona.html'
    success_url = reverse_lazy('inicio')





def crearPersona(request):
    if request.method == 'POST':
        form = DatosPersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = DatosPersonaForm()
    return render(request, 'crear_persona.html', {'form':form})

def listarPersona(request):
    persona = DatosPersona.objects.all()
    context = {'persona':persona}
    return render(request,'listar_persona.html',context)

def editarPersona(request,id):
    persona = DatosPersona.objects.get(id = id)
    if request.method == 'GET':
        form = DatosPersonaForm(instance = persona)
    else:
        form = DatosPersonaForm(request.POST, instance = DatosPersona)
        if form.instance():
            form.save()
        return   redirect('inicio')
    return render(request, 'crear_persona.html', {'form':form})

def eliminarPersona(request,id):
    persona = DatosPersona.objects.get(id=id)
    if request.method == 'POST':
        persona.delete()
        return redirect('inicio')
    return render(request,'eliminar_persona.html',{'persona':persona})