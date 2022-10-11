from django.urls import path

from apps.blop_storage.views import BlobStorageView

urlpatterns = [
    path('', BlobStorageView.as_view()),
]