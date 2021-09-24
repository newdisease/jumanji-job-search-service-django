from django.shortcuts import redirect

from vacancies.models import Company


class IsNotCompanyMixin:
    """give access if user has a company"""

    def dispatch(self, request, *args, **kwargs):
        if Company.objects.filter(owner=self.request.user):
            return super().dispatch(request, *args, **kwargs)
        return redirect('no_company')


class IsCompanyMixin:
    """redirect to the create company page if user doesn't have a company"""

    def dispatch(self, request, *args, **kwargs):
        if not Company.objects.filter(owner=self.request.user):
            return super().dispatch(request, *args, **kwargs)
        return redirect('my_company')
