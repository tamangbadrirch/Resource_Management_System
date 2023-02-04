from django.urls import path
from user_mgmt.views import UserLoginView, UserLoginOutView, UserAddView
urlpatterns = [
   path('login',UserLoginView.as_view(),name="UserLogin"),
   path('signup',UserAddView.as_view(),name="UserSignUp"),
   path('logout',UserLoginOutView.as_view(),name="UserLogOut"),
  # path('user/add',UserAddView.as_view(),name="Useradd"),
]