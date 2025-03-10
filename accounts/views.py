from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView
)
from accounts.forms import (
    CustomLoginForm,
    CustomUserCreationForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm
)  # pylint: disable=import-error, no-name-in-module
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.utils.translation import gettext as _
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = "login.html"

class CustomUserCreationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")  # Melhor prática

# class CustomPasswordResetView(PasswordResetView):
#     form_class = CustomPasswordResetForm
#     template_name = "password_reset.html"
#     success_url = reverse_lazy("password_reset_done")


class CustomPasswordResetView(PasswordResetView):
    email_template_name = "registration/password_reset_email.html"
    extra_email_context = None
    form_class = CustomPasswordResetForm
    from_email = None
    html_email_template_name = None
    subject_template_name = "registration/password_reset_subject.txt"
    success_url = reverse_lazy("password_reset_done")
    template_name = "password_reset.html"
    title = _("Password reset")
    token_generator = default_token_generator

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            print("❌ Usuário não encontrado.")
            return self.form_invalid(form)

        # 🔹 Gerar UID e Token
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = self.token_generator.make_token(user)

        # 🔹 Gerar a URL corretamente usando `reverse()`
        reset_url = self.request.build_absolute_uri(
            reverse("password_reset_confirm", kwargs={"uidb64": uid, "token": token})
        )

        # 🔹 Imprimir UID, Token e Link corrigido
        print(f"🔹 UID Gerado: {uid}")
        print(f"🔹 Token Gerado: {token}")
        print(f"🔗 Link Corrigido: {reset_url}")

        opts = {
            "use_https": self.request.is_secure(),
            "token_generator": self.token_generator,
            "from_email": self.from_email,
            "email_template_name": self.email_template_name,
            "subject_template_name": self.subject_template_name,
            "request": self.request,
            "html_email_template_name": self.html_email_template_name,
            "extra_email_context": self.extra_email_context,
        }
        form.save(**opts)

        return super().form_valid(form)

INTERNAL_RESET_SESSION_TOKEN = "_password_reset_token"

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "password_reset_done.html"
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = "password_reset_confirm.html"
    success_url = reverse_lazy("password_reset_complete")

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "password_reset_complete.html"


class CustomChangePasswordView(PasswordChangeView):
    form_class = CustomSetPasswordForm  # Ou PasswordChangeForm se for alteração autenticada
    template_name = "password_change_form.html"
    success_url = reverse_lazy("password_change_done")
class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "password_change_done.html"

from django.core.mail import send_mail
from django.http import HttpResponse

def test_email(request):
    send_mail(
        'Teste de E-mail',
        'Este é um e-mail de teste enviado pelo Django.',
        'fmartns@hotmail.com',  # Deve ser igual ao `DEFAULT_FROM_EMAIL`
        ['fmartns@hotmail.com'],  # Substitua pelo e-mail para onde quer enviar o teste
        fail_silently=False,
    )
    return HttpResponse("E-mail enviado com sucesso!")
