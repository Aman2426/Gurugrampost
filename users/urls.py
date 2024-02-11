from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy,reverse
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', 
        auth_views.LoginView.as_view(
            template_name='users/login.html',
            next_page=reverse_lazy('blog:article_list')),
        name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('password_change/', 
        auth_views.PasswordChangeView.as_view(
            template_name='users/password_change_form.html', 
            success_url='password_change_done'), 
        name='password_change'),
    path('password_change_done/', 
        auth_views.PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'), 
        name='password_change_done'),

    path('profile/',views.user_page,name='profile'),
    path('update_profile/',views.update_profile,name='update_profile'),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('password_reset_confirm/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_done'),

]