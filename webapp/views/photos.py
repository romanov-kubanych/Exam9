from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView

from webapp.models import Photo


class PhotoIndex(ListView):
    model = Photo
    template_name = 'photos/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        photos = Photo.objects.filter(isPrivate=False).order_by('-created_at')
        context['photos'] = photos
        return context



