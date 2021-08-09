from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# URLs para preço Real time:
urlpatterns = [
    path('assets/', include('kurama.assets_rt.urls')),
] 
