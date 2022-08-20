from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="bags"),
    path("create/", views.create_bag, name="create"),
    path("create/term/", views.create_term, name="create-term"),
    path("edit/term/<int:id>", views.edit_term, name="edit-term"),
    path("delete/term/<int:id>", views.delete_term, name="delete-term"),
]