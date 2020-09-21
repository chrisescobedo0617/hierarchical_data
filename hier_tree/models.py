from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class File(MPTTModel):
    FILE_TYPES = ((True, 'Folder'), (False, 'File'))

    name = models.CharField(max_length=200, unique=True)
    type_of_file = models.BooleanField(choices=FILE_TYPES, null=False)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
