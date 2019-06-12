from django.contrib import admin
from .models import User, Admin, Producer

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Producer)
