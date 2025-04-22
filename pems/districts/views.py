from django.views.generic import TemplateView

from .models import District


class IndexView(TemplateView):
    template_name = "districts/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["district_queryset"] = District.objects.all()
        return context


class DistrictView(TemplateView):
    template_name = "districts/district.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        district = self.kwargs.get("district")
        context["url_district"] = district
        context["district_queryset"] = District.objects.all()
        context["district_query"] = District.objects.all().get(number=district)
        return context
