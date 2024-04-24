from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            # Asignar al usuario a un group
            group = Group.objects.get(name='Operarios')
            user.groups.add(group)
            messages.success(request, 'Registro exitoso. Bienvenido!')
            return redirect('home')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += 'is-invalid'
            messages.error(request, 'Por favor corrija los errores en el formulario')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html')
    