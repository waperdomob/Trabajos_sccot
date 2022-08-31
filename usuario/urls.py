from django.urls import path
from usuario.views import *

app_name = 'user'
urlpatterns = [
    # user
    path('list/', UserListView.as_view(), name='user_list'),
    path('edit_User/<int:pk>/', UserUpdate.as_view(), name='user_update'),
    path('delete_user/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]