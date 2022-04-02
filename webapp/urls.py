from django.urls import path

from webapp.views.photos import PhotoIndex

app_name = "webapp"

urlpatterns = [
    path('', PhotoIndex.as_view(), name="photo_index"),

]
