from django.urls import path
from . import views

urlpatterns = [
    path('relatorios/', views.RelatorioListCreate.as_view(), name='relatorios_list_create'),
]
