# The admin is where we will write our first Tweet
from django.contrib import admin
from .models import Tweet

admin.site.register(Tweet) # we will have access to the data specified in our models file