from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),
    path('videos/', include('videos.urls')),
    path('admin/', admin.site.urls),
]