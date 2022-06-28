from django.urls import path
from.views import Admin_Login, All_Employee, Change_Passwordadmin, Edit_Education, Emp_Login, Index, My_Education, Signup, Emp_Home, Profile, Logout, My_Experience, Edit_Experience, Change_Password, Admin_Home

urlpatterns = [
    path('', Index, name= 'index' ),
    path('signup/', Signup, name= 'signup'),
    path('emp_login/', Emp_Login, name= 'emp_login'),
    path('emp_home/', Emp_Home, name= 'emp_home'),
    path('profile/', Profile, name= 'profile'),
    path('logout/',Logout, name= 'logout'),
    path('my_experience/', My_Experience, name= 'my_experience'),
    path('edit_experience/', Edit_Experience, name= 'edit_experience'),
    path('edit_education/', Edit_Education, name= 'edit_education'),
    path('my_education/', My_Education, name= 'my_education'),
    path('admin_login/', Admin_Login, name= 'admin_login'),
    path('change_password/', Change_Password, name= 'change_password'),
    path('admin_home/', Admin_Home, name= 'admin_home'),
    path('change_passwordadmin/', Change_Passwordadmin, name= 'change_passwordadmin'),
    path('all_employee/', All_Employee, name= 'all_employee'),
    
]
