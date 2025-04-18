from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "districts/index.html"


class DistrictView(TemplateView):
    template_name = "districts/district.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        district = self.kwargs.get("district")
        context["district"] = district
        return context
