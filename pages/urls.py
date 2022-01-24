from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('profile/<str:pk>/',views.profile,name="profile"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout,name="logout"),
    path('inbox/',views.inbox,name="inbox"),
    path('account/',views.account,name="account"),
    path('skill-form/',views.skill_form,name="skill-form"),
    path('update-skill/<str:pk>/',views.update_skill,name="update-skill"),
    path('delete-skill/<str:pk>/',views.delete_skill,name="delete-skill"),
    path('send-message/',views.message_form,name="send-message"),
    path('user-detail/<str:pk>/',views.user_detail,name="user-detail"),
]
