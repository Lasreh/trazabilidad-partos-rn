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
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import F, Value, CharField
from django.db.models.functions import Concat
from .models import Paciente

@login_required
def lista_pacientes(request):
    run_query = request.GET.get('run', '').strip()  # Obtenemos el RUT completo con DV

    pacientes_queryset = Paciente.objects.all().order_by('apellido_paterno', 'apellido_materno')

    if run_query:
        # Creamos un campo temporal "rut_completo" = run + "-" + dv
        pacientes_queryset = pacientes_queryset.annotate(
            rut_completo=Concat('run', Value('-'), 'dv', output_field=CharField())
        ).filter(rut_completo__icontains=run_query)

    # Paginación: 20 pacientes por página
    paginator = Paginator(pacientes_queryset, 20)
    page_number = request.GET.get('page')
    pacientes = paginator.get_page(page_number)

    return render(request, "pacientes/lista.html", {
        "pacientes": pacientes,
        "run_query": run_query,
    })


def lista_hospitalizaciones(request):
    return render(request, "pacientes/hospitalizaciones.html")
