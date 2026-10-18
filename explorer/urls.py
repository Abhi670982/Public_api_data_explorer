from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("export/csv/", views.export_csv, name="export_csv"),
    path("export/excel/", views.export_excel, name="export_excel"),
    path("sync-users/", views.sync_users, name="sync_users"),
]