from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from hier_tree.models import File

# Register your models here.

admin.site.register(File, DraggableMPTTAdmin)
