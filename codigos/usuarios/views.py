from django.shortcuts import render, redirect
from usuarios.forms import LoginForm
from django.contrib import auth, messages

# Create your views here.
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form['username'].value()
            password = form['password'].value()

        user = auth.authenticate(
            request,
            username=user,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login Efetuado")
            return redirect('index')
        else:
            messages.error(request, "Usuário não cadastrado")
            return redirect('login')
        
    return render(request, 'usuarios/login.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.error(request, "Logout Realizado")
    return redirect('login')
