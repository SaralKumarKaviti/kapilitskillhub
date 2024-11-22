"""
URL configuration for kapilit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from counselor_app.views import counselor_login,manager_login,manager_dashboard_page,manager_logout,counselor_login,counselor_dashboard_page,counselor_logout,manager_logout,add_role
from counselor_app.views import employee_login,employee_logout,employee_dashboard_page, manager_login,manager_logout,manager_dashboard_page,add_role,edit_role_type,view_team,add_enroll_students,edit_enrolled_student,delete_enrolled_student,view_enrolled_student,register_payment_enrolled_student
urlpatterns = [
    path('admin/', admin.site.urls),

    path('employee-login',employee_login,name="employee_login"),
    path('employee-dashboard-page',employee_dashboard_page,name="employee_dashboard_page"),
    path('employee-logout',employee_logout,name="employee_logout"),


    path('manager-login',manager_login,name="manager_login"),
    path('manager-dashboard-page',manager_dashboard_page,name="manager_dashboard_page"),
    path('add-role',add_role,name='add_role'),
    path('view-team',view_team,name='view_team'),
    path('edit-role/<str:role_id>/', edit_role_type, name='edit_role_type'),
    path('manager-logout',manager_logout,name="manager_logout"),

    path('add-enroll-student',add_enroll_students,name="add_enroll_students"),
    path('edit-enroll-student/<int:student_id>',edit_enrolled_student,name="edit_enrolled_student"),
    path('delete-enroll-student/<int:student_id>',delete_enrolled_student,name="delete_enrolled_student"),
    path('view-enroll-student/<int:student_id>',view_enrolled_student,name="view_enrolled_student"),
    path('register-payment-enroll-student/<int:student_id>',register_payment_enrolled_student,name="register_payment_enrolled_student"),
    # path('download-excel/', download_excel, name='download_excel'),
    #path('razorpay-callback/', razorpay_callback, name='razorpay_callback')

]
