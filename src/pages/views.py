import os

   from django import get_version
   from django.conf import settings
   from django.shortcuts import render


def home(request):
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version() + "Proyecto modificado por Karina",
        "python_ver": os.environ["PYTHON_VERSION"]
        + "Este texto fue agregado como parte de la práctica de Django",
    }

    return render(request, "pages/home.html", context)

