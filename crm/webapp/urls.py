from django.urls import path
from . import views

urlpatterns = [
    # Home and Dashboard
    path('', views.home, name=''),
    path('dashboard', views.dashboard, name='dashboard'),
    # User Authentication
    path('register', views.register, name='register'),
    path('my-login', views.my_login, name='my-login'),
    path('user-logout', views.user_logout, name='user-logout'),
    # CRUD
    path('create-record', views.create_record, name='create-record'),          # C
    path('view-record/<int:id>', views.view_record, name='view-record'),       # R = read = view
    path('update-record/<int:id>', views.update_record, name='update-record'), # U
    path('delete-record/<int:id>', views.delete_record, name='delete-record'), # D
]

