from django.contrib import admin
from django.urls import include, path
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #View for admin site
    path('admin/', admin.site.urls),
    #View for user registration
    path('api/users/register/', CreateUserView.as_view(), name="register"),
    #View for creating access token and refresh token
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    #View for refreshing access token
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    
    #Path for Notes RestAPI
    path("api/", include("api.urls")),
    
]
