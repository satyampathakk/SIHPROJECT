from django.urls import path
from . import views


urlpatterns = [ 
    path('',views.index,name='home'),
    path('submit',views.submit,name='submit'),
    path('retrieve/',views.retrieve,name='retrieve'),
    path('register',views.register,name="register"),
    path('login',views.login,name='login'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('particular/<int:rollno>',views.particular,name='particular'),
    path('show',views.show,name='show'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('forgot',views.forgot,name='forgot'),
    path('logout',views.logout,name='logout'),

]