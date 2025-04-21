"""
The core application: context processors for enriching request context data.
"""

from pems import __version__


def pems_version(request):
    """Context processor adds information about the PeMS application's version."""

    return {"pems_version": __version__}
