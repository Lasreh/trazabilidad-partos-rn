from .models import Paciente

def lista_pacientes(request):
    pacientes = Paciente.objects.all().order_by('apellido_paterno', 'apellido_materno', 'nombre')
    return render(request, 'pacientes/lista.html', {
        'pacientes': pacientes
    })

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import PacienteForm

@login_required
def crear_paciente(request):

    if request.method == "POST":
        form = PacienteForm(request.POST)

        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.created_by = request.user
            paciente.save()

            # Mensaje simple y claro
            messages.success(request, "Paciente registrado correctamente.")

            # Mostrar formulario vacío nuevamente
            return render(request, "pacientes/crear.html", {
                "form": PacienteForm()
            })

    else:
        form = PacienteForm()

    return render(request, "pacientes/crear.html", {
        "form": form
    })

from django.shortcuts import render
from .models import Paciente
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def lista_pacientes(request):
    pacientes_list = Paciente.objects.all().order_by('apellido_paterno', 'apellido_materno', 'nombre')
    
    paginator = Paginator(pacientes_list, 20)  # máximo 20 pacientes por página
    page_number = request.GET.get('page')
    pacientes = paginator.get_page(page_number)  # devuelve un objeto Page
    
    return render(request, 'pacientes/lista.html', {'pacientes': pacientes})


def lista_hospitalizaciones(request):
    return render(request, "pacientes/hospitalizaciones.html")
