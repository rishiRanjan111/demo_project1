
from django.contrib import admin
from django.urls import path,include
#here include is used for ...they include the urls created in apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('Posts.urls')),
]
