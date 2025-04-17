import pytest

from pems.districts import views


class TestDistrictView:
    @pytest.fixture
    def view(app_request):
        v = views.DistrictView()
        v.setup(app_request, district=1)

        return v

    def test_get_context_data(self, view):

        context = view.get_context_data()

        assert context["district"] == 1

    def test_template_name(self, view):
        assert view.template_name == "districts/district.html"
