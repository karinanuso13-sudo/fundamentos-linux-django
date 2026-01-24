from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from .forms import ProductModelForm
from .models import ProductModel

# Create your views here.
#def home (request):
#    html = """
#    <!DOCTYPE html>
#    <html>
#        <head>
#            <style>
#                h1 {color:blue}
#            </style>
#        </head>
#
#        <body>
#            <h1>Arriba yo, mi ama y Blink </h1>
#        </body>
#    </html>
#   """
#   return HttpResponse(html)

#def home (request):
#    response = HttpResponse()
#    response.write("<p>Texto de prueba para ecommerce </p>")
#    response.write("<p>Texto de prueba para ecommerce </p>")
#    response.write("<p>Texto de prueba para ecommerce </p>")
#    return response

#@login_required
def product_model_create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.succes(request, "Producto creado con éxito")
        return HttpResponseRedirect("/ecommerce/{product_id}".format(product_id=instance.id))
    context = {
        "form":form
    }
    template = "ecommerce/create-view.html"
    return render(request, template, context)


def product_model_detail_view(request, product_id):
    instance = get_object_or_404(ProductModel, id=product_id)
    context = {
        "product":instance
    }
    template = "ecommerce/detail-view.html"
    return render(request, template, context)

def product_model_list_view(request):
    print(request.user)
    queryset = ProductModel.objects.all()
    template = "ecommerce/list-view.html"
    context = {
        "products": queryset
    }

    if request.user.is_authenticated:
        template = "ecommerce/list-view.html"
    else: 
        template = "ecommerce/list-view-public.html"

    return render(request, template, context)

@login_required
def login_required_view(request):
    print(request.user)
    queryset = ProductModel.objects.all()
    template = "ecommerce/list-view.html"
    context = {
        "products": queryset
    }

    if request.user.is_authenticated:
        template = "ecommerce/list-view.html"
    else: 
        template = "ecommerce/list-view-public.html"
    return render(request, template, context)    