from django.views.generic import TemplateView

from .models import District


class DistrictContextMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        districts_ctx = {}
        districts_ctx["all"] = District.objects.all()
        context["districts"] = districts_ctx
        return context


class IndexView(DistrictContextMixin, TemplateView):
    template_name = "districts/index.html"


class DistrictView(DistrictContextMixin, TemplateView):
    template_name = "districts/district.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        district_number = self.kwargs.get("district")
        context["district_number"] = district_number
        context["district"] = context.get("districts").get("all").get(number=district_number)
        return context
