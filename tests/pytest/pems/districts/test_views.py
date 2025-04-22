import pytest

from pems.districts import views
from pems.districts.models import District


class TestIndexViewView:
    @pytest.fixture
    def view(app_request):
        v = views.IndexView()
        v.setup(app_request)

        return v

    @pytest.mark.django_db
    def test_get_context_data(self, view):

        context = view.get_context_data()

        assert set(context["district_queryset"]) == set(District.objects.all())

    def test_template_name(self, view):
        assert view.template_name == "districts/index.html"


class TestDistrictView:
    @pytest.fixture
    def view(app_request):
        v = views.DistrictView()
        v.setup(app_request, district=1)

        return v

    @pytest.mark.django_db
    @pytest.mark.usefixtures("model_District")
    def test_get_context_data(self, view):

        context = view.get_context_data()

        assert context["url_district"] == 1

    def test_template_name(self, view):
        assert view.template_name == "districts/district.html"
