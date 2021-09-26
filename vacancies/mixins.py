from django.contrib.auth.models import AnonymousUser
from django.shortcuts import redirect

from vacancies.models import Company, Application


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


class IsSendApplicationMixin:
    """redirect to the application sent page"""

    def dispatch(self, request, *args, **kwargs):
        if Application.objects.filter(user_id=self.request.user.id):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('vacancies_view')
