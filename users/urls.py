from django.urls import path

from users.views import UserList, UserDetail, UserMatch

urlpatterns = [
    path('', UserList.as_view(), name='Users'),
    path('<int:pk>/', UserDetail.as_view(), name='User'),
    path('<int:follower_id>/follow/<int:user_id>', UserMatch.as_view(), name='Follow a user')
]
