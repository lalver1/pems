"""
URLConf for the districts app.
"""

from django.urls import path

from pems.districts import views

app_name = "districts"
urlpatterns = [
    # /districts
    path("", views.IndexView.as_view(), name="index"),
    path("<int:district_number>", views.DistrictView.as_view(), name="district"),
]
