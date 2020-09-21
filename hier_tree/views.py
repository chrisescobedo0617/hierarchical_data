from django.shortcuts import render
from hier_tree.models import File

# Create your views here.


def homepage_view(request):
    files = File.objects.filter()

    return render(request, 'homepage.html', {'files': files})
