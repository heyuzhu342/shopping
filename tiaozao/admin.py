from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Article)
admin.site.register(models.Reporter)
admin.site.register(models.Board)
admin.site.register(models.Topic)

