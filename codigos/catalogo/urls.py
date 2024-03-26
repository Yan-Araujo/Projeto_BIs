from django.urls import path
from catalogo.views import index, search, add_bi, edit_bi, delete_bi

urlpatterns = [
    path('', index, name='index'),
    path('search', search, name='search'),
    path('add_bi', add_bi, name='add_bi'),
    path('edit_bi', edit_bi, name='edit_bi'),
    path('delete_bi', delete_bi, name='delete_bi'),
]