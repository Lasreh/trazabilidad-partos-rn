from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Parto
from .forms import (
    PartoForm,
    AnestesiaForm,
)


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Parto
from .forms import PartoForm


@login_required
def crear_parto(request):
    if request.method == "POST":
        form = PartoForm(request.POST)
        if form.is_valid():
            parto = form.save(commit=False)
            parto.created_by = request.user
            parto.save()

            messages.success(request, "Parto creado correctamente.")
            return redirect("editar_parto", pk=parto.pk)
    else:
        form = PartoForm()

    return render(request, "partos/crear_parto.html", {
        "form": form
    })


# ==========================
# EDITAR PARTO (TAB PRINCIPAL)
# ==========================
@login_required
def editar_parto(request, pk):
    parto = get_object_or_404(Parto, pk=pk)

    if request.method == "POST":
        form = PartoForm(request.POST, instance=parto)
        if form.is_valid():
            form.save()
            messages.success(request, "Datos del parto actualizados.")
            return redirect("editar_parto", pk=pk)
    else:
        form = PartoForm(instance=parto)

    return render(request, "partos/editar_parto.html", {
        "form": form,
        "parto": parto,
    })


# ==========================
# EDITAR ANESTESIA
# ==========================
@login_required
def editar_anestesia(request, pk):
    parto = get_object_or_404(Parto, pk=pk)

    # Verificar si existe módulo de anestesia
    if not hasattr(parto, "anestesia"):
        return render(request, "partos/no_anestesia.html", {
            "parto": parto
        })

    anestesia = parto.anestesia

    if request.method == "POST":
        form = AnestesiaForm(request.POST, instance=anestesia)
        if form.is_valid():
            form.save()
            messages.success(request, "Anestesia actualizada.")
            return redirect("editar_anestesia", pk=pk)
    else:
        form = AnestesiaForm(instance=anestesia)

    return render(request, "partos/editar_anestesia.html", {
        "form": form,
        "parto": parto,
    })


# ==========================
# CREAR ANESTESIA (CUANDO NO EXISTE)
# ==========================
@login_required
def crear_anestesia(request, pk):
    parto = get_object_or_404(Parto, pk=pk)

    # Si ya existe el módulo → redirigir a editar
    if hasattr(parto, "anestesia"):
        return redirect("editar_anestesia", pk=pk)

    if request.method == "POST":
        form = AnestesiaForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.parto = parto
            obj.created_by = request.user
            obj.save()
            messages.success(request, "Anestesia registrada.")
            return redirect("editar_anestesia", pk=pk)
    else:
        form = AnestesiaForm()

    return render(request, "partos/crear_anestesia.html", {
        "form": form,
        "parto": parto,
    })

@login_required
def finalizar_parto(request, pk):
    messages.success(request, "Proceso de registro finalizado correctamente.")
    return redirect("crear_parto")


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Parto

@login_required
def lista_partos(request):
    # Obtener todos los partos, ordenados por fecha descendente
    partos_queryset = Parto.objects.all().order_by('-fecha')

    # Paginación: 20 partos por página
    paginator = Paginator(partos_queryset, 20)
    page_number = request.GET.get('page')
    partos = paginator.get_page(page_number)

    return render(request, "partos/lista_partos.html", {
        "partos": partos,
    })
