from django.contrib import admin
from .models import Room , Message

# Registering mychat models.
admin.site.register(Room)
admin.site.register(Message)
