from django.urls import path

from webapp.views.photos import PhotoIndex, PhotoView, PhotoCreateView

app_name = "webapp"

urlpatterns = [
    path('', PhotoIndex.as_view(), name="photo_index"),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_create'),
]
