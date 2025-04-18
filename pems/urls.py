from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("districts/", include("pems.districts.urls")),
    path("streamlit/", include("pems.streamlit_sample.urls")),
]
