from django.urls import path
from .views import CreateBagView, CreateTermView, UpdateTermView
from .views import index, autofill_bag_from_url, delete_term

app_name = "bags"
urlpatterns = [
    path("", index, name="index"),
    path("add/", CreateBagView.as_view(), name="add-bag"),
    path("add/term/", CreateTermView.as_view(), name="add-term"),
    path("update/term/<pk>", UpdateTermView.as_view(), name="update-term"),
    path("autofill/", autofill_bag_from_url, name="autofill"),
    path("delete/term/<pk>", delete_term, name="delete-term"),
]