from django.contrib import admin
from django.urls import path, include
from accounts import urls
from rest_framework.authtoken import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth',views.obtain_auth_token, name='auth'),
    path('api/v1/accounts/', include('accounts.urls'))
]
