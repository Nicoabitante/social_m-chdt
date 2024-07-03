from django.urls import path

from users.views import UserList, UserDetail

urlpatterns = [
    path('', UserList.as_view(), name='Users'),
    path('<int:pk>/', UserDetail.as_view(), name='User')
]
