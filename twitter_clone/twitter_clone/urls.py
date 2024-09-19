from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tweets.urls')),  # Route for tweets
    path('users/', include('users.urls')),  # Route for users
]