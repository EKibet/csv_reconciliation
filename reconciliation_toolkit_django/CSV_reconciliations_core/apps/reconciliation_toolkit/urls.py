from django.urls import path
from .views import FileUploadView
app_name = "reconciliation"

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='upload_file'),
]
