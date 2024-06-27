from typing import Any, Dict

from django.views.generic import TemplateView

from .forms import UserRegistrationForm

# Create your views here.


class RegistrationPage(TemplateView):
    template_name = "accounts/register.html"

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        form = UserRegistrationForm()
        context.update(
            {
                "form": form,
            }
        )
        return context
