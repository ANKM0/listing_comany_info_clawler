from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    # ホーム
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path('', views.IndexView.as_view(), name='index'),
    path('howto/', views.HowtoView.as_view(), name='howto'),
    path('logout_safety/', views.LogoutSafetyView.as_view(), name='logout_safety'),


    path("create/", views.UserInfoCreateView.as_view(), name="create"),
    path("detail/<int:pk>", views.UserInfoDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", views.UserInfoUpdateView.as_view(), name="update"),
    # path("delete/<int:pk>/", views.UserInfoDeleteView.as_view(), name="delete"),
]
