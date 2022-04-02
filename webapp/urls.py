from django.urls import path

from webapp.views import TestView

app_name = "webapp"

urlpatterns = [
    path('', TestView.as_view(), name="test-view")
]
