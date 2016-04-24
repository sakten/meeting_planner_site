from django.contrib import admin
from Main_Static import models

# Register your models here.
admin.site.register([models.myuser])
admin.site.register( [ models.event ] )