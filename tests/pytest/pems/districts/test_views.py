import pytest

from django.urls import reverse
from pems.districts import views
from pems.districts.models import District


class TestIndexView:
    @pytest.fixture
    def view(app_request):
        v = views.IndexView()
        v.setup(app_request)

        return v

    @pytest.mark.django_db
    def test_get_context_data(self, view):

        context = view.get_context_data()

        assert set(context.get("districts").get("all")) == set(District.objects.all())

    def test_template_name(self, view):
        assert view.template_name == "districts/index.html"


@pytest.mark.django_db
def test_district_view(client, model_District):
    url = reverse("districts:district", kwargs={"district_number": model_District.number})
    response = client.get(url)

    assert response.status_code == 200
    assert response.context["current_district"] == model_District
