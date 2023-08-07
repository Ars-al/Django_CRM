from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('hr_panel/', views.hr_panel, name='hr_panel'),
    path('hr_record_view/<int:pk>', views.hr_record_view, name='hr_record_view'),
    path('add_hr_record/', views.add_hr_record, name='add_hr_record'),
    path('update_hr_record/<int:pk>', views.update_hr_record, name='update_hr_record'),
    path('delete_hr_record/<int:pk>', views.delete_hr_record, name='delete_hr_record'),
    path('employee_panel/', views.employee_panel, name='employee_panel'),
    path('employee_record_view/<int:pk>', views.employee_record_view, name='employee_record_view'),
    path('add_employee_record/', views.add_employee_record, name='add_employee_record'),
    path('update_employee_record/<int:pk>', views.update_employee_record, name='update_employee_record'),
    path('delete_employee_record/<int:pk>', views.delete_employee_record, name='delete_employee_record'),
]
