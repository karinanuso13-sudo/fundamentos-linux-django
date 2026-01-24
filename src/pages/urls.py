from django.urls import path

from pages import views

urlpatterns = [
    path("", views.product_model_list_view, name="list"),
    path("<int:product_id>", views.product_model_detail_view, name="detail"),
]
