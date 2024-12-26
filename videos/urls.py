from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exibir_video/<slug:nome>', views.exibir_video, name='exibir'),
    path('videos_novos/', views.videos_novos, name='videos_novos'),
]