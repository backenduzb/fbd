from django.urls import path
from .views import access_doc

urlpatterns = [
    path('doc/<int:pk>/', access_doc, name='doc-access'),
]
