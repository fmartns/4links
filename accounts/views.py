from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms import CustomLoginForm, CustomUserCreationForm  # pylint: disable=import-error, no-name-in-module
from django.contrib.auth.views import LoginView  # pylint: disable=unused-import
from django.shortcuts import render

class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm  # Sua CustomLoginForm
    template_name = "login.html"  # O template do seu login
    
    def form_invalid(self, form):
        # Aqui você renderiza a página, mas sem as mensagens de erro automáticas
        # Passamos os erros manualmente para o template
        return render(self.request, self.template_name, {
            'form': form,
            'errors': form.non_field_errors()  # Exibe os erros manualmente
        })


class CustomUserCreationView(CreateView):  # Usando CreateView em vez de UserCreationView
    form_class = CustomUserCreationForm
    template_name = "signup.html"  # Substitua pelo seu template
    success_url = '/'  # Após o cadastro, redireciona para a página inicial ou a página que você escolher
