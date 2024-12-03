from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pems")
except PackageNotFoundError:
    # package is not installed
    pass
