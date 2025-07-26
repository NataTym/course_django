from django.views.generic import TemplateView
from hr.models import Company


class HomeViev(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        company = Company.objects.first()
        if company and company.logo:
            context['logo_url'] = company.logo.url
        else:
            context['logo_url'] = None

        return context
