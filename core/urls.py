from django.contrib import admin
from django.urls import path, include

# QUANDO O USURIO ENTRAR SEM NENHUMA URLS DEFINIDA ELE VAI PRA PAGINA CONTROLE.
urlpatterns = [
    path('', include('controle.urls')),
    path('admin/', admin.site.urls),
]
