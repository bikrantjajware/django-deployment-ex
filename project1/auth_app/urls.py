from django.conf.urls import url
from auth_app import views
from django.urls import path
app_name = 'auth_app'
#to make use  template tags {% url ......... %}

app_name = 'auth_app'
urlpatterns = [
    path('^register/$',views.register,name="register"),
    path(r'^user_login/$',views.user_login,name='user_login'),
]