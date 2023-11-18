
from django.contrib import admin
from django.urls import path
from cadastro import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('tabela', views.base2, name='base2'),
    
]
