from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('profile/',views.profile,name="profile"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('inbox/',views.inbox,name="inbox"),
    path('account/',views.account,name="account"),
    path('skill-form/',views.skill_form,name="skill-form"),
    path('send-message/',views.message_form,name="send-message"),
    path('user-detail/',views.user_detail,name="user-detail"),
]
