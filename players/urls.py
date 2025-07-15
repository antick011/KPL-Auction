from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.search_player, name='search_player'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)