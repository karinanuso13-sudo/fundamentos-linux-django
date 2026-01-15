from django.shortcuts import render
from django.http import HttpResponse 

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

def home (request):
    response = HttpResponse()
    response.write("<p>Texto de prueba para ecommerce </p>")
    response.write("<p>Texto de prueba para ecommerce </p>")
    response.write("<p>Texto de prueba para ecommerce </p>")
    return response