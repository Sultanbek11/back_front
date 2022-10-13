from django.urls import path
from .views import (
    list_view,
    detail_view,
    create_view,
    update_view,
    delete_view,
)

urlpatterns = [
    path('', list_view),
    path('detail/<int:id>', detail_view),
    path('create/', create_view),
    path('update/<int:id>', update_view),
    path('delete/<int:id>', delete_view),
]
