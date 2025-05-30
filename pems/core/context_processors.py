"""
The core application: context processors for enriching request context data.
"""

from pems import __version__
from django.conf import settings


def pems_version(request):
    """Context processor adds information about the PeMS application's version."""

    return {"pems_version": __version__}


def streamlit(request):
    """Context processor adds Streamlit-related information."""

    return {"streamlit": {"url": settings.STREAMLIT_URL}}
