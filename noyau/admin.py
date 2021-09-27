from django.contrib import admin
from .models import Netfeelex
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class NetfeelexAmin(admin.ModelAdmin):
    fields =["Titre_filme","Date_publie","Contenu_filme"]

    formfield_overrides = {
    models.TextField: {'widget': TinyMCE()},
    }
admin.site.register(Netfeelex, NetfeelexAmin)

 



