# urgencias/views.py

from django.shortcuts import render, redirect
from .forms import PacienteForm
from .models import Paciente

# Vista para cargar un nuevo paciente
def ingresar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente_guardado')
    else:
        form = PacienteForm()
    return render(request, 'urgencias/ingresar_paciente.html', {'form': form})

# Vista de confirmación después de guardar un paciente
def paciente_guardado(request):
    return render(request, 'urgencias/paciente_guardado.html')

# Vista principal para elegir entre cargar o buscar paciente
def pagina_principal(request):
    return render(request, 'urgencias/pagina_principal.html')

# Vista para buscar pacientes
def buscar_paciente(request):
    query = request.GET.get('q', '')  # Obtener el valor de búsqueda (si existe)
    pacientes = Paciente.objects.filter(nombre__icontains=query)  # Filtrar por nombre
    return render(request, 'urgencias/buscar_paciente.html', {'pacientes': pacientes, 'query': query})
